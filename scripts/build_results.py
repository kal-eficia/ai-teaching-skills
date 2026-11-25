#!/usr/bin/env python3
"""Build _site/results.html from evals/results.json, reusing the site's styles. Called by build_site.py."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/kal-eficia/ai-teaching-skills"


def e(s):
    return html.escape(str(s))


def bar(pct, strong):
    colour = "var(--ink)" if strong else "var(--rule)"
    return (f'<div class="bar" role="img" aria-label="{pct:.0f} percent"><span style="width:{pct:.1f}%;background:{colour}"></span></div>')


def build(index_html: str, out: Path) -> None:
    data = json.loads((ROOT / "evals" / "results.json").read_text(encoding="utf-8"))
    s, cases = data["summary"], sorted(data["cases"], key=lambda c: c["without"]["total"] - c["with"]["total"])
    style = re.search(r"<style>(.*?)</style>", index_html, re.S).group(1)
    head = index_html[:index_html.index("<main>")]
    head = re.sub(r"<title>.*?</title>", "<title>Results: do the teaching skills make Claude better? | Kalid Nur</title>", head)
    head = head.replace('href="#setup" class="hide-sm"', 'href="./#setup" class="hide-sm"').replace('href="#skills"', 'href="./#skills"')
    foot = index_html[index_html.index('<footer class="site">'):index_html.index("</footer>") + len("</footer>")]
    extra = """
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px solid var(--ink);margin-top:40px}
.stat{padding:28px 24px 12px 0}.stat+.stat{padding-inline-start:24px;border-inline-start:1px solid var(--rule)}
.stat b{font-family:var(--font-display);font-weight:600;font-size:clamp(34px,4vw,52px);line-height:1;display:block}
.stat span{display:block;color:var(--ink-2);font-size:16px;margin-top:10px}.stat small{color:var(--ink-3);font-size:14px}
@media (max-width:860px){.stats{grid-template-columns:1fr 1fr}.stat:nth-child(3){padding-inline-start:0;border-inline-start:none}.stat:nth-child(n+3){border-top:1px solid var(--rule)}}
.case{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:32px;padding:28px 0;border-bottom:1px solid var(--rule)}
@media (max-width:860px){.case{grid-template-columns:1fr;gap:16px}}
.case h3{font-size:20px;margin-bottom:6px}.case .meta{color:var(--ink-3);font-size:14px;margin:0 0 10px}
.case p{margin:0 0 10px;color:var(--ink-2);font-size:16px}
.row{display:grid;grid-template-columns:110px 1fr 64px;gap:12px;align-items:center;font-size:15px;margin:6px 0}
.bar{height:12px;background:var(--paper-2)}.bar span{display:block;height:100%}
.tag{display:inline-block;font-size:13px;font-weight:600;padding:3px 8px;border:1px solid var(--rule);margin:8px 8px 0 0;color:var(--ink-2)}
.tag.ok{border-color:var(--ink);color:var(--ink)}.tag.no{color:var(--brass);border-color:var(--brass)}
.rt{border-collapse:collapse;width:100%;max-width:860px;font-size:16px}.rt th,.rt td{text-align:start;padding:10px 12px 10px 0;border-bottom:1px solid var(--rule)}.rt th{border-bottom:1.5px solid var(--ink)}.rt td:first-child{text-transform:capitalize}
.limits li{margin:8px 0;color:var(--ink-2)}.limits{max-width:70ch;padding-inline-start:20px}
"""
    rows = []
    for c in cases:
        w, wo = c["with"], c["without"]
        tags = ""
        if w.get("auto"):
            for label, a in (("With skill", w["auto"]), ("Without", wo["auto"])):
                state = "ok" if a["pass"] else "no"
                verdict = "pass" if a["pass"] else ("fail" if a["pass"] is False else "not checked")
                tags += f'<span class="tag {state}">{e(a["name"])}: {label.lower()} {verdict}</span>'
        prefer = c["preferences"].count("with")
        task = c["task"].split("\n\nFormat:")[0]
        task = task if len(task) < 330 else task[:327].rsplit(" ", 1)[0] + "..."
        rows.append(f"""<article class="case">
