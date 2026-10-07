"""The four California industry pillar pages. Rules cited here were checked against
the CSLB, DRE and State Bar sources (see CA_PAGES_PLAN.md)."""


def mk(**kw):
    kw.setdefault("kind", "industry")
    kw["crumb"] = kw["name"]
    kw.setdefault("service_type", "Local SEO, website and lead follow-up")
    return kw


LAW = mk(
    slug="law-firms", name="Law firms in California", short="Law firms",
    title="California Law Firm Marketing: Found, Compliantly | ART3RY",
    title_short="California law firm marketing",
    meta="Growth work for California law firms: practice-area pages, a tuned Google profile, and intake follow-up, built around the State Bar's advertising rules.",
    kicker="Law firms",
    h1="California law firm marketing<br>that respects the rules.",
    sub="Practice-area pages, a complete profile and a fast intake reply, built with the State Bar's advertising rules in mind.",
    hub_line="Practice-area pages and intake follow-up that stay inside the State Bar's advertising rules.",
    lead=[
        "A person who needs a lawyer is rarely browsing. They have a problem, a deadline or a fear, and they search for a practice area plus a place: a family law attorney in a county, a criminal defense lawyer near a courthouse, an immigration lawyer who speaks their language. The firm that appears, reads clearly and answers fast gets the first conversation.",
        "I work remotely with California businesses and do not run a law office or give legal advice. What I build is the marketing system around a firm: the pages, the profile, the intake follow-up. The legal judgment stays with you, and so does the final say on every claim a page makes.",
    ],
    secs=[
        ("Advertising rules are part of the design", [
            "California lawyers advertise under the State Bar's Rules of Professional Conduct, in the chapter on information about legal services (rules 7.1 through 7.5, effective November 1, 2018). The core rule is simple to state: a communication cannot be false or misleading, and that includes leaving out a fact needed to keep it from misleading. A rule on language also says a lawyer may not imply they can provide services in a language other than English unless they actually can.",
            "I treat those rules as a constraint at the drafting stage. Pages describe what a firm does and who it helps, avoid guarantees, and keep claims you can stand behind. Before anything publishes, the attorney reviews it. I am not a substitute for your own read of the rules or for ethics counsel.",
        ]),
        ("How clients actually search", [
            "Searches cluster around practice area, location and urgency. A firm that handles several practice areas does better with a distinct page for each than with one page listing everything. A firm that serves several counties benefits from pages that reflect the courts and communities of each, rather than a swapped city name.",
            "Local details matter and are easy to get wrong, so they are written with the firm, not for it. Some of the details are on the city and combination pages, such as the [Fresno law firm page](/california/fresno-law-firms/) and the [Los Angeles law firm page](/california/los-angeles-law-firms/).",
        ]),
        ("Intake is where marketing pays off", [
            "A call that goes to voicemail at 7 PM on a Friday is often a call that hires the next firm. A good intake path acknowledges the inquiry immediately, collects the basics and tells the person what happens next. It never gives legal advice and never promises an outcome.",
            "That is the same system I describe on the [AI receptionist for law firms](/assistant-for-law-firms/) page: it covers the phone. This page is about being found in the first place and what the site and profile need to do once you are.",
        ]),
        ("What I would build for a California firm", [
            "In order of impact:",
        ], [
            "A distinct, honest page for each practice area and each county or city you really serve.",
            "A complete [Google Business Profile](/google-business-profile-optimization/) for each office you actually staff.",
            "A [website](/services/websites/) that makes the next step obvious and works on a phone.",
            "[Intake follow-up](/services/lead-follow-up/) that answers instantly and keeps the conversation moving.",
            "Review requests that follow the State Bar's rules and your own judgment.",
        ]),
    ],
    faq=[
        ("Can you guarantee clients or rankings?", "No, and a law firm should not publish such a promise either. I promise the work and honest reporting."),
        ("Do you give legal advice or write legal content?", "No. I build the marketing system. Anything touching the law is drafted with and approved by the attorney."),
        ("Do you have an office in California?", "No. Art3ry is remote and works with businesses across the state."),
        ("How do you handle advertising rules?", "I draft with the State Bar's chapter 7 rules in mind, keep claims factual, and have the attorney review every page. Ethics questions belong with your own counsel."),
        ("Where do I start?", "With the free diagnostic. It shows how a prospective client sees your firm and what I would fix first."),
    ],
    cta_h2="Let me look at how a new client finds your firm.",
    cta_p="The free diagnostic covers your visibility, your pages and your intake speed.",
)

