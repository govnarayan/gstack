# Worked operating model: two business lines on one platform

Synthetic. This case applies [operating model design](operating-model-design.md) end to end: diagnose, compare, design, secure agreement, implement and maintain. The [org design case](org-design-worked-case.md) then designs the teams, roles and costs inside the chosen model.

## Three things that get confused

| | Operating model | Org chart | Meeting cadence |
|---|---|---|---|
| Answers | How value reaches customers: which capabilities exist, who owns and decides what, how work and information flow, how performance is measured and rewarded | Who reports to whom | When people meet to review and decide |
| Changes when | Strategy, customer mix or scale changes what must work together | Leadership, spans or team boundaries change | Decision needs or information flow change |
| Common error | Redrawn boxes presented as a new model | Reporting lines used to settle decision rights | New forums added without removing old ones |

A reorganization that changes reporting lines and leaves decision rights, interfaces and incentives untouched usually leaves the original problem in place. In a [2014 McKinsey survey](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-secrets-of-successful-organizational-redesigns-mckinsey-global-survey-results), 21 percent of those involved in a redesign called it a success. Where leaders were fully aligned, 49 percent reported success, against 1 percent where they were slightly or not at all aligned. That is a self-reported survey, not a controlled study. It still argues for designing beyond the chart and aligning leaders first. Galbraith's [Star Model](https://jaygalbraith.com/services/star-model/) names the levers that must fit together: strategy, structure, processes, rewards and people. The target-state table in section 3 covers each of them.

## Setting

A US software company of about 1,100 people, preparing for an IPO in two years. It sells two ways. A self-serve product is bought by small teams with a card. An enterprise product is sold by account executives with security reviews, implementation and annual contracts. Enterprise is 40 percent of revenue and growing at 70 percent a year. Self-serve is 60 percent and growing at 25 percent.

Today the company is organized by function. One Product and Engineering organization, one Sales organization, one Customer Success organization, and shared Security, Data, Finance and Legal. Each function has its own priorities. Nobody below the CEO owns either business line's results.

## 1. Diagnose

The CEO asked the Chief of Staff for a recommendation on whether to create business units. The CoS started with work, not boxes.

**Strategic choices that must hold.** Grow enterprise revenue fast while keeping self-serve efficient. Keep one product platform: the self-serve funnel feeds enterprise accounts, and two codebases would double cost.

**Value flows traced.** The CoS reconstructed eight recent enterprise deals and six self-serve growth experiments from records and interviews.

| Flow | Where time went | Evidence |
|---|---|---|
| Enterprise deal to signed contract | Security questionnaires waited a median of 15 working days in the shared queue, legal redlines 9 days | Ticket timestamps for 8 deals |
| Enterprise implementation | Integrations work competed with self-serve features in one roadmap, and 3 of 8 implementations slipped a month | Roadmap history, project records |
| Self-serve experiment | Experiments waited 2 to 4 weeks for data pipeline changes | Data team queue |
| Pricing decisions | Discount and packaging requests bounced between Sales, Product and Finance. There were two reversals in a quarter | Decision notes |

**Competing explanations tested.**

1. *Unclear direction?* No. Both strategies were clear and written.
2. *Insufficient capacity?* Partly. Security review demand had doubled with enterprise volume. Reviewers had not.
3. *Poor interfaces and decision rights?* Yes. Nobody could set priority between an enterprise integration and a self-serve feature without escalating to the CEO. Pricing had no single decider.
4. *Incentives?* Yes. Sales was paid on bookings with no view of implementation cost. Product goals were all self-serve funnel metrics.
5. *Grouping?* Partly. Enterprise-specific work (integrations, solutions engineering) was scattered across four leaders.

The diagnosis is that enterprise growth needs an owner who can set priorities across the work that is specific to it. The platform, data and security capabilities stay shared and gain explicit service commitments. The problem is not that the functional structure exists. The problem is that it has no mechanism to arbitrate between two business lines.

## 2. Compare options

