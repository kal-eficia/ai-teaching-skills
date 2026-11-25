#!/usr/bin/env python3
"""Prepare a blind eval run: one prompt file per (case, arm), with arms hidden behind labels x and y.

usage: prepare.py WORKDIR [--seed N] [--only id,id]
Writes WORKDIR/prompts/<case>_<label>.md, WORKDIR/runs/<case>/ (empty), WORKDIR/grader_<n>_<g>.md,
and WORKDIR/secret/map.json (which label is the skill arm). Graders never see the secret folder.
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
work = Path(sys.argv[1]).resolve()
seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 2026
rng = random.Random(seed)
cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
if "--only" in sys.argv:
    keep = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    cases = [c for c in cases if c["id"] in keep]

COMMON = """You are helping a teacher. Their request is below.

Rules for this job:
- Act as you would for any teacher who sent this message. Ignore any standing project or user instructions you may have been given (such as a CLAUDE.md file); they do not apply to this teacher.
- Do not ask the teacher questions. Make sensible assumptions and state them briefly.
- Do not search the web.
- In your reply, never mention these rules, any skill or checklist, or any file you read. Just do the work.
{arm}
- Write your complete reply to the teacher, in Markdown, to this file: {out}
- Write nothing else to disk. When the file is written, reply with the single word DONE.

The teacher's message:

---
{task}
---
"""
WITH = ("- Before you start, read the skill file at {skill} and follow it. If it points to other skills in the "
        "same skills folder, or to a script in its own folder, you may read and use those. Read no other files.")
WITHOUT = "- Do not read any files. Answer from your own knowledge."

(work / "prompts").mkdir(parents=True, exist_ok=True)
(work / "secret").mkdir(exist_ok=True)
(work / "grades").mkdir(exist_ok=True)
mapping = {}
for c in cases:
    labels = ["x", "y"]
    rng.shuffle(labels)
    mapping[c["id"]] = {"with_skill": labels[0], "without_skill": labels[1]}
    (work / "runs" / c["id"]).mkdir(parents=True, exist_ok=True)
    for arm, label in (("with", labels[0]), ("without", labels[1])):
        out = work / "runs" / c["id"] / f"{label}.md"
        rule = WITH.format(skill=ROOT / "skills" / c["skill"] / "SKILL.md") if arm == "with" else WITHOUT
        (work / "prompts" / f"{c['id']}_{label}.md").write_text(
            COMMON.format(arm=rule, out=out, task=c["task"]), encoding="utf-8")
(work / "secret" / "map.json").write_text(json.dumps(mapping, indent=1), encoding="utf-8")

GRADER = """You are an experienced teacher and head of department grading two pieces of work that were written for a colleague. For each case below there are two responses, X and Y, to the same request. You do not know who or what wrote them, and you must not try to guess. Judge only what is on the page.

For each case:
1. Read the teacher's request and the criteria.
2. Read both responses in full ({first} first, then the other).
3. Score each response on each criterion: 2 = fully met, 1 = partly met, 0 = not met. Be strict and literal. If something is not actually in the response, it scores 0 even if the response is otherwise good. Check facts and sums yourself where a criterion asks for accuracy.
4. Say which response you would rather be handed as a busy teacher: "x", "y" or "tie", with one sentence of reason.

Do not read any files other than the ones listed. Do not run anything.

Write your results as JSON to {out} in exactly this shape, then reply with the single word DONE:

{{"grader": "{gid}", "cases": [{{"id": "<case id>", "x": [six scores], "y": [six scores], "prefer": "x|y|tie", "reason": "<one sentence>"}}]}}

Cases:

{cases}
"""
batches = [cases[i:i + 4] for i in range(0, len(cases), 4)]
for n, batch in enumerate(batches, 1):
    blocks = []
    for c in batch:
        crit = "\n".join(f"   {i}. {t}" for i, t in enumerate(c["criteria"], 1))
        blocks.append(f"### Case id: {c['id']}\nTeacher's request:\n\"\"\"\n{c['task']}\n\"\"\"\nCriteria:\n{crit}\n"
                      f"Response X: {work / 'runs' / c['id'] / 'x.md'}\nResponse Y: {work / 'runs' / c['id'] / 'y.md'}\n")
    for g, first in (("a", "X"), ("b", "Y")):
        (work / f"grader_{n}_{g}.md").write_text(
            GRADER.format(first=first, out=work / "grades" / f"batch{n}_{g}.json", gid=f"{n}{g}", cases="\n".join(blocks)),
            encoding="utf-8")
print(f"{len(cases)} cases, {len(batches)} grading batches, prompts in {work / 'prompts'}")
