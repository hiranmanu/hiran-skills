"""Tests for scripts/background_inbox.py: the parallel-run-safe way to add facts
to the master fact file. Includes a real multi-process stress test.

Run from the repo root:  python3 -m unittest discover -s tests -v
"""

import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugins/cv-tailoring/skills/cv-tailoring/scripts/background_inbox.py"

MASTER = """# Master

## Section 1: Master Bullet Bank

### Alpha Co - Role A, 2020 - 2021
Some descriptor line
- Existing alpha fact (P)

### Beta Co (acquired by X) - Role B, 2019 - 2020
- Existing beta fact (P)

### Beta Co Two - Role C, 2018 - 2019
- Existing beta-two fact (P)

---

## Section 2: Cross-Role Facts & Guardrails

- **Existing:** a cross-role fact (C 2026-01-01)

---

## Section 3: Notable Absences

- No CFO experience
"""


def run(master, inbox, *args):
    return subprocess.run([sys.executable, str(SCRIPT), "--master", str(master), "--inbox", str(inbox), *args],
                          capture_output=True, text=True)


class InboxBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.master = self.dir / "master.md"
        self.master.write_text(MASTER, encoding="utf-8")
        self.inbox = self.dir / "inbox"

    def tearDown(self):
        self.tmp.cleanup()

    def text(self):
        return self.master.read_text(encoding="utf-8")


class Basics(InboxBase):
    def test_add_pending_merge_places_fact_under_the_right_role(self):
        self.assertEqual(run(self.master, self.inbox, "add", "--role", "Alpha Co", "--text", "New alpha fact", "--tag", "C 2026-09-30").returncode, 0)
        pend = run(self.master, self.inbox, "pending").stdout
        self.assertIn("New alpha fact", pend)
        r = run(self.master, self.inbox, "merge")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        t = self.text()
        self.assertIn("- New alpha fact (C 2026-09-30)", t)
        alpha, beta = t.index("### Alpha Co"), t.index("### Beta Co (acquired")
        self.assertTrue(alpha < t.index("New alpha fact") < beta, "fact must sit inside Alpha's block")
        self.assertIn("(no pending facts)", run(self.master, self.inbox, "pending").stdout)

    def test_role_matching_is_prefix_but_not_substring(self):
        run(self.master, self.inbox, "add", "--role", "Beta Co", "--text", "beta new")
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 2)  # "Beta Co" is ambiguous: two headings start with it
        self.assertIn("beta new", run(self.master, self.inbox, "pending").stdout)  # stays queued, not lost

    def test_unique_full_prefix_matches_despite_parenthetical(self):
        run(self.master, self.inbox, "add", "--role", "Beta Co (acquired by X)", "--text", "beta ok")
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 0)
        t = self.text()
        self.assertTrue(t.index("### Beta Co (acquired") < t.index("beta ok") < t.index("### Beta Co Two"))

    def test_unknown_role_stays_in_inbox_and_exits_2(self):
        run(self.master, self.inbox, "add", "--role", "Nowhere Ltd", "--text", "lost fact")
        r = run(self.master, self.inbox, "merge")
        self.assertEqual(r.returncode, 2)
        self.assertIn("lost fact", run(self.master, self.inbox, "pending").stdout)
        self.assertNotIn("lost fact", self.text())

    def test_duplicates_are_skipped_and_merge_is_idempotent(self):
        for _ in range(2):
            run(self.master, self.inbox, "add", "--role", "Alpha Co", "--text", "Same fact twice")
        run(self.master, self.inbox, "add", "--role", "Alpha Co", "--text", "existing alpha fact")  # already there (case/tag-insensitive)
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 0)
        self.assertEqual(self.text().lower().count("same fact twice"), 1)
        self.assertEqual(self.text().lower().count("existing alpha fact"), 1)
        before = self.text()
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 0)  # nothing pending
        self.assertEqual(self.text(), before)

    def test_cross_role_fact_goes_to_section_2(self):
        run(self.master, self.inbox, "add-cross", "--title", "New capability", "--text", "spans roles")
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 0)
        t = self.text()
        self.assertTrue(t.index("## Section 2") < t.index("**New capability:**") < t.index("## Section 3"))

    def test_corrupt_inbox_file_never_breaks_readers(self):
        self.inbox.mkdir()
        (self.inbox / "20260101-000000_1_deadbeef.json").write_text("{ half written", encoding="utf-8")
        self.assertEqual(run(self.master, self.inbox, "pending").returncode, 0)
        self.assertEqual(run(self.master, self.inbox, "merge").returncode, 0)

    def test_list_roles(self):
        out = run(self.master, self.inbox, "list-roles").stdout
        self.assertIn("Alpha Co - Role A", out)
        self.assertIn("Beta Co Two - Role C", out)


