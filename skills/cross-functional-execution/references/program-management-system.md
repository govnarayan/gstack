# Program management: choose, set up and run

Spotify's squads received overlapping migration requests from infrastructure groups. Each request looked reasonable alone. The shared constraint was how many migrations a receiving team could absorb. [Spotify Engineering](https://engineering.atspotify.com/2020/06/tech-migrations-the-spotify-way)

Estimate demand by receiving team and week before announcing dates. Pilot with a few teams, record the work they actually did, then revise the sequence and name the migration owner.

At Shopify, leads submitted status in writing and could cancel a call if they resolved exceptions asynchronously. An unresolved escalation needed urgency, an owner and a recorded decision. [Carla Wright](https://shopify.engineering/running-engineering-program-guide)

On an integrated launch, test whether completed components can operate together. Crossrail underestimated remaining completion work even after resetting its plan. Distinguish component readiness from integrated testing and operational acceptance. [National Audit Office](https://www.nao.org.uk/reports/crossrail-progress-update/)

A program is a set of related projects and operating changes that must land together to produce an outcome none of them produces alone. A pricing change that touches billing, sales compensation, revenue policy and customer contracts is a program. A single system upgrade owned by one team is a project. The distinction matters because a program's main risk is the interfaces between parts, not the work inside any one of them.

This reference covers the components, how to choose an approach and tools, and how to establish context, people, authority, artifacts and cadence. [Decision rights](decision-rights-rapid-raci.md) covers RAPID, RACI and lighter choices. The [worked program](worked-program.md) shows every artifact completed for one synthetic program, checked by a [runnable script](../scripts/program_check.py). The existing [delivery and decision methods](delivery-and-decisions.md) hold the underlying schedule, readiness and handover method.

## Components and the question each answers

| Component | Question | Artifact | Usual owner |
|---|---|---|---|
| Intake and prioritization | Should this be a program at all, ahead of what else? | Intake record and portfolio ranking | Executive team or portfolio owner, operator prepares |
| Charter and business case | What outcome, why now, within what limits? | Charter, with economics where material | Sponsor approves, program lead drafts |
| Sponsorship | Who resolves conflicts and holds the resources? | Named sponsor in the charter | CEO or executive team |
| Outcomes and benefits | How will we know it worked, measured against what baseline? | Benefits register | Benefit owners in the functions |
| Scope | What is in, what is adjacent and excluded? | Scope statement and change log | Program lead, sponsor for changes above threshold |
| Workstreams | Which parts can run with their own lead? | Workstream list with leads | Program lead |
| Milestones | What verifiable evidence marks progress? | Milestones with acceptance criteria and acceptor | Workstream leads, acceptors named |
| Dependencies and critical path | Which chain sets the finish date? | Integrated schedule | Program lead |
| Staffing and capacity | Do the named people have the time, after other work? | Capacity view by person and week | Functional managers confirm |
| Budget | What will it cost, and who approved it? | Budget line and actuals | Finance partner |
| Stakeholders and communication | Who is affected, who must know what, when? | Stakeholder map, communication plan | Program lead |
| Risks, assumptions, issues, dependencies (a RAID log) | What could go wrong, what are we assuming, what has gone wrong? | RAID log with owners and dates | Item owners, program lead maintains |
| Decisions and escalation | Who decides what, and where do conflicts go? | Decision-rights record, decision log | Sponsor sets, deciders record |
| Change control | Which changes need whose approval? | Change threshold and change log | Sponsor |
| Delivery acceptance | Who accepts each deliverable, against what test? | Acceptance record | Named acceptors |
| Transition and closure | Who runs it afterward, and did the outcome occur? | Handover record, closure report, benefits check | Receiving owners, sponsor closes |

A small program can hold all of this in one document. A large one needs separate logs and a tool. The components stay the same.

## Choose the approach

Methods differ mainly in how much they fix in advance. Choose by the work's uncertainty, scale and interdependence, the company's existing systems, the cost of the method itself and the adoption burden on people already busy.

| Approach | Fixes in advance | Fits | Costs and failure modes |
|---|---|---|---|
| Single owner with a written plan | Outcome and owner | One team or two, low interdependence, reversible choices | Breaks when interfaces multiply. The owner becomes a router |
| Stage-gated, predictive plan (the logic of [PRINCE2](https://www.prince2.com/usa/blog/the-7-principles-themes-and-processes-of-prince2): continued business justification, manage by stages, manage by exception) | Scope, stages, business case, tolerances | Known work with hard dates, contracts, regulators, physical or financial systems | Slow to absorb learning. Gate reviews become theater if nobody can stop the program |
| Iterative delivery inside fixed dates | Date and outcome, scope flexes | Product and software work with uncertain solutions | Without a scope-cut rule, the date slips anyway |
| Fixed time, variable scope ([Shape Up](https://basecamp.com/shapeup/1.2-chapter-03): an appetite, six-week cycles, a betting table, and a circuit breaker that cancels work not shipped in one cycle) | The appetite (weeks allowed) per bet | Product teams choosing what to build next | Weak for cross-functional work with external deadlines |
| Scaled agile frameworks ([SAFe](https://framework.scaledagile.com/): planning events for a whole train of teams, usually every eight to twelve weeks) | Shared cadence across many teams | Dozens of interdependent engineering teams | Heavy roles, training and ceremony. Rarely worth it for business programs |
| Reference standards ([PMBOK Guide, 8th edition](https://www.pmi.org/standards/pmbok), November 2025: six principles, seven performance domains named governance, scope, schedule, finance, stakeholders, resources and risk, and 40 tailorable processes. PMI's fifth [program standard](https://www.pmi.org/standards/program-management-fifth-edition) adds eight program principles and a collaboration domain) | Nothing by itself | A shared vocabulary and checklist of what to consider | Treated as a method, it produces documents rather than decisions |

Most strategy and operations programs combine a predictive spine (fixed external dates, contracts, compliance steps, money) with iterative work inside workstreams (product, enablement content). Make that mix explicit in the charter. A frequent mistake is running the whole program in the style of its largest workstream, usually engineering.

**When to change approach.** Add structure when a dependency slips unnoticed for two status cycles, when two workstreams forecast incompatible dates, or when decisions bounce between reviews. Remove structure when status preparation consumes more hours than the coordination it replaces, or when the program has shrunk to one team. These triggers are judgment, not measured thresholds.

## Forecast from the outside view

Plans built bottom-up from task estimates are optimistic by construction. Lovallo and Kahneman brought the inside and outside view to managers in HBR in 2003. Flyvbjerg's work turned it into reference-class forecasting. Pick a class of similar past programs and look at how their actual cost and duration compared with plan. Place your program inside that distribution before adjusting for its specifics.

Two findings matter for an operator. First, overruns are not normally distributed. A study of 5,392 IT projects found cost overruns follow a fat-tailed power law. The average overrun therefore understates the risk of a few extreme failures ([Flyvbjerg et al., 2022](https://arxiv.org/abs/2210.01573)). Second, the base rates are poor. Flyvbjerg's database of over 16,000 projects reportedly shows 8.5 percent finishing on time and on budget, and 0.5 percent also delivering the promised benefits. That figure comes from a review of *How Big Things Get Done*, not from the database itself.

A company rarely has a published reference class for its own internal programs. Build one from your own history: the last five to ten cross-functional launches, migrations or pricing changes, with planned and actual dates. If none exists, state the planned date as a forecast with a range, and record actuals so the next program has a base rate.

For a cost estimate, GAO's guide gives a usable test. A reliable estimate is comprehensive, well documented, accurate and credible. [GAO-20-195G](https://www.gao.gov/products/gao-20-195g) sets out 12 steps and 18 best practices to get there. Its summary and chapter 3 were read. Its accuracy test includes a record of past estimates against actuals, the same base rate this section asks for.

## Count owners, not headcount

The limit on how many programs a company can run at once is usually the number of people who can take one from idea to delivery without supervision. Keith Rabois calls them "barrels", with everyone else as "ammunition". In [a First Round interview](https://review.firstround.com/keith-rabois-on-the-role-of-a-coo-how-to-hire-and-why-transparency-matters) he gives the arithmetic: with five barrels, a company can do five things at once. Adding ammunition does not add a sixth. His estimate of 2 to 15 barrels per company is anecdotal, reported secondhand from a podcast.

Owners also need to spend their own time by return. Shreyas Doshi's [LNO framework](https://docs.superhuman.com/@shreyas/lno-framework) sorts tasks into Leverage, Neutral and Overhead. Leverage tasks return ten times the effort or more and deserve the best hours. Overhead tasks deserve a deliberately quick job. He finds very few Leverage tasks on any list, and strategy is the one most often postponed for firefighting.

Amazon's answer is the single-threaded leader. This is one person whose only job is the initiative. Their team has its dependencies cut so it can move on its own ([First Round Review, 2021](https://review.firstround.com/how-to-build-an-invention-machine-6-lessons-that-powered-amazons-success/)). The named failure mode is the part-time owner. At intake, ask who will own each program full time. A program with no available owner should wait, however attractive it is.

## Plan in sequence, and evolve the process

Will Larson's [planning essay](https://lethain.com/planning) splits annual planning into three steps done in order: the financial plan, each function's portfolio split, then the 3 to 12 month roadmap. Holding the other two fixed while settling each one forces real trade-offs. Planning everything at once invites spreadsheets where tripling a team triples output. He lists how planning goes wrong in practice. Budgets get set and then ignored in headcount requests. The least efficient teams get rewarded for asking more. Reviews end up checking format instead of the decisions.

His [companion essay](https://lethain.com/good-process-is-evolved) argues that good process is evolved, not designed. Write the problem with its constraints. Look first for an existing process to fix. Try the new one cheaply on one team, and when it fails, look for the constraint the problem statement missed. Practice it before judging it, because no process goes well the first time. A program's own operating rhythm should be built this way, not imported whole.

Lenny Rachitsky and Nels Gilbreth's [W framework](https://review.firstround.com/the-secret-to-a-great-planning-process-lessons-from-airbnb-and-eventbrite), from Airbnb and Eventbrite, sets who does what. Leadership shares context: strategy and a concrete goal. Teams respond with plans. Leadership integrates them into one plan, and teams confirm buy-in. It suits companies above roughly 25 people. One person drafts the strategy first, because a group improves a draft faster than it writes one.

[A 2024 First Round piece](https://review.firstround.com/annual-planning-sucks-a-cpo-cro-cfo-and-coo-share-advice-on-how-to-make-it-better/) adds the hard edges. Its four executives come from Notion, Stripe, Linear and Linktree. Cristina Cordova of Linear says to constrain the timeline, since time spent planning is time not shipping. Linktree finished its plan in five weeks. Limit investment areas to three to five and name what you will not do. Cordova quotes Hughes Johnson: strategy should hurt. Start from the finance constraint rather than asking teams for three staffing scenarios, which wastes time. Ask each team instead for a list of what it cannot do. A short list means the plan is not realistic. Expect high fidelity for the first half and a fuzzier second half.

## Run reviews as the engine of the cadence

Andy Grove calls meetings the medium of managerial work, not a tax on it. The source here is [Lebrero's chapter notes](https://danlebrero.com/2023/04/12/high-output-management-summary). He separates regular process meetings, such as one-on-ones and operation reviews, from ad hoc mission meetings called to decide something. Mission meetings should have eight people or fewer. Spending more than a quarter of one's time in ad hoc meetings signals a badly designed organization.

Andrew Bosworth, Meta's CTO, describes the same system in [an essay on operations](https://boz.com/articles/ops). Reviews unblock teams, so they set the delay on progress. Communication sets how much people can coordinate. Cadence sets throughput. A monthly review means work slips a month at a time, and a weekly one cuts that by four. Anyone can call a review, and leaders hold large weekly blocks for them. He treats being blocked as worse than being wrong. His [essay on reviews](https://boz.com/articles/reviews) sorts them into three kinds: inform, discuss and decide. Discuss reviews advance shared understanding without a decision. Many reviews work over email or a two-day chat thread, and attendance should be as small as possible. Presenters should bring their hardest questions, not a polished pitch.

Kevin Fishner, Chief of Staff at HashiCorp, splits the cadence into annual, quarterly and weekly speeds. He described it to [First Round](https://review.firstround.com/focus-on-your-first-10-systems-not-just-your-first-10-hires-this-chief-of-staff-shares-his-playbook). Each speed needs a source of truth and a ritual for reviewing it. Most companies build the scorecard and skip the ritual, and that is how OKRs die. HashiCorp's weekly executive hour opens with 15 minutes on the metrics pack. Linktree runs a weekly scorecard meeting where each owner grades a goal on track, at risk or off track and states the help needed. That way nobody is surprised at the quarterly review. The [standing sweeps](../../operating-cadence/references/reviews-and-health.md#build-the-pack-from-standing-sweeps) in the operating cadence skill build the weekly pack. They check each blocked item, handoff and due decision against this program's RACI and RAPID records.

## A transformation office is a cadence, not an owner

For a large change spanning many programs, McKinsey describes a transformation office led by a senior executive. It sets a strict review rhythm, tracks value captured against value promised, and escalates stalled decisions. It does not own the targets. The business owners do ([McKinsey, 2019](https://www.mckinsey.com/capabilities/transformation/our-insights/the-transformation-office-key-success-factors)). For a Chief of Staff this is often the actual job: running the cadence and the escalation path while owners keep accountability.

## What the failure statistics do and do not show

Headline failure rates disagree because they measure different things.

| Source | Population and measure | Figure |
|---|---|---|
| [PMI Pulse of the Profession 2021](https://www.businesswire.com/news/home/20210324005712/en/PMI-Pulse-of-the-Profession-2021-Report-Uncovers-Benefits-of-Organizational-Agility-During-Times-of-Great-Change) | 3,950 self-reporting practitioners | 73 percent met original goals, 62 percent on budget, 55 percent on time |
| [BCG, 2020](https://www.bcg.com/publications/2020/increasing-odds-of-success-in-digital-transformation) | 825 executives plus 70 engagements, digital transformations | 30 percent succeed |
| McKinsey (Harry Robinson, 2019) | Transformations, no named study | About 70 percent fail |
| Flyvbjerg database, via review | Over 16,000 projects, mostly capital projects | 8.5 percent on time and on budget |

Eveleens and Verhoef showed that the widely quoted Standish CHAOS figures define success only as hitting the original estimate. That is a one-sided test ([IEEE Software, 2010](https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/)). Do not quote one failure rate as a fact. Quote the measure and the population, or use your own history.

The causes named across these sources are more useful than the rates. Aspirations are set too low, skilled people keep their day jobs, there is no review cadence, decisions stall without escalation, and plans ignore base rates.

## Operator templates worth borrowing

Shopify's engineering program guide opens each program with a problem statement, objectives, guiding principles, a definition of done, top risks and a path to done. It runs six-week cycles. Each has weekly status, a ranked risk list and a logged escalation board ([Shopify Engineering, 2021](https://shopify.engineering/running-engineering-program-guide)). The program ends when the definition of done is met. Shopify's product review tool puts every project through Proposal, Prototype, Build, Release and Results reviews, with two approval levels. These are lighter than a full charter and fit a growth-stage company.

## Choose the software

Use what the company already runs unless it cannot do the job. A second work-management tool splits the truth. The test is not features. It is whether owners will update it weekly without being chased.

| Need | Minimum capability | Notes |
|---|---|---|
| Fewer than about 30 tracked items, two or three workstreams | A shared document or spreadsheet with a schedule table and logs | Cheapest to adopt. Breaks when dependencies need recalculating |
| Cross-team dependencies and a real critical path | Dependencies, Gantt view, critical path, baselines | Check which plan tier includes critical path. It is often not the base tier |
| Shared people across programs | Workload or resource views by person and week | Only useful if other commitments are entered too |
| Several programs reporting upward | Portfolio rollups | Agree status definitions before buying rollups |
| Engineering already in an issue tracker | Use its planning layer and link business workstreams to it | Avoid copying tickets by hand into a second tool |

List prices read on official pricing pages on 2026-11-14, per user per month billed annually, for orientation only:

| Tool | Tiers and price | Program features by tier |
|---|---|---|
| [Asana](https://asana.com/pricing) | Starter $10.99, Advanced $24.99, Enterprise by quote | Dependencies and Gantt from Starter. Critical path, portfolios and resource management from Advanced ([help](https://help.asana.com/s/article/critical-path-on-timeline)) |
| [Smartsheet](https://www.smartsheet.com/pricing) | Pro $9, Business $19, Enterprise by quote | Gantt from Pro. Workload tracking on Business. Portfolios on Enterprise. Resource management is an add-on |
| [Jira](https://www.atlassian.com/software/jira/pricing) | Free to 10 users, Standard and Premium priced by user count (about $7.92 and $16.25 at 10 users on annual billing) | Cross-team planning and dependency management on Premium |
| [monday work management](https://monday.com/pricing) | Basic $9, Standard $12, Pro $19, Enterprise by quote, three-seat minimum | Timeline and Gantt from Standard. Resource and portfolio management on Enterprise |
| [Linear](https://linear.app/pricing) | Basic $10, Business $16, Enterprise by quote | Built for software teams. Initiatives on all plans, API on all plans |
| [Microsoft Planner](https://www.microsoft.com/en-us/microsoft-365/planner/microsoft-planner-plans-and-pricing) | Planner Plan 1 $10, Planner and Project Plan 3 $30 | Dependencies and timeline on Plan 1. Baselines, critical path and portfolios on Plan 3 |
| [Notion](https://www.notion.com/pricing) | Plus $10, Business $20, Enterprise by quote | Databases with dependencies. Better for documents and lightweight tracking than schedules |
| [Airtable](https://airtable.com/pricing) | Team $20, Business $45, Enterprise by quote | Gantt and timeline from Team. Flexible, but you build the program model yourself |

Feature placement changes often. Confirm the tier against the vendor's documentation and run a two-week trial with the real program before committing.

## Set it up

### Context

Before drafting anything, gather five inputs. First, the strategy or plan the program serves. Second, the decision that created it and who made it. Third, the constraints: dates, budget, contracts and regulatory steps. Fourth, other programs competing for the same people. Fifth, the systems where work and money are already tracked. Interview each likely workstream lead and the sponsor separately. Ask what success looks like, what worries them and what they need from others. The differences between those answers are the program's real risks.

### People

| Role | Holds | Typical time |
|---|---|---|
| Sponsor | Outcome, resources, conflicts above the program lead, change approval above threshold | One to two hours a week, more at decisions |
| Program lead (often BizOps, Chief of Staff or a program manager) | Integrated plan, logs, cadence, escalation, interfaces | Half to full time for a material program |
| Workstream leads | Their workstream's plan, forecast and risks | Part of their role, protected in their goals |
| Decision owners | Specific decisions in the decision-rights record | At the decision dates |
| Finance partner | Budget, benefits baselines, economic assumptions | A few hours a month |
| Acceptors | Acceptance of named deliverables | At milestones |
| Steering group, if one is needed | Sponsor plus the executives whose resources are committed | Monthly or at gates |

At an early startup one person can hold several roles. Write down which.

### Authority

The charter states what the program lead may decide, what they may require from others, and where conflicts go. Set a change threshold: changes below it are the program lead's call and are logged. Changes above it go to the sponsor. The worked program uses one week of schedule or $25,000. A title or a seat in the steering meeting is not authority. If the program lead lacks the mandate to require updates from workstreams, fix that with the sponsor before building trackers.

### Artifacts by scale

| Scale | Minimum set |
|---|---|
| Small, two or three workstreams | One-page charter, schedule table with dependencies, a single log for risks, issues and decisions, weekly written update |
| Medium, four to eight workstreams | Charter with economics, benefits register, integrated schedule with critical path, capacity view, separate RAID and decision logs, change log, status pack, steering every two to four weeks |
| Large or regulated | All of the above with baselines, formal gates, acceptance records, audit trail in the company's system of record |

### Cadence

Weekly: workstream leads update forecasts and logs before a short working session that handles cross-workstream issues only. Every two to four weeks: a steering review that takes decisions, using a written pack sent beforehand. At milestones: acceptance against the stated test. Connect these to the company's existing [operating cadence](../../operating-cadence/SKILL.md) rather than adding parallel meetings.

## Run and maintain it

1. Recompute the forecast each week from updated durations and remaining work. Never edit the finish date by hand.
2. Report status from rules, not feelings. Off track means the forecast misses the commitment. At risk means a blocking finding exists. Status colors without the rule invite optimism.
3. Bring decisions, not updates, to steering. Each decision arrives with options, their finish date and cost, and what each gives up.
4. Check the logs for hygiene: owners, due dates, items not updated in three weeks, issues without a decision route.
5. Check recorded decisions against the decision-rights record.
6. Re-baseline only through change control. Keep the old baseline.

## Failure signals

| Signal | Likely cause | Response |
|---|---|---|
| Status green until two weeks before the date | Forecasts not recomputed, or status by sentiment | Status from rules. Recompute weekly |
| Same issue discussed in three meetings | Missing decision owner or veto confusion | RAPID for that decision |
| Workstream leads stop updating | Tool burden or no consequence | Simplify the tool. Sponsor reinforces |
| Program lead doing workstream work | Capacity gap in a function | Name it as a staffing issue to the sponsor |
| Benefits never measured | No baseline or owner at the start | Benefits register before approval |
| Program never closes | No handover criteria | Closure record with receiving owners |

## Closure

Close delivery when acceptors have signed and receiving owners run the new process. Keep benefits measurement open until the benefit dates in the register. The closure report states what was delivered, what moved to a later phase, and which open risks transferred and to whom. It also gives actual cost against budget, lessons, and when benefits will be checked. A program that lands its scope and misses its benefit has not succeeded, and the closure report says so.

## Prepare teams before the planning meeting

At SimCorp, roughly 500 developers worked on one product. Teams arrived at joint planning with features they had barely seen. The first sprint exposed enough uncertainty to force replanning. The coaches moved feature review before the meeting and asked teams to signal which items they could take. Assign someone to resolve items that no team can take before teams commit to dates. [SimCorp experience report](https://agilealliance.org/resources/experience-reports/what-safe-doesnt-tell-you/).

When a sponsor approves a revised cost baseline, preserve and reconcile actual costs against the original record. Record the date, scope and approval for the reset. Check whether controls operated consistently before relying on the new variance. [GAO Cost Estimating and Assessment Guide](https://www.energy.gov/sites/default/files/2024-08/gao-20-195g.pdf).

After launch, distinguish new use from activity that shifted from an existing service. Transport for London tracked both on the Elizabeth line. It also distinguished observed use and journey outcomes from early employment and housing changes near stations. Preserve those boundaries when a sponsor reports benefit. [Post-opening evaluation summary](https://content.tfl.gov.uk/elizabeth-line-post-opening-evaluation-summary-findings.pdf).

In a follow-up review, record whether the response is good enough and whether the team has proved the fix works. The Webb review board rated some responses appropriate with work still due. Keep the action open until its owner supplies acceptance evidence. [2019 Webb follow-up](https://www.nasa.gov/wp-content/uploads/2018/06/webb_irb_assessment_with_nasa_response_03.01.19.pdf).
