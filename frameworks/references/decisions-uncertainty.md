# Decision rights and uncertainty

Read only the selected card. Mechanisms summarize the cited public sources. Application procedures, examples, and fit judgments are this library's own synthesis. All examples are synthetic.

## Before selecting a card

1. Identify required consent and one final decider to distinguish advice from a veto. [Bain RAPID](https://www.bain.com/insights/rapid-decision-making)
2. Change the assumption most likely to reverse the choice before authorizing expenditure. [Green Book uncertainty guidance](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)
3. Record the latest safe date for input separately from the time the decider needs to rule.

<a id="rapid"></a>

## rapid: RAPID decision roles

Supports: decision-rights, cross-functional-delivery, executive-governance-support.

Context: work.domain=decision_support, role.authority, org.scope, task.consequence.

Decision trigger: A consequential or recurring decision stalls because recommendation, agreement, input, execution, and final authority are confused.

Inputs and evidence: Specific decision, real delegation, required approvals, execution owner, dependencies, and deadline.

Procedure: Define the decision and criteria. Assign Recommend, Agree, Perform, Input, and Decide roles. Limit mandatory agreement to necessary sign-offs and involve those people early. Set the input deadline, escalation path, and decision timing. Record the decision and ensure the performer can execute it.

Output: A decision-role agreement and a decision ready for execution.

Illustrative decision: A synthetic pricing exception has Sales recommend, Finance provide economics, Legal agree only on contractual conditions, a delegated executive decide, and Operations implement. Unresolved required agreement follows the stated escalation route.

Failure conditions and alternatives: A chart cannot grant authority its sponsor lacks. Do not make every stakeholder an agreer. A small routine decision may need only a named owner and boundary. RACI maps delivery tasks instead.

Source: [Bain & Company, RAPID Decision Making](https://www.bain.com/insights/rapid-decision-making).

[Crossrail's baseline review](https://learninglegacy.crossrail.co.uk/documents/initial-control-baseline-and-review-points/index.html) tied delegated authority to sponsor funding decisions. Identify the actual reserved approval and its threshold before giving anyone an agreement role. Escalate only the reserved issue.

<a id="raci"></a>

## raci: RACI responsibility assignment

Supports: decision-rights, cross-functional-delivery, organization-design.

Context: work.domain=cross_functional_delivery, role.authority, org.scope.

Decision trigger: A project has duplicated work, ownerless deliverables, or unclear consultation.

Inputs and evidence: Actual deliverables and tasks, responsible teams, accountable owners, needed expertise, and communication needs.

Procedure: List concrete deliverables or tasks. Assign Responsible for performing work, Accountable for its completion, Consulted for necessary two-way input, and Informed for notification. Resolve gaps and conflicting accountability with actual owners. Check capacity and update assignments when scope changes.

Output: A responsibility matrix tied to delivery, with acknowledged ownership.

Illustrative decision: A synthetic product launch separates release approval, customer communication, and support readiness into distinct rows rather than labeling the entire launch jointly owned by three departments.

Failure conditions and alternatives: Responsibility for a task is not a complete decision process. This card uses Atlassian's published practice and makes no claim that Atlassian invented RACI. Do not import a veto variant without explicit authority. Use DACI or RAPID for a decision.

Source: [Atlassian, Understanding and using RACI charts](https://www.atlassian.com/work-management/project-management/raci-chart).

[Carla Wright's Shopify guide](https://shopify.engineering/running-engineering-program-guide) assigns escalation work and records the resulting decision. A responsibility chart can name a delivery owner while leaving a contested decision unsettled. Test the chart with the last real exception.

<a id="daci"></a>

## daci: DACI decision process

Supports: decision-rights, facilitation, cross-functional-delivery.

Context: work.domain=decision_support, role.authority, task.consequence.

Decision trigger: A cross-functional decision needs one driver and one final approver.

Inputs and evidence: Decision scope, criteria, alternatives, relevant contributors, delegated approver, and deadline.

Procedure: Name the Driver who gathers information and moves the process to a decision. Name one Approver who makes the decision. Identify Contributors and people to be Informed. Gather options and evidence against stated criteria, obtain the approver's decision, then document rationale, effects, and follow-up.

Output: A decision document with owner, date, alternatives, rationale, and notification list.

Illustrative decision: A synthetic analytics-tool choice has an Operations driver and a budget-owning approver. Security and Engineering contribute requirements. Users are informed after a documented choice and implementation assignment.

Failure conditions and alternatives: The approver is an active decision maker, not only a rubber stamp. Contributors do not implicitly have vetoes. Use RAPID when distinct mandatory agreement roles matter, or RACI to assign the resulting work.

Source: [Atlassian Team Playbook, DACI](https://www.atlassian.com/team-playbook/plays/daci).

[Gokul Rajaram's Square account](https://review.firstround.com/square-defangs-difficult-decisions-with-this-system-heres-how/) describes both ambiguous ownership and insufficient consultation. Choose a driver who can collect evidence from dissenters. Preserve the final approver's name separately from the person who announces the outcome.

<a id="spade"></a>

## spade: SPADE for difficult decisions

Supports: decision-rights, facilitation, executive-communications.

Context: work.domain=decision_support, task.consequence=material or high_impact, role.authority.

Decision trigger: An important decision lacks a transparent rationale and accountable execution.

Inputs and evidence: Exact what, when, and why, a responsible decision maker, required approvers, consultants, and feasible alternatives.

Procedure: Set the decision context and deadline. Define People: one responsible decision maker accountable for execution, consultants, and necessary approvers. Develop feasible and meaningfully different Alternatives. Decide after gathering input without equating consultation with consensus. Explain the choice, trade-offs, and ownership in a durable decision record.

Output: A decision narrative that others can understand and execute.

A synthetic team defines the service and timing for a new region. It compares a narrow launch, a partner launch and a delay. It explains its choice and conditions to affected teams.

Failure conditions and alternatives: Use this effort for difficult decisions. Explain does not mean seeking endless agreement after the decision. Do not attribute SPADE to the Heath brothers or WRAP to Gokul Rajaram.

Source: [Gokul Rajaram, Gokul's S.P.A.D.E. Toolkit](https://docs.superhuman.com/@gokulrajaram/gokuls-spade-toolkit).

[Gokul Rajaram's Square account](https://review.firstround.com/square-defangs-difficult-decisions-with-this-system-heres-how/) describes consulting stakeholders before the decision. Ask each to state what evidence would change their preference privately. Give the decider the strongest objection alongside the recommendation.

<a id="wrap"></a>

## wrap: WRAP decision process

Supports: strategy-choices, scenario-response, facilitation.

Context: work.domain=decision_support, task.consequence, role.authority.

Decision trigger: The decision is framed too narrowly or confidence exceeds the evidence.

Inputs and evidence: Current alternatives, assumptions, outside-view evidence, priorities, and potential reconsideration signals.

Procedure: Widen options beyond a binary choice. Reality-test assumptions using disconfirming questions, comparable situations, and small experiments. Attain distance before deciding by changing perspective and clarifying priorities. Prepare to be wrong with plausible outcome ranges and triggers for revisiting the choice.

Output: An expanded option set, assumption tests, chosen option, and reconsideration triggers.

Illustrative decision: A synthetic team considering a permanent hire also tests a time-limited assignment and process redesign. It examines actual workload and sets a revisit point before committing.

Failure conditions and alternatives: A process reduces avoidable mistakes without proving the best choice. It does not allocate formal authority. Pair with DACI or RAPID if ownership is unclear and a decision tree if sequential economics matter.

Source: [Chip Heath and Dan Heath, The WRAP Process](https://heathbrothers.com/wp-content/uploads/resources/The_WRAP_Process_one_pager.pdf).

[Jeff Bezos's shareholder letter](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) distinguishes disagreement with a choice from a fundamental conflict between teams. Test whether both groups can implement the selected option. If they cannot, get the resource conflict resolved before inviting commitment.

<a id="premortem"></a>

## premortem: Premortem

Supports: risk-governance, scenario-response, product-delivery.

Context: work.domain=risk_and_controls, task.consequence, org.scope.

Decision trigger: A team has a favored plan and may be reluctant to voice why it could fail.

Inputs and evidence: A concrete plan, success criteria, participants with different information, dependencies, and a time horizon.

Procedure: Assume the plan has failed at the stated future date. Have participants generate reasons independently before discussion. Collect the failure explanations, examine evidence and controllability, and identify neglected threats. Revise the plan with prevention, detection, contingencies, owners, and a follow-up date.

Output: A revised plan and a short owned risk register.

Illustrative decision: A synthetic migration team imagines that customers could not access service on launch day. The exercise exposes an untested rollback dependency, prompting a rehearsal and a named stop decision.

Failure conditions and alternatives: Vivid risks may crowd out common mundane failures. Do not treat imagined causes as observed facts or use the exercise to manufacture consensus. Scenario planning examines multiple external futures rather than only failure of one plan.

Source: [Gary Klein, Premortem](https://www.gary-klein.com/premortem).

[NASA's Webb review](https://www.nasa.gov/news-release/nasa-completes-webb-telescope-review-commits-to-launch-in-early-2021/) revisited integration and test work. Seed the failure review with a plausible failed handover, ask which evidence would arrive too late, and move that check before the commitment.

<a id="scenario-planning"></a>

## scenario-planning: Scenario planning

Supports: scenario-response, strategy-review, long-range-plan.

Context: work.domain=strategy, task.consequence, org.scope.

Decision trigger: The strategy depends on external conditions that cannot responsibly be reduced to one forecast.

Inputs and evidence: Focal decision and horizon, trends, key uncertainties, plausible causal relationships, and strategic options.

Procedure: Name the decision scenarios will inform. Separate relatively predetermined trends from critical uncertainties. Construct distinct, internally consistent futures, then test the same options across them. Identify moves that remain useful across these futures, contingent moves, vulnerabilities, and observable signals that would change the plan.

Output: Scenario narratives or tables, option implications, and contingent response triggers.

Illustrative decision: A synthetic company tests capacity plans against combinations of demand strength and supplier availability. It reserves a small amount now and specifies what observed orders would justify expansion.

Failure conditions and alternatives: Scenarios are not predictions or assigned probabilities unless separate evidence supports them. Avoid relabeling an optimistic, base, and pessimistic spreadsheet as strategic scenarios. Use sensitivity for parameter ranges and minimax regret for a formal robustness criterion.

Source: [Shell, What are Shell Scenarios?](https://www.shell.com/news-and-insights/scenarios/what-are-shell-scenarios.html).

Use [Crossrail's baseline review](https://learninglegacy.crossrail.co.uk/documents/initial-control-baseline-and-review-points/index.html) to separate an approved baseline from permission to spend the next tranche. For each scenario, name the release gate, which purchase can still wait and who can change it.

[Shell's retrospective](https://www.shell.com/news-and-insights/scenarios/what-are-shell-scenarios/_jcr_content/root/main/section_509167378/promo/links/item0.stream/1652289755448/a0e75f042fee5322b72780ee36e5ba17c35a4fc6/shell-scenarios-40yearsbook080213.pdf) connects its scenarios to refinery investment decisions. Ask executives which asset they would sell or decline to build under a different future. If every scenario funds the same portfolio, revisit the point of disagreement.

<a id="minimax-regret"></a>

## minimax-regret: Minimax regret

Supports: scenario-response, financial-resource, risk-governance.

Context: work.domain=decision_support, task.consequence, role.authority.

Decision trigger: Plausible states have credible payoffs but defensible state probabilities are unavailable.

Inputs and evidence: Feasible options, an explicit state set, comparable payoff units, constraints, and unacceptable losses.

Procedure: Create an option-by-state payoff table. For each state identify the best feasible payoff. Subtract each option's payoff from that state-best payoff to calculate regret. Find each option's maximum regret, then select the feasible option with the smallest maximum. Test whether added states or payoff errors change the result.

Output: A regret table, option with the lowest maximum regret under the specified rule, and sensitivity to the state set.

Illustrative decision: Synthetic payoffs for small, large, and flexible capacity are (40,50), (-20,100), and (30,80) under low/high demand. Maximum regrets are 50,60,20, so flexible capacity wins under minimax regret.

Failure conditions and alternatives: This criterion trades expected upside for protection from foregone opportunity. It can depend heavily on included alternatives and extreme states. It is not expected-value optimization or a guarantee against absolute loss. Use a decision tree when credible probabilities exist.

Source: [Jörg Stoye, Minimax regret treatment choice, author research paper](https://stoye.economics.cornell.edu/docs/CeMMAP-Stoye.pdf).

Use [Jeff Bezos's shareholder letter](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) to check reversibility before applying worst-case regret. Include the cost of waiting and the cost of undoing a bad trial. A cheap reversal can justify testing first.

[Fletcher and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC6468001/) modeled a dam under different rainfall conditions. Maximum regret was $77 million for a small fixed design and $4 million for a flexible one. Those are modeled opportunity costs. Require the same scenarios for all choices and price the flexibility explicitly.

<a id="bayesian-updating"></a>

## bayesian-updating: Bayesian updating

Supports: research-analysis, scenario-response, financial-resource.

Context: work.domain=decision_support, task.consequence, operating.maturity.

Decision trigger: A new signal should change a belief and a decision, but the team is ignoring the prior or confusing conditional probabilities.

Inputs and evidence: Explicit prior probability, competing hypotheses, evidence likelihood under each, and the action threshold.

Procedure: State the hypothesis and prior, including the source. Estimate how likely the observed evidence is under the hypothesis and its alternative. Apply Bayes' rule and normalize across hypotheses. Compare the posterior with the action threshold and test uncertain priors or likelihoods. Update again only for new information.

Output: A posterior belief, assumptions, and an action or further-information decision.

Illustrative decision: In a synthetic demand test, prior success probability is 0.2. A positive signal occurs with probability 0.8 if successful and 0.1 otherwise. Posterior success is 0.16/(0.16+0.08), about 0.667.

Failure conditions and alternatives: A subjective input remains subjective after arithmetic. Correlated signals must not be counted as independent. A posterior alone does not choose an action without payoffs and constraints. Use decision-tree analysis for that step.

Source: [MIT OpenCourseWare, Conditional probability, Bayes' Rule](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/d642d816867bcd205926eefaa116edd8_MIT6_042JF10_chap15.pdf).
[NASA's Webb review](https://www.nasa.gov/news-release/nasa-completes-webb-telescope-review-commits-to-launch-in-early-2021/) revised the schedule after new evidence. Identify which event distinguishes the two explanations. Repeated updates drawn from the same unresolved test delay are dependent observations.

[The ALERTS device review](https://www.fda.gov/media/96418/download) set a safety threshold before collecting the result. The observed event-free share was 96.7%. Its probability of exceeding the 90% threshold was above 0.9999 under the model. Report the observed fraction and the probability about the threshold separately.