class ParallelRuns(InboxBase):
    def test_many_processes_adding_and_merging_at_once_lose_nothing(self):
        """12 worker processes, each adding 6 facts across all roles and calling merge
        at random points, then 4 simultaneous final merges. Every fact must appear
        exactly once, the file structure must survive, and no temp/partial files remain."""
        roles = ["Alpha Co", "Beta Co (acquired by X)", "Beta Co Two"]
        workers, per = 12, 6
        procs = []
        expected = []
        for w in range(workers):
            cmds = []
            for i in range(per):
                text = f"stress fact w{w:02d}-{i}"
                expected.append(text)
                cmds.append(["add", "--role", roles[(w + i) % 3], "--text", text])
                if random.random() < 0.35:
                    cmds.append(["merge"])
            procs.append(cmds)

        def worker(cmds):
            script = "import subprocess,sys\n" + "\n".join(
                f"subprocess.run({[sys.executable, str(SCRIPT), '--master', str(self.master), '--inbox', str(self.inbox), *c]!r}, capture_output=True)"
                for c in cmds)
            return subprocess.Popen([sys.executable, "-c", script])

        running = [worker(c) for c in procs]
        for p in running:
            self.assertEqual(p.wait(timeout=180), 0)
        finals = [subprocess.Popen([sys.executable, str(SCRIPT), "--master", str(self.master), "--inbox", str(self.inbox), "merge"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE) for _ in range(4)]
        for f in finals:
            f.communicate(timeout=120)
            self.assertIn(f.returncode, (0,))

        t = self.text()
        missing = [x for x in expected if t.count(x) != 1]
        self.assertEqual(missing, [], f"facts lost or duplicated: {missing[:5]}")
        # structure intact and in order
        order = [t.index(h) for h in ("## Section 1", "### Alpha Co", "### Beta Co (acquired", "### Beta Co Two", "## Section 2", "## Section 3")]
        self.assertEqual(order, sorted(order))
        for line in ("- Existing alpha fact (P)", "- Existing beta fact (P)", "- No CFO experience"):
            self.assertEqual(t.count(line), 1)
        # every fact sits inside its own role's block
        for w in range(workers):
            for i in range(per):
                role = roles[(w + i) % 3]
                head = {"Alpha Co": "### Alpha Co", "Beta Co (acquired by X)": "### Beta Co (acquired", "Beta Co Two": "### Beta Co Two"}[role]
                start = t.index(head)
                markers = ("\n### ", "\n---", "\n## ")
                end = min(t.index(h, start + 1) for h in markers if t.find(h, start + 1) != -1)
                self.assertIn(f"stress fact w{w:02d}-{i}", t[start:end])
        self.assertEqual(list(self.dir.glob("*.tmp")) + list(self.inbox.glob("*.tmp")), [])
        self.assertEqual(list(self.inbox.glob("*.json")), [], "nothing should be left pending")
        self.assertEqual(len(list((self.inbox / "merged").glob("*.json"))), workers * per)


if __name__ == "__main__":
    unittest.main()
