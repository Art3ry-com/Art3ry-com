"""City pages, batch 1: Los Angeles, San Diego, San Jose, San Francisco, Sacramento, Fresno.
Every geographic name here was checked against Wikipedia (see CA_PAGES_PLAN.md). No statistics."""


def mk(**kw):
    kw.setdefault("kind", "city")
    kw["crumb"] = kw["name"]
    kw.setdefault("service_type", "Local SEO, website and lead follow-up")
    return kw


LOS_ANGELES = mk(
    slug="los-angeles", name="Los Angeles",
    title="Los Angeles Business Growth: Be Found Where You Serve | ART3RY",
    title_short="Los Angeles business growth",
    meta="Remote growth work for Los Angeles service businesses: area pages for the Valley, Westside and South Bay, a tuned profile, and fast follow-up.",
    kicker="Los Angeles",
    h1="Los Angeles is twenty<br>markets wearing one name.",
    sub="A customer in Van Nuys and a customer in San Pedro both search for a Los Angeles business, and they are not looking for the same one.",
    hub_line="Many markets under one name: the Valley, the Westside, the South Bay and the east side.",
    lead=[
        "Most advice about ranking in Los Angeles treats the city as a single target. It is not. The city of Los Angeles runs from San Pedro in the south up into the San Fernando Valley, and inside and around it sit separate cities like Santa Monica, Beverly Hills, Glendale, Pasadena and Burbank. Customers know this even when marketers forget it. Someone in Sherman Oaks wants a business that works in Sherman Oaks.",
        "I run growth work for California service businesses remotely, over email and video. I do not have an office in Los Angeles and I will not pretend to. What I bring is the system: pages that match how Angelenos split up their own city, a profile that tells Google where you actually work, and follow-up that answers the inquiry before the next business does.",
    ],
    secs=[
        ("How the map is carved up", [
            "Think in sub-markets, because customers do. The San Fernando Valley (Encino, Van Nuys, Sherman Oaks, Woodland Hills) is its own world. The Westside around Westwood and Venice is another. Hollywood, Echo Park and Koreatown sit in the central core, Boyle Heights anchors the east side, and the South Bay and the harbor area around San Pedro pull a different customer again.",
            "The practical effect is that a single page reading \"Los Angeles plumber\" or \"Los Angeles attorney\" is a weak answer to nearly every real search. A person typing a neighborhood, a freeway exit or a nearby city wants proof you serve that spot.",
        ]),
        ("How people search here", [
            "In a metro this spread out, the phrasing carries the location. Expect searches that pair your trade with a neighborhood (Encino, Westwood, Koreatown), with a neighboring city, or with a freeway corridor people use to describe where they live. Before I build anything I run your trade through those modifiers and look at who shows up on the map and in the organic results for each one.",
            "What I check on competitors is structural, not gossip: does their site have a real page for each area they serve, or one blanket Los Angeles page? Is their profile's service area filled in? Gaps there are where a smaller business can win.",
        ]),
        ("What I would build first for a Los Angeles business", [
            "The first ninety days follow the geography. Pick the three or four sub-markets where your best customers live and where you can really show up, and build for those before anything else.",
        ], [
            "A real service page per sub-market you work in, written around that part of town rather than swapped city names.",
            "A [Google Business Profile](/google-business-profile-optimization/) with the service area, categories and services filled to the last field.",
            "Review requests timed to the finished job, so reviews arrive steadily instead of in a burst.",
            "A [fast follow-up system](/services/lead-follow-up/) so the Saturday-night inquiry gets an answer before Monday.",
            "A [site built to convert](/services/websites/) the traffic those pages bring, with click-to-call that works on a phone in traffic.",
        ]),
    ],
    ind_notes={
        "law-firms": "Los Angeles attorneys compete court by court and practice area by practice area. See the full plan on the [law firm page](/california/law-firms/), and the [Los Angeles law firm page](/california/los-angeles-law-firms/) for the local specifics.",
        "contractors": "Contractors here win by sub-market, because a job across the Santa Monica Mountains is a different trip than one in the Valley. The [contractor page](/california/contractors/) covers the system.",
        "real-estate": "Agents are known by neighborhood in Los Angeles more than almost anywhere. The [real estate page](/california/real-estate/) shows how I build that.",
        "salons-med-spas": "Salons and med spas live and die on discovery and bookings. The [salon and med spa page](/california/salons-med-spas/) covers the booking and no-show side.",
    },
    nearby=["long-beach", "orange-county", "inland-empire"],
    faq=[
        ("Do you have an office in Los Angeles?", "No. Art3ry works remotely with businesses across California. Everything happens over email and video, and you see each piece of work live on your own site."),
        ("Which part of Los Angeles should I focus on first?", "The part where your best customers already live and where you can serve them quickly. I look at where your current jobs come from and build there first, then expand."),
        ("Why not one big Los Angeles page?", "Because it answers almost no real search well. People search by neighborhood or nearby city, so each area you serve deserves a page that proves it."),
        ("Can you promise a top ranking in Los Angeles?", "No. Nobody controls Google. I promise the work, the order it ships in, and honest numbers as they move."),
    ],
    cta_h2="Tell me which part of town pays your bills.",
    cta_p="The free diagnostic shows where you are invisible in your own sub-markets and what I would fix first.",
)

