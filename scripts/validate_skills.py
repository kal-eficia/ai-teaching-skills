#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md in this repo.

Checks: frontmatter present, `name` matches the folder and is lowercase-hyphen
(max 64 chars), `description` present and at most 1,024 characters, no em
dashes anywhere, and (with --require-context) that the skill reads
teaching-context.md. Exits 1 if anything fails.
"""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def check(skill_dir, require_context):
    errors = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return ["missing SKILL.md"]
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return ["no YAML frontmatter"]
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if name != skill_dir.name:
        errors.append(f"name '{name}' does not match folder '{skill_dir.name}'")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append("name must be lowercase letters, digits and hyphens, max 64")
    if not desc:
        errors.append("missing description")
    elif len(desc) > 1024:
        errors.append(f"description is {len(desc)} characters (max 1024)")
    for f in skill_dir.rglob("*"):
        if f.is_file() and f.suffix in {".md", ".py", ".txt", ".json"}:
            if "—" in f.read_text(encoding="utf-8", errors="ignore"):
                errors.append(f"em dash in {f.relative_to(skill_dir)}")
    if require_context and name != "teaching-context" and "teaching-context.md" not in text:
        errors.append("does not read teaching-context.md")
    return errors


def main():
    require_context = "--require-context" in sys.argv
    root = Path(__file__).resolve().parent.parent / "skills"
    dirs = sorted(d for d in root.iterdir() if d.is_dir())
    failed = 0
    for d in dirs:
        errs = check(d, require_context)
        if errs:
            failed += 1
            for e in errs:
                print(f"FAIL {d.name}: {e}")
    print(f"{len(dirs) - failed}/{len(dirs)} skills valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
