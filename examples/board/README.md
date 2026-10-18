# Board: a provider-neutral decision skill

Board is a reusable decision workflow for high-stakes technology choices,
especially enterprise agent and harness work. It creates constructive tension
before a team commits money, data, or operational authority.

The model is an execution backend, not the source of governance. The same
workflow can be used with Claude, Gemini, OpenAI models, or a local inference
runtime when each backend operates under the same task, tool, permission,
budget, and approval contract.

## The five roles

| Role | Responsibility |
| --- | --- |
| Audit Red Team | Identify security, operational, financial, and compliance risks; state no-go conditions and rollback needs. |
| Hypothesis Prosecutor | Ask only decision-changing questions and make the strongest credible case against the preferred option. |
| Research & Traction Explorer | Compare alternatives, identify adoption constraints, and design a small pilot that produces useful evidence. |
| Strategic Advisor | Turn evidence into options, trade-offs, ownership, governance, and a staged plan. |
| Executive President | Make a proceed, change-course, pause, or stop recommendation with a named owner and review gate. |

Every role follows the **Professor standard**: explain the central idea plainly,
separate facts from assumptions and recommendations, and make success criteria
observable.

## What the harness owns

Use one provider-independent contract for every execution backend:

```text
HarnessSpec = {
  task_contract,
  context_policy,
  tool_allowlist,
  permission_profile,
  budget,
  approval_gates,
  output_schema,
  eval_suite
}
```

An adapter may translate the contract for a provider or runtime. It may report
that a capability is unavailable; it must not widen tools, permissions, budget,
or approval authority.

## Included templates

- [`codex/`](codex/) is a validated Harness² Codex tree. Its `AGENTS.md`
  contains the required trigger and its skill lives at the supported
  `.agents/skills/board/SKILL.md` path.
- [`claude-code/`](claude-code/) is a reference template for a Claude Code
  project. Harness² does not presently materialize a Claude Code substrate, so
  treat it as a portable instruction pattern rather than a native integration.

## Practical examples

### Choose a coding-agent provider

Run the council against two cloud providers and one local option on the same
holdout tasks: issue diagnosis, test generation, code review, and a bounded
migration. Compare accepted-task quality, cost per successful task, latency,
security findings, and developer acceptance. Start with read-only work and do
not grant merge authority as part of the pilot.

### Add multi-model routing

Keep one `HarnessSpec` for a bounded workflow, such as test-failure diagnosis.
Build an adapter for the current provider and one alternative, then compare them
on the identical evaluation set. The router may select an approved backend; it
may not expand data access or tool permissions.

### Introduce pull-request review

Start with repository search, diff analysis, and evidence-backed suggestions.
Require each finding to reference a file location, test result, or policy.
Evaluate against known defective and clean pull requests. Only expand scope when
false positives, missed defects, cost, and developer acceptance meet a written
threshold.

## Safety baseline

Version prompts, skills, policies, adapters, tool definitions, evaluation
suites, and approved changes in Git. Default to isolated workspaces, least
privilege, bounded budgets, and human approval for consequential actions. Do
not promote a workflow based only on vendor benchmarks or a successful demo.