SAN_DIEGO = mk(
    slug="san-diego", name="San Diego",
    title="San Diego Business Growth: Coast, Inland and Border | ART3RY",
    title_short="San Diego business growth",
    meta="Remote growth work for San Diego County businesses: pages for La Jolla to Chula Vista, a tuned Google profile, and follow-up that does not miss calls.",
    kicker="San Diego",
    h1="San Diego searches change<br>every ten miles.",
    sub="La Jolla, North Park, El Cajon and Chula Vista are all San Diego to a customer, and each one searches differently.",
    hub_line="A coastline, a navy town and a border region, each searching in its own way.",
    lead=[
        "San Diego is a good example of a market where the label hides the structure. The city includes La Jolla, Pacific Beach, Point Loma, Ocean Beach, Mission Valley, North Park, Hillcrest and Clairemont, and the county around it adds Chula Vista, El Cajon, Escondido, Oceanside, Carlsbad and Encinitas. A customer almost always searches with one of those names attached.",
        "I work with California businesses remotely, so I do not claim an office in San Diego. I do bring a method that fits how this county is laid out: cover the coastal, central and inland clusters separately, and make each one believable.",
    ],
    secs=[
        ("Three clusters, three kinds of customer", [
            "The coastal cluster (La Jolla, Pacific Beach, Ocean Beach, Point Loma) leans on visitors, renters and higher-touch home services. The central cluster (Downtown, Little Italy, North Park, Hillcrest, Mission Valley) is dense and walkable, and customers there often decide from the map in seconds. The inland and south county cluster (El Cajon, Escondido, Chula Vista) covers a different set of households and a different search vocabulary.",
            "Treating those as one audience is how businesses end up with a generic page that fits nobody. The better move is to choose the one or two clusters you serve best and build a distinct, specific page for each.",
        ]),
        ("The two things unique to San Diego", [
            "First, the military. Naval Base San Diego is the home port of the Pacific Fleet, and Marine Corps Air Station Miramar and Camp Pendleton are in the county. A steady flow of service members and families arrives and leaves, and many of them search from scratch for a dentist, a mover, a landscaper or an agent. A page that speaks to newcomers, with clear service areas near the bases, earns a real audience here.",
            "Second, the border. Tijuana sits right across it, and the region has a binational economy and a large bilingual population. If you serve Spanish-speaking customers, say so plainly on the pages, and make sure whoever answers can actually deliver it. Do not advertise a language you cannot back up.",
        ]),
        ("What I would build first for a San Diego business", [
            "The order is the same as everywhere, adapted to the county.",
        ], [
            "A page for each cluster you really serve, using neighborhood names a local would recognize.",
            "A complete [Google Business Profile](/google-business-profile-optimization/) with the right service area, since a coastal address and an inland service radius are not the same thing.",
            "A newcomer page for people relocating to the area, if your work suits it.",
            "[Lead follow-up](/services/lead-follow-up/) so a text-in at 6 PM gets an answer the same evening.",
        ]),
    ],
    ind_notes={
        "law-firms": "Practice areas such as family, immigration and injury behave very differently across the county. The [law firm page](/california/law-firms/) lays out the compliance-aware plan.",
        "contractors": "From coastal remodels to inland builds, the work spans very different jobs. See the [contractor page](/california/contractors/).",
        "real-estate": "Military relocation changes how agents here get found. The [San Diego real estate page](/california/san-diego-real-estate/) goes deeper.",
        "salons-med-spas": "Tourist foot traffic and loyal locals both matter. See the [salon and med spa page](/california/salons-med-spas/).",
    },
    nearby=["orange-county", "inland-empire", "long-beach"],
    faq=[
        ("Do you work with businesses outside the city of San Diego?", "Yes. Chula Vista, El Cajon, Escondido, Oceanside, Carlsbad and Encinitas are separate markets, and I treat them that way."),
        ("Is there an office in San Diego I can visit?", "No. I work remotely across California, over email and video."),
        ("Should I mention military families on my site?", "If you actually serve them well, yes. Say it in plain terms, such as service near a base, flexible scheduling, or help with a relocation timeline. Do not add claims you cannot back up."),
        ("What does a free diagnostic show me?", "Where you stand on the map and in organic results for your trade across the neighborhoods you serve, and the three fixes I would make first."),
    ],
    cta_h2="Which San Diego cluster pays you most?",
    cta_p="Start with the free diagnostic and I will show you where you disappear in the places you already work.",
)

