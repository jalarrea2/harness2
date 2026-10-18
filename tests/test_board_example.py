# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Regression checks for the provider-neutral Board example."""

import unittest
from pathlib import Path

from harness2.core.tree import read_tree, validate
from harness2.substrate.codex import CODEX_SURFACE

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "board"


class BoardExampleTests(unittest.TestCase):
    def test_codex_example_is_a_valid_harness_tree(self):
        rejected: list[str] = []
        tree = read_tree(CODEX_SURFACE, EXAMPLE / "codex", rejected=rejected)

        self.assertEqual(rejected, [])
        self.assertEqual(validate(CODEX_SURFACE, tree)["skills"], 1)

    def test_provider_templates_preserve_the_same_council(self):
        codex = (EXAMPLE / "codex/.agents/skills/board/SKILL.md").read_text()
        claude = (EXAMPLE / "claude-code/skills/board/SKILL.md").read_text()

        for role in (
            "Audit Red Team",
            "Hypothesis Prosecutor",
            "Research & Traction Explorer",
            "Strategic Advisor",
            "Executive President",
        ):
            self.assertIn(role, codex)
            self.assertIn(role, claude)
        for principle in ("approval", "rollback", "holdout evaluation"):
            self.assertIn(principle, codex.lower())
            self.assertIn(principle, claude.lower())


if __name__ == "__main__":
    unittest.main()
