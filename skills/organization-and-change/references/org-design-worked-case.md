# Worked org design: teams, roles and costs inside the model

Synthetic. This continues the [operating model case](operating-model-worked-case.md), which chose an Enterprise business line on shared platforms. Here the design team works out the teams, roles, interfaces, staffing sequence and cost for the 57-person Product and Platform organization. Every number comes from [org_design_check.py](../scripts/org_design_check.py) run on the [roster](../examples/org-roster.csv) and [plan](../examples/org-design-plan.json):

```sh
python skills/organization-and-change/scripts/org_design_check.py --roster skills/organization-and-change/examples/org-roster.csv --plan skills/organization-and-change/examples/org-design-plan.json --markdown <scratch>/org.md
```

The design team has four members. The SVP Product and Platform decides within the organization. The Chief of Staff runs the design. The People business partner owns employment steps. The Finance partner owns cost. The CEO approved the operating model and holds the budget.

## 1. Start from work and workload

Before drawing anything, the team estimated the work each capability must deliver next year, from the plan's deal and implementation volume.

| Capability | Demand next year | Current capacity | Basis |
|---|---|---|---|
| Enterprise engineering (features, integrations) | 9 FTE rising to 11 | 8 (5 enterprise engineers, 2 integrations engineers, 1 former manager returning to engineering) | Enterprise roadmap and 40 planned implementations |
| Solutions engineering | 4 rising to 5 | 1.5 (one engineer and a manager at half time) | One SE per 10 active enterprise deals, from the last two quarters' records |
| Security review | 4.3 rising to 5.0 | 3.5 (three reviewers and a lead at half time) | Offered review hours at 32 productive hours a week, planned at 80 percent utilization |

Solutions engineering is the binding constraint, not structure. A reorganization that ignored it would move boxes and leave deals waiting.

## 2. Spans and layers: read the flags, decide each one

The check compares each manager's span with the range for the role type they were hired for. The ranges follow McKinsey's manager archetypes. They are player-coach 3 to 5 reports, coach 6 to 7, supervisor 8 to 10 and facilitator 11 to 15. Source: [McKinsey, 2017](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/how-to-identify-the-right-spans-of-control-for-your-organization). McKinsey says no single span fits all managers. These ranges are prompts to ask why, not targets.

| Measure | Before | After |
|---|---:|---:|
| People | 57 | 59 |
| Managers | 14 | 15 |
| Layers | 5 | 5 |
| Median span | 3 | 3 |

The team took each flag and made a decision with a reason.

| Manager | Span | Flag | Decision |
|---|---:|---|---|
| Eng manager, Integrations | 2 | One or two reports | Role becomes senior engineer and the two engineers join Enterprise engineering. People leads the conversation and the role change |
| Analytics manager | 12 | Above supervisor range | Split into two pods: a new Analytics lead for the Enterprise partner pod takes six analysts |
| Director Solutions Engineering and Solutions manager | 1 each | Two stacked one-report layers | Solutions manager becomes a player-coach lead. The director keeps the role because three SE hires arrive this year. Review when the team reaches five |
| Director Security | 2 | One or two reports | Kept: a specialist leader with a review lead and a security engineer. The review lead is a player-coach. Revisit if the pool grows past six |
| Head of Data | 2 | One or two reports | Kept: two managers with distinct technical work (platform and analytics) |
| VP Engineering | 2 | One or two reports | Kept for now, see below |
| Director Product Engineering | 1 after | New flag created by the design | Moving Enterprise and Integrations out left this director with one manager |

The last row matters. The first draft of the design created a span-one director. The team considered folding Self-serve engineering directly under the VP. It chose to keep the director for one quarter because a Self-serve growth squad is planned for Q2, with a dated review. That is a judgment the check cannot make, but it made the team look.

## 3. Staffing and hiring sequence

Capacity after hiring ramp, counting new hires at half capacity in their first quarter:

| Team (quarterly gap) | Q1 | Q2 | Q3 | Q4 |
|---|---:|---:|---:|---:|
| Enterprise engineering | 0.0 | +0.5 | +1.5 | +1.0 |
| Solutions engineering | −1.5 | −0.5 | −1.0 | −0.5 |
| Security review | −0.3 | 0.0 | −0.3 | −0.5 |

Solutions engineering is short every quarter even with three hires. Two moves follow:

1. **Resequence a hire.** Enterprise engineering runs ahead of demand from Q2. The Q3 enterprise engineering requisition moves to a second Q1 solutions hire.
   This trades a later feature capacity surplus for deal coverage when it is needed. The Finance partner confirmed the cost is close to neutral.
2. **Bounded temporary cover.** One enterprise engineer with implementation experience covers solutions work for Q1 under a written loan agreement.
   The agreement sets 50 percent, ends when the second SE completes ramp, and has the GM deciding priority conflicts.

Security review stays slightly short. The pooling test below decides how to use the fifth reviewer.

## 4. Cost the transition

| Quarter | Added run-rate | One-time | Total |
|---|---:|---:|---:|
| Q1 | $410,000 | $295,000 | $705,000 |
| Q2 | $475,000 | $52,000 | $527,000 |
| Q3 | $597,500 | $98,000 | $695,500 |
| Q4 | $597,500 | $0 | $597,500 |

First-year total $2.53 million. Exit annual run-rate $2.39 million. One-time costs are recruiting fees at 20 percent of first-year cost, intake tooling and Finance set-up of business-line reporting. They also include a quarter of dual running while the former Integrations manager hands over people duties.