SAN_JOSE = mk(
    slug="san-jose", name="San Jose",
    title="San Jose Business Growth: Get Found in Silicon Valley | ART3RY",
    title_short="San Jose business growth",
    meta="Remote growth work for San Jose and Santa Clara County businesses: neighborhood pages, a precise Google profile, and quick follow-up for busy buyers.",
    kicker="San Jose",
    h1="In Silicon Valley, a good business<br>still loses to a faster reply.",
    sub="San Jose customers are busy and comparison-minded. The business that answers first usually gets the job.",
    hub_line="A busy, comparison-minded market where speed of reply decides the job.",
    lead=[
        "San Jose sits at the center of Silicon Valley, and that shapes the customer more than the competition. Many households here are time-poor and used to fast digital service, so they compare two or three options and go with the one that responds. That is a follow-up problem as much as a search problem.",
        "Art3ry is remote and works with businesses across California, so I will not claim a San Jose office. The work is a system: be present for the neighborhood searches, then reply so quickly that the customer never keeps shopping.",
    ],
    secs=[
        ("Neighborhoods that people actually search", [
            "Inside San Jose, customers use names like Willow Glen, Almaden, Evergreen, Berryessa, Cambrian, Japantown and the Rose Garden. Around the city sit Santa Clara, Sunnyvale, Campbell, Los Gatos, Milpitas, Cupertino, Mountain View and Palo Alto, all in the same county, each its own city. A home-service business in Almaden and one in Berryessa have different customers and different traffic patterns.",
            "That is why a single \"San Jose\" page undersells you. A short, honest page for each area you really cover, in the language locals use, does more than a long page that tries to cover the valley.",
        ]),
        ("A market that rewards the fast reply", [
            "When customers have several nearly identical choices, speed becomes the tiebreaker. Look at your own inquiries for a week. If the median reply takes hours, a competitor with a text-back and a short booking link is quietly taking your jobs.",
            "The fix is not complicated. An immediate acknowledgement, a qualifying question or two, and a clear next step, delivered the moment someone fills in a form or misses your call. I build that into the same system that brings the traffic, so the work SEO earns is not lost after the click.",
        ]),
        ("What I would build first for a San Jose business", [
            "Start with the places you can win, then protect the leads they produce.",
        ], [
            "Neighborhood and service pages for the two or three areas where your best customers live.",
            "A precise [Google Business Profile](/google-business-profile-optimization/), because a lot of this market decides straight from the map.",
            "A [site built to convert](/services/websites/) fast on a phone, with a booking path that takes seconds.",
            "[Automated follow-up](/services/automation/) for missed calls and form fills, around the clock.",
        ]),
    ],
    ind_notes={
        "law-firms": "San Jose clients often research several firms before they call. The [law firm page](/california/law-firms/) covers advertising rules and intake.",
        "contractors": "Remodel and repair customers here want quick, specific quotes. See the [contractor page](/california/contractors/).",
        "real-estate": "In a market this comparison-driven, the agent who answers first stands out. See the [real estate page](/california/real-estate/).",
        "salons-med-spas": "Busy clients value easy booking and confirmations. See the [salon and med spa page](/california/salons-med-spas/).",
    },
    nearby=["san-francisco", "oakland", "sacramento"],
    faq=[
        ("Do you cover Santa Clara County beyond San Jose?", "Yes. Santa Clara, Sunnyvale, Campbell, Los Gatos and the other cities in the county are their own markets, and I plan pages around the ones you serve."),
        ("Is this only for tech companies?", "No. I work with local service businesses. The Silicon Valley context only matters because it makes customers expect fast, easy replies."),
        ("How fast should I reply to an inquiry?", "As fast as you can. Automation can acknowledge instantly and keep the conversation going until you are free."),
        ("Do you have a San Jose office?", "No. I work remotely with businesses across California."),
    ],
    cta_h2="Find out where a slower reply is costing you.",
    cta_p="The free diagnostic checks both your visibility and your response time, because a lead lost after the click costs the same.",
)

