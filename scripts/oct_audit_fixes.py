#!/usr/bin/env python3
"""Idempotent in-place fixes from the 2026-10-07 blog audit.

1. Adds a closing 'Next step' block (service page + /diagnostic/ CTA) to posts that lack
   a /diagnostic/ link.  Marker: <!-- next-step -->
2. Adds an operator section to thin posts.  Marker: <!-- oct-expand -->
3. Fixes unsourced / vaguely attributed claims.
Does not touch sitemap.xml or build_pages.py.
"""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
D = '<a href="/diagnostic/">free diagnostic</a>'

NEXT = {
 "how-to-get-more-customers": ("/services/lead-follow-up/", "lead follow-up", "If you want your three leaks found for you, the"),
 "how-much-should-i-charge-for-my-services": ("/services/", "growth services", "If you are repricing and want to see where the rest of your money is leaking, the"),
 "how-to-grow-a-small-business": ("/services/", "growth services", "If you want the biggest lever found first, the"),
 "after-hours-answering-service": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "If you want to see how many after-hours calls are slipping past you right now, I will walk through it in the"),
 "ai-agents-for-business": ("/services/automation/", "automation", "If you are not sure which job to hand an agent first, the"),
 "ai-appointment-scheduling-software": ("/services/automation/", "automation", "Scheduling is one piece of a longer chain, and the"),
 "ai-assistant-for-families": ("/assistant/", "assistant", "If you are curious how an assistant like this would fit your household, start with the"),
 "ai-phone-agent-integrations": ("/services/automation/", "automation", "Integrations are where most setups break. If you want yours checked, the"),
 "ai-receptionist-cost-vs-front-desk-hire": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "Before you commit to a hire or a tool, run your own numbers in the"),
 "ai-receptionist-for-contractors-missed-calls": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "To count how many jobs your phone is costing you, start with the"),
 "all-in-one-business-software-kill-saas-bloat": ("/services/automation/", "automation", "If you want a second set of eyes on which subscriptions to cut, the"),
 "answering-service-pricing": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "To compare real options against your own call volume, start with the"),
 "business-money-leaks": ("/services/", "growth services", "To find which of these five is costing you the most, the"),
 "business-operating-system": ("/services/", "growth services", "If you want this running in your business, the"),
 "diy-voice-ai-what-it-really-costs": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "If you would rather skip the build, the"),
 "do-i-need-a-website-for-my-business": ("/services/websites/", "websites", "If you are not sure whether you need one, the"),
 "fresno-seo-for-small-business": ("/seo-company-fresno/", "Fresno SEO", "To see where your business stands in Fresno search today, the"),
 "gohighlevel-alternative-done-for-you": ("/services/automation/", "automation", "If you want the result without owning the software, the"),
 "growth-as-a-service-for-small-business": ("/services/", "growth services", "The easiest way to see what this looks like for your business is the"),
 "hire-an-ai-employee": ("/services/automation/", "automation", "To work out which job to hand off first, the"),
 "how-long-does-a-call-ring-before-voicemail": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "If you want to know how many calls are landing in voicemail, the"),
 "how-much-does-a-small-business-website-cost": ("/services/websites/", "websites", "For a straight answer on what your site should cost, talk through it in the"),
 "how-to-automate-a-small-business": ("/services/automation/", "automation", "If you want help picking the first thing to automate, the"),
 "how-to-rank-on-google-maps": ("/google-business-profile-optimization/", "Google Business Profile optimization", "To see where you rank on the map right now and what to fix first, the"),
 "how-to-reduce-no-shows": ("/services/lead-follow-up/", "lead follow-up", "To set up the reminders without doing it by hand, the"),
 "instant-lead-response-software-5-minute-rule": ("/services/lead-follow-up/", "lead follow-up", "To find out how long your leads actually wait, the"),
 "local-seo-automation": ("/services/seo/", "SEO", "To see which part of your local search upkeep is slipping, the"),
 "marketing-agency-alternative-fire-without-losing-leads": ("/services/", "growth services", "Before you cut anyone loose, see what your leads are really doing in the"),
 "missed-call-lead-capture": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "To see how many calls you are missing, the"),
 "run-my-business-on-autopilot-not-the-receptionist": ("/services/automation/", "automation", "If you want to get the front desk off your calendar, the"),
 "virtual-receptionist-companies-compared": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "To choose between human, hybrid, and AI for your call volume, the"),
 "what-hiring-an-employee-actually-costs": ("/services/automation/", "automation", "If you are weighing a hire against automation, the"),
 "what-is-an-ai-receptionist": ("/never-lose-a-job-to-voicemail/", "never lose a job to voicemail", "To see whether one fits your business, the"),
 "why-is-my-business-not-showing-up-on-google": ("/services/seo/", "SEO", "To find out which of these causes is yours, the"),
}
# page-specific tails (what the diagnostic does for that reader), keeps blocks from reading as clones
TAIL = {
 "default": "checks your calls, follow-up, search visibility, and reviews, and tells you what to fix first. It takes about fifteen minutes.",
}

