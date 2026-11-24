# Executed delivery, readiness and response

All inputs and outcomes below are synthetic. The calculations are this library's own worked application. They demonstrate a bounded decision, not a universal launch checklist. [Google's account of reliable launches](https://sre.google/sre-book/reliable-product-launches/) describes tailored readiness checks, dependency capacity, contingency planning and gradual rollout. Its specialist engineering roles and release rights do not transfer to a BizOps or Chief of Staff operator.

## Inputs and authority

A US growth-stage SaaS company proposes a customer beta on workday 8. The operator is the delegated delivery coordinator, not the technical release approver. The Product lead chooses invitation scope within the approved beta. Engineering decides technical release readiness. The support owner accepts coverage. Existing Security and Legal owners retain their actual required approvals. The sponsor resolves conflicts outside those boundaries.

The outcome is usable access for the selected customers with no unresolved launch-blocking findings and accepted support coverage. Delivery acceptance requires the signed readiness disposition, access tests, tested invite cap, support routing and trained backup. Customer adoption is a separate later outcome.

## 1. Execute the schedule

Durations are forecast working days, with day 0 as the start and finish-to-start dependencies. The owners confirm that the parallel support work uses different people from integration work. There are no additional calendar or resource restrictions in this example.

| Work | Duration | Prerequisite | Earliest start → finish | Latest start → finish for day 8 | Slack |
|---|---:|---|---|---|---:|
| Integration A | 4 | None | 0 → 4 | 1 → 5 | 1 |
| Technical review B | 2 | A | 4 → 6 | 5 → 7 | 1 |
| Support preparation C | 3 | None | 0 → 3 | 4 → 7 | 4 |
| Joint rehearsal D | 1 | B and C | 6 → 7 | 7 → 8 | 1 |

The longest dependency chain A–B–D takes seven days, leaving one day before the committed beta. These activities share one day of deadline slack, not three independent recovery days. A five-day review instead of two makes the forecast finish day 10, two days late. Adding people to Support does not shorten that chain. If the same engineer is later assigned to A and C, the table must be recalculated with the resource conflict.

The review interface is: Engineering provides the identified release candidate and test results at A's finish. Reviewers return their dispositions by B's finish. Engineering verifies closure of launch-blocking findings before D. Any scope change identifies the changed candidate and whether previous evidence still applies. A completed review of an obsolete candidate cannot make the new one ready.

## 2. Calculate the operating limit

Support has 90 staffed hours available in the first beta week, after leave and other assignments. Current service requires 72 hours. Twelve existing cases need half an hour each to recover the backlog, or six hours. The support owner supplied two beta load scenarios: 0.6 or 1 case per account in that week, with half an hour per case. These are scenario assumptions, not probability estimates.

| Invitation choice | Beta demand at 0.6 cases/account | Total with service + backlog | Beta demand at 1 case/account | Total with service + backlog |
|---|---:|---:|---:|---:|
| 60 accounts | 18 hours | 96 hours | 30 hours | 108 hours |
| 20 accounts | 6 hours | 84 hours | 10 hours | 88 hours |

The 60-account proposal fails both cases even if the code ships on time. The upper-load arithmetic permits at most `(90 − 72 − 6) / 0.5 = 24 accounts`. Twenty provides two hours beyond the modeled upper case. Neither 24 nor 20 proves service readiness: validate arrival peaks, shift coverage, required skills and the evidence behind case duration. If only one person can resolve beta issues, aggregate hours can conceal that bottleneck.

Recommend a 20-account beta, preserving backlog recovery. The strongest alternative is delaying invitations until coverage expands, which avoids exposing customers to a thin service margin. Full launch becomes feasible on this arithmetic only with at least 108 suitable staffed hours in the upper case, or lower validated demand. More nominal headcount without available skills does not meet that condition. With 80 available hours instead of 90, the same upper-case limit falls to four accounts, so the 20-account recommendation must be reopened.

## 3. Make the contingency actionable

A qualified temporary support provider could add 18 hours. Confirming and preparing that coverage takes three working days. The provider must be operational before the day-8 beta. Checking availability and obtaining a sponsor decision can consume one day. The latest condition-observation time is `8 − 3 − 1 = day 4`. A weekly check that next occurs on day 6 is too late.

The trigger record therefore says: the support owner checks confirmed qualified coverage by day 4. If less than 108 hours is credibly available, the Product lead must choose the bounded invitation plan or seek another authorized option by day 5. Budget approval remains with its owner. A supplier promise alone is not staffed coverage. This branch uses the same upper-load assumption as the readiness calculation, avoiding contradictory plans.

On day 5 the sponsor declines extra coverage. Within the approved capacity, Product sets the 20-account invitation cap. Cost of that choice: 40 planned invitations wait and their product learning arrives later. Benefit: the plan does not depend on unconfirmed people. The operator records the recommendation separately from the sponsor's funding decision and Product's invitation decision. The Product lead owns the customer sequencing. The technical owner can still stop release for an unresolved finding.

## 4. Execute a control and inspect its evidence

Control objective: invitations stay within the accepted service envelope. Product owns invitation configuration. Support accepts the envelope. Engineering owns its implementation. Before first invitations and before each expansion, retain the proposed cap, support capacity acceptance, authorized disposition, config version and observed invite count. The check covers all invitation changes during this bounded beta, not a sample of configuration activity.

In the synthetic first run, the operator reconciles all three proposed changes before the first invitations. Initial cap 20 had prior acceptance. A proposed increase to 40 lacked updated coverage evidence and was rejected before activation. Product then narrowed the initial cohort to 15, within its scope right, with the required disposition and an observed system cap of 15. Thus two authorized configuration changes operated and one proposed change was prevented. The rejected proposal is evidence of the control acting, not a third launched configuration. A screenshot of the policy alone would not prove any of this. The control owner still judges sufficiency and residual risk.

This scoped check detects no unapproved change in that stated population. It does not establish security compliance, permanent control effectiveness or absence of changes in other systems. If an unauthorized expansion had activated, restore the accepted exposure through the authorized response path, assess affected customers and retained evidence, then investigate why prevention failed. A later signature would not erase the exception.

## 5. Handover and outcome check

The beta proceeds on day 8 only after the required owners accept readiness. Support receives working access, routing instructions, the upper-load assumption, a backup demonstration and the live count source. Of the 15 invited accounts, 14 were active. Seven beta cases consumed 3.5 hours. The team completed six backlog hours and met every existing service commitment in the scoped record. Total observed effort is `72 + 6 + 3.5 = 81.5 hours`, below the 90-hour envelope. Seven cases over 14 active accounts is 0.5 cases per active account. Report that denominator separately from the 15 invited and the initially approved maximum of 20.

This week supports continuing the bounded beta, not extrapolating to 60 invitations. Review unresolved cases, duration distribution, customer use and coverage before expansion. Support accepts ongoing operational ownership. Product retains invitation decisions. The operator leaves the recurring workflow after verifying the next change runs through those owners. The outcome check records learning and service behavior separately from the on-time delivery claim.

## Transfer to other contexts

At a small startup, one founder may hold several approval roles, but the technical evidence and capacity arithmetic still matter. An influence-only BizOps operator prepares these choices and seeks acknowledged commitments rather than assigning other teams' resources. In a public-company unit, use the established release, financial and risk systems and enterprise dependency owners. The operator can maintain the integrated view without creating a second approval authority or substituting an internal spreadsheet for the official record.