| Option | Description | Fixes | Costs and risks |
|---|---|---|---|
| A. Keep functions, add interfaces | Functional structure stays. Add service agreements, a priority forum and a pricing decision owner | Queues and pricing reversals, if the forum works | No one owns enterprise results. The CEO stays the arbiter |
| B. Full business units | Two GMs, each with their own product, engineering, sales, success, data and security | Clear ownership for each line | Two platforms in practice, duplicated scarce specialists, self-serve funnel no longer feeds enterprise |
| C. Hybrid: business lines on shared platforms | An Enterprise GM owns enterprise P&L and the enterprise-specific capabilities. Platform engineering, data, security, finance and legal stay shared, with service commitments and priority rights | Ownership of enterprise results, arbitration through the GM and the service agreements | GM role is new and hard to fill. Shared teams can still starve one line without real priority rules |

**Design requirements** written before choosing, each with a test:

1. Enterprise deals get security responses within 5 working days at planned volume. Test: queue model at next year's demand.
2. One platform and one data foundation. Test: no duplicated core engineering or data platform roles.
3. A single decider for enterprise priorities below the CEO. Test: replay the last three priority conflicts.
4. Pricing has one decision owner per decision type. Test: replay the two reversals.
5. The transition does not pause enterprise implementations. Test: implementation plan through the change.

**Capability sort.** Each capability was placed by two questions: does it create differentiation the strategy needs, and does it need business-line-specific context?

| Capability | Differentiating? | Business-specific? | Placement |
|---|---|---|---|
| Core platform engineering | Yes | No | Shared, platform team |
| Enterprise integrations and admin features | Yes for enterprise | Yes | Enterprise business line |
| Solutions engineering and implementation | Yes for enterprise | Yes | Enterprise line |
| Self-serve growth engineering | Yes for self-serve | Yes | Self-serve line, under Product |
| Security review | No, but a constraint on deals | Partly | Shared pool with enterprise priority and a service commitment |
| Data platform | No | No | Shared |
| Analytics | No | Yes, needs line context | Shared team with embedded partner pods |
| Pricing and packaging | Yes | Partly | Decision rights per decision type, Finance agrees |
| Finance, Legal, People | No | No | Shared, with a business partner per line |

**Replay on real work.** Under option C, the three priority conflicts would have been decided by the Enterprise GM within the GM's capacity envelope. One escalation to the CEO would remain where shared platform capacity was contested. Under option A, all three still go to the CEO. Under option B, they disappear. The security replay shows each business unit would need its own reviewers. The self-serve unit's queue would be the worst in the company (see the pooling test in the org design case).

**Recommendation:** option C. **Strongest argument against:** the hybrid needs a GM with strong cross-functional judgment and shared teams that honor priority rules. If either fails, it becomes option A with an extra executive. **Flip condition:** if enterprise grows past roughly half of revenue and its product needs diverge enough to justify a separate platform roadmap, revisit option B. That threshold is a judgment marker for the next review, not a researched cut-off.

## 3. Design the target, and the interim

| Element | Current | Interim (quarters 1–2) | Target (quarter 3 on) |
|---|---|---|---|
| Ownership of results | CEO only | Enterprise GM owns enterprise bookings and contribution. Self-serve is still under the CPO | Enterprise GM and a self-serve owner, each with a business-line P&L |
| Decision rights | Escalate to CEO | Enterprise GM decides enterprise priorities inside a capacity envelope, RAPID for pricing types | Same, with a quarterly capacity allocation decided by the CEO with both owners |
| Structure | Functional | Enterprise engineering, integrations and solutions move to the GM and shared teams stay unchanged | As interim, plus an embedded analytics pod per line |
| Processes | One roadmap queue | Separate enterprise roadmap, shared platform roadmap with an intake form | Quarterly allocation of shared capacity, monthly service review |
| Interfaces | Ad hoc tickets | Service agreements for security, data and platform | Service agreements with measured response times and an escalation path |
| Systems and data | One P&L | Finance builds business-line contribution reporting | Business-line P&L in the monthly close |
| Measures | Functional metrics | Enterprise: bookings, time to security response, implementation on time. Shared teams: service response, consumer satisfaction | Plus business-line contribution margin |
| Incentives | Sales on bookings | GM on enterprise contribution plus a company revenue goal | Sales on bookings with an implementation-cost adjustment, proposed to People and Finance |
| Governance | Weekly exec meeting | Monthly business-line reviews in the existing operating cadence | Annual operating-model review |

