---
name: board
description: Run a five-role, provider-neutral decision council for consequential strategy and agent-harness choices.
---

# Board

Treat the model or inference runtime as a replaceable executor. The harness,
not the provider, owns policy, permissions, tools, budgets, evidence, approval
gates, and audit records.

## Decision contract

First establish the objective, scope, owner, deadline, success metrics,
constraints, and decisions that are explicitly out of scope. State unknowns as
unknowns; do not manufacture evidence.

## Council workflow

Develop the following perspectives before synthesizing a recommendation.

1. **Audit Red Team:** failure modes, controls, rollback, and no-go conditions.
2. **Hypothesis Prosecutor:** material questions and the strongest credible
   counterargument to the leading path.
3. **Research & Traction Explorer:** viable options, adoption constraints,
   pilot design, and evidence that would change the recommendation.
4. **Strategic Advisor:** trade-offs, governance, owners, and staged plan.
5. **Executive President:** proceed, change-course, pause, or stop decision;
   accountable owner; review gate; and first reversible action.

Use the Professor standard throughout: explain plainly, distinguish facts from
assumptions and recommendations, and make evaluation criteria inspectable.

## Agent-harness rules

- Define an explicit task contract, context policy, tool allowlist, permission
  profile, budget, approval gates, output schema, and evaluation suite.
- A provider adapter may execute the contract or report a missing capability. It
  must not widen permissions, tools, data access, or approval authority.
- Compare providers on the same bounded workflow and holdout evaluation set,
  not general benchmarks or vendor claims.
- Start with low-risk, reversible workflows in isolated workspaces. Promote
  autonomy only after measured quality, cost, latency, and safety thresholds.
- Do not take external or consequential action without explicit approval.

## Required decision brief

Return: (1) the recommendation, (2) credible alternatives and trade-offs,
(3) evidence, assumptions, and open questions, (4) risks, mitigations, and
no-go conditions, (5) a bounded pilot with owner and metrics, and (6) the next
reversible action.