Most of the run-rate is hiring the enterprise plan needs under any structure. The cost attributable to the operating model itself is the GM role, the analytics lead uplift and the three set-up items. It is $507,000 in the first year ($420,000 + $30,000 + $57,000). Presenting the full $2.53 million as "the cost of the reorganization" would overstate it. Presenting only the model-specific cost would hide the hiring commitment. The pack shows both. Resequencing the Q3 hire (section 3) changes these figures slightly, and the Finance partner reran them before approval.

## 5. A staffing conflict, tested

Enterprise asked for three security reviewers dedicated to its deals. Security proposed one pool serving all reviews with enterprise priority. The team modeled both with the Erlang C queueing formula, which estimates waits for a pool of parallel servers under random arrivals. Real arrivals are burstier, so these waits are lower bounds.

Demand: 8 enterprise reviews a week at 10 hours each, 5 vendor and self-serve reviews at 6 hours each, 32 productive hours per reviewer week.

| Option | Pool | Reviewers | Utilization | Chance of waiting | Mean wait (working days) |
|---|---|---:|---:|---:|---:|
| Dedicated | Enterprise | 3 | 83% | 70% | 2.2 |
| Dedicated | Vendor and self-serve | 1 | 94% | 94% | 14.1 |
| Pooled | All | 4 | 86% | 71% | 1.7 |
| Pooled with one hire | All | 5 | 69% | 36% | 0.3 |

Dedicated reviewers make the enterprise wait longer than a pool of the same size. They push the other queue to about three weeks, which would block vendor onboarding and product launches. Pooling with the fifth reviewer brings everyone under half a day on average. Enterprise priority inside the pool shortens the enterprise wait further. The Director Security decided, with the GM's agreement, on one pool of five, enterprise priority and weekly queue reporting. The decision includes a review if enterprise demand passes 10 reviews a week.

The Enterprise GM's underlying worry was losing influence over reviewers' priorities. The service agreement answered it directly: enterprise deal reviews go first, with an escalation path. Dedicated headcount was a proxy for that control.

## 6. Role profiles

**GM Enterprise.** Purpose: grow enterprise revenue profitably on the shared platform. Outcomes: enterprise bookings, contribution margin, implementation on time, time to security response. Decides: enterprise roadmap priorities within the allocated capacity, solutions staffing and enterprise packaging inside the pricing decision rights. Does not decide: platform architecture, security policy, company pricing strategy. Reports to: CEO. Direct reports in this scope: Enterprise engineering manager, Director Solutions Engineering. Outside this scope: enterprise sales and customer success. Interfaces: platform, data and security service agreements and the monthly business-line review. Capabilities sought: has run a P&L or a business line through rapid growth, and can win trade-offs with peers without escalating every one. Success evidence at six months: priority conflicts decided without CEO escalation, implementations on time, response commitments met.

**Solutions lead (player-coach).** Purpose: technical win and implementation plan for enterprise deals. Outcomes: deals supported per quarter, implementation hand-off quality. Decides: SE assignment to deals within the GM's priorities. Spends about half the time on deals. Reports to: Director Solutions Engineering.

**Security review lead.** Purpose: run the review pool to its service agreement. Outcomes: response times by stream, quality of reviews. Decides: queue order inside the priority rule. Escalates exceptions to the Director Security. Player-coach, about half time on reviews.

**Analytics lead, Enterprise partner pod.** Purpose: enterprise analysis with company-consistent definitions. Outcomes: GM's review pack, deal and implementation analytics, metric definitions agreed with the data team. Reports to: Analytics manager. Works day to day with the GM's team.

## 7. Interface agreement: Enterprise engineering and Platform engineering

| Term | Agreement |
|---|---|
| Platform provides | Core services, APIs and infrastructure on the shared roadmap |
| Enterprise may | Build on public platform interfaces without approval and request platform changes through the intake form |
| Platform commits | Triage requests within 5 working days, quarterly allocation of 20 percent of platform capacity to business-line requests, split by the CEO's quarterly allocation |
| Enterprise commits | Requests with business case and deadline and no private forks of platform code |
| Conflicts | Platform director and GM first, then the SVP. Capacity allocation disputes go to the CEO at the quarterly allocation |
| Measures | Request age, allocation used, incidents caused by business-line changes |
| Review | Quarterly, with both leads |

## 8. Manager capacity and incentives

The Enterprise engineering manager goes from 5 to 8 reports, inside the supervisor range, with two senior engineers able to lead work. The GM starts with two direct reports in this scope, plus sales and customer success leaders outside it. The span is narrow by design while the role is new.

Incentives: the GM's goals combine enterprise contribution with a company revenue goal, so local wins that damage self-serve do not pay. Shared-team leaders are measured on their service commitments and a twice-yearly consumer survey. A proposal to adjust sales compensation for implementation cost went to People and Finance, who own the decision.

## 9. Implement

1. People and Legal plan individual conversations, role changes and any changes to terms before anything is announced. The operator does not hold those conversations.
2. Announce the new decision rights, service agreements and reporting changes together.
3. Move teams at a sprint boundary. Integrations work in flight stays with its engineers.
4. First 30 days: the GM and Platform director replay the last quarter's three conflicts under the new interface agreement.
5. At 90 days: check spans against the flags list, the Solutions gap, the security queue and whether the CEO is still arbitrating priorities.

## The failed alternative: delayering to a span target

An earlier proposal from outside the design team applied a minimum span of six to every manager. It would have removed the Director Security, Head of Data and Solutions director roles. It failed the work test. The Security director is the escalation point in the priority rule. Removing the role sends review conflicts to the SVP. The data managers run technically distinct teams. The Solutions director is about to absorb three hires. A low span does not identify a role to remove. It identifies a question to ask. McKinsey reports savings of 10 to 15 percent of managerial costs from rightsizing spans and layers in its client work. Those savings come from examining each role's work, not from a universal minimum.