SAN_FRANCISCO = mk(
    slug="san-francisco", name="San Francisco",
    title="San Francisco Business Growth: Win the Neighborhood | ART3RY",
    title_short="San Francisco business growth",
    meta="Remote growth work for San Francisco businesses: Mission to Sunset neighborhood pages, a sharp Google profile, and follow-up that fits a dense city.",
    kicker="San Francisco",
    h1="San Francisco is won one<br>neighborhood at a time.",
    sub="The Mission, the Sunset, Noe Valley and the Marina are a few miles apart and feel like different cities to the people who live in them.",
    hub_line="A dense city-county where each neighborhood is its own search habit.",
    lead=[
        "San Francisco is a consolidated city and county, compact on the map and divided into neighborhoods with strong identities. People say they live in the Mission, the Richmond, the Sunset, Noe Valley, the Marina or Bayview, and they search that way. A business that shows up for the neighborhood reads as local in a way a citywide page cannot.",
        "I am remote and work with businesses across California, so there is no San Francisco office behind this page. The value is a method: choose the neighborhoods you can truly serve, make each page unmistakably about that place, and answer every inquiry before the next tab opens.",
    ],
    secs=[
        ("Dense city, many small markets", [
            "Walk a few blocks in San Francisco and the character changes: Pacific Heights, North Beach, Chinatown, Haight-Ashbury, the Castro, Potrero Hill, South of Market, the Excelsior. A customer with a leaking pipe or a legal question tends to trust the business that knows their street, not one that lists the whole city.",
            "Density cuts both ways. Parking, tight buildings and older housing stock shape the work itself, and customers notice when a page acknowledges that. A contractor who writes honestly about working in older multi-unit buildings builds more trust than a generic remodeling pitch.",
        ]),
        ("How people reach a business here", [
            "Plenty of San Franciscans do not drive, so transit lines and walking distance are part of how they think about location. For a storefront or studio, say what is near your door and how people reach you by Muni or BART, once you have confirmed those details for your own address. For a mobile service, name the neighborhoods you cover and keep the list truthful.",
            "Because the city is small and busy, competitors are close. The structural check I run is simple: for each neighborhood you want, who holds the map spots, and is their profile and site actually about that neighborhood?",
        ]),
        ("What I would build first for a San Francisco business", [
            "Narrow first, then widen.",
        ], [
            "Pages for the neighborhoods you serve best, with real local detail and no copy-and-paste swaps.",
            "A tight [Google Business Profile](/google-business-profile-optimization/), with hours, categories and photos that match the street-level reality.",
            "A [website](/services/websites/) that loads fast and puts the phone number and booking link where a thumb can reach them.",
            "[Follow-up](/services/lead-follow-up/) that replies in minutes, since the customer is also messaging two competitors a few blocks away.",
        ]),
    ],
    ind_notes={
        "law-firms": "Clients choose counsel by practice area and trust more than by size. See the [law firm page](/california/law-firms/).",
        "contractors": "Older buildings and tight access make the work specific. The [contractor page](/california/contractors/) shows how to say so.",
        "real-estate": "Neighborhood authority is everything in a city this small. See the [real estate page](/california/real-estate/).",
        "salons-med-spas": "Walk-in discovery and repeat bookings drive revenue. See the [salon and med spa page](/california/salons-med-spas/).",
    },
    nearby=["oakland", "san-jose", "sacramento"],
    faq=[
        ("Should I list every San Francisco neighborhood on my site?", "Only the ones you really serve. A short, true list works better than a long one that Google and customers can both tell is padded."),
        ("Do you work with East Bay and Peninsula businesses too?", "Yes. Oakland and San Jose have their own pages, and nearby cities are treated as separate markets."),
        ("Is there a San Francisco office?", "No. Art3ry is remote and works with businesses across California."),
        ("How long does neighborhood SEO take?", "Expect the first movement in weeks and compounding results over months. I will not promise a specific ranking."),
    ],
    cta_h2="Which neighborhoods should be yours?",
    cta_p="Start with the free diagnostic and I will show you where nearby competitors are strong and where they are thin.",
)

