#!/usr/bin/env python3
"""
background_inbox.py - parallel-run-safe updates to the master fact file
(references/02-background.md).

Problem: several CV runs can be going at once (batch, or several sessions).
If each edited 02-background.md directly they would overwrite each other's
newly confirmed facts. So during a run the master file is READ-ONLY, and:

  * a run that learns a new fact writes it to its OWN inbox file (unique name,
    written atomically, so two runs can never touch the same file);
  * every run reads the master AND the pending inbox at intake, so a fact one
    run just confirmed is usable by the others straight away;
  * `merge` folds pending inbox files into the master under a lock (only one
    merger at a time, atomic replace, dedupes, idempotent), then archives them.
    It is safe to call from several runs at the same time.

Usage:
    python3 background_inbox.py list-roles
    python3 background_inbox.py add --role "dunnhumby/Tesco" --text "Ran demand intake ..." [--tag "C 2026-09-29"] [--source "Softcat run"]
    python3 background_inbox.py add-cross --title "CEO-level stakeholders" --text "..." [--tag ...]
    python3 background_inbox.py pending
    python3 background_inbox.py merge

Paths can be overridden for tests with --master and --inbox.

Exit codes: 0 ok; 2 some entries could not be merged (they stay in the inbox);
3 could not get the merge lock in time.
"""

import argparse
import datetime
import json
import os
import re
import sys
import time
import uuid
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
DEFAULT_MASTER = SKILL / "references" / "02-background.md"
DEFAULT_INBOX = SKILL / "inbox"
LOCK_NAME = ".merge.lock"
LOCK_STALE_SECONDS = 120
LOCK_TIMEOUT_SECONDS = 60

SECTION1_RE = re.compile(r"^## Section 1\b")
SECTION2_RE = re.compile(r"^## Section 2\b")
H2_RE = re.compile(r"^## ")
H3_RE = re.compile(r"^### ")
TAG_RE = re.compile(r"\s*\((?:P|DA|P/DA|C[^)]*)\)\s*$")


# ---------------------------------------------------------------- file helpers
def atomic_write(path: Path, text: str):
    tmp = path.with_name(f"{path.name}.{os.getpid()}.{uuid.uuid4().hex[:6]}.tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    for attempt in range(60):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:  # Windows: a reader has the file open for a moment
            time.sleep(0.05)
    os.replace(tmp, path)


def norm(text: str) -> str:
    t = TAG_RE.sub("", text)
    return re.sub(r"\s+", " ", t.lower()).strip(" .-")


def acquire_lock(inbox: Path):
    inbox.mkdir(parents=True, exist_ok=True)
    lock = inbox / LOCK_NAME
    deadline = time.time() + LOCK_TIMEOUT_SECONDS
    while True:
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()} {time.time()}".encode())
            os.close(fd)
            return lock
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > LOCK_STALE_SECONDS:
                    lock.unlink()  # stale lock from a crashed run
                    continue
            except FileNotFoundError:
                continue
            if time.time() > deadline:
                return None
            time.sleep(0.1)


def release_lock(lock: Path):
    try:
        lock.unlink()
    except FileNotFoundError:
        pass


