# Structure choices and the evidence behind them

This reference collects what credible public sources say about the structural choices operators face, and how strong that evidence is. Use it alongside [operating model design](operating-model-design.md) and the two worked cases. Most sources here are operator accounts and consultancy surveys. An experienced operator's account of what worked, and why, is primary evidence for this library, which is written for operators. Each source is labeled by type so a reader can weigh it. Surveys are flagged where they rest on self-reported data.

## Replay the contested priority before moving people

At Grafana, three product teams needed the same API platform while its team needed a refactor. Separate senior reporting lines made arbitration slow. [Goutham Veeramachaneni](https://www.gouthamve.dev/my-first-re-org/)

Change the level where competing priorities meet if that is where work waits. Grafana grouped cloud work under one senior owner and kept most individual roles intact.

At Braze, functional teams helped specialists learn together at 10 to 15 people. Later, local product priorities competed across functions. Product groups gained autonomy but shared interfaces needed attention. [Kevin Wang](https://www.braze.com/resources/articles/building-braze-product-team-reorganization-success)

Test both a product-local change and one affecting every product. If the proposal only improves the first, assign a shared interface owner before moving reporting lines.

WeMaintain let engineers propose teams. Two priority teams still lacked enough people. Leaders supplied constraints, and participants revised the staffing proposals. [WeMaintain](https://www.wemaintain.com/en-gb/blog/about-us/timothee-bourguignon-reorganisation-of-wemaintains-tech-teams)

Self-selection for a bounded staffing decision differs from transferring recurring management duties. At Spotify, removing six IT managers shifted work upward and informal feedback fell away. [Viktor Cessan](https://www.viktorcessan.com/what-we-learned-from-removing-all-middle-managers-in-the-it-tribe-at-spotify/)

Replay both decisions. Who fills the unpopular but necessary team this week? Who gives difficult feedback next quarter? A design can solve one and fail the other.

## Functional or general-manager structure

The most common structural decision at a scaling technology company is whether to organize by function (one engineering, one product, one sales organization) or by business line. Each business line has a general manager who owns its results.

| Consideration | Points toward functional | Points toward general managers | Source |
|---|---|---|---|
| Product integration | One tightly integrated experience | Loosely related products | [Cagan, SVPG, 2024](https://svpg.com/the-product-model-and-org-design) |
| Distance of the main metric from revenue | Far from revenue | Close to revenue, owned end to end | [Lenny's Newsletter, 2024](https://lennysnewsletter.com/p/general-management-functional-and) |
| Cost of duplication | Cannot afford duplicate functions | Can afford them | Lenny's Newsletter, 2024 |
| Stage | Early companies | Later, with distinct businesses | Lenny's Newsletter, 2024 |

Companies move in both directions. Block, Shopify and Airbnb moved toward functional structures, and Coinbase moved toward general managers in late 2022. Apple's post-1997 functional organization is the best-known case for functional design ([Podolny and Hansen, HBR, 2020](https://hbr.org/2020/11/how-apple-is-organized-for-innovation), read in full). Jobs removed the business-unit general managers in one day and put the company on one P&L. Senior vice presidents run functions, not products, and only the CEO sees every function meet on a product. The stated principle is to align expertise with decision rights, where a divisional design aligns accountability with control. Its cost is coordination. Portrait mode needed about 40 specialist teams, with disputes escalated as far as the CEO. Apple held the senior layer down as it grew. Employees rose from about 17,000 in 2006 to 137,000 in 2019, while vice presidents went from 50 to 96. Both authors lead Apple University, so this is an insider account. Cagan's view that functional, GM and hybrid cover at least 95 percent of product organizations is his own estimate.

Ben Horowitz's rule is a useful corrective: all organizational designs are bad ([a16z, 2010](https://a16z.com/taking-the-mystery-out-of-scaling-a-company/)). Each design optimizes some communication paths and degrades others. His method ends by listing the paths you did not optimize and planning how to mitigate them. The [operating model case](operating-model-worked-case.md) does this through service agreements for the shared functions.

## Operators who reason from the problem

The sources above mostly report what companies chose. A smaller set of operator essays reasons from the problem itself. Each is one person's experience, not a study, but the reasoning can be checked against the case at hand.

Steven Sinofsky's [2016 essay](https://medium.learningbyshipping.com/functional-versus-unit-organizations-6b82bfbaa57) on the Windows reorganization says nearly every company sits in the middle. Unit-led companies still centralize sales, finance and talent. Functional ones still run small autonomous teams. His test is the go-to-market. One product sold one way favors functional, while different customers, channels or ship dates favor units. When Windows went functional he found more than 100 general managers but too few leaders for each discipline. Managers fell from over 35 percent of the team to about 20 percent. He warns that a P&L for part of a business breeds infighting unless its leader truly controls it. His closing rule is to know your structure's weaknesses and compensate for them.

Ben Thompson's [analysis of Apple](https://stratechery.com/2016/apples-organizational-crossroads/), from the same year, runs the logic the other way. A functional structure suits one integrated product line and does not stretch to a different business model. DuPont created divisions when gunpowder and paint needed different structures. Thompson argued Apple's services needed their own structure, incentives and rhythm, and noted that Apple Retail already ran as a separate division.

Cedric Chin's [Commoncog essay on the skill](https://commoncog.com/org-design-skill/) frames org design as a search for fit between form and context. People react in ways no designer predicts, so the work is iteration: change, watch, then roll back or adjust. He borrows Andy Grove's three levers, which are economic incentives, contractual obligations such as structure and policy, and culture. A [follow-up](https://commoncog.com/org-structure-isnt-everything-org-design/) argues that structure gets too much attention because it is the most visible lever. To make a change take, he judges receptivity first and spends trust deliberately. He tries a smaller, reversible version before the full one.

Will Larson gives the most usable arithmetic, written for engineering but portable. His [reorg method](https://lethain.com/running-an-engineering-reorg) starts by checking that the problem is structural. Working around a broken relationship is the worst reason to reorganize. He projects headcount a year out from three directions and designs from the boxes, not from key individuals. In [his sizing rules](https://lethain.com/sizing-engineering-teams/), a manager supports six to eight people, or four to six managers. Teams under four are not really teams, and a new team buds from one of eight to ten. His [evolution method](https://lethain.com/how-to-evolve-eng-org) builds from three units. A team is six to eight people with one manager and a shared on-call. Each team runs one or two workstreams of three or four people. About five teams make a group under a group manager. The method ends with rest: do not change again before the measurements from the last change are in.

Molly Graham helped Facebook grow from about 500 to 5,500 people. In [a First Round interview](https://review.firstround.com/give-away-your-legos-and-other-commandments-for-scaling-startups) she calls scaling "giving away your Legos," handing off what you built so you can take the next job. She places the real chaos between about 30 and 750 people. She warns against grafting a large company's elaborate process onto a small one. Write principles first, such as a pay philosophy before a pay system.

Andy Grove's *High Output Management* (1983) is where much of this reasoning starts. It was read here through several detailed chapter summaries, including [Kudija's notes](https://matthewkudija.com/reading-notes/2021-04-11-High-Output-Management.html) and [Lebrero's](https://danlebrero.com/2023/04/12/high-output-management-summary). Grove frames the choice as responsiveness against leverage. Mission-oriented units respond fast to their market. Functional groups share scale and can move people to company priorities. "Grove's Law" says every large organization with a common business purpose ends up a hybrid of the two. Conglomerates are the exception, because they share no common purpose. Functions then act as internal subcontractors to the business units. The cost is a function overloaded by requests and a constant negotiation over its time. His fix is dual reporting, first used in the Apollo program. A person reports to a mission manager for what to work on, and to a functional manager or peer group for how. He warns it creates ambiguity and needs a culture where peers can decide.

Read together, these essays agree on three things. Name the problem before choosing a shape. Expect every shape to have weak points and plan the patches. Change in steps small enough to learn from.

## Team types and interaction modes

Team Topologies, by Skelton and Pais, gives a vocabulary that fits interface agreements well ([key concepts](https://teamtopologies.com/key-concepts)).

| Team type | Purpose |
|---|---|
| Stream-aligned | Delivers a flow of work for one product, customer segment or business line |
| Platform | Provides internal services so stream-aligned teams carry less load |
| Enabling | Helps other teams build a capability, then steps back |
| Complicated-subsystem | Owns work that needs scarce specialist knowledge |

It names three ways teams interact: collaboration (working closely for a period), X-as-a-service (one team consumes another's service through a clear interface) and facilitation (one team coaches another). Its central constraint is cognitive load: a team can only handle so much before it breaks down. Martin Fowler calls the model a useful simplification ([Fowler, 2023](https://martinfowler.com/bliki/TeamTopologies.html)).

For an operator the practical use is threefold. Name each team's type. Write each interface as one of the three modes. Treat collaboration as time-boxed, with a planned move to a service once the work stabilizes. In the [org design case](org-design-worked-case.md), Enterprise engineering is stream-aligned. Platform and the security pool are platform-like services. The analytics partner pod is close to an enabling team.

## Structure shapes what gets built

[Conway observed in 1968](https://www.melconway.com/Home/Committees_Paper.html) that a system's design copies its builders' communication structure. The "inverse Conway maneuver" designs teams to produce the architecture you want ([Fowler, 2022](https://martinfowler.com/bliki/ConwaysLaw.html)). Fowler cautions that it does not quickly fix a rigid existing system. DORA's research treats loosely coupled teams, able to test and deploy without others, as a predictor of delivery performance ([DORA](https://dora.dev/capabilities/loosely-coupled-teams/)).

The best-known test compared matched pairs of products built by open-source communities and by commercial firms. In every pair, the loosely coupled organization built the more modular product, by up to a factor of six ([MacCormack, Rusnak and Baldwin, 2012](https://www.hbs.edu/ris/Publication%20Files/Research%20Policy%2041%20(2012)%201309%E2%80%93%201324_c5c2350e-013c-4065-a2f9-d95eb32177d5.pdf), abstract and introduction read). A 2016 review by Colfer and Baldwin found strong support in about 70 percent of studies, partial support in 22 percent and none in 8 percent. Mirroring is common, not universal.

The operator implication is that splitting or merging engineering teams is also a product and architecture decision. Bring the engineering leaders into it early rather than presenting a finished chart.

## Ownership and duplication

Amazon's [two-pizza teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/) own a service end to end under a single-threaded leader. Leaders use guardrails rather than approval gates. AWS itself notes that autonomous teams risk duplicated and siloed work and need governance to decide when to combine efforts. Autonomy is bought with some duplication. Price it, as the org design case does for security reviewers.

Removing managers altogether has been tried. Google eliminated engineering managers in 2002 and reversed it within months, because day-to-day issues flowed to the founders (Garvin, HBR, 2013). Its later Project Oxygen drew on more than 10,000 data points from reviews and surveys. Teams with highly effective managers had better results and lower turnover ([Google re:Work](https://rework.withgoogle.com/intl/en/guides/following-the-data-the-research-behind-great-managers)). Google first published eight manager behaviors and now lists ten. Spotify's widely copied squads and tribes model was, by later accounts, never fully implemented as described ([Lee, 2020](https://jeremiahlee.com/posts/failed-squad-goals/)). Copying another company's chart without its conditions rarely works.

Delayering often does the opposite of what it promises. Rajan and Wulf studied more than 300 large U.S. firms from 1986. In their [NBER summary](https://www.nber.org/digest/oct03/flattening-corporate-management), the CEO's direct reports rose from about four to seven. Layers between division heads and the CEO fell by about a quarter. In a [2012 paper](https://www.hbs.edu/ris/Publication%20Files/12-087_bc50bde2-3016-457a-9bee-dc988cb1056b.pdf), Wulf found flattened firms often show more control at the top, not less. Neilson and Wulf report the CEO's span going from about five to almost ten over a similar period, counting a wider set of roles. When a flattening is proposed, ask where the removed layer's decisions will go.

## How reorganizations go

| Source | Finding | Caveat |
|---|---|---|
| [McKinsey, 2010](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/taking-organizational-redesigns-from-plan-to-practice-mckinsey-global-survey-results) | 16 percent met all objectives on time, and 8 percent also improved performance | Self-reported survey |
| McKinsey, 2015 | Fewer than a quarter of redesigns succeed, and 44 percent run out of steam | Self-reported survey |
| [McKinsey, 2025](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-new-rules-for-getting-your-operating-model-redesign-right) | Of 2,000 executives, 79 percent completed redesigns and 63 percent met most objectives. Managing transition risks doubled the odds | Executive respondents, self-reported |
| [Bain, 2026](https://www.bain.com/insights/when-a-new-organizational-structure-isnt-enough-how-to-truly-live-your-operating-model/) | 88 percent of senior leaders, against 36 percent of people in the new structure, expect it to meet expectations. Only 22 percent of employees got enough training or tools | 976 respondents, both leaders and employees |
| [Hughes, 2011](https://research.brighton.ac.uk/en/publications/do-70-per-cent-of-all-organizational-change-initiatives-really-fa/) | No valid evidence supports the often-quoted claim that 70 percent of change efforts fail | Literature review |

Two lessons follow. Leaders consistently rate a reorganization better than the people living in it, so ask the people doing the work before declaring success. And transition planning is a separate job from design, with middle managers carrying most of it.

## Two published design sequences

| Step | Kesler and Kates, *Leading Organization Design* (2011) | Heidari-Robinson and Heywood, *ReOrg* (2016) |
|---|---|---|
| 1 | Business case and discovery: strategy, current-state assessment and design criteria | Build a profit and loss for the reorg: its value, costs and disruption |
| 2 | Strategic grouping, judged on six design drivers | Diagnose what works and what does not in the current organization |
| 3 | Integration: governance, networks and shared services that tie units back together | Choose among more than one option |
| 4 | Talent and leadership: staff the critical roles | Get the "plumbing and wiring" right: reporting, metrics, processes and systems |
| 5 | Transition: pacing, measures and adjustment | Launch, listen and course-correct |

Neither book was read in full. The sources were an [author interview](https://bobmorris.biz/stephen-heidari-robinson-and-suzanne-heywood-on-how-to-get-a-reorganization-right-part-2-of-an-interview-by-bob-morris), the [contents page](https://www.oreilly.com/library/view/leading-organization-design/9780470589595) and reviews. They agree on the order: value and criteria first, then structure, then the detailed mechanics, then the transition. Heidari-Robinson names step 4 as the hardest and the one executives underinvest in. The authors cite McKinsey survey data in the same direction. Only 37 percent of reorganizations met their own timelines, and 43 percent underestimated the time ([book extract](https://www.livemint.com/news/business-of-life/book-extract-reorg-how-to-get-it-right-1541625306970.html)).

Change frameworks such as Kotter's eight steps and Prosci's ADKAR are widely used, but their own pages publish no controlled outcome data. Prosci's correlation between change management quality and project success is its own practitioner survey. In its 12th edition, 88 percent of respondents rating their change management excellent met objectives, against 13 percent rating it poor. The often-quoted 82 percent is the U.S. subset, whose poor group had five respondents. Kotter's own 1995 article is an observer's account, not a study. He says well over half the companies he watched failed at the first step, urgency, and sets the bar at about 75 percent of managers convinced. Beer and Nohria (HBR, 2000) contrast Theory E, top-down change for economic value, with Theory O, participative change that builds capability. They argue for combining both, using ASDA as the case. The same article repeats the 70 percent failure figure without a source. Even Lewin's unfreeze, change and refreeze is shakier than its reputation. In [a 2016 paper](https://journals.sagepub.com/doi/full/10.1177/0018726715577707), Cummings, Bridgman and Brown argue Lewin never built that model. Later writers assembled it after his death. Use these frameworks as checklists, not as evidence that a plan will work.

## Speed and secrecy of a reorganization

Sources disagree. Elad Gil advises consulting a few executives privately. He then announces and implements within about a day, never pre-announcing ([Gil, 2018](https://blog.eladgil.com/p/how-to-do-re-org)). McKinsey advises involving the full leadership team early and cascading interactively. The difference is largely scale and the kind of change. A startup moving reporting lines benefits from speed and minimal uncertainty. A redesign that changes how work flows across a large company needs the managers who will run it to help design it. People and Legal still own the employment steps either way.

## Operating model typologies

[Operating model choices and evidence](operating-model-choices-and-evidence.md) covers the MIT CISR types, the Operating Model Canvas, the Star Model, 7S and classic coordination theory. The CISR types there are verified against Ross's 2005 briefing. Any typology can frame the first conversation. None replaces tracing actual work, as the worked case does.