**Service agreement, security review (excerpt).** Provider: Security review lead. Consumers: Enterprise GM, CPO, Procurement. Scope: customer security questionnaires, vendor reviews, product security sign-off. Commitment: enterprise questionnaires answered within 5 working days for 90 percent of requests at planned volume. Priority rule: enterprise deal reviews ahead of vendor reviews unless a vendor review blocks a launch, in which case the Director Security decides. Capacity: reviewed each quarter against the queue model. Escalation: Director Security, then the COO. Reporting: weekly queue age and response times.

**Transition cost** appears line by line in [the cost section of the companion write-up](org-design-worked-case.md#4-cost-the-transition). It is about $2.5 million in the first year, mostly new hires that would have been needed for enterprise growth under any option. The structural costs specific to the model are the GM role, finance reporting set-up, intake tooling and a quarter of dual running.

## 4. Secure agreement

The CoS sequenced agreement so the debate happened on principles and evidence before names and boxes.

1. **Principles first.** The executive team agreed the five design requirements in one session.
   Bain recommends setting design principles, typically between seven and fifteen, before choosing structure ([Bain, 2015](https://www.bain.com/insights/design-principles-for-a-robust-operating-model/)). Five were enough here because the scope was one decision.
2. **Evidence second.** Each executive saw the value-flow evidence for their area before the group session.
3. **Decision rights for the decision itself.** The CEO decided. The CFO held Agree because the model changes how the P&L is reported. The CRO, CPO and General Counsel gave input.
4. **Pre-wiring.** The CRO initially preferred option B. The CoS walked through the security and platform replays with the CRO privately.
   The CRO's concern was losing account executives' influence over implementation timing. The design addressed it through the GM's priority rights, so it was not a concession.
5. **Recorded decision and dissent.** The CPO's concern that self-serve would become "the other business" was recorded, and a self-serve owner with equal standing was added to the target state.

## 5. Implement

1. People and Legal own the employment steps: role changes, communication to affected people and any changes to terms. The CoS coordinates the plan, not those decisions.
2. Announce the decision rights and service agreements at the same time as the reporting changes. A chart announced alone signals that nothing else changes.
3. Pilot the security service agreement for six weeks before the GM starts, measuring queue age weekly.
4. Track adoption on real work: are priority conflicts decided by the GM, are shared teams meeting response commitments, has the CEO stopped arbitrating?
5. Review at 90 days with the same evidence used in the diagnosis.

**What happened in the synthetic run.** The security pilot cut median response from 15 to 6 working days with a fifth reviewer hired. It missed the 5-day target in two of six weeks during a quarter-end surge. The GM started in month three. In the first quarter, the GM decided 11 priority conflicts and escalated 2. Pricing reversals stopped. Self-serve experiment wait times did not improve, because the data platform queue had not been given a service commitment. That gap was added at the 90-day review.

## 6. Maintain

An operating model drifts. Hold an annual review with the leaders of each line and shared function, chaired by the COO or CoS. It reviews service performance, unresolved accountability gaps and requested changes to capability ownership, and sends recommendations to the CEO. Review earlier when:

1. An acquisition adds a business line or a capability.
2. One business line passes the flip condition above.
3. A shared service misses its commitment for two consecutive quarters.
4. Priority escalations to the CEO rise back above a handful a quarter.

## The failed alternative, in more detail

The CRO's first proposal was option B: a full Enterprise business unit with its own engineering, security and data. Costed on the same demand, it needed three dedicated security reviewers for enterprise and left self-serve and vendor reviews with one. The queue model shows that splitting makes the enterprise wait worse than a shared pool of the same total size. Splitting also pushes the other queue to about 14 working days. It also needed duplicate data engineers. The proposal solved ownership by sacrificing the shared platform the strategy depended on.
