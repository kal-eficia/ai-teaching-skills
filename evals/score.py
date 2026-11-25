#!/usr/bin/env python3
"""Unblind and score an eval run.

usage: score.py WORKDIR [--publish]
Reads WORKDIR/runs, WORKDIR/grades and WORKDIR/secret/map.json. Prints a summary and, with --publish,
copies the outputs and writes evals/results.json into the repo.
"""
import json
import re
import shutil
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "server"))
sys.path.insert(0, str(ROOT / "server" / "vendor"))
from classroom import tools  # noqa: E402

work = Path(sys.argv[1]).resolve()
cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
mapping = json.loads((work / "secret" / "map.json").read_text(encoding="utf-8"))


def between(text):
    parts = re.split(r"^\s*={3,}\s*$", text, flags=re.M)
    return parts[1].strip() if len(parts) >= 3 else None


def auto_check(kind, text):
    """Objective checks done by code. Returns {name, pass, detail} or None if not applicable."""
    if kind == "key":
        m = re.findall(r"ANSWER KEY:\s*([A-Da-d][A-Da-d\s,;/-]*)", text)
        if not m:
            return {"name": "No guessable answer pattern", "pass": None, "detail": "no ANSWER KEY line found"}
        key = "".join(re.findall(r"[A-Da-d]", m[-1])).upper()
        if len(key) < 4:
            return {"name": "No guessable answer pattern", "pass": None, "detail": f"key too short: {key}"}
        rep = tools.check_answer_key(key=key, options=4)
        fails = [f"{f['rule']} at {f['where']}" for r in rep["reports"] for f in r["findings"] if f["severity"] == "fail"]
        return {"name": "No guessable answer pattern", "pass": rep["ok"],
                "detail": f"key {key}: " + ("clean" if rep["ok"] else "; ".join(fails))}
    if kind == "reports":
        rows = re.findall(r"^\W*\[(S\d)\]\W*:\s*(.+)$", text, flags=re.M)
        latest = {}
        for code, body in rows:
            latest[code] = re.sub(r"[*_`]", "", body).strip()
        if len(latest) < 6:
            return {"name": "Reports pass length, repetition and jargon checks", "pass": None,
                    "detail": f"only {len(latest)} reports found in the requested format"}
        rep = tools.check_reports(reports=[{"student": f"[{k}]", "text": v} for k, v in sorted(latest.items())])
        bad = [f"{r['student']}: {'; '.join(r['issues'])}" for r in rep["reports"] if not r["ok"]]
        return {"name": "Reports pass length, repetition and jargon checks", "pass": rep["ok"],
                "detail": rep["summary"] + (" " + " | ".join(bad) if bad else "")}
    if kind == "message":
        msg = between(text)
        if not msg:
            return {"name": "Message is under 100 words", "pass": None, "detail": "no === markers found"}
        n = len(msg.split())
        return {"name": "Message is under 100 words", "pass": n <= 100, "detail": f"{n} words"}
    if kind == "reading":
        body = between(text)
        if not body:
            return {"name": "Reading age 10.5 or below", "pass": None, "detail": "no === markers found"}
        s = tools.text_stats(text=re.sub(r"[*_#`>]", "", body))
        return {"name": "Reading age 10.5 or below", "pass": s["reading_age_estimate"] <= 10.5,
                "detail": f"estimated reading age {s['reading_age_estimate']}, {s['words_per_sentence']} words per sentence"}
    return None


def plain(reason, arms):
    """Rewrite a grader's X/Y wording now that the labels are unblinded."""
    names = {arms["with"].upper(): "the skill answer", arms["without"].upper(): "the plain answer"}
    out = re.sub(r"\b([XY])(?='s\b|\b)", lambda m: names[m.group(1)], reason)
    return out[0].upper() + out[1:] if out else out


grades = {}
for f in sorted((work / "grades").glob("batch*.json")):
    data = json.loads(f.read_text(encoding="utf-8"))
    for c in data["cases"]:
        grades.setdefault(c["id"], []).append({**c, "grader": data.get("grader", f.stem)})

