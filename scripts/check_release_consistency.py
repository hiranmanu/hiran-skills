#!/usr/bin/env python3
"""
check_release_consistency.py — verifies every plugin in this marketplace
has a consistent version across every file that declares it.

Root cause this guards against: a version bump landing in one plugin's
plugin.json without also updating marketplace.json's matching entry, that
plugin's own README.md/CHANGELOG.md, or its row in the root SKILLS.md
catalog. Happened in practice before per-plugin versioning existed (see
plugins/cv-tailoring/CHANGELOG.md's v1.9.0 and v1.11.1 entries) — this
script is plugin-aware so it keeps catching it as more skills are added.

For each plugin under plugins/*/, checks that its version agrees across:
  - plugins/<name>/.claude-plugin/plugin.json
  - .claude-plugin/marketplace.json's matching plugin entry
  - plugins/<name>/CHANGELOG.md's top "## [X.Y.Z]" entry
  - plugins/<name>/README.md's "# <name> (vX.Y.Z)" header
  - SKILLS.md's catalog row for that plugin

Usage:
    python3 scripts/check_release_consistency.py

Exit code: 0 if every plugin's sources agree, 1 otherwise.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def discover_plugins():
    plugin_files = sorted((ROOT / "plugins").glob("*/.claude-plugin/plugin.json"))
    return [(p.parent.parent.name, p) for p in plugin_files]


def check_plugin(name: str, plugin_json_path: Path, marketplace_json: dict):
    versions = {}
    failures = []

    plugin_data = json.loads(read(plugin_json_path))
    versions["plugin.json"] = plugin_data.get("version")
    if plugin_data.get("name") != name:
        failures.append(f"plugin.json's \"name\" ({plugin_data.get('name')!r}) doesn't match its folder ({name!r})")

    entry = next((p for p in marketplace_json.get("plugins", []) if p.get("name") == name), None)
    if entry is None:
        failures.append(f"marketplace.json has no entry for plugin {name!r}")
    else:
        versions["marketplace.json entry"] = entry.get("version")

    plugin_dir = plugin_json_path.parent.parent

    changelog_path = plugin_dir / "CHANGELOG.md"
    if not changelog_path.exists():
        failures.append(f"missing {changelog_path.relative_to(ROOT)}")
    else:
        m = re.search(r"## \[([\d.]+)\]", read(changelog_path))
        if not m:
            failures.append(f"{changelog_path.relative_to(ROOT)}: could not find a top '## [X.Y.Z]' entry")
        else:
            versions["CHANGELOG.md (top entry)"] = m.group(1)

    readme_path = plugin_dir / "README.md"
    if not readme_path.exists():
        failures.append(f"missing {readme_path.relative_to(ROOT)}")
    else:
        m = re.search(rf"^# {re.escape(name)} \(v([\d.]+)\)", read(readme_path), re.MULTILINE)
        if not m:
            failures.append(f"{readme_path.relative_to(ROOT)}: could not find '# {name} (vX.Y.Z)' header")
        else:
            versions["README.md"] = m.group(1)

    skills_md = read(ROOT / "SKILLS.md")
    m = re.search(rf"\|\s*`{re.escape(name)}`\s*\|\s*([\d.]+)\s*\|", skills_md)
    if not m:
        failures.append(f"SKILLS.md: could not find a catalog row for `{name}`")
    else:
        versions["SKILLS.md"] = m.group(1)

    distinct = set(v for v in versions.values() if v is not None)
    if len(distinct) > 1:
        failures.append("version mismatch:\n    " + "\n    ".join(f"{k}: {v}" for k, v in versions.items()))

    return versions, failures


def main():
    marketplace_json_path = ROOT / ".claude-plugin/marketplace.json"
    marketplace_json = json.loads(read(marketplace_json_path))

    plugins = discover_plugins()
    if not plugins:
        print("FAIL: no plugins found under plugins/*/.claude-plugin/plugin.json")
        sys.exit(1)

    print("check_release_consistency.py\n" + "=" * 60)
    overall_ok = True

    for name, plugin_json_path in plugins:
        versions, failures = check_plugin(name, plugin_json_path, marketplace_json)
        ok = not failures
        overall_ok = overall_ok and ok
        status = "PASS" if ok else "FAIL"
        print(f"\n[{status}] {name}")
        for k, v in versions.items():
            print(f"  {k}: {v}")
        for f in failures:
            print(f"  FAIL  {f}")

    print("\n" + "=" * 60)
    print("OVERALL: " + ("PASS" if overall_ok else "FAIL"))
    sys.exit(0 if overall_ok else 1)


if __name__ == "__main__":
    main()