EXPAND = {
 "after-hours-answering-service": ("What an after-hours call is really worth, and how to check", [
   "I will not hand you a number for what an evening call is worth, because it depends on your trade. You can find your own in ten minutes. Open your phone log for the last month and mark every call that came in after you closed. Then look at which ones left a voicemail and which did not. Most callers with an urgent need do not leave a message at all. They hang up and dial the next name.",
   "Now multiply the count of unanswered after-hours calls by your average job value and by how often you normally win a call you do answer. That figure is a conservative estimate of what the evenings cost you. It is yours, built from your phone, and it is more persuasive than any statistic I could quote.",
   "For California trades this matters more in peak seasons. HVAC in a Central Valley July, a burst pipe on the first cold night, a lockout on a Friday: the highest-urgency work clusters in hours when you are off. If you are weighing a person against software for covering them, [the real math on a front-desk hire](/blog/ai-receptionist-cost-vs-front-desk-hire/) lays out the comparison, and [how long a phone rings before voicemail](/blog/how-long-does-a-call-ring-before-voicemail/) explains why even daytime calls are slipping."]),
 "gohighlevel-alternative-done-for-you": ("How to decide: three honest questions", [
   "Before you pick any platform or any service, answer three questions. Who will build it? Who will maintain it six months from now? And what happens on the week you are too busy to touch it? If the honest answer to all three is you, you are not buying relief, you are buying a part-time job.",
   "GoHighLevel and tools like it are real products, and for an agency with staff they can be the right choice. For an owner-operator, the question is whether the software or the outcome is the thing you want. If you want the outcome, whether that is calls answered, leads followed up, or a steady content cadence, the cheapest path is usually to have someone run the system for you and judge them on results you can see: calls captured, quotes followed up, reviews added.",
   "Ask any provider, including me, to show you the live proof. I run a one-person California field-services company on this system, and over 700 jobs have gone through it. If a provider cannot show you their own business running on what they sell, keep looking. When you are comparing options, [growth-as-a-service explained](/blog/growth-as-a-service-for-small-business/) and [all-in-one business software](/blog/all-in-one-business-software-kill-saas-bloat/) cover the model and the trade-offs."]),
 "growth-as-a-service-for-small-business": ("What you should be able to see in the first month", [
   "Any growth service, mine included, should be judged on things you can observe, not on a deck. In the first month you should be able to point to concrete changes: calls and messages being answered that were not before, a follow-up sequence that fires on your open quotes, a Google profile that is complete and current, and a list of pages or posts that went live with a reason behind each.",
   "Be wary of any plan that cannot tell you what it will change in thirty days. Search results take longer to move, and I will say so plainly, but the plumbing work, such as answering, follow-up, and review requests, shows up quickly. On my own site, organic traffic rose 60% in 28 days with zero ad spend, and the work behind it was a steady cadence of useful pages, not a trick.",
   "If you are comparing this model to an agency, [the marketing agency alternative post](/blog/marketing-agency-alternative-fire-without-losing-leads/) covers how to part ways cleanly, and [how to grow a small business](/blog/how-to-grow-a-small-business/) lays out the five levers underneath all of it."]),
 "hire-an-ai-employee": ("Write the job description first", [
   "Treat it like a real hire. Before you set anything up, write the job description: the three to five tasks you want off your plate, what a good result looks like for each, and what the employee must never do without asking you. For most owners the list reads like this: answer the phone, log every lead, send the follow-up, send the invoice, ask for the review.",
   "Then decide the boundaries. Anything involving money leaving your account, a price change, a legal commitment, or an upset customer should stop and wait for you. A good AI employee is fast on the routine and careful on the rest. Start with one task, watch it for two weeks, and add the next only after the first runs clean.",
   "If you are still working out whether a person or software fits your situation, [what hiring an employee actually costs](/blog/what-hiring-an-employee-actually-costs/) shows the full cost of the person side, and [how to automate a small business](/blog/how-to-automate-a-small-business/) gives the order to hand tasks over in."]),
 "local-seo-automation": ("What to automate and what to keep human", [
   "Automation is good at the repetitive, scheduled parts of local SEO: reminding you to post to your Google profile, requesting reviews after each job, flagging when your business information drifts out of sync, and publishing pages on a steady cadence. These are the tasks that die first when you are busy.",
   "Keep the judgment human. The words on your service pages, the replies to reviews, and the decisions about which cities to cover should come from someone who knows the work. Google's own guidance is to make [helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), and a page that exists only to fill a schedule fails that test.",
   "The order matters too. Get the basics in place first, as laid out in [SEO for local business](/blog/seo-for-local-business/), then automate the upkeep. If you serve more than one city, read [service area pages that rank](/blog/service-area-pages-that-rank/) before you let any tool publish city pages for you."]),
 "all-in-one-business-software-kill-saas-bloat": ("A one-hour audit you can do tonight", [
   "Open your bank or card statements for the last three months and highlight every recurring software charge. For each one, write down three things: what job it does, the last date you used it, and what breaks if you cancel it. Most owners find at least a few subscriptions that overlap, a few that nobody has opened in months, and one or two that exist only because a free trial turned into a charge.",
   "Then group what is left by job: communication, scheduling, billing, marketing, and records. The jobs that appear under several tools are your consolidation targets. Do not cancel everything at once. Move one job at a time, export your data first, and keep the old tool until the new one has run clean for a full billing cycle.",
   "This is also the best time to ask which tools are actually connected. A stack where each tool needs you to copy information into the next one is a stack that is costing you hours. The method for deciding what to automate first is in [how to automate a small business](/blog/how-to-automate-a-small-business/)."]),
 "instant-lead-response-software-5-minute-rule": ("The evidence, and its limits", [
   "The five-minute rule is shorthand, so here is what the research actually supports. A Harvard Business Review study of 1.25 million sales leads found that [firms that contacted a lead within an hour were nearly seven times as likely to qualify it as those that waited even one hour longer](https://hbr.org/2011/03/the-short-life-of-online-sales-leads), and far more likely than firms that waited a day or more. The pattern is strong and it has held up in how people talk about lead handling ever since.",
   "Two cautions. The study covered B2C and B2B companies broadly, so treat the exact multiples as directional for a plumber or a salon rather than a promise. And speed only helps if the first response is useful. A reply that says we got your message and nothing else buys you minutes, not a customer.",
   "The practical test is simple: submit a form on your own site tonight and time how long it takes to get a human-sounding reply. If it is hours, you have found your first fix. [Missed call lead capture](/blog/missed-call-lead-capture/) covers the phone side, and [how to follow up on a quote](/blog/how-to-follow-up-on-a-quote/) covers what comes after the first reply."]),
 "marketing-agency-alternative-fire-without-losing-leads": ("A clean exit checklist", [
   "Before you send a termination note, secure what is yours. Confirm you own your domain, your Google Business Profile, your ad accounts, your analytics, and your email list, and that your name is on each as owner. Agencies often set these up under their own logins, and getting them back after a dispute is slow.",
   "Ask for a handoff in writing: logins, ad account access, the content library, and a list of what is running. Check your contract for notice periods and auto-renewal so you do not pay for a month you did not use. Keep the tone professional. You may want a reference, and the industry is smaller than it looks.",
   "Then put the basics in place before the agency stops, so leads do not fall through the gap: make sure calls are answered, form submissions get a fast reply, and follow-up is running. Those are the pieces that decide whether marketing spend turns into customers, and they are the same fundamentals described in [how to get more customers](/blog/how-to-get-more-customers/)."]),
 "run-my-business-on-autopilot-not-the-receptionist": ("What autopilot should and should not mean", [
   "Autopilot is a bad word for it, so let me be precise. You are not removing yourself from the business. You are removing yourself from the tasks that do not need you. The work that needs your skill, your judgment, and your name stays with you.",
   "A useful rule: if the task is the same every time and the outcome is obvious, automate it. Confirmations, reminders, intake questions, invoices on completion, review requests. If the task needs judgment, relationships, or a decision about money, keep it. The goal is a day where your phone gets answered and your follow-up happens without you, and the customer who needs you gets all of your attention.",
   "Start with the front desk, since that is the job you did not apply for. [What an AI receptionist is](/blog/what-is-an-ai-receptionist/) explains the first piece, and [how to automate a small business](/blog/how-to-automate-a-small-business/) shows the order to add the rest."]),
 "ai-assistant-for-families": ("Start small and keep the control", [
   "If you try something like this, start with one recurring headache rather than the whole household. Pick the thing that costs you the most mental space, such as school schedules, appointment reminders, or the weekly meal plan, and hand only that over for two weeks.",
   "Decide in advance what the assistant may do without asking and what always needs your yes. Reminders and drafts are low risk. Anything involving payments, sharing a child's information, or messaging someone on your behalf should wait for your approval. A tool you can switch off and see into is one you will actually keep using.",
   "The same discipline runs the business side of ART3RY: small scope, clear boundaries, and a person who approves the sensitive parts. [Hire an AI employee](/blog/hire-an-ai-employee/) describes that model for owners."]),
}

