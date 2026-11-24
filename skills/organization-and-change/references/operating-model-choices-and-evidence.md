# Operating model choices and the evidence behind them

[Operating model design](operating-model-design.md) is the procedure for running a design. The [operating model case](operating-model-worked-case.md) runs it end to end. This reference covers the published canon behind those steps. It compares what the main frameworks say an operating model contains, names the choice that comes first, and weighs the evidence. Decision rights are one element of an operating model. They have their own reference in [decision rights](../../cross-functional-execution/references/decision-rights-rapid-raci.md).

Sources were read on 2026-11-15. Where only a summary or abstract was available, the text says so. The [knowledge index](../../../catalog/knowledge-index.md) lists every source checked, including those that could not be read.

## Test the operating boundary on a real transaction

Pick one request crossing a team boundary. Record who recognizes demand, decides priority, allocates capacity, performs the work and accepts the result. Measure waiting separately from work time.

At Uswitch, affiliate marketing initially collaborated with product teams to learn what they needed. Once the interface stabilized, teams consumed it as a service. [Paul Ingles](https://teamtopologies.com/industry-examples/organizational-evolution-accelerating-delivery-of-comparison-services-uswitch)

Keep people working together while both sides still discover the requirement. Switch to a service when the provider can specify inputs, output, support and failure handling without a meeting.

At Spotify, independent tool choices made service ownership hard to find. A shared catalog with locally supplied extensions addressed discoverability while preserving local development. [Spotify Engineering](https://engineering.atspotify.com/2021/05/a-product-story-the-lessons-of-backstage-and-spotifys-autonomous-culture)

If the problem is missing ownership information, test a catalog entry on a real support request before transferring the team. Report response time and who actually resolved it.

Onfolio found manual customer follow-up inside one portfolio business. Its central team changed the system and leadership together. [Onfolio](https://onfolio.com/the-operating-model-shift-that-fixed-our-portfolio/)

Central operation fits when the local unit lacks the capability and the center can supply it. Reassess after the local team can reproduce the result without central intervention.

## What an operating model contains

The frameworks overlap far more than their labels suggest.

| Framework | Elements | Best use | Source and read status |
|---|---|---|---|
| Bain operating model | Structure, accountabilities, governance, behaviors, people, process and technology | Starting a design. Bain has the senior team write 7 to 15 design principles on one page before drawing options | [Blenko and Root, 2015](https://www.bain.com/insights/design-principles-for-a-robust-operating-model/), read in full |
| Galbraith Star Model | Strategy, structure, processes, rewards and people, all aligned with each other | Checking that a new structure is backed by matching processes and rewards | Galbraith's own six-page paper, text extracted and checked |
| McKinsey 7S | Strategy, structure, systems, shared values, style, staff and skills, with no element ranked above another | Diagnosing why a structural change did not change behavior | [McKinsey Quarterly, 2008](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/enduring-ideas-the-7-s-framework), read in full |
| Operating Model Canvas (POLISM) | Processes, organization, locations, information, suppliers and management system, around a value promise | Starting with one chain of work that delivers customer value before choosing owners, cross-unit processes and suppliers | Campbell, Gutierrez and Lancelott, 2017. [Author-hosted first chapter](https://operatingmodelcanvas.com/wp-content/uploads/2017/03/omc-chapter1.pdf), pp. 2 to 33 |
| Nadler and Tushman congruence model | Work, people, formal organization and culture, judged by fit | Explaining performance gaps as misfit between parts | 1980 journal article, library access only. Secondary summaries only |

Read together, they reduce to seven questions an operator can ask about any unit:

1. What work and capabilities must this unit perform, and which ones distinguish it?
2. How standardized and how integrated must processes and data be across units?
3. How is the work grouped, and how do the groups coordinate?
4. Where is the work done, and by whom (internal, shared service or outside provider)?
5. Who decides what, and who can block?
6. How is the unit run: goals, reviews, metrics and incentives?
7. What skills, behaviors and tools does it need?

Questions 1 and 4 are covered in the design procedure. Question 5 is decision rights. Question 6 is the [operating cadence](../../operating-cadence/SKILL.md) skill. The sections below cover the published evidence on 2, 3, 6 and the newer models.

## The first choice: how standardized and how integrated

Jeanne Ross at MIT CISR defines an operating model as the level of process integration and standardization a company needs to deliver to its customers. Standardization means units do the same work the same way. Integration means units share data, customers or supply chains. The two choices give four types ([Ross, CISR briefing, December 2005](https://cisr.mit.edu/publication/2005_12_3C_OperatingModels), read in full from the [PDF](https://public.dhe.ibm.com/la/documents/imc/la/pe/news/events/mit_2010/1_2005_12_3c_operatingmodels.pdf)).

| Type | Standardization | Integration | Example in the briefing | What units keep |
|---|---|---|---|---|
| Diversification | Low | Low | Carlson's autonomous hospitality businesses | Almost everything |
| Replication | High | Low | Marriott hotels running the same systems | Customer relationships, within mandated processes |
| Coordination | Low | High | Toyota Europe sharing product data across countries | Products and processes, within shared data and customer interfaces |
| Unification | High | High | Delta and Dow Chemical on one global process set | Little. Process owners design centrally |

Four points from the briefing matter in practice.

1. **Most companies aim for the hardest type.** Of 103 companies surveyed in 2004, 63 percent targeted unification. Only 9 percent targeted diversification, 17 percent coordination and 11 percent replication.
2. **Unification is the slowest to pay back.** It needs a great deal of time, money and management attention. Replication and coordination produce reusable capabilities sooner.
3. **The off-diagonal types are decision-rights designs.** Replication trades central process standards for local customer ownership. Coordination trades shared data and customer interfaces for local processes.
4. **Different levels can run different types.** Johnson & Johnson ran diversification across the company while one U.S. pharmaceutical group used coordination and a European unit used replication.

Ross's later books extend the idea. *Enterprise Architecture as Strategy* (2006) adds four maturity stages: business silos, standardized technology, optimized core and business modularity. The authors hold that a company cannot skip a stage. *Designed for Digital* (2019) names five building blocks: shared customer insights, an operational backbone, a digital platform, an accountability framework and an external developer platform. Both books were read only through reviews and CISR's own summary ([Larson's notes](https://lethain.com/notes-on-enterprise-architecture-as-strategy), [CISR, 2018](https://cisr.mit.edu/publication/2018_0601_BuildingBlocks_RossMockerBeath)).

Do not confuse the company types with CISR's December 2025 briefing on IT operating models. It asks a narrower question: how the company organizes to get value from technology. Its two axes are innovation velocity and enterprise IT leadership with reuse ([Thorogood and Woerner, 2025](https://cisr.mit.edu/publication/2025_1201_EntITOperatingModels_ThorogoodWoerner), read in full from the authors' published audio transcript).

| IT model | Velocity | Reuse | Share of firms | Operations on enterprise platforms | Revenue from innovation |
|---|---|---|---|---|---|
| Legacy Modernizer | Low | Low | 33 percent | 53 percent | 37 percent |
| Creative Sprinter | High | Low | 16 percent | 70 percent | 49 percent |
| Efficient Builder | Low | High | 18 percent | 65 percent | 54 percent |
| Adaptive Innovator | High | High | 33 percent | 80 percent | 71 percent |

The authors' headline is that strong IT leadership with high reuse goes with more innovation at either velocity. The transcript gives no sample size or method, and the link is correlation. Their advice is to decide the needed velocity first, then how hard to push shared platforms, rather than arguing centralize versus decentralize.

For a software company with two business lines on one platform, the question becomes concrete. Do the lines share customers or data that must stay consistent? Then coordination at least. Must they run the same billing, support and release processes? Then replication or unification. The worked case linked above works through a version of this choice.

## Grouping and coordination: the classic theory

The older organization-theory work gives the most usable rule for drawing boxes. Group by interdependence first.

James Thompson (1967) named three kinds of interdependence between units. Pooled means units share resources but do not depend on each other's work, and coordination is by standard rules. Sequential means one unit's output feeds the next, and coordination is by plans and schedules. Reciprocal means units feed each other back and forth, and coordination is by mutual adjustment, which is the most expensive kind. His proposition is to put reciprocally interdependent work in the same group first, then sequential, then pooled ([Nickols, 2019](https://www.nickols.us/ThompsonPropositions.pdf), an eight-page list of Thompson's propositions, text checked).

Henry Mintzberg (1980) listed five ways work gets coordinated: mutual adjustment, direct supervision, and standardizing work processes, outputs or skills. He described five typical structures, each leaning on one mechanism. A simple structure relies on direct supervision. A machine bureaucracy relies on standard processes, and a professional bureaucracy on standard skills. A divisional form relies on standard outputs, and an adhocracy on mutual adjustment (Management Science 26(3), checked against the scanned article).

Lawrence and Lorsch (1967) showed that units facing different environments become different in goals and time horizons. The more different they are, the more deliberate integration they need. Only secondary summaries of the book were read.

The practical sequence is to map who depends on whom before choosing a structure. Then put the heaviest two-way dependencies inside one leader's scope. Coordinate the rest by plans, shared standards or service agreements.

## Shared services, centers of excellence and embedded teams

Hackett describes a three-layer pattern. Transaction work sits in shared service centers, specialist advice in centers of excellence, and knowledge workers stay embedded in the business. Deloitte's 2023 shared services survey had about 500 responses. Both sources are vendor or self-reported, and neither publishes controlled outcome data. The design procedure's section on ownership, delivery mode and location is the method to use. Treat the vendors' savings claims as marketing until the company's own baseline shows them.

## Product and team-based models

| Model | What it says | Evidence and caution |
|---|---|---|
| Product operating model | Empowered, cross-functional product teams own outcomes, not feature lists. Funding follows teams rather than projects | [Cagan, SVPG, 2023](https://www.svpg.com/the-product-operating-model/). His book *Transformed* (2024), read through reviews, frames the move as three changes: how you build, how you solve problems, and how you decide which problems to solve. It estimates six months to two years. His view that most transformation attempts fail comes from coaching many of them |
| Amazon single-threaded ownership | One leader owns one product or service end to end. Clear ownership matters more than team size | [AWS executive insights](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/), read. The page itself names duplication and silos as the cost |
| Spotify squads and tribes | Autonomous squads grouped into tribes, with chapters and guilds across them | The 2012 paper calls itself a snapshot of "a journey in progress" (Kniberg and Ivarsson, text checked). A former employee says it was never fully implemented ([Lee, 2020](https://jeremiahlee.com/posts/failed-squad-goals/)) |
| Team Topologies | Four team types and three interaction modes | Covered in [structure choices](structure-choices-and-evidence.md#team-types-and-interaction-modes) |

The common thread is that these models move authority to teams and pay for it in duplication. Use them when work can be split into products or services that change independently. Do not copy one company's chart without its conditions.

## Distributed authority

| Case | Reported design | Evidence quality |
|---|---|---|
| Buurtzorg | Teams of up to 12 nurses, with about 50 back-office staff and about 20 coaches for more than 10,000 nurses | [HBS Working Knowledge, 2023](https://www.library.hbs.edu/working-knowledge/this-company-lets-employees-take-charge-buurtzorg), read. Reported satisfaction and overhead figures are not independently audited |
| Haier | More than 4,000 microenterprises, most of 10 to 15 people. About 200 face the market, 50 or more incubate new businesses, and about 3,800 sell services such as design or HR to the others. Market-facing units can drop an internal supplier and buy outside | Hamel and Zanini, HBR 2018, read through the authors' own excerpt ([Zanini](https://www.michelezanini.com/haier-hbr)). The chairman told McKinsey he removed a middle layer of more than 12,000 employees ([2021](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/shattering-the-status-quo-a-conversation-with-haiers-zhang-ruimin)). Growth figures are company-reported |
| Zappos and Holacracy | Roles and governance replace managers | Departure figures conflict, from about 14 percent to nearly a third. Hsieh blamed the buyout offer, while critics blamed the model |
| Netflix | Context rather than control, with an informed captain for each significant decision | [Netflix culture page](https://jobs.netflix.com/culture), read |

Lee and Edmondson's 2017 review of self-managing organizations is the scholarly counterweight. It treats these as experiments whose limits are not yet known (abstract only). These models fit best where work is done by one profession in small, modular units. They fit worst where many functions must coordinate on one product.

## The management system

Most operator writing treats the operating model as including how the company is run: goals, reviews and incentives. Claire Hughes Johnson's *Scaling People* describes founding documents, then an operating cadence, then an operating system. Stripe published her [founding documents chapter](https://stripe.com/guides/atlas/creating-your-founding-documents) free, and it was read in full. Founding documents hold a mission, long-term goals, operating principles and team charters. She says they matter most once a company passes about 40 or 50 people. Stripe's two-page list of long-term goals, written in 2014, was unchanged eight years later. Quarterly and annual goals ladder up to it. Her principles guide daily work rather than state beliefs ([First Round](https://review.firstround.com/the-6-decision-making-frameworks-that-help-startup-leaders-tackle-tough-calls)). When two conflict, context decides which wins. EOS describes a six-part system for companies of 10 to 250 people (vendor page, read). Both are systems built and run by operators, refined across many companies.

Paul Graham's 2024 essay ["Founder Mode"](https://paulgraham.com/foundermode.html) challenges the usual advice to treat each part of the org chart as a black box run by a direct report. He predicts that skip-level contact will become normal. His example is Steve Jobs's annual retreat for the 100 people he thought most important, who were not the top 100 on the chart. The essay draws on what founders told him after Brian Chesky's talk at a Y Combinator event: hiring "good people" and giving them room had failed them. Graham warns that the idea will be misused as an excuse not to delegate. For operating model work, his question is where the borders of autonomy sit. He expects them to vary by company and to move as managers earn trust.

The strongest evidence that management practices matter comes from economics. Bloom and Van Reenen measured management practices in 732 medium-sized manufacturers in the U.S., France, Germany and the U.K. Their scores were strongly associated with productivity, profitability, sales growth and survival ([NBER w12216, 2006](https://www.nber.org/papers/w12216), abstract read from the PDF). The practices scored were monitoring, targets and people incentives, close to what an operating cadence covers. The sample is manufacturing, and the link is an association, not proof that adopting the practices causes the gain.

## Claims about AI-era operating models

The large firms have published views. Treat them as hypotheses.

| Firm | Claim | What is missing |
|---|---|---|
| [McKinsey, 2025](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era) | Two to five people can supervise 50 to 100 agents on one end-to-end process | Method and sample |
| [Bain, 2026](https://www.bain.com/insights/an-operating-model-for-the-age-of-ai/) | Org charts become accountability charts, and judgment, not capacity, becomes scarce | Footnotes for its company examples |
| [BCG, 2026](https://www.bcg.com/publications/2026/design-your-company-for-ai-not-ai-for-your-company) | Only 5 percent of organizations capture AI value at scale, and the work is 70 percent people | A disclosed method |

All three pages were read in full.

The useful test is local. Pick one end-to-end process, measure its current cost, cycle time and error rate, redesign it with agents, and compare. The [AI-augmented operator](../../ai-augmented-operator/SKILL.md) skill covers that method.

## What the evidence does and does not show

No controlled study of operating-model redesign outcomes was found. What exists is surveys, cases and firm experience.

| Source | Finding | Caveat |
|---|---|---|
| [McKinsey, 2010](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/taking-organizational-redesigns-from-plan-to-practice-mckinsey-global-survey-results) | 16 percent of redesigns met all objectives on time. Only 8 percent also improved performance | Self-reported, "redesign" undefined |
| [McKinsey, 2014](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-secrets-of-successful-organizational-redesigns-mckinsey-global-survey-results) | 21 percent called theirs a success. With fully aligned leaders, 49 percent did, against 1 percent with poor alignment | Self-reported correlation |
| [BCG, 2012](https://www.bcg.com/publications/2012/people-organization-design-flipping-odds-successful-reorganization) | About 90 percent of 1,600 executives had recently reorganized, and fewer than half called it a success | Executives rating their own work |
| [Public Digital, 2023](https://public.digital/2023/01/03/the-traps-of-target-operating-models) | A detailed target operating model is often a best guess that encourages command and control | The author's firm sells an alternative |

The definitions of success differ, so the percentages do not compare with each other. The consistent pattern is that leadership alignment, a narrative the leaders tell themselves, and attention to transition separate the better outcomes. Survey respondents report those links, and no study tests them.

When a reorganization stalls, trace one decision under the new reporting lines. Check who received the information, who had the skills and which behavior the review meeting rewarded. Change the condition that still favors the old decision, then watch the next one. Waterman, Peters and Phillips describe seven interdependent factors with no fixed starting point. [Read the original paper](https://tompeters.com/docs/Structure_Is_Not_Organization.pdf).

When two parts of a company need different ways of working, identify each part’s coordination needs. Check whether their shared approvals or performance measures create an actual conflict. Mintzberg distinguishes workable hybrids and transitions from combinations that impose conflicting controls. [Management Science, pages 338 to 339](https://ocw.uniovi.es/pluginfile.php/10949/mod_resource/content/1/Disen_o_Organizativo.pdf).

## Choose a lens by situation

| Situation | Start with | Why |
|---|---|---|
| Units argue about what should be common | CISR standardization and integration | It forces the one decision every other choice depends on |
| A structure is chosen but behavior has not changed | Star Model or 7S | Both show which matching process, reward or skill is missing |
| Drawing boxes for a function or division | Thompson and Mintzberg | Group by two-way dependence, then pick coordination mechanisms |
| The senior team cannot agree on options | Bain design principles | Agreeing criteria first turns a power contest into a comparison |
| A one-page picture for a workshop | Operating Model Canvas | It covers locations and suppliers, which the others skip |
| Moving to product teams | Product operating model, single-threaded ownership | Also price the duplication they create |
| Considering self-management | Buurtzorg and the critics | The fit conditions are narrow |
| Someone proposes an AI-era redesign | One measured process trial | Published claims have no method behind them |

The strongest argument against using any of these lenses is time. A small company can lose weeks on frameworks when the real problem is one unclear owner. When the problem traces to a single interface or decision, fix that and skip the framework.