CONTRACTORS = mk(
    slug="contractors", name="Contractors in California", short="Contractors",
    title="Contractor Marketing in California: More Booked Jobs | ART3RY",
    title_short="California contractor marketing",
    meta="Growth work for California contractors: service-area pages, a tuned Google profile with your license number, and missed-call follow-up that books jobs.",
    kicker="Contractors",
    h1="California contractor marketing<br>for people who are on a job.",
    sub="You are under a sink or on a roof. The customer calls the next name. This is how you stop losing that job.",
    hub_line="Service-area pages, license number done right and follow-up while you are on the tools.",
    lead=[
        "Contractors lose work in a very specific way. The phone rings while you are on a roof, in a crawlspace or driving between jobs. The customer does not leave a voicemail, they call the next result. Meanwhile the businesses with the best marketing are often not the best contractors, just the most visible and the fastest to reply.",
        "I work remotely with California businesses, so I have no shop near you. I build the system around your work: being visible where you serve, looking trustworthy on first contact, and catching every call you cannot pick up.",
    ],
    secs=[
        ("Your license number is part of the ad", [
            "California requires contractors to include their license number in advertising. The Contractors State License Board's rule under Business and Professions Code section 7030.5 reaches online ads, business cards, vehicle lettering and promotional materials, and the number has to be preceded by \"License #\" or \"Lic. #\" and be clearly legible. Radio spots under 30 seconds are exempt.",
            "On a website that means the number belongs in the header or footer of every page and on every ad, not buried in a fine-print paragraph. It also builds trust, since customers can verify a license on the CSLB site in a minute, and the ones who do are often the ones ready to hire. Check the current rules directly with CSLB for your specific situation.",
        ]),
        ("Service areas, not one big page", [
            "Contractors serve places, and customers search places. A roofer working a few cities does better with a real page for each than with a single page listing every town. The detail that makes a page real is the work itself: housing age, climate, permit habits and typical problems in that area.",
            "I go deeper on how this plays out in [Sacramento](/california/sacramento-contractors/) and the [Inland Empire](/california/inland-empire-contractors/), where heat, growth and distances shape the trade differently.",
        ]),
        ("Catch the call you cannot answer", [
            "Rankings only pay if the phone gets answered. A missed-call text-back that says you are on a job and will call back, with a link to describe the work, saves a large share of the jobs that would otherwise vanish. It takes minutes to set up and works while you work.",
            "That is the same logic as the [AI receptionist for contractors](/assistant-for-contractors/): this page covers getting found, that page covers answering the phone.",
        ]),
        ("What I would build for a California contractor", [
            "In order:",
        ], [
            "Service and service-area pages for what you do best and where you actually work.",
            "A [Google Business Profile](/google-business-profile-optimization/) with license number, categories, photos and a truthful service area.",
            "A [phone-first website](/services/websites/) with one-tap calling and quote requests.",
            "[Missed-call and quote follow-up](/services/lead-follow-up/) that keeps warm leads from cooling.",
            "A steady review habit, asked for at the end of a finished job.",
        ]),
    ],
    faq=[
        ("Do I need my license number on my website?", "California requires it in advertising, which covers online ads and promotional materials. Putting it in the header or footer of every page is the simplest way to comply."),
        ("Do you do paid ads?", "My focus is organic search and follow-up, so work keeps paying when the budget stops."),
        ("Do you have an office in California?", "No. Art3ry is remote and works with businesses across the state."),
        ("I only get work by referral. Is this worth it?", "A referred customer still looks you up. A strong profile and site convert more of them, and organic pages bring in the ones you never meet."),
        ("What do I do first?", "Run the free diagnostic. It shows what a customer sees when they search your trade in your area."),
    ],
    cta_h2="Stop losing jobs to the next name on the list.",
    cta_p="The free diagnostic checks your visibility, your license display and what happens to a missed call.",
)

