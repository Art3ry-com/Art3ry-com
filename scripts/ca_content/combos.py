"""Six city x industry pages. Each exists only because the local detail changes the plan."""


def mk(**kw):
    kw.setdefault("kind", "combo")
    kw["crumb"] = kw["title_short"]
    kw.setdefault("service_type", "Local SEO, website and lead follow-up")
    return kw


FRESNO_LAW = mk(
    slug="fresno-law-firms", city="fresno", industry="law-firms", name="Fresno",
    title="Fresno Law Firm Marketing: Courts, Clients, Intake | ART3RY",
    title_short="Fresno law firm marketing",
    meta="Marketing for Fresno law firms: pages that reflect Fresno's state and federal courts, a tuned Google profile, and intake follow-up within State Bar rules.",
    kicker="Law firms in Fresno",
    h1="Fresno law firm marketing,<br>written around Fresno's courts.",
    sub="Fresno is home to a Court of Appeal and a federal courthouse. A firm here should read like it knows both.",
    hub_line="Fresno's appellate and federal courts, Valley clients and Spanish-speaking intake.",
    lead=[
        "Fresno is more than a county seat. It is the home of the California Court of Appeal for the Fifth Appellate District, and it is one of the two seats of the United States District Court for the Eastern District of California, alongside Sacramento. For a law firm, that means the legal community here is deeper than a city this size suggests, and clients searching for counsel often have matters that reach beyond the local superior court.",
        "Art3ry is remote and works with California businesses, so I do not have a Fresno office and I do not give legal advice. This page is the Fresno-specific plan for a firm. The general version, with the State Bar rules, is on the [California law firm page](/california/law-firms/), and the broader [Fresno overview](/california/fresno/) covers the city.",
    ],
    secs=[
        ("What Fresno changes about the pages", [
            "A firm in Fresno works across a wide area. Clients come from Clovis, Madera, Sanger and Kerman as well as from Fresno proper, and they travel along Highway 99, 41 and 180 to reach a downtown office near the courthouses. A page that names those communities, and the practical question of how to get to you, answers the first thing many clients wonder.",
            "Practice areas also have a Valley flavor. Fresno County is one of the nation's leading agricultural regions, so agricultural employment, land and business matters are a real category that a firm in Los Angeles or San Francisco would never write about. If your firm handles that work, a dedicated, factual page is a lane few competitors fill. If it does not, leave it out.",
        ]),
        ("Language and trust", [
            "Many Valley clients are more comfortable in Spanish, and a firm that really offers services in Spanish should say so plainly. California's rules on lawyer communications are explicit: a lawyer may not state or imply they can provide services in a language other than English unless they actually can. If the person who answers the phone speaks Spanish but the attorney does not, the page has to reflect that exactly.",
            "That precision builds trust. A prospective client reading carefully worded, accurate claims is more likely to call than one reading a vague promise. Every page I draft is reviewed by the attorney before it goes live.",
        ]),
        ("Intake that fits how Valley clients call", [
            "Many calls come from people who just left work or are in the middle of a hard day. A firm that answers a missed call with an immediate text, a short set of qualifying questions and a clear next step keeps the lead. A firm that sends it to voicemail usually does not.",
            "The same intake system runs behind the [AI receptionist for law firms](/assistant-for-law-firms/). It never gives legal advice and never promises an outcome.",
        ]),
        ("The Fresno plan, in order", [
            "What I would build, and in what order:",
        ], [
            "A distinct page per practice area, each written with the attorney, with no outcome promises.",
            "Community pages for Clovis, Madera and other places you really serve.",
            "A [Google Business Profile](/google-business-profile-optimization/) for your Fresno office, with accurate hours and categories.",
            "[Intake follow-up](/services/lead-follow-up/) with a Spanish option only if the firm can deliver it.",
            "A [website](/services/websites/) that loads fast on a phone and makes calling one tap.",
        ]),
    ],
    faq=[
        ("Why do Fresno firms need their own approach?", "The court structure, the agricultural economy and the language mix of the Valley change which pages matter and how they should read."),
        ("Can you promise Fresno clients or rankings?", "No, and a firm should not advertise such a promise. I promise the work and honest reporting."),
        ("Can my page say we serve Spanish-speaking clients?", "Only if the firm can really deliver services in Spanish. The State Bar's rules on language claims are specific, so have your own counsel confirm the wording."),
        ("Do you have a Fresno office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="See how a Fresno client finds your firm.",
    cta_p="The free diagnostic checks your pages, your profile and your intake speed.",
)

LA_LAW = mk(
    slug="los-angeles-law-firms", city="los-angeles", industry="law-firms", name="Los Angeles",
    title="Los Angeles Law Firm Marketing: Courts, Clients | ART3RY",
    title_short="Los Angeles law firm marketing",
    meta="Marketing for Los Angeles law firms: pages by practice area and courthouse region, a tuned Google profile, and intake follow-up within State Bar rules.",
    kicker="Law firms in Los Angeles",
    h1="Los Angeles law firm marketing<br>for a county, not a city.",
    sub="A client in Pasadena, one in Van Nuys and one in downtown often need the same firm and search for it very differently.",
    hub_line="Many courthouses, many sub-markets and practice areas that are specific to this region.",
    lead=[
        "Los Angeles County is a vast legal market, with a Superior Court that holds hearings across many courthouse locations and a federal Central District court with courthouses in downtown Los Angeles. A client's matter is often tied to a particular courthouse, and clients search with that in mind: a family law attorney near a certain courthouse, a criminal defense lawyer in a particular district.",
        "I work remotely with California businesses, have no Los Angeles office and do not give legal advice. This is the Los Angeles-specific plan for a firm. The statewide version, with the State Bar's advertising rules, is on the [California law firm page](/california/law-firms/), and the [Los Angeles overview](/california/los-angeles/) covers the city's sub-markets.",
    ],
    secs=[
        ("Location is a courthouse and a commute", [
            "Los Angeles clients think about location in terms of court assignment and drive time. A firm with an office in Encino and one in downtown draws different clients, and the pages should reflect that. Pasadena and Glendale are separate cities with their own communities, and a firm that serves them should say so rather than assuming one Los Angeles page covers everyone.",
            "I plan pages around the offices you staff and the courthouses where you appear. The detail has to come from the attorneys, since they know which locations they really work. My job is structure, consistency and schema so Google can read it.",
        ]),
        ("Practice areas with a Los Angeles accent", [
            "Entertainment is the obvious regional specialty, but it is also a good example of a niche where a general page would be useless. Employment, immigration, intellectual property and personal injury all play out differently here too. A firm that does one of these well should have a dedicated, factual page and not bury it in a list.",
            "The caution is the same as everywhere. A page must not be false or misleading, and California's rules on lawyer specialization claims and communications apply. Ask your own ethics counsel before claiming a specialty, a ranking or a result.",
        ]),
        ("Many languages, one rule", [
            "Los Angeles is a multilingual region. If your firm offers services in Korean, Spanish, Armenian or another language, say so on the relevant page in that language, as the rules contemplate, and only if someone at the firm really delivers it.",
            "The same discipline applies to the intake path. The first response a prospective client gets, whether by text or call, should match what the firm can really do, and should never offer legal advice.",
        ]),
        ("The Los Angeles plan, in order", [
            "What I would build, and when:",
        ], [
            "Practice-area pages, each written with the attorney and free of outcome promises.",
            "Office and sub-market pages for the places you really staff.",
            "A [Google Business Profile](/google-business-profile-optimization/) per staffed office.",
            "[Intake follow-up](/services/lead-follow-up/) that replies in minutes and routes by practice area.",
            "A [site](/services/websites/) that works on a phone in a courthouse hallway.",
        ]),
    ],
    faq=[
        ("Do I need a different page for each Los Angeles neighborhood?", "Only for places where you really have an office or regularly work. Separate cities like Pasadena and Glendale usually deserve their own pages."),
        ("Can I advertise a specialty?", "California has specific rules for claiming certification or specialization. Check with your own ethics counsel before publishing."),
        ("Do you give legal advice?", "No. I build the marketing system and the attorney approves every page."),
        ("Do you have a Los Angeles office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="See how a Los Angeles client finds your firm.",
    cta_p="The free diagnostic checks your pages, your profile and your intake speed.",
)

SAC_CONTRACTORS = mk(
    slug="sacramento-contractors", city="sacramento", industry="contractors", name="Sacramento",
    title="Sacramento Contractor Marketing: Heat, Homes, Suburbs | ART3RY",
    title_short="Sacramento contractor marketing",
    meta="Marketing for Sacramento contractors: pages for Midtown to Elk Grove, a tuned Google profile with your license number, and missed-call follow-up.",
    kicker="Contractors in Sacramento",
    h1="Sacramento contractor marketing,<br>from Midtown to Elk Grove.",
    sub="Old homes in the city, new builds in the suburbs and a summer that tests every system. The pages should reflect all three.",
    hub_line="Hot summers, historic neighborhoods and suburbs that each run their own permits.",
    lead=[
        "Sacramento is a contractor's market with two faces. Inside the city, historic neighborhoods such as East Sacramento, Midtown, Land Park and Curtis Park carry older housing and steady repair, remodel and restoration work. Around it, Elk Grove, Roseville, Folsom and Rancho Cordova are separate cities with their own growth, their own building departments and their own customers.",
        "I am remote and work with California businesses, so I have no Sacramento shop. This is the local plan for a contractor. The statewide version, including the license-number rule, is on the [California contractor page](/california/contractors/), and the [Sacramento overview](/california/sacramento/) covers the region.",
    ],
    secs=[
        ("Older homes are a page, not a footnote", [
            "A customer in East Sacramento or Midtown often owns a home with decades of history. The questions they ask are specific: old wiring, older plumbing, preserving original details, working in tight lots. A contractor who writes honestly about that work, using real examples from real jobs, stands out against a generic remodeling page.",
            "I help structure those pages and make them readable to Google. The photos and the lessons have to come from you, since I was not on the job. A few real project write-ups do more than a long list of services.",
        ]),
        ("Each suburb is its own jurisdiction", [
            "Elk Grove, Roseville, Folsom and the City of Sacramento each run their own building department, and permit practices differ. A contractor who works across them knows this, and a page that says so, for example by describing how you handle permits in that city, is more believable than one that treats the whole region as identical. Confirm the specifics with each city rather than assuming.",
            "The same goes for service area. Drive time across the region is real, and an honest list of the cities you serve, kept current, helps both customers and your Google profile.",
        ]),
        ("Summer sets the calendar", [
            "Hot Sacramento summers drive demand for cooling, roofing, insulation and shade work. Publish seasonal content in spring so pages are indexed by the time the heat arrives, and prepare your phone line for the weeks when it rings nonstop.",
            "A missed-call text-back that says you are on a job and links to a short quote form saves a large share of the calls that would otherwise go to the next result. It is the same logic as the [AI receptionist for contractors](/assistant-for-contractors/).",
        ]),
        ("The Sacramento plan, in order", [
            "What I would build, and when:",
        ], [
            "Neighborhood and suburb pages for the places you actually work, with real project detail.",
            "A [Google Business Profile](/google-business-profile-optimization/) showing your license number, services and an honest service area.",
            "Seasonal pages published ahead of the summer demand.",
            "[Missed-call and quote follow-up](/services/lead-follow-up/) that works while you are on the roof.",
            "A [phone-first website](/services/websites/) with one-tap calling.",
        ]),
    ],
    faq=[
        ("Do I need separate pages for Elk Grove and Roseville?", "If you serve them, yes. They are separate cities with their own customers and building departments."),
        ("Must my license number be on my site?", "California requires it in contractor advertising. The header or footer of every page is the simplest place for it."),
        ("When should I publish seasonal pages?", "Before the season. Pages need time to be crawled and trusted, so spring is right for summer demand."),
        ("Do you have a Sacramento office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="See what a Sacramento homeowner finds.",
    cta_p="The free diagnostic checks your visibility, your license display and what happens to a missed call.",
)

IE_CONTRACTORS = mk(
    slug="inland-empire-contractors", city="inland-empire", industry="contractors", name="Riverside and the Inland Empire",
    title="Inland Empire Contractor Marketing: Heat, Drives | ART3RY",
    title_short="Inland Empire contractor marketing",
    meta="Marketing for Inland Empire contractors: corridor-based service pages, a Google profile with your license number, and follow-up for the busiest weeks.",
    kicker="Contractors in the Inland Empire",
    h1="Inland Empire contractor marketing<br>that respects the drive.",
    sub="A job in Temecula and a job in Fontana are an hour apart. Your pages should say where you really work.",
    hub_line="Long drives, extreme heat and fast-growing communities across two counties.",
    lead=[
        "For a contractor, the Inland Empire is a geography problem first. Riverside County and San Bernardino County together cover Riverside, San Bernardino, Ontario, Fontana, Rancho Cucamonga, Corona, Moreno Valley, Redlands, Temecula and Murrieta, and a job at one end is a long drive from the other. Customers know it, and they pick the contractor who works near them.",
        "I work remotely with California businesses and have no Riverside shop. This is the Inland Empire plan for a contractor. The statewide version, including the license-number rule, is on the [California contractor page](/california/contractors/), and the [Inland Empire overview](/california/inland-empire/) covers the region.",
    ],
    secs=[
        ("Choose a corridor, then own it", [
            "The Inland Empire is organized around its freeways. Contractors who work the 91 corridor around Corona and Riverside, the 10 through Redlands and Ontario, or the 15 through Temecula and Murrieta, are serving different markets. A page that names the corridor and the cities along it reads as local, while a page claiming the whole region reads as an aggregator.",
            "Pick the stretch you can reach in a reasonable drive, build for it, and let your Google profile say exactly the same thing. Overclaiming a service area is a common way to lose trust with customers and with Google.",
        ]),
        ("Heat changes the work, and the desert changes it more", [
            "Summers are hot across the region, and the Coachella Valley around Palm Springs and the High Desert beyond are desert climates in their own right. Cooling, roofing, pool and landscape work run on a seasonal clock, and desert jobs involve different materials and different homeowner concerns than the western valleys.",
            "If you work in the desert, write for it with real project detail. If you do not, leave it out. A page honest about its limits earns more trust than one that claims everything.",
        ]),
        ("A logistics economy and fast growth", [
            "Ontario's warehousing and logistics economy creates steady commercial work alongside the household customers. Many communities have also grown quickly, so there is constant demand for work on newer homes and for upgrades after a move. Separate pages for commercial and residential work help each audience find you.",
            "In busy weeks the phone will outrun you. A missed-call text-back and a short quote form keep the lead warm until you can call. That is the same logic as the [AI receptionist for contractors](/assistant-for-contractors/).",
        ]),
        ("The Inland Empire plan, in order", [
            "What I would build, and when:",
        ], [
            "Corridor and city pages for the places you really serve, with real project detail.",
            "A [Google Business Profile](/google-business-profile-optimization/) with your license number and a truthful service area.",
            "Separate residential and commercial pages if you do both.",
            "[Follow-up automation](/services/automation/) for the high-volume weeks.",
            "A [phone-first site](/services/websites/) with one-tap calling and quote requests.",
        ]),
    ],
    faq=[
        ("How many cities should I list?", "Only those you can reach in a reasonable drive. A short, true list is better for customers and for ranking."),
        ("Do desert jobs need their own pages?", "If you do them regularly, yes. The materials, climate and concerns differ from the western valleys."),
        ("Must my license number be on my site?", "California requires it in contractor advertising. The header or footer of every page is the simplest place."),
        ("Do you have an Inland Empire office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="Map the corridor you really work.",
    cta_p="The free diagnostic checks your visibility in the cities you serve and your response to missed calls.",
)

SD_REAL_ESTATE = mk(
    slug="san-diego-real-estate", city="san-diego", industry="real-estate", name="San Diego",
    title="San Diego Real Estate Marketing: Beach to Base | ART3RY",
    title_short="San Diego real estate marketing",
    meta="Marketing for San Diego real estate agents: neighborhood and relocation pages, a tuned Google profile with your DRE number, and instant lead response.",
    kicker="Real estate in San Diego",
    h1="San Diego real estate marketing<br>for a market that keeps moving in.",
    sub="Coastal, central, inland and the military. Each buys, and searches, differently.",
    hub_line="A relocation market shaped by the Navy, the Marines and a binational region.",
    lead=[
        "San Diego has a feature most California markets do not: a constant, built-in stream of newcomers tied to the military. Naval Base San Diego is the home port of the Pacific Fleet, and Marine Corps Air Station Miramar and Camp Pendleton sit in the county. Families arrive on orders, need a home on a timeline, and search from scratch.",
        "Art3ry is remote and works with California businesses. I am not a broker and I do not sell homes. This is the San Diego plan for an agent. The statewide version, including the DRE license rule, is on the [California real estate page](/california/real-estate/), and the [San Diego overview](/california/san-diego/) covers the county.",
    ],
    secs=[
        ("Write for the family that is arriving", [
            "A relocating family asks different questions from a lifelong local. How far is the base from this neighborhood? What does a commute look like? Which communities suit a short timeline? An agent who answers those on a dedicated page earns searches that a generic listing page never will.",
            "I help structure those pages so Google can read them. The knowledge has to be yours: you know which neighborhoods work for which commutes. Be careful with promises about financing or timelines, which belong to lenders and not to a marketing page.",
        ]),
        ("The county has clusters", [
            "Coastal neighborhoods such as La Jolla, Pacific Beach and Point Loma attract a different buyer than the central neighborhoods of North Park, Hillcrest and Mission Valley, and both differ from inland Escondido and El Cajon or from south county Chula Vista. A strong agent chooses one or two clusters and writes with real depth.",
            "The border adds another layer. The region's binational economy and large bilingual population mean that Spanish-language pages can reach buyers and sellers who would otherwise never find you. Offer them only if you can really serve in Spanish.",
        ]),
        ("License display and lead speed", [
            "Your DRE license number has to appear on first-point-of-contact solicitation materials, which includes your website and internet advertising. The header or footer of every page is the safe place. Confirm the specifics with the DRE.",
            "Relocating buyers usually contact several agents at once, often from another state and another time zone. A reply within minutes, including evenings, is a real competitive edge. It is the same idea behind the [AI receptionist for real estate](/assistant-for-real-estate/).",
        ]),
        ("The San Diego plan, in order", [
            "What I would build, and when:",
        ], [
            "A relocation page covering the communities near the bases you know best.",
            "Neighborhood pages for the one or two clusters where you really work.",
            "A [Google Business Profile](/google-business-profile-optimization/) carrying your DRE number and an honest service area.",
            "[Instant lead response](/services/lead-follow-up/) that works in any time zone.",
            "A [website](/services/websites/) that makes calling or booking a showing one tap.",
        ]),
    ],
    faq=[
        ("Should I build a page for military families?", "If you work with them regularly, yes. Keep it factual and avoid promises about loans or timelines."),
        ("Must my DRE number be on my site?", "Real estate licensees must disclose it on first-point-of-contact solicitation materials. Put it in the header or footer."),
        ("Can I advertise in Spanish?", "Only if you can really serve clients in Spanish. Say what you can actually deliver."),
        ("Do you have a San Diego office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="See how a San Diego buyer finds you.",
    cta_p="The free diagnostic checks your neighborhood pages, your profile and how fast you reply.",
)

OC_SALONS = mk(
    slug="orange-county-salons-med-spas", city="orange-county", industry="salons-med-spas", name="Orange County",
    title="Orange County Salon and Med Spa Marketing | ART3RY",
    title_short="Orange County salon and med spa marketing",
    meta="Marketing for Orange County salons and med spas: city-by-city profiles, honest service pages, and booking reminders that cut no-shows.",
    kicker="Salons and med spas in Orange County",
    h1="Orange County salon and med spa<br>marketing, city by city.",
    sub="Newport Beach, Irvine, Huntington Beach and Anaheim are a short drive apart and very different clients.",
    hub_line="Newport, Irvine, Laguna and Anaheim, each a different client and a different competitor.",
    lead=[
        "Orange County is dense with beauty and wellness businesses, and the competition is a short drive away in every direction. A client in Newport Beach, one in Irvine and one in Huntington Beach will each choose from a handful of nearby options, usually from a map listing, and usually within a few minutes.",
        "I am remote and work with California businesses, so there is no Orange County salon behind this page. The statewide version, with the licensing cautions, is on the [California salon and med spa page](/california/salons-med-spas/), and the [Orange County overview](/california/orange-county/) covers the county.",
    ],
    secs=[
        ("One city at a time", [
            "A client searches for the city she lives or works in. Newport Beach and Laguna Beach on the coast, Irvine as a planned city anchored by the University of California, Irvine, Huntington Beach, Costa Mesa and Anaheim each have a distinct feel. A salon should choose the one or two cities where it really draws clients and build a profile and page for each.",
            "Mind the boundary. Orange County meets Los Angeles County at the north and west, and clients cross it easily. If you also draw from Long Beach or Seal Beach, a separate page can serve them.",
        ]),
        ("Visitors and locals, handled differently", [
            "Anaheim is a major tourism hub with Disneyland at its center, and the coast draws visitors too. A business near those areas can serve both: visitors who need a quick, easy booking and locals who want a regular chair. Do not blur them. A page for one audience, honest about what it offers, beats a page that tries to be for everyone.",
            "Photos and reviews do the heavy lifting here. A complete profile with current, real photos of the work, and steady reviews, is often the deciding factor between two similar salons.",
        ]),
        ("Med spas: precise and careful", [
            "Where a med spa offers injectables or lasers, those are medical services. The Medical Board of California expects them to be performed by appropriately licensed professionals under physician supervision, and a salon licensed by the Board of Barbering and Cosmetology cannot offer them on its own license. Marketing pages should match exactly who performs each service.",
            "I draft factual descriptions and leave medical judgment to your licensed professionals and their advisors. This is not legal advice.",
        ]),
        ("The Orange County plan, in order", [
            "What I would build, and when:",
        ], [
            "A complete [Google Business Profile](/google-business-profile-optimization/) for each location, with real photos and services.",
            "City pages for the one or two cities where you draw clients.",
            "Honest service pages that say who performs each service.",
            "[Reminders and rebooking](/services/automation/) that cut no-shows.",
            "A [website](/services/websites/) where booking takes under a minute on a phone.",
        ]),
    ],
    faq=[
        ("Should I list every Orange County city?", "No. List the ones you really draw clients from. A short, true list is more credible."),
        ("Can my salon advertise injectables?", "Injectables are medical services. Check with your licensed professionals and compliance advisor about who may perform and advertise them."),
        ("Do reminders really cut no-shows?", "Confirmations and reminders are a standard way to reduce them, and a waitlist can fill the slots that do open."),
        ("Do you have an Orange County office?", "No. Art3ry is remote and works with businesses across California."),
    ],
    cta_h2="See what a new Orange County client finds.",
    cta_p="The free diagnostic checks your profile, your booking path and your no-show leaks.",
)

COMBOS = [FRESNO_LAW, LA_LAW, SAC_CONTRACTORS, IE_CONTRACTORS, SD_REAL_ESTATE, OC_SALONS]
