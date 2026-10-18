# Claude Code reference template

This directory shows how to carry the Board workflow into a Claude Code
project. It is a documentation template: Harness² does not currently expose a
Claude Code substrate or validate its configuration surface.

Use `CLAUDE.md` as the project-level discovery instruction and keep the detailed
workflow in `skills/board/SKILL.md`. If your Claude Code deployment uses a
different skills discovery path, preserve the same separation: one short,
explicit trigger and one on-demand skill body.

The policy is intentionally provider-neutral. The same skill can be adapted for
another model provider or a local runtime without transferring policy authority
to that provider.