results, missing = [], []
for c in cases:
    m = mapping[c["id"]]
    arms = {"with": m["with_skill"], "without": m["without_skill"]}
    texts = {}
    for arm, label in arms.items():
        p = work / "runs" / c["id"] / f"{label}.md"
        texts[arm] = p.read_text(encoding="utf-8") if p.exists() else None
    if not all(texts.values()) or c["id"] not in grades:
        missing.append(c["id"])
        continue
    gs = grades[c["id"]]
    per_arm = {}
    for arm, label in arms.items():
        crit = [statistics.mean(g[label][i] for g in gs) for i in range(len(c["criteria"]))]
        per_arm[arm] = {"criteria": [round(x, 2) for x in crit], "total": round(sum(crit), 2),
                        "max": 2 * len(c["criteria"]), "words": len(texts[arm].split())}
        if c.get("auto"):
            per_arm[arm]["auto"] = auto_check(c["auto"], texts[arm])
    prefs = []
    for g in gs:
        p = str(g.get("prefer", "tie")).lower()
        prefs.append("with" if p == arms["with"] else "without" if p == arms["without"] else "tie")
    agree = statistics.mean(
        1 if abs(sum(gs[0][l]) - sum(gs[-1][l])) <= 2 else 0 for l in ("x", "y")) if len(gs) > 1 else None
    results.append({
        "id": c["id"], "skill": c["skill"], "subject": c["subject"], "task": c["task"], "criteria": c["criteria"],
        "with": per_arm["with"], "without": per_arm["without"], "preferences": prefs,
        "reasons": [plain(g.get("reason", ""), arms) for g in gs], "graders": len(gs), "graders_close": agree,
    })

n = len(results)
if not n:
    sys.exit(f"nothing to score yet (missing: {missing})")
w = sum(r["with"]["total"] for r in results)
wo = sum(r["without"]["total"] for r in results)
mx = sum(r["with"]["max"] for r in results)
prefs = [p for r in results for p in r["preferences"]]
autos = [(r["with"].get("auto"), r["without"].get("auto")) for r in results if r["with"].get("auto")]
summary = {
    "cases": n, "skills": len({r["skill"] for r in results}),
    "with_pct": round(100 * w / mx, 1), "without_pct": round(100 * wo / mx, 1),
    "cases_skill_higher": sum(1 for r in results if r["with"]["total"] > r["without"]["total"] + 0.25),
    "cases_baseline_higher": sum(1 for r in results if r["without"]["total"] > r["with"]["total"] + 0.25),
    "cases_level": sum(1 for r in results if abs(r["with"]["total"] - r["without"]["total"]) <= 0.25),
    "prefer_with": prefs.count("with"), "prefer_without": prefs.count("without"), "prefer_tie": prefs.count("tie"),
    "auto_with_pass": sum(1 for a, _ in autos if a["pass"]), "auto_without_pass": sum(1 for _, b in autos if b and b["pass"]),
    "auto_total": len(autos),
    "median_words_with": int(statistics.median(r["with"]["words"] for r in results)),
    "median_words_without": int(statistics.median(r["without"]["words"] for r in results)),
}
print(json.dumps(summary, indent=1))
for r in sorted(results, key=lambda r: r["with"]["total"] - r["without"]["total"]):
    a = r["with"].get("auto")
    print(f"{r['id']:<24} with {r['with']['total']:>5} / without {r['without']['total']:>5}   prefs {r['preferences']}"
          + (f"   auto: with={a['pass']} without={r['without']['auto']['pass']}" if a else ""))
if missing:
    print("not scored yet:", missing)

if "--publish" in sys.argv:
    out = ROOT / "evals"
    pub = out / "outputs"
    if pub.exists():
        shutil.rmtree(pub)
    for r in results:
        m = mapping[r["id"]]
        d = pub / r["id"]
        d.mkdir(parents=True)
        src = work / "runs_original" if (work / "runs_original").exists() else work / "runs"
        shutil.copy(src / r["id"] / f"{m['with_skill']}.md", d / "with-skill.md")
        shutil.copy(src / r["id"] / f"{m['without_skill']}.md", d / "without-skill.md")
    (out / "results.json").write_text(json.dumps({"summary": summary, "cases": results}, indent=1, ensure_ascii=False),
                                      encoding="utf-8")
    print("published to", out)