FIXES = [
 # (slug, regex, replacement)
 ("all-in-one-business-software-kill-saas-bloat",
  r"Studies of small business software stacks routinely find owners running well over a dozen tools, and plenty cross 30 or 40 without noticing\.?",
  "I have not seen a reliable census of small business stacks, so count your own: most owners I talk to are running more tools than they would have guessed."),
 ("instant-lead-response-software-5-minute-rule",
  r"There&#x27;s a well-documented pattern in lead response: contact a new lead within five minutes",
  "There&#x27;s a pattern in lead response that I have seen hold up in my own business: contact a new lead within five minutes"),
]

G_LOCAL = ("[How Google decides local ranking: relevance, distance, and prominence](https://support.google.com/business/answer/7091)")
HBR = ("[The Short Life of Online Sales Leads, Harvard Business Review](https://hbr.org/2011/03/the-short-life-of-online-sales-leads)")
G_HELP = ("[Google: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)")
SOURCES = {
 "how-to-rank-on-google-maps": [G_LOCAL], "why-is-my-business-not-showing-up-on-google": [G_LOCAL],
 "fresno-seo-for-small-business": [G_LOCAL, G_HELP], "local-seo-automation": [G_LOCAL],
 "do-i-need-a-website-for-my-business": [G_HELP],
 "after-hours-answering-service": [HBR], "missed-call-lead-capture": [HBR],
 "ai-receptionist-for-contractors-missed-calls": [HBR], "how-long-does-a-call-ring-before-voicemail": [HBR],
 "how-to-reduce-no-shows": [], "how-to-get-more-customers": [G_LOCAL, HBR],
}

