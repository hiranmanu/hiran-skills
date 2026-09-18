#!/usr/bin/env python3
"""
check_release_consistency.py — verifies every file that declares the
cv-tailoring plugin's version agrees, and that CHANGELOG.md has a matching
entry.

Root cause this guards against: a version bump landing in plugin.json /
marketplace.json without also updating README.md, SKILLS.md, or
CHANGELOG.md (happened in practice — see CHANGELOG.md v1.9.0 and v1.11.1
entries). Run this after any version bump, before considering it done.

Usage:
    python3 scripts/check_release_consistency.py

Exit code: 0 if every source agrees, 1 otherwise.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main():
    failures = []
    versions = {}

    plugin_json = json.loads(read(ROOT / "plugins/cv-tailoring/.claude-plugin/plugin.json"))
    versions["plugin.json"] = plugin_json["version"]

    marketplace_json = json.loads(read(ROOT / ".claude-plugin/marketplace.json"))
    versions["marketplace.json (top-level)"] = marketplace_json["version"]
    cv_entry = next(p for p in marketplace_json["plugins"] if p["name"] == "cv-tailoring")
    versions["marketplace.json (cv-tailoring entry)"] = cv_entry["version"]

    readme = read(ROOT / "README.md")
    m = re.search(r"### cv-tailoring \(v([\d.]+)\)", readme)
    if not m:
        failures.append("README.md: could not find '### cv-tailoring (vX.Y.Z)' header")
    else:
        versions["README.md"] = m.group(1)

    skills_md = read(ROOT / "SKILLS.md")
    m = re.search(r"## cv-tailoring \(v([\d.]+)\)", skills_md)
    if not m:
        failures.append("SKILLS.md: could not find '## cv-tailoring (vX.Y.Z)' header")
    else:
        versions["SKILLS.md"] = m.group(1)

    changelog = read(ROOT / "CHANGELOG.md")
    m = re.search(r"## \[([\d.]+)\]", changelog)
    if not m:
        failures.append("CHANGELOG.md: could not find a top '## [X.Y.Z]' entry")
    else:
        versions["CHANGELOG.md (top entry)"] = m.group(1)

    distinct = set(versions.values())
    if len(distinct) > 1:
        failures.append("Version mismatch across files:\n  " + "\n  ".join(f"{k}: {v}" for k, v in versions.items()))

    print("check_release_consistency.py\n" + "=" * 60)
    for k, v in versions.items():
        print(f"{k}: {v}")
    print("=" * 60)

    if failures:
        print("FAIL\n")
        for f in failures:
            print(f)
        sys.exit(1)

    print(f"PASS - all sources agree on v{distinct.pop()}")
    sys.exit(0)


if __name__ == "__main__":
    main()