# ---------------------------------------------------------------- inbox entries
def load_pending(inbox: Path):
    entries = []
    if not inbox.exists():
        return entries
    for f in sorted(inbox.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue  # half-written by a crashed run: ignore, never crash the reader
        data["_file"] = f
        entries.append(data)
    return entries


def cmd_add(args, entry_type):
    inbox = Path(args.inbox)
    inbox.mkdir(parents=True, exist_ok=True)
    tag = args.tag or f"C {datetime.date.today().isoformat()}"
    entry = {"type": entry_type, "text": args.text.strip(), "tag": tag,
             "source": args.source or "", "created": datetime.datetime.now().isoformat(timespec="seconds")}
    if entry_type == "fact":
        entry["role"] = args.role.strip()
    else:
        entry["title"] = args.title.strip()
    name = f"{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}_{os.getpid()}_{uuid.uuid4().hex[:8]}.json"
    target = inbox / name
    atomic_write(target, json.dumps(entry, indent=2, ensure_ascii=False) + "\n")
    print(f"queued: {target.name}")
    return 0


def cmd_pending(args):
    entries = load_pending(Path(args.inbox))
    if not entries:
        print("(no pending facts)")
        return 0
    for e in entries:
        where = e.get("role") or f"cross-role: {e.get('title')}"
        print(f"- [{where}] {e['text']} ({e.get('tag','')}) <{e['_file'].name}>")
    return 0


# ---------------------------------------------------------------- master parsing
def split_lines(text: str):
    return text.split("\n")


def section_bounds(lines, start_re):
    start = next((i for i, l in enumerate(lines) if start_re.match(l)), None)
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if H2_RE.match(lines[j]):
            end = j
            break
    return start, end


def role_headings(lines):
    b = section_bounds(lines, SECTION1_RE)
    if not b:
        return []
    out = []
    for i in range(b[0] + 1, b[1]):
        if H3_RE.match(lines[i]):
            out.append((i, lines[i][4:].strip()))
    return out


def find_role(lines, key: str):
    key_l = key.strip().lower()
    hits = []
    for i, heading in role_headings(lines):
        h = heading.lower()
        if h.startswith(key_l) and (len(h) == len(key_l) or h[len(key_l)] in " ,("):
            hits.append(i)
    return hits


def format_line(text: str, tag: str) -> str:
    text = text.strip()
    if tag and not TAG_RE.search(text):
        return f"- {text} ({tag})"
    return f"- {text}"


def apply_fact(lines, entry):
    hits = find_role(lines, entry["role"])
    if not hits:
        return None, f'no role heading matches "{entry["role"]}" (run list-roles)'
    if len(hits) > 1:
        return None, f'role "{entry["role"]}" matches {len(hits)} headings'
    h = hits[0]
    end = len(lines)
    for j in range(h + 1, len(lines)):
        if H3_RE.match(lines[j]) or H2_RE.match(lines[j]) or lines[j].strip() == "---":
            end = j
            break
    key = norm(entry["text"])
    for l in lines[h + 1:end]:
        if l.lstrip().startswith("-") and norm(l.lstrip()[1:]) == key:
            return False, "duplicate"
    last_bullet = h
    for j in range(h + 1, end):
        if lines[j].lstrip().startswith("-") or (lines[j].startswith("  ") and lines[j].strip()):
            last_bullet = j
    lines.insert(last_bullet + 1, format_line(entry["text"], entry.get("tag", "")))
    return True, "added"


def apply_cross(lines, entry):
    b = section_bounds(lines, SECTION2_RE)
    if not b:
        return None, "no '## Section 2' heading in the master file"
    start, end = b
    text = f"**{entry['title']}:** {entry['text']}"
    key = norm(text)
    for l in lines[start:end]:
        if l.lstrip().startswith("-") and norm(l.lstrip()[1:]) == key:
            return False, "duplicate"
    j = end
    while j - 1 > start and lines[j - 1].strip() in ("", "---"):
        j -= 1
    lines.insert(j, format_line(text, entry.get("tag", "")))
    return True, "added"


def cmd_merge(args):
    master = Path(args.master)
    inbox = Path(args.inbox)
    lock = acquire_lock(inbox)
    if lock is None:
        print("could not get the merge lock in time; another merge is running. Try again.")
        return 3
    try:
        entries = load_pending(inbox)
        if not entries:
            print("nothing to merge")
            return 0
        text = master.read_text(encoding="utf-8")
        lines = split_lines(text)
        merged_dir = inbox / "merged"
        merged_dir.mkdir(parents=True, exist_ok=True)
        added = dup = 0
        errors = []
        done = []
        for e in entries:
            ok, msg = (apply_fact if e["type"] == "fact" else apply_cross)(lines, e)
            if ok is None:
                errors.append(f"{e['_file'].name}: {msg}")
                continue
            if ok:
                added += 1
            else:
                dup += 1
            done.append(e["_file"])
        if added:
            atomic_write(master, "\n".join(lines))
        for f in done:
            os.replace(f, merged_dir / f.name)
        print(f"merged {added} new fact(s), skipped {dup} duplicate(s), {len(errors)} left in the inbox")
        for err in errors:
            print("  ERROR " + err)
        return 2 if errors else 0
    finally:
        release_lock(lock)


def cmd_list_roles(args):
    lines = split_lines(Path(args.master).read_text(encoding="utf-8"))
    for _, heading in role_headings(lines):
        print(heading)
    return 0


def main():
    ap = argparse.ArgumentParser(description="Parallel-run-safe updates to the master fact file.")
    ap.add_argument("--master", default=str(DEFAULT_MASTER))
    ap.add_argument("--inbox", default=str(DEFAULT_INBOX))
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="queue a fact under a role")
    a.add_argument("--role", required=True)
    a.add_argument("--text", required=True)
    a.add_argument("--tag")
    a.add_argument("--source")
    c = sub.add_parser("add-cross", help="queue a cross-role fact")
    c.add_argument("--title", required=True)
    c.add_argument("--text", required=True)
    c.add_argument("--tag")
    c.add_argument("--source")
    sub.add_parser("pending", help="show unmerged facts from any run")
    sub.add_parser("merge", help="fold pending facts into the master file (locked, idempotent)")
    sub.add_parser("list-roles", help="show valid --role values")
    args = ap.parse_args()
    fn = {"add": lambda: cmd_add(args, "fact"), "add-cross": lambda: cmd_add(args, "cross"),
          "pending": lambda: cmd_pending(args), "merge": lambda: cmd_merge(args),
          "list-roles": lambda: cmd_list_roles(args)}[args.cmd]
    sys.exit(fn())


if __name__ == "__main__":
    main()