<div><h3>{e(c['skill'].replace('-', ' '))}</h3><p class="meta">{e(c['subject'])} · graders preferred the skill answer {prefer} of {len(c['preferences'])}</p>
<p>"{e(task)}"</p></div>
<div>
<div class="row"><span>With skill</span>{bar(100 * w['total'] / w['max'], True)}<b>{w['total']:g}/{w['max']}</b></div>
<div class="row"><span>Without</span>{bar(100 * wo['total'] / wo['max'], False)}<b>{wo['total']:g}/{wo['max']}</b></div>
{tags}
<p style="margin-top:14px;font-size:15px">{e(c['reasons'][0])}</p>
<p style="font-size:15px;font-weight:600"><a href="{REPO}/blob/main/evals/outputs/{c['id']}/with-skill.md">Read the skill answer</a> &nbsp; <a href="{REPO}/blob/main/evals/outputs/{c['id']}/without-skill.md">Read the plain answer</a></p>
</div></article>""")
    retest = ""
    rp = ROOT / "evals" / "retest.json"
    if rp.exists():
        rt = json.loads(rp.read_text(encoding="utf-8"))
        first = {c["id"]: c for c in data["cases"]}
        trs = "".join(
            f"<tr><td>{e(c['skill'].replace('-', ' '))}</td><td>{first[c['id']]['with']['total']:g} v {first[c['id']]['without']['total']:g}</td>"
            f"<td><b>{c['with']['total']:g} v {c['without']['total']:g}</b></td><td>{c['preferences'].count('with')} of {len(c['preferences'])}</td></tr>"
            for c in rt["cases"])
        rs = rt["summary"]
        retest = f"""<section><div class="wrap">
<p class="kicker">Fixed and tested again</p><h2>The re-test</h2>
<p class="lead">Eight skills were tightened using the graders' notes, then tested again with fresh answers and new blind graders. Scores are skill v plain, out of 12. The skill answer was preferred in {rs['prefer_with']} of {rs['prefer_with'] + rs['prefer_without'] + rs['prefer_tie']} judgements.</p>
<table class="rt"><tr><th>Skill</th><th>First run</th><th>Re-test</th><th>Graders preferred skill</th></tr>{trs}</table>
</div></section>"""
    body = f"""<main>
<section class="hero" style="padding-bottom:64px"><div class="wrap">
<p class="kicker">Tested, not just claimed</p>
<h1>Do the skills work?</h1>
<p class="lead">{s['cases']} real teaching tasks. Each one answered twice by Claude, once with the skill and once without. Graded blind by a second model that didn't know which was which, and checked by code where code can check.</p>
<div class="stats">
<div class="stat"><b>{s['with_pct']:g}%</b><span>of criteria met with the skill</span><small>{s['without_pct']:g}% without</small></div>
<div class="stat"><b>{s['prefer_with']}/{s['prefer_with'] + s['prefer_without'] + s['prefer_tie']}</b><span>blind judgements preferred the skill answer</span><small>two graders per task</small></div>
<div class="stat"><b>{s['auto_with_pass']}/{s['auto_total']}</b><span>code checks passed with the skill</span><small>{s['auto_without_pass']} of {s['auto_total']} without</small></div>
<div class="stat"><b>{s['cases_skill_higher']}/{s['cases']}</b><span>tasks where the skill scored higher</span><small>{s['cases_baseline_higher']} lower, {s['cases_level']} level</small></div>
</div></div></section>
<section><div class="wrap">
<p class="kicker">Task by task</p><h2>Every result</h2>
<p class="lead" style="margin-bottom:8px">Biggest differences first. Scores are out of 12, averaged over two graders. Both answers to every task are public.</p>
{''.join(rows)}
</div></section>
{retest}
<section class="on-ink"><div class="wrap">
<p class="kicker">Read this too</p><h2>The limits</h2>
<ul class="limits">
<li>The marking criteria were written by me, the skills' author. The graders' overall preference and the code checks are the fairer measures.</li>
<li>One run per task. Single results can vary; the pattern across {s['cases']} tasks is the finding.</li>
<li>The graders are AI models, not teachers. A teacher panel is the next step.</li>
<li>Many answers scored near full marks, so the scores understate differences at the top.</li>
<li>The skill lost on the exam-question task in the first run. Eight skills were tightened and re-tested the same day; the re-test is shown above.</li>
</ul>
<p style="margin-top:28px"><a href="{REPO}/tree/main/evals">Full method, every answer and the grading files are on GitHub</a>.</p>
</div></section>
</main>
"""
    page = head.replace("</style>", extra + "</style>") + body + foot + "\n</body>\n</html>\n"
    assert "—" not in page
    out.write_text(page, encoding="utf-8")
