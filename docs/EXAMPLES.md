# Examples

These examples show small, reusable harness components. They are reference
material, not benchmark baselines and not a recommendation to run an executor
with unrestricted network access or a disabled sandbox.

## Board: a provider-neutral decision skill

[`examples/board/`](../examples/board/) is a practical multi-perspective
decision skill for evaluating agent-harness initiatives and other consequential
technical decisions. It has a runnable **Codex** harness tree and a **Claude
Code** reference template. The two templates carry the same decision protocol;
they differ only in their instruction-discovery conventions.

The skill is provider-neutral at the policy layer: Claude, Gemini, OpenAI, and
local or open-weight models may be used as execution backends. This repository
currently materializes and validates only the Codex and OpenCode substrates, so
the Claude Code template is deliberately documentation-only rather than an
unsupported runtime integration.

Before adapting the example for a real environment:

1. Give the agent an explicit tool allowlist, budget, and approval gate.
2. Keep sensitive data and production credentials outside model context unless
   there is a reviewed, least-privilege route for them.
3. Evaluate the workflow on a holdout task set before promotion.
4. Preserve a human owner, a rollback path, and an auditable record of each
   approved change.

For Codex harness trees, every skill needs a `description:` frontmatter field
and an explicit trigger in `AGENTS.md`; the tree validator rejects an
untriggered skill. The Board example is covered by a regression test so
those requirements cannot silently drift.