SACRAMENTO = mk(
    slug="sacramento", name="Sacramento",
    title="Sacramento Business Growth: Capital, Suburbs | ART3RY",
    title_short="Sacramento business growth",
    meta="Remote growth work for Sacramento-area businesses: Midtown to Elk Grove pages, a precise Google profile, and follow-up built for a spread-out region.",
    kicker="Sacramento",
    h1="Sacramento customers search<br>by suburb, not by city.",
    sub="Midtown, Natomas, Elk Grove, Roseville and Folsom share a metro, and almost none of them shares a search.",
    hub_line="A capital region where suburbs, not the city name, drive local search.",
    lead=[
        "Sacramento is the state capital, set where the Sacramento and American rivers meet, and the metro around it is a wide ring of distinct communities. Midtown, East Sacramento, Land Park, Curtis Park, Oak Park and Natomas are inside the city. Elk Grove, Roseville, Folsom, Rancho Cordova and Citrus Heights are separate cities, and West Sacramento and Davis sit across the river in Yolo County.",
        "Art3ry is a remote company that works with California businesses, so I will not claim a Sacramento office. What I offer is a plan that matches this region: build for the suburb or neighborhood where your customers actually live, then connect each page to a fast response.",
    ],
    secs=[
        ("A region of suburbs", [
            "Residents of Elk Grove, Roseville and Folsom tend to identify with their own city, and they search with it. A business based in one of them that only writes about \"Sacramento\" is competing for the wrong phrase. The same holds in reverse for a Midtown business trying to reach the suburbs.",
            "The state capital also shapes the professional landscape. With the Capitol here, a lot of legal, consulting and association work orbits government, and that creates a different B2B audience than in most of the Central Valley.",
        ]),
        ("Seasons that move the work", [
            "Sacramento summers are hot, and service businesses see it in the calendar: air conditioning, irrigation, roofing and landscaping demand moves with the weather. If you sell anything seasonal, publish ahead of the season, not during it. A page that goes live in May is far more useful than one that goes live in July.",
            "The same logic applies to older neighborhoods like East Sacramento, where long-established housing creates steady repair and remodeling searches. Naming the real conditions of the work, such as older homes, builds credibility.",
        ]),
        ("What I would build first for a Sacramento business", [
            "Pick the ring you serve, then go deep.",
        ], [
            "A page for each suburb or neighborhood that matters to your revenue.",
            "A [Google Business Profile](/google-business-profile-optimization/) with a service area that matches where you really drive.",
            "Seasonal content published ahead of the demand curve.",
            "[Lead follow-up](/services/lead-follow-up/) that catches the inquiry from a customer who is comparing three businesses on a hot afternoon.",
        ]),
    ],
    ind_notes={
        "law-firms": "Courts and government-adjacent work shape the market. See the full plan on the [law firm page](/california/law-firms/).",
        "contractors": "Heat, older homes and fast suburban growth all matter. See the [Sacramento contractor page](/california/sacramento-contractors/).",
        "real-estate": "Agents here are chosen by suburb and school area. See the [real estate page](/california/real-estate/).",
        "salons-med-spas": "A spread-out region rewards strong booking and reminders. See the [salon and med spa page](/california/salons-med-spas/).",
    },
    nearby=["san-francisco", "oakland", "fresno"],
    faq=[
        ("Does a Sacramento business need pages for Elk Grove and Roseville?", "If you serve them, yes. Those are separate cities with their own searches, and each deserves a page that shows real coverage."),
        ("Do you serve West Sacramento and Davis?", "Yes. They are in Yolo County rather than Sacramento County, but customers treat them as part of the same region."),
        ("Is there a Sacramento office?", "No. I work remotely with businesses across California."),
        ("When should seasonal pages go live?", "Before the season starts. Search interest builds ahead of the weather, and pages need time to be crawled and trusted."),
    ],
    cta_h2="Where in the region do your best customers live?",
    cta_p="The free diagnostic maps your visibility by suburb and shows where you are missing from the places that pay.",
)