REAL_ESTATE = mk(
    slug="real-estate", name="Real estate agents in California", short="Real estate",
    title="California Real Estate Agent Marketing | ART3RY",
    title_short="California real estate marketing",
    meta="Growth work for California real estate agents: neighborhood pages, a tuned Google profile, and instant lead response, with DRE license display handled.",
    kicker="Real estate",
    h1="California real estate marketing<br>built on neighborhood authority.",
    sub="The agent who owns a neighborhood gets the listing call. Pages, profile and fast response are how you own it.",
    hub_line="Neighborhood authority pages and instant lead response, with DRE license display handled.",
    lead=[
        "Buyers and sellers rarely hire the biggest brand. They hire the agent who seems to know their street and who answered first. In a state this varied, that means neighborhood knowledge expressed online: pages that read as if someone who works there wrote them, and a reply to an inquiry in minutes, not hours.",
        "Art3ry is remote and works with California businesses. I do not sell homes and I am not a broker. I build the marketing system around an agent or team, and the licensed professional approves every claim.",
    ],
    secs=[
        ("License display is not optional", [
            "California requires real estate licensees to disclose their license identification number on solicitation materials intended to be the first point of contact with consumers. The Department of Real Estate's rule under Business and Professions Code section 10140.6 covers things like business cards, flyers, mail and internet advertising, with some exceptions such as certain print ads and \"For Sale\" signs. The type size cannot be smaller than the smallest type used in the material.",
            "On a site, that means your DRE number belongs in the header or footer, and on every lead-gen page or flyer. Confirm current requirements with the DRE for your specific materials.",
        ]),
        ("Neighborhood authority beats a general listing page", [
            "Search results for real estate are crowded with national portals. A local agent cannot out-spend them and does not need to. What portals cannot do is explain the difference between two nearby streets, describe what a school boundary means for a buyer, or tell a seller what usually happens on a street like theirs.",
            "I build pages around the neighborhoods you really work. The detail has to come from you, since you are the one who knows it. My part is structure, schema and consistency. Some of that is on the city pages, and the [San Diego real estate page](/california/san-diego-real-estate/) shows how local context changes the plan.",
        ]),
        ("Speed to lead", [
            "A buyer who asks about a listing is usually asking several agents. The first useful reply tends to win the conversation. If you are at a showing, an instant acknowledgement with your next available time keeps the lead warm until you can call.",
            "That is the topic of the [AI receptionist for real estate](/assistant-for-real-estate/) page. Here the focus is getting the lead in the first place.",
        ]),
        ("What I would build for a California agent", [
            "In order:",
        ], [
            "A page for each neighborhood or city where you want to be known, with honest local detail.",
            "A [Google Business Profile](/google-business-profile-optimization/) that carries your DRE number and your real service area.",
            "A [website](/services/websites/) that makes calling or booking a showing one tap.",
            "[Instant lead response](/services/lead-follow-up/) and a nurture sequence for people not ready yet.",
            "A review flow from closed clients.",
        ]),
    ],
    faq=[
        ("Do I need my DRE number on my website?", "Real estate licensees must disclose it on first-point-of-contact solicitation materials, and the header or footer of every page is the safest place for it."),
        ("Can you promise listings?", "No. I promise the work and honest numbers."),
        ("Do you have an office in California?", "No. Art3ry is remote and works with businesses across the state."),
        ("Should I compete with the national portals?", "No. Compete on local knowledge and speed, which portals cannot copy."),
        ("Where do I start?", "The free diagnostic shows how you look to a buyer or seller searching your area."),
    ],
    cta_h2="Own the neighborhoods you already know.",
    cta_p="The free diagnostic shows where you are visible, where you are not, and how fast you respond.",
)

