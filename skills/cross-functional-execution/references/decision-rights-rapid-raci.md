# Choosing how a company decides

Start with the decision, cost of reversal, authority and uncertainty. Identify who controls implementation. Read the existing charter and replay the last contested decision before choosing a method.

If priorities and resources sit in different reporting lines, use [matrix stakeholder alignment](stakeholder-alignment-in-a-matrix.md) before convening the decision. A nominal owner may control neither budget nor people.

## Choose how much participation the decision needs

| Method | Use when | Failure to test |
|---|---|---|
| An owner decides after taking advice | One person can act and affected people hold information the owner lacks. At AES a project developer retained the call after consulting directors. [Bakke](https://ethix.org/2004/06/01/creating-real-fun-at-work) | The acquisition performed poorly after an electricity-price forecast miss. Advice from senior people cannot validate a common assumption. |
| A group consents | A bounded team shares an aim and can explain what would make implementation unsafe. [Rau](https://www.sociocracyforall.org/the-day-i-consented-to-a-proposal-i-hated/) | A preference becomes a veto, or silence hides an unacceptable impact. Hear concerns separately and test each against the shared aim. |
| A leader decides, consults individually, consults the group or delegates | Vary participation with distributed information, ability to implement and time. [Vroom and Jago](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Leadership/Vroom_Jago_2007_The_role_of_the_situtation_in_leadership.pdf) | A vote counts equally informed views by assumption. Name who knows the work, who must commit and whose approval is mandatory. |
| Classify the problem before selecting a method | A repeatable task can use an established rule. A specialist can analyze a tractable problem. An uncertain interaction may require small probes. [Snowden](https://thecynefin.co/part-five-origins-of-cynefin/) | Debate over categories delays containment. Stabilize immediate harm through the incident owner, then revisit what can be learned. |
| Set the process by reversibility | An owner can test a reversible change within a bounded loss. Escalate a conflict of objectives the team lacks authority to resolve. [Bezos](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) | Calling a choice reversible ignores downstream commitments. State the rollback owner, deadline, cost and customers affected. |
| Allocate explicit roles | Separate who proposes, who can block, who decides and who executes when authority crosses teams. [Choi](https://www.coinbase.com/blog/how-we-make-decisions-at-coinbase) | A chart can exist while three executives still believe they own the same call. Confirm the names against an actual disputed case. |

In a single reporting line, an outcome owner can often consult and act. In a matrix, another manager may retain staffing or a policy veto even after the decision.

At Square, an engineering lead reopened consultation on a testing policy after objections. Engineers could raise concerns before the same policy was reissued. [Rajaram](https://review.firstround.com/square-defangs-difficult-decisions-with-this-system-heres-how/)

## Assigning work, advice and approval

| Tool | Question it answers | Roles | Source |
|---|---|---|---|
| RACI (a responsibility assignment matrix) | Who does each task or deliverable, and who answers for it being done | Responsible does the work. Accountable answers for completion, one per task. Consulted gives input before. Informed is told after | Project-management practice. PMI treats it as one form of responsibility assignment matrix |
| RAPID | Who holds which role in one important decision | Recommend leads the process and proposes. Agree must sign off before it moves. Perform executes. Input advises without a veto. Decide makes the call, one person | [Bain, "Make decisions work"](https://www.bain.com/insights/decision-insights-3-make-decisions-work) (2010), Rogers and Blenko, "[Who has the D?](https://www.bain.com/insights/who-has-d-how-clear-decision-roles-enhance-organizational-performance/)", HBR, January 2006 |
| DACI | Who drives a decision to closure and who approves | Driver runs the process to a date. Approver is one person who decides. Contributors have a voice, not a vote. Informed have neither | [Atlassian Team Playbook](https://www.atlassian.com/team-playbook/plays/daci) |
| Single owner (often called a directly responsible individual) | Who owns this outcome end to end | One named owner, with stated limits | Common startup practice |

Bain's guidance on Agree is the part most often lost. Only a few roles should hold that veto, such as legal counsel for certain decisions or the head of an affected unit. Anyone exercising a veto must offer an alternative or escalate to the person with the D ([Bain, 2007](https://www.bain.com/insights/manager-at-work-who-has-the-d/)). RAPID is a registered Bain trademark. The roles are what matter, not the label.

## Why RACI fails on contested decisions

RACI's Accountable answers for a task being completed. It does not say who may block a decision or whose input is advisory. "Consulted" lumps together a finance leader who can stop a pricing change and a regional lead who only has a view. When a decision is contested, everyone Consulted behaves as if they hold a veto. The decision bounces between reviews, and the Accountable person cannot close it without risking a later reversal.

RAPID fixes that by separating Agree (veto, rare) from Input (advice, common) and making one person Decide. It does nothing for tracking forty deliverables. A RAPID chart for "update the support runbook" is ceremony.

## Choose by situation

| Situation | Use | Why |
|---|---|---|
| Many deliverables, clear ownership in principle, risk of dropped handoffs | RACI on deliverables, one Accountable each | Makes work and handoffs visible |
| A few high-value decisions crossing units, with real disagreement | RAPID on those decisions only | Separates veto from advice and names one decider |
| A decision with one obvious owner and limited spillover | Single owner plus a short decision record | Anything more slows a reversible call |
| A product or engineering team that already uses DACI | DACI, mapping Approver to the D | Use the vocabulary people know and check that the Approver has real authority |
| Committee or board approval required | Record the actual approval body and quorum | Do not force a single decider where governance requires a vote |
| Crisis or incident | The incident process's commander | Decision-rights design is for normal operation |

Bain ties process depth to the value at stake. When a decision reopens, identify what failed. A missing approval needs an authority change. Conflicting incentives may require a new option. An unresolved factual question needs evidence.

Bain's survey work links decision effectiveness to financial results. It covered nearly 800 companies, at 95 percent confidence or better in every country, industry and size it studied (Bain, "Decision insights 1: Score your organization," 2010). That is a correlation across companies. It does not show that adopting a chart causes better results.

## Other arrangements operators use

| Arrangement | What it says | Where it fits | Source |
|---|---|---|---|
| One-way and two-way doors | Irreversible decisions get slow deliberation. Reversible ones are made fast by a person or small group. Never use one process for every decision, and decide with about 70 percent of the information you want | Setting how much process a decision deserves, before choosing roles | Bezos shareholder letters [2015](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) and [2016](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) |
| Disagree and commit | After a decision, people who argued against it commit to making it work. Unescalated disagreement otherwise ends by exhaustion | Closing contested decisions without consensus | Bezos 2016 and Grove's *High Output Management* (secondary summaries) |
| Directly responsible individual with approval triggers | One person owns and decides after consulting. A separate decider is needed when three or more functions, large money, significant risk, reputation or competing success measures are involved | Fast-moving companies that want ownership by default | [GitLab handbook](https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/) |
| SPADE | Setting, People, Alternatives, Decide, Explain. Participants commit out loud. Coinbase's variant gives each decision an expiry date | A single large decision that needs a written record | [Rajaram's toolkit](https://docs.superhuman.com/@gokulrajaram/gokuls-spade-toolkit), read |
| Advice process and consent | Anyone may decide after seeking advice from those affected (advice process), or a proposal passes when no one has a reasoned objection (consent) | Teams that have granted authority to seek advice or consent and can explain how an objection is resolved | Reinventing Organizations wiki, sociocracy advocates |

Three cautions from the wider evidence. First, letters mean different things in different frameworks. DACI's D is a Driver who does not decide, while GitLab's DRI does. Define your letters. Second, no independent study shows that RAPID, RACI or DACI improves results. Atlassian's page cites a "McKinsey" finding of 25 percent higher success for DACI, which could not be traced to any McKinsey publication. Third, McKinsey's 2019 survey found clear roles alone are not sufficient ([McKinsey, 2019](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/decision-making-in-the-age-of-urgency)). It splits decisions into big bets, cross-cutting decisions and delegated decisions. Big bets depend on debate quality, with a designated devil's advocate. Cross-cutting decisions depend on meeting design and coordination. Delegated decisions depend on empowerment and coaching. It is a self-reported survey, but it argues for matching the mechanism to the decision type rather than charting everything.

Roles settle who decides, not how well. Lovallo and Sibony asked managers about 1,048 major decisions. In [their 2010 regression](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-case-for-behavioral-strategy), process explained six times as much of the outcome as analysis did. The process items included exploring uncertainties and hearing views that contradicted the senior leader. Outcomes were self-rated, so read it as a strong association. For the D on a big bet, a [12-question checklist](https://hbr.org/2011/06/the-big-idea-before-you-make-that-big-decision) by Kahneman, Lovallo and Sibony screens a recommendation for bias. The decider asks three questions privately. Is the team self-interested? Has it fallen in love with its proposal? Were dissenting views explored?

Rajaram's own toolkit adds two points the summaries skip. Consensus means no ownership, so the goal is that everyone is heard, not that everyone agrees. And most fights over a decision are really unstated differences about why it matters, so write the "why" before listing options. His alternatives must be feasible, different in kind from each other and cover the problem space.

When the same kind of decision recurs, companies often create a standing group, such as an architecture review or product review. Will Larson's [essay on these groups](https://lethain.com/scaling-consistency) lists the design choices: how it influences (binding or advisory), how teams reach it, size, time commitment and how members are picked. Six or fewer can work as a real team, and more than ten needs subgroups. He names four failure modes. Domineering groups decide without living with the consequences. Bottlenecked groups take on more than they can review. Status-oriented groups become about membership, and inert groups do nothing. Check a proposed forum against all four before creating it.

Andy Grove set out much of this in 1983, before RAPID existed. The source here is [Kudija's chapter notes](https://matthewkudija.com/reading-notes/2021-04-11-High-Output-Management.html). His ideal process runs from free discussion to a clear decision to full support, including from those who disagreed. Decisions belong at the lowest competent level, nearest the facts. Peers deciding among themselves fall into "peer-group syndrome," each waiting to sense the consensus before speaking. His fix is a senior chair who drives to a decision. Before deciding, he answers six questions. What is the decision, and by when? Who decides, and who is consulted? Who can ratify or veto, and who is told afterward? RACI and RAPID are later formalizations of the same list.

Three more operator methods fill gaps in the charts above. James Everingham ran engineering at Instagram. He allowed one accountable person per decision in a RACI ([First Round roundup](https://review.firstround.com/the-6-decision-making-frameworks-that-help-startup-leaders-tackle-tough-calls)). The chart was published so nobody learned of a decision secondhand. A matrix from Shklarski, featured in the same roundup, lists each option's benefits, costs and risks, then a mitigations row for softening each risk. It suits the reversible decisions that should never reach the top. Hughes Johnson's Stripe operating principles settle conflicts by context: "think rigorously" governs irreversible decisions, and "move with urgency" governs reversible ones. Principles written that clearly let people decide as a founder would.

Andrew Bosworth separates reviews by purpose: inform, discuss or decide ([boz.com](https://boz.com/articles/reviews)). Naming which one a meeting is stops a discussion from being mistaken for a decision.

A practical sequence: first decide whether the decision is a one-way or two-way door. Then decide its type. Then assign roles, using a single owner for two-way doors and RAPID for contested one-way doors that cross units.

## Who sets decision rights, and how

1. **The program lead drafts.** List the decisions the program needs, with the date each must be made by. Propose roles for each, with a one-line reason.
2. **The sponsor confirms who holds the D.** For decisions that cross units, the sponsor or the executive above both units assigns it. A program lead cannot give themselves the D for another function's call.
3. **Affected executives confirm their roles in one session**, not by email chains. Disagreement about who decides is the first real decision. Settle it before the substantive debate.
4. **Publish the record** where the program's decision log lives. Link each decision entry to its rights.
5. **Hold the line.** When someone with Input tries to block, the program lead points to the record and offers escalation to the D. When a decider wants to re-decide, check whether new evidence warrants it.
6. **Revisit when the organization changes.** A reorganization, a new executive or a merger invalidates parts of the record.

## Worked decision: one pricing call, two ways

Synthetic. A growth-stage software company is moving to usage-based pricing. Product recommends a usage metric with a platform minimum. Sales wants flat tiers for small customers, who dislike unpredictable bills. Finance worries about forecastability and revenue recognition. Customer Success worries about existing annual contracts.

**First attempt, RACI only.** The program's single responsibility chart listed "Pricing model" with Accountable: VP Product, Consulted: CRO, CFO, VP Customer Success, Head of Data, General Counsel. Over three weekly reviews, the CRO and CFO each raised objections. Each revision satisfied one and reopened the other. Nobody could say whether the CRO's objection was a veto or advice. The VP Product had accountability for the task but no authority to close a choice that set the company's revenue model. Three weeks of the critical path were spent.

**Second attempt, RAPID on this decision.** The COO, as sponsor, proposed and the CEO confirmed:

| Role | Holder | Reason |
|---|---|---|
| Recommend | VP Product | Owns the analysis and the product consequences |
| Agree | CFO | Revenue recognition and forecast commitments to the board make this a finance sign-off, not advice |
| Input | CRO, VP Customer Success and Head of Data | Their knowledge shapes the recommendation. None holds a veto |
| Decide | CEO | The decision sets the company revenue model across units |
| Perform | Billing engineering, Sales enablement | Carry out the decision |

The recommendation came back with the CRO's concern addressed inside the design rather than traded against Finance. The design was a platform minimum plus usage, with small accounts on a capped monthly price. Resolving a two-sided conflict with an option that serves both interests, rather than splitting the difference, is the pattern to look for. The CFO agreed with a condition on forecast reporting. The CEO decided in the next review. The CRO's preference for flat tiers was recorded as dissent and considered.

The grandfathering of annual contracts went to a separate RAPID, with the CRO deciding and General Counsel holding Agree. Sales compensation for usage revenue went to a third, with the CFO deciding. Putting all three into one "pricing" decision would have recreated the original stall.

**Where RAPID went wrong in the same case.** The comp-plan decision was later logged as decided by the CRO, who held Agree, not the D. The [program check](../scripts/program_check.py) flags exactly this, and the [worked program](worked-program.md) shows the correction. A chart only helps if the decision log is checked against it.

## Decision-rights record

| Field | Example |
|---|---|
| Decision ID and question | D-01: usage price metric and list price |
| Needed by | Week 5, because rating-engine work starts in week 6 |
| Recommend | VP Product |
| Agree | CFO (forecast and revenue recognition) |
| Input | Head of Data, VP Customer Success, CRO |
| Decide | CEO |
| Perform | Billing engineering, Sales enablement |
| Escalation if Agree withholds | CFO proposes an alternative or escalates to the CEO within one review |
| Confirmed by and date | COO and CEO, week 1 |

## Failure signals

1. Decisions reopen after being recorded, by someone not holding the D or an Agree.
2. Every decision lists four or more Agree holders. Consensus by veto has returned.
3. The chart exists but meetings still end with "let's take it offline."
4. RAPID charts appear for routine work, and people stop reading them.
5. A decision is recorded as decided by the person who recommended it.

When these appear, fix the specific decision's roles. Re-running a company-wide RACI workshop rarely helps.

## Start the decision clock at the right event

[Emilie Choi on The Peel](https://www.thespl.it/p/the-coo-playbook-with-emilie-choi) describes Coinbase's practice for complex decisions. One person recommends, up to two must agree, and one decides. The group usually numbers five to ten. Coinbase aims to decide within 48 hours after full input arrives.

Record when the question opened, when required input arrived and when the decider ruled. Otherwise the team can meet the decision deadline while the business waits weeks for input. Give each outstanding input an owner and latest useful date.

[Gokul Rajaram on X](https://x.com/gokulr/status/2123819618871767260) compares Coinbase with Square's SPADE. Both concentrate authority and limit consultation. He highlights private input, an explicit deadline and commitment after dissent. He calls out committee growth as a threat to ownership.

Keep the distinction Choi makes for required committees. Where approval belongs to a committee, identify its reserved decision and name the individual accountable for implementation. A working group need not become another approval body.