def block(slug):
    href, label, lead = NEXT[slug]
    tail = TAIL["default"]
    return ('<!-- next-step --><h2>Next step</h2><p>' + lead + ' <a href="/diagnostic/">free diagnostic</a> '
            + tail + ' If you would rather hand the work off, see <a href="' + href + '">' + label + '</a>.</p><!-- /next-step -->')

_LINK = re.compile(r"\[([^\]\[]+)\]\((/[A-Za-z0-9\-/]*/)\)")
_EXT = re.compile(r"\[([^\]\[]+)\]\((https://[^)\s]+)\)")
def md(p):
    p = p.replace("&", "&amp;").replace("'", "&#x27;") if False else p
    p = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', p)
    p = _EXT.sub(lambda m: f'<a href="{m.group(2)}" rel="noopener" target="_blank">{m.group(1)}</a>', p)
    return p

def main():
    for slug in sorted(set(NEXT) | set(EXPAND) | set(SOURCES)):
        f = ROOT / "blog" / slug / "index.html"
        h = f.read_text(encoding="utf-8")
        orig = h
        for s, rx, rep in FIXES:
            if s == slug:
                h = re.sub(rx, rep, h)
        add = ""
        if slug in EXPAND and "<!-- oct-expand -->" not in h:
            h2, ps = EXPAND[slug]
            add += "<!-- oct-expand --><h2>" + h2 + "</h2>" + "".join("<p>" + md(p) + "</p>" for p in ps) + "<!-- /oct-expand -->"
        if slug in NEXT and "<!-- next-step -->" not in h and 'href="/diagnostic/' not in h:
            add += block(slug)
        if slug in SOURCES and SOURCES[slug] and "<!-- sources -->" not in h:
            add += "<!-- sources --><p><strong>Further reading:</strong> " + " &middot; ".join(md(x) for x in SOURCES[slug]) + "</p><!-- /sources -->"
        if add:
            if "<h2>FAQ</h2>" not in h:
                raise SystemExit("no FAQ anchor in " + slug)
            h = h.replace("<h2>FAQ</h2>", add + "<h2>FAQ</h2>", 1)
        if h != orig:
            f.write_text(h, encoding="utf-8"); print("fixed", slug)

if __name__ == "__main__":
    main()
