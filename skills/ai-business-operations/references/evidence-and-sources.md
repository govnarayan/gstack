# Evidence and source limits

The operating evidence should match the choice. Build an evidence map across offline evaluations, production monitoring, human review, user feedback, experiments and incident analysis. Explain what each source resolves and what it leaves unknown. The operator owns the map, reconciliations and operating implications rather than merely collecting expert opinions.

For task evaluations, check that test cases represent actual users, tools, data and failure costs. Inspect whether the grader rewards the intended outcome. Verify resulting records or environment state when the task changes a system. Distinguish success in at least one of several attempts from reliability across repeated attempts. Preserve the full attempt cost and avoid silently excluding failed runs. Report material cohort regressions even when the overall score improves.

For research work, inspect factual grounding, question coverage, source quality, contradictions, and whether the recommendation follows from the evidence. Human judgment remains necessary where the quality standard is context-dependent.

For services, distinguish the measured user-relevant indicator, its target, and any contractual consequence. A target must include a measurement window and validity conditions. Do not transfer an infrastructure availability target to a business function or import Google's operating model as a requirement.

## Methodological references

Use these references for the specific question they address:

- [Anthropic agent evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) for task-specific tests, repeated trials, traces, and complementary forms of evidence.
- [Google SRE service objectives](https://sre.google/sre-book/service-level-objectives/) for distinguishing a measured service indicator, its target and an agreement.

Technical service examples do not determine business-function targets or staffing.

Use [research and release operations](research-and-release-operations.md) to turn these distinctions into an evidence packet. Use [service economics and capacity](service-economics-and-capacity.md) to reconcile quality with the cost and capacity of all attempts.

These references do not supply current model pricing, provider rankings, or a universal operating cadence. Retrieve current facts when they affect a real decision. See [source credits](../../../SOURCES.md) for library influences and attribution.