SALONS = mk(
    slug="salons-med-spas", name="Salons and med spas in California", short="Salons and med spas",
    title="California Salon and Med Spa Marketing | ART3RY",
    title_short="California salon and med spa marketing",
    meta="Growth work for California salons and med spas: a profile that books, honest service pages, and reminders that cut no-shows. Remote, statewide.",
    kicker="Salons and med spas",
    h1="California salon and med spa marketing<br>that fills the chair.",
    sub="A great stylist with an empty chair has a visibility problem or a no-show problem. Usually both.",
    hub_line="A profile that books, honest service pages and reminders that cut no-shows.",
    lead=[
        "Salons and med spas are discovered on the map, judged by photos and reviews, and booked on a phone. The business that makes those three steps easy gets the appointment. The ones with beautiful work but a half-filled profile and a booking process that needs a phone call quietly lose the client.",
        "I work remotely with California businesses and do not own a salon or practice medicine. I build the marketing system, and the licensed professionals in your business are responsible for what is claimed about their services.",
    ],
    secs=[
        ("Be careful what the page promises", [
            "Cosmetology and barbering businesses in California operate under the Board of Barbering and Cosmetology, which licenses establishments as well as individuals. Med spas add another layer: services such as injectables and lasers are medical, and the Medical Board of California expects them to be performed by appropriately licensed people under physician supervision.",
            "For marketing, that means service pages should match who really performs each service and under what supervision. Do not describe a procedure in a way that suggests a different provider than the one who does it. I draft carefully, and your own compliance advisor should confirm anything medical. This is not legal advice.",
        ]),
        ("The profile is the storefront", [
            "Most new clients meet you on a map listing. Complete categories, accurate hours, a full service list, current photos of real work and steady reviews often matter more than the website itself. Reviews matter twice, since they influence ranking and the decision to book.",
            "A good review habit asks at the right moment, such as right after a good appointment, and never pressures. I build the flow so it runs without a front desk remembering. My notes on the [Google Business Profile](/google-business-profile-optimization/) page go deeper.",
        ]),
        ("No-shows are a marketing problem too", [
            "An empty chair from a no-show costs as much as one from a slow week. Confirmation and reminder messages, plus a simple way to reschedule, cut it down. A waitlist that fills a canceled slot turns a loss into a booking.",
            "This is the same logic as the [AI receptionist for salons and med spas](/assistant-for-salons/): this page is about being found and booked, that one is about the phone and the schedule. The [Orange County salon and med spa page](/california/orange-county-salons-med-spas/) shows how local context changes the plan.",
        ]),
        ("What I would build for a California salon or med spa", [
            "In order:",
        ], [
            "A [Google Business Profile](/google-business-profile-optimization/) built to the last field, with photos and services.",
            "Service pages that name each service honestly and who performs it.",
            "A [website](/services/websites/) with one-tap booking on a phone.",
            "[Reminders and rebooking](/services/automation/) that cut no-shows and bring clients back.",
            "A steady review flow.",
        ]),
    ],
    faq=[
        ("Do you handle medical claims for med spas?", "I write factual service descriptions and leave medical judgment and compliance to the licensed professionals and their advisors."),
        ("Can you promise a full calendar?", "No. I promise visibility work, easier booking and fewer no-shows, with honest numbers."),
        ("Do you have an office in California?", "No. Art3ry is remote and works with businesses across the state."),
        ("What matters more, my website or my profile?", "For most local appointment businesses, the profile is the first impression and the site finishes the job."),
        ("Where do I start?", "The free diagnostic shows what a new client sees and where bookings leak."),
    ],
    cta_h2="Keep the chair filled.",
    cta_p="The free diagnostic checks your profile, your booking path and your no-show leaks.",
)

INDUSTRIES = [LAW, CONTRACTORS, REAL_ESTATE, SALONS]