FRESNO = mk(
    slug="fresno", name="Fresno",
    title="Fresno Business Growth: Search, Calls and Follow-Up | ART3RY",
    title_short="Fresno business growth",
    meta="The Fresno overview: how local search, your website and follow-up fit together, with links to the Fresno SEO and web design pages.",
    kicker="Fresno",
    h1="Fresno growth is three jobs,<br>not one.",
    sub="Get found, win the call, follow up. Most Fresno businesses are strong at one and leaking at the other two.",
    hub_line="The overview page for Fresno, with the SEO and web design pages as its deep dives.",
    lead=[
        "This is the overview for Fresno. If you are shopping for one specific thing, go straight to the deep dives: [SEO company in Fresno](/seo-company-fresno/) for rankings and the map, or [web design in Fresno](/web-design-fresno/) for the site itself. This page is the connective tissue, the plain view of how the three parts of growth fit together for a Fresno business.",
        "Art3ry is remote and works with businesses across California, and Fresno is the Central Valley market closest to my own work. I do not run a storefront here. I run a system, and I can show you what it does.",
    ],
    secs=[
        ("The three jobs", [
            "Growth for a local business reduces to three jobs. First, being found: the map, the search results and the reviews that decide who gets considered. Second, winning the call: a site and profile that make the next step obvious on a phone. Third, following up: answering the inquiry and chasing the quote so a warm lead does not go cold.",
            "Most owners I talk to have paid for one of these. A good site with no visibility, strong rankings with a slow reply, or a fast reply to very few leads. The money leaks at whichever job is missing.",
        ]),
        ("What makes Fresno its own market", [
            "Fresno sits at the center of the San Joaquin Valley, and Fresno County is one of the leading agricultural counties in the country. That shapes who the customers are: farm-linked businesses, tradespeople serving growing suburbs, professionals around the downtown courthouses, and households in neighborhoods like the Tower District, Fig Garden, Woodward Park, River Park and Sunnyside.",
            "Clovis, Sanger, Madera and Kerman are separate towns with their own habits. A Clovis customer and a Tower District customer use different words, and Highway 99, 41 and 180 shape what \"close\" means. Local pages that respect that read as real.",
        ]),
        ("Where to start", [
            "If you are not sure which job is leaking, the diagnostic answers it. Otherwise pick the page that matches your sharpest problem.",
        ], [
            "Not showing up for your trade: [SEO company Fresno](/seo-company-fresno/).",
            "Showing up but not getting calls: [web design Fresno](/web-design-fresno/).",
            "Getting calls but losing them: [lead follow-up](/services/lead-follow-up/).",
            "Not sure: [the free diagnostic](/diagnostic/).",
        ]),
    ],
    ind_notes={
        "law-firms": "Fresno has a deep legal community around its state and federal courts. See the [Fresno law firm page](/california/fresno-law-firms/).",
        "contractors": "Valley heat and growing suburbs keep trades busy. The [contractor page](/california/contractors/) has the system.",
        "real-estate": "Neighborhood knowledge sells here, from Fig Garden to Clovis. See the [real estate page](/california/real-estate/).",
        "salons-med-spas": "Referrals and reminders drive repeat business. See the [salon and med spa page](/california/salons-med-spas/).",
    },
    nearby=["bakersfield", "sacramento", "san-jose"],
    faq=[
        ("How is this different from your Fresno SEO and web design pages?", "Those pages go deep on one service. This one explains how search, site and follow-up work together, and sends you to the right deep dive."),
        ("Do you cover Clovis and Madera?", "Yes. They are separate markets with their own searches, and I plan pages for them when you serve them."),
        ("Is there a Fresno storefront?", "No. Art3ry is remote and works with businesses across California."),
        ("What should I do first?", "Run the free diagnostic. It tells you which of the three jobs is leaking the most."),
    ],
    cta_h2="Find the leak in your Fresno funnel.",
    cta_p="The free diagnostic shows whether you have a visibility problem, a conversion problem or a follow-up problem.",
)

CITIES1 = [LOS_ANGELES, SAN_DIEGO, SAN_JOSE, SAN_FRANCISCO, SACRAMENTO, FRESNO]
