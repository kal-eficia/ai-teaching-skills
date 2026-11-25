#!/usr/bin/env python3
"""Build the teacher-facing site (index.html + zip downloads) into _site/.

Everything comes from skills/*/SKILL.md, scripts/categories.json and examples/,
so the page and the downloads always match the repo. Brand assets (logo, fonts)
live in site/. Run: python scripts/build_site.py
"""
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OUT = ROOT / "_site"
REPO = "https://github.com/kal-eficia/ai-teaching-skills"


def title_of(text, name):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else name.replace("-", " ").title()


def zip_skill(skill_dir, dest):
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                z.write(f, Path(skill_dir.name) / f.relative_to(skill_dir))


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "site", OUT)
    (OUT / "downloads").mkdir()
    cats = json.loads((ROOT / "scripts" / "categories.json").read_text(encoding="utf-8"))
    examples = {p.stem for p in (ROOT / "examples").glob("*.md") if p.stem != "README"}
    data, seen = [], set()
    for c in cats:
        for s in c["skills"]:
            d = SKILLS / s["name"]
            text = (d / "SKILL.md").read_text(encoding="utf-8")
            zip_skill(d, OUT / "downloads" / f"{s['name']}.zip")
            data.append({
                "name": s["name"],
                "title": title_of(text, s["name"]),
                "summary": s["summary"],
                "category": c["category"],
                "example": s["name"] in examples,
                "text": text,
            })
            seen.add(s["name"])
    missing = {d.name for d in SKILLS.iterdir() if d.is_dir()} - seen
    if missing:
        raise SystemExit(f"skills missing from categories.json: {sorted(missing)}")
    with zipfile.ZipFile(OUT / "downloads" / "ai-teaching-skills-all.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILLS.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(SKILLS))
    banner = ROOT / ".github" / "banner.png"
    if banner.exists():
        shutil.copy(banner, OUT / "banner.png")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = (TEMPLATE.replace("__COUNT__", str(len(data)))
            .replace("__GROUPS__", str(len(cats) - 1))
            .replace("__REPO__", REPO)
            .replace("__CATS__", json.dumps([c["category"] for c in cats], ensure_ascii=False)))
    assert "—" not in page
    page = page.replace("__DATA__", payload)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(data)} skills into {OUT}")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teaching Skills for Claude by Kalid Nur: __COUNT__ free skills for teachers</title>
<meta name="description" content="__COUNT__ free Claude skills that make Claude work like an experienced teacher: lesson packs, retrieval, assessment, reports, parent messages and more.">
<meta property="og:title" content="Teaching Skills for Claude by Kalid Nur">
<meta property="og:description" content="__COUNT__ free skills that make Claude work like an experienced teacher.">
<meta property="og:image" content="banner.png">
<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/cinzel-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/inter-tight-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{font-family:"Cinzel";src:url(fonts/cinzel-latin-600-normal.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:"Inter Tight";src:url(fonts/inter-tight-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Inter Tight";src:url(fonts/inter-tight-latin-500-normal.woff2) format("woff2");font-weight:500;font-display:swap}
@font-face{font-family:"Inter Tight";src:url(fonts/inter-tight-latin-600-normal.woff2) format("woff2");font-weight:600;font-display:swap}
:root{
  --ink:#16140F;--ink-2:#4A453C;--ink-3:#6B6357;--paper:#F4EFE4;--paper-2:#EBE4D6;--rule:#CFC5B3;
  --brass:#7A5C23;--brass-light:#C9A45C;--on-dark-2:#BDB4A3;
  --font-display:"Cinzel","Trajan Pro",Georgia,serif;--font-body:"Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;
  --fs-h1:clamp(40px,29.5px + 2.7vw,64px);--fs-h2:clamp(32px,24px + 2.03vw,50px);--fs-h3:clamp(22px,20px + .5vw,28px);
  --fs-lead:clamp(19px,17.3px + .45vw,23px);--wrap:1200px;--gutter:40px;--section:96px;--dur:200ms;--ease:cubic-bezier(.2,.7,.2,1)
}
@media (max-width:720px){:root{--gutter:20px;--section:64px}}
*{box-sizing:border-box;border-radius:0}
html{background:var(--ink);scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:18px;line-height:1.6;-webkit-font-smoothing:antialiased}
a,.link{color:var(--ink);text-decoration:underline;text-decoration-color:var(--brass);text-decoration-thickness:2px;text-underline-offset:3px}
button.link{background:none;border:none;padding:0;font:inherit;font-weight:600;cursor:pointer}
:focus-visible{outline:2px solid var(--brass);outline-offset:3px}
.wrap{max-width:var(--wrap);margin-inline:auto;padding-inline:var(--gutter)}
.kicker{display:flex;align-items:center;gap:12px;font-weight:600;font-size:14px;letter-spacing:.32em;text-transform:uppercase;color:var(--brass);margin:0 0 20px}
.kicker::before{content:"";width:7px;height:7px;background:currentColor;flex:none}
.on-ink .kicker{color:var(--brass-light)}
h1,h2,h3{font-family:var(--font-display);font-weight:600;text-transform:uppercase;letter-spacing:.02em;margin:0}
h1{font-size:var(--fs-h1);line-height:1.08}
h2{font-size:var(--fs-h2);line-height:1.12;margin-bottom:16px}
h3{font-size:var(--fs-h3);line-height:1.15}
.lead{font-size:var(--fs-lead);line-height:1.55;color:var(--ink-2);max-width:64ch;margin:24px 0 36px;text-wrap:pretty}
section{padding-block:var(--section);border-top:1px solid var(--rule)}
.on-ink{background:var(--ink);color:var(--paper);border-top:none}
.on-ink p,.on-ink li{color:var(--on-dark-2)}
.on-ink a{color:var(--paper);text-decoration-color:var(--brass-light)}

header.site{border-bottom:1px solid var(--rule)}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;padding-block:20px}
header.site img{height:52px;width:auto;display:block;margin-inline-start:-8px}
nav.top{display:flex;gap:28px;font-size:16px;font-weight:500}
nav.top a{text-decoration:none}nav.top a:hover{text-decoration:underline;text-decoration-color:var(--brass)}
@media (max-width:720px){nav.top .hide-sm{display:none}header.site img{height:44px}}

.hero{border-top:none;padding-block:80px var(--section)}
.hero-grid{display:grid;grid-template-columns:1fr auto;gap:56px;align-items:start}
.hero-mark{width:300px;height:auto}
@media (max-width:960px){.hero-grid{grid-template-columns:1fr}.hero-mark{width:120px;order:-1}}
.btns{display:flex;flex-wrap:wrap;align-items:center;gap:16px 28px}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:16px 26px;font:600 17px/1 var(--font-body);background:var(--ink);color:var(--paper);text-decoration:none;border:1.5px solid var(--ink);cursor:pointer;transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.btn:hover{background:var(--brass);border-color:var(--brass)}
.btn.small{padding:10px 16px;font-size:15px}
.more{font-weight:600;font-size:17px}
.more::after{content:" \2192";display:inline-block;transition:transform var(--dur) var(--ease)}
.more:hover::after{transform:translateX(4px)}
.receipts{display:flex;flex-wrap:wrap;gap:8px 28px;margin-top:40px;color:var(--ink-3);font-size:15px;list-style:none;padding:0}
.receipts li{display:flex;align-items:center;gap:10px}
.receipts li::before{content:"";width:7px;height:7px;background:var(--brass)}

.cols{display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px solid var(--ink);margin-top:40px}
.col{padding:28px 28px 8px 0}
.col+.col{padding-inline-start:28px;border-inline-start:1px solid var(--rule)}
.col .num{font-family:var(--font-display);color:var(--brass);font-size:20px;display:block;margin-bottom:14px}
.col h3{font-size:22px;margin-bottom:10px}
.col p{margin:0;color:var(--ink-2);font-size:17px}
@media (max-width:960px){.cols{grid-template-columns:1fr 1fr}.col:nth-child(3){padding-inline-start:0;border-inline-start:none}.col:nth-child(n+3){border-top:1px solid var(--rule)}}
@media (max-width:600px){.cols{grid-template-columns:1fr}.col,.col+.col{padding-inline-start:0;border-inline-start:none}.col+.col{border-top:1px solid var(--rule)}}
.panel{background:var(--paper-2);padding:28px 32px;margin-top:48px;max-width:860px}
.panel .kicker{margin-bottom:10px}
.panel p{margin:0;color:var(--ink-2)}

.tabs{display:flex;flex-wrap:wrap;gap:4px 32px;border-bottom:1px solid #3a352b;margin:32px 0 28px}
.tab{background:none;border:none;color:var(--on-dark-2);font:500 17px var(--font-body);padding:0 0 14px;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-1px}
.tab[aria-selected=true]{color:var(--paper);border-bottom-color:var(--brass-light)}
.tab:hover{color:var(--paper)}
.guide ol{margin:0;padding-inline-start:22px;max-width:72ch}
.guide li{margin:10px 0}
.guide b{color:var(--paper);font-weight:600}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:15px;background:#2a261e;color:var(--paper);padding:2px 7px}

.tools{display:flex;flex-wrap:wrap;gap:16px;margin:40px 0 20px}
.search{flex:1;min-width:240px;padding:14px 16px;border:1.5px solid var(--ink);background:var(--paper);font:400 17px var(--font-body);color:var(--ink)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:8px}
.chip{padding:8px 14px;border:1px solid var(--rule);background:transparent;font:500 15px var(--font-body);cursor:pointer;color:var(--ink-2)}
.chip:hover{border-color:var(--ink);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.cat{margin:64px 0 0;padding-bottom:18px;border-bottom:1.5px solid var(--ink);display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.cat small{font:500 15px var(--font-body);color:var(--ink-3);text-transform:none;letter-spacing:0}
.rows{display:grid;grid-template-columns:repeat(3,1fr)}
.skill{padding:28px 28px 28px 0;border-bottom:1px solid var(--rule);display:flex;flex-direction:column;gap:10px}
.skill:not(:nth-child(3n+1)){padding-inline-start:28px;border-inline-start:1px solid var(--rule)}
.skill h4{font-family:var(--font-display);font-weight:600;font-size:20px;line-height:1.2;text-transform:uppercase;margin:0;letter-spacing:.02em}
.skill .slug{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;color:var(--ink-3)}
.skill p{margin:0;color:var(--ink-2);font-size:16.5px;line-height:1.55;flex:1}
.acts{display:flex;flex-wrap:wrap;align-items:center;gap:10px 20px;margin-top:6px;font-size:15px;font-weight:600}
@media (max-width:960px){.rows{grid-template-columns:1fr 1fr}.skill:not(:nth-child(3n+1)){padding-inline-start:0;border-inline-start:none}.skill:nth-child(2n){padding-inline-start:28px;border-inline-start:1px solid var(--rule)}}
@media (max-width:600px){.rows{grid-template-columns:1fr}.skill,.skill:nth-child(2n){padding-inline-start:0;border-inline-start:none}}
.start{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;background:var(--paper-2);padding:28px 32px;margin-top:40px}
.start h3{font-size:24px;margin:4px 0 8px}
.start p{margin:0;color:var(--ink-2)}
.start .kicker{margin:0}
@media (max-width:720px){.start{grid-template-columns:1fr}}
.empty{color:var(--ink-3);display:none;margin-top:32px}

footer.site{background:var(--ink);color:var(--on-dark-2);padding-block:56px;font-size:15px}
footer.site .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:32px;align-items:flex-start}
footer.site img{height:60px;width:auto;margin-inline-start:-10px}
footer.site p{margin:0;max-width:56ch}
footer.site a{color:var(--paper);text-decoration-color:var(--brass-light)}

dialog{max-width:820px;width:calc(100% - 32px);border:1.5px solid var(--ink);padding:0;background:var(--paper);color:var(--ink)}
dialog::backdrop{background:rgba(22,20,15,.7)}
.dhead{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 28px;border-bottom:1px solid var(--rule);position:sticky;top:0;background:var(--paper);flex-wrap:wrap}
.dhead strong{font-family:var(--font-display);font-weight:600;text-transform:uppercase;font-size:18px}
.dbody{padding:8px 28px 32px;max-height:72vh;overflow:auto;font-size:17px}
.dbody h1{font-size:30px;margin:20px 0 12px}
.dbody h2,.dbody h3{font-family:var(--font-body);text-transform:none;letter-spacing:0;font-weight:600}
.dbody h2{font-size:22px;margin:28px 0 8px}
.dbody h3{font-size:18px;margin:20px 0 6px}
.dbody p,.dbody li{color:var(--ink-2)}
.dbody blockquote{margin:16px 0;padding:12px 18px;border-inline-start:3px solid var(--brass);background:var(--paper-2)}
.dbody blockquote p{margin:0 0 6px}.dbody blockquote p:last-child{margin:0}
.dbody pre{background:var(--ink);color:var(--paper);padding:16px;overflow:auto;font-size:14px}
.dbody code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.88em;background:var(--paper-2);padding:1px 5px}
.dbody pre code{background:none;padding:0}
.dbody table{border-collapse:collapse;width:100%;font-size:15px}
.dbody td,.dbody th{border-bottom:1px solid var(--rule);padding:8px 10px 8px 0;text-align:start;vertical-align:top}
.dbody th{border-bottom:1.5px solid var(--ink)}
.toast{position:fixed;bottom:24px;left:50%;transform:translate(-50%,12px);background:var(--ink);color:var(--paper);padding:14px 20px;opacity:0;transition:opacity var(--dur) var(--ease),transform var(--dur) var(--ease);pointer-events:none;font-weight:500;font-size:16px}
.toast.show{opacity:1;transform:translate(-50%,0)}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a href="./" aria-label="Teaching Skills for Claude home"><img src="brand/kalid-nur-logo-no-tagline.svg" alt="Kalid Nur logo: نور (light) in square Kufic" width="160" height="52"></a>
    <nav class="top" aria-label="Main">
      <a href="#setup" class="hide-sm">Add to Claude</a>
      <a href="#skills">Skills</a>
      <a href="__REPO__">GitHub</a>
    </nav>
  </div>
</header>

<main>
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">__COUNT__ free Claude skills for teachers</p>
      <h1>Teaching skills for Claude</h1>
      <p class="lead">Teach Claude to work like an experienced teacher. Each skill is a short playbook for one job, from lesson packs and retrieval starters to reports, parent messages and hinge questions. Add a skill to Claude once and it uses it whenever that job comes up.</p>
      <div class="btns">
        <a class="btn" href="#skills">Browse the skills</a>
        <a class="more" href="#how">How to add them to Claude</a>
      </div>
      <ul class="receipts">
        <li>Written by a working teacher</li>
        <li>Built for Claude</li>
        <li>Free, MIT licence</li>
      </ul>
    </div>
    <img class="hero-mark" src="brand/nur-mark.svg" alt="" width="300" height="300">
  </div>
</section>

<section id="how">
  <div class="wrap">
    <p class="kicker">How it works</p>
    <h2>Add once, then just ask</h2>
    <p class="lead" style="margin-bottom:0">No coding. Each skill is a small zip you upload to Claude in a minute. After that, Claude uses it whenever your request matches.</p>
    <div class="cols">
      <div class="col"><span class="num">01</span><h3>Download</h3><p>Press <b>Add to Claude</b> on a skill to download its zip. Start with <button class="link" data-open="teaching-context">Teaching Context</button>.</p></div>
      <div class="col"><span class="num">02</span><h3>Upload</h3><p>In Claude, go to Customize, then Skills. Press +, then Create skill, then Upload a skill, and choose the zip.</p></div>
      <div class="col"><span class="num">03</span><h3>Set up</h3><p>Ask Claude to set up your teaching context. It asks about your classes and rules once, and every skill reads it.</p></div>
      <div class="col"><span class="num">04</span><h3>Just ask</h3><p>"Plan tomorrow's Year 9 lesson on networks." Claude picks the right skill on its own.</p></div>
    </div>
    <div class="panel" role="note">
      <p class="kicker">Student data</p>
      <p>Use initials or numbers instead of names, and leave out health, SEND, safeguarding and family details unless your school's data protection and AI policy allow them in Claude. When in doubt, anonymise first.</p>
    </div>
  </div>
</section>

<section class="on-ink" id="setup">
  <div class="wrap">
    <p class="kicker">Set it up</p>
    <h2>Three ways to use them in Claude</h2>
    <p>Skills need code execution switched on: in Claude, open Settings, then Capabilities, and turn on "Code execution and file creation".</p>
    <div class="tabs" role="tablist" aria-label="Choose how you use Claude">
      <button class="tab" role="tab" aria-selected="true" data-tab="claude">Claude app</button>
      <button class="tab" role="tab" aria-selected="false" data-tab="school">School Team or Enterprise</button>
      <button class="tab" role="tab" aria-selected="false" data-tab="projects">Claude Projects</button>
      <button class="tab" role="tab" aria-selected="false" data-tab="code">Claude Code</button>
    </div>
    <div class="guide" data-panel="claude"><ol>
      <li><b>Download:</b> press "Add to Claude" on a skill. You get a zip; don't unzip it.</li>
      <li><b>Upload:</b> on claude.ai or the desktop app, go to Customize, then Skills. Press +, then Create skill, then Upload a skill, and choose the zip.</li>
      <li><b>Turn it on</b> with the switch next to it. Then just ask for the job, for example "Write a hinge question on the fetch-decode-execute cycle". Claude loads the skill when the request matches.</li>
      <li><b>Start small:</b> Teaching Context, Lesson Pack Builder, Recall Starter, Misconception Finder and Student Report Writer cover most of a week.</li>
    </ol></div>
    <div class="guide" data-panel="school" hidden><ol>
      <li>An owner of your school's Claude organisation may need to switch skills on in Organization settings first.</li>
      <li>Once a skill is uploaded, an owner can share it with colleagues or publish it to the whole organisation from Customize, then Skills, so every teacher has it without uploading anything.</li>
      <li>Check your school's policy on what student data can go into Claude, and keep using placeholders like [S1] where it says to.</li>
    </ol></div>
    <div class="guide" data-panel="projects" hidden><ol>
      <li>Create a Project for a class or a subject.</li>
      <li>Press "Copy text" on a skill and paste it into the project instructions, or add it as a project file. Add your <span class="mono">teaching-context.md</span> too.</li>
      <li>Every chat in that Project now follows the skill, which works well for one class's lessons, reports or parent messages.</li>
    </ol></div>
    <div class="guide" data-panel="code" hidden><ol>
      <li>Install as a plugin: <span class="mono">/plugin marketplace add kal-eficia/ai-teaching-skills</span>, then <span class="mono">/plugin install ai-teaching-skills</span></li>
      <li>Or copy them in: download <a href="downloads/ai-teaching-skills-all.zip">all __COUNT__ skills</a> and unzip into <span class="mono">~/.claude/skills/</span>.</li>
      <li>Type <span class="mono">/lesson-pack-builder</span> (or any skill name) to run one directly. Source is on <a href="__REPO__">GitHub</a>.</li>
    </ol></div>
    <p style="margin-top:40px;font-size:16px">Using ChatGPT, Gemini or Copilot as well? The skills are plain text, so "Copy text" and paste one into a custom GPT, a Gem or the chat. Or install with <span class="mono">npx skills add kal-eficia/ai-teaching-skills</span> for other coding agents.</p>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <p class="kicker">The library</p>
    <h2>__COUNT__ skills, __GROUPS__ groups</h2>
    <div class="start">
      <div><p class="kicker">Start here</p><h3>Teaching Context</h3><p>Records your classes, exam boards, timetable and house rules once. Every other skill reads it first.</p></div>
      <div class="btns"><a class="btn small" href="downloads/teaching-context.zip" download>Add to Claude</a><button class="link" data-open="teaching-context">Read</button><button class="link" data-copy="teaching-context">Copy text</button></div>
    </div>
    <div class="tools"><input class="search" id="q" type="search" placeholder="Search, e.g. reports, quiz, SEND, revision" aria-label="Search skills"></div>
    <div class="chips" id="chips" role="group" aria-label="Filter by group"></div>
    <div id="list"></div>
    <p class="empty" id="empty">No skills match that search.</p>
  </div>
</section>
</main>

<footer class="site"><div class="wrap">
  <img src="brand/kalid-nur-logo-reversed.svg" alt="Kalid Nur logo: نور (light) in square Kufic" width="186" height="60">
  <p>Written by Kalid Nur, who teaches Computer Science, ICT and AI to 11 to 18 year olds and trains schools and teams on adopting AI. Free under the MIT licence. Something wrong for your subject or country? <a href="__REPO__/issues">Tell me on GitHub</a>.</p>
</div></footer>

<dialog id="dlg" aria-labelledby="dtitle">
  <div class="dhead"><strong id="dtitle"></strong><div class="acts"><a class="btn small" id="dzip">Add to Claude</a><button class="link" id="dcopy">Copy text</button><button class="link" id="dclose">Close</button></div></div>
  <div class="dbody" id="dbody"></div>
</dialog>
<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
const SKILLS = __DATA__;
const CATS = __CATS__;
const REPO = "__REPO__";
const $ = s => document.querySelector(s);
const byName = Object.fromEntries(SKILLS.map(s => [s.name, s]));
let active = "All";

function esc(t){return t.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
function inline(t){return esc(t).replace(/`([^`]+)`/g,"<code>$1</code>").replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/\*([^*]+)\*/g,"<i>$1</i>").replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>')}
function md(src){
  const body = src.replace(/^---[\s\S]*?\n---\n/, "");
  const lines = body.split("\n"); let out = [], list = null, pre = false, buf = [], table = [], quote = [];
  const flushList = () => { if (list) { out.push(`<${list.t}>${list.items.map(i=>`<li>${inline(i)}</li>`).join("")}</${list.t}>`); list = null; } };
  const flushTable = () => { if (table.length) { const rows = table.filter(r=>!/^\|[\s|:-]+\|$/.test(r)).map(r=>r.slice(1,-1).split("|").map(c=>inline(c.trim()))); out.push("<table>"+rows.map((r,i)=>"<tr>"+r.map(c=>i?`<td>${c}</td>`:`<th>${c}</th>`).join("")+"</tr>").join("")+"</table>"); table = []; } };
  const flushQuote = () => { if (quote.length) { out.push("<blockquote>"+quote.filter(Boolean).map(q=>`<p>${inline(q)}</p>`).join("")+"</blockquote>"); quote = []; } };
  for (const l of lines) {
    if (l.startsWith("```")) { if (pre) { out.push("<pre>"+esc(buf.join("\n"))+"</pre>"); buf = []; pre = false; } else { flushList(); flushTable(); flushQuote(); pre = true; } continue; }
    if (pre) { buf.push(l); continue; }
    if (l.startsWith(">")) { flushList(); flushTable(); quote.push(l.replace(/^>\s?/, "")); continue; } else flushQuote();
    if (/^\|.*\|$/.test(l.trim())) { flushList(); table.push(l.trim()); continue; } else flushTable();
    let m;
    if ((m = l.match(/^(#{1,3}) (.*)/))) { flushList(); out.push(`<h${m[1].length}>${inline(m[2])}</h${m[1].length}>`); }
    else if ((m = l.match(/^\s*[-*] (?:\[ \] )?(.*)/))) { if (!list || list.t !== "ul") { flushList(); list = {t:"ul", items:[]}; } list.items.push(m[1]); }
    else if ((m = l.match(/^\s*\d+\. (.*)/))) { if (!list || list.t !== "ol") { flushList(); list = {t:"ol", items:[]}; } list.items.push(m[1]); }
    else if (l.trim() === "") { flushList(); }
    else { flushList(); out.push(`<p>${inline(l)}</p>`); }
  }
  flushList(); flushTable(); flushQuote(); return out.join("\n");
}
function toast(msg){const t=$("#toast");t.textContent=msg;t.classList.add("show");clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove("show"),2000)}
async function copy(name){
  const s = byName[name];
  try { await navigator.clipboard.writeText(s.text); }
  catch { const ta=document.createElement("textarea"); ta.value=s.text; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); }
  toast(`Copied ${s.title}. Paste it into a Claude Project or chat.`);
}
function row(s){
  const ex = s.example ? `<a href="${REPO}/blob/main/examples/${s.name}.md" target="_blank" rel="noopener">See an example</a>` : "";
  return `<article class="skill">
    <h4>${esc(s.title)}</h4><span class="slug">${s.name}</span>
    <p>${esc(s.summary)}</p>
    <div class="acts">
      <a class="btn small" href="downloads/${s.name}.zip" download>Add to Claude</a>
      <button class="link" data-open="${s.name}">Read</button>
      <button class="link" data-copy="${s.name}">Copy text</button>
      ${ex}
    </div></article>`;
}
function render(){
  const q = $("#q").value.trim().toLowerCase();
  const match = s => s.name !== "teaching-context" && (active==="All"||s.category===active) && (!q || (s.title+" "+s.name+" "+s.summary+" "+s.text).toLowerCase().includes(q));
  let html = "", n = 0;
  for (const c of CATS) {
    const items = SKILLS.filter(s => s.category===c && match(s));
    if (!items.length) continue; n += items.length;
    html += `<h3 class="cat">${esc(c)} <small>${items.length} skill${items.length>1?"s":""}</small></h3><div class="rows">${items.map(row).join("")}</div>`;
  }
  $("#list").innerHTML = html; $("#empty").style.display = n ? "none" : "block";
}
function open(name){
  const s = byName[name]; if (!s) return;
  $("#dtitle").textContent = s.title; $("#dbody").innerHTML = md(s.text);
  $("#dcopy").dataset.copy = name; $("#dzip").href = `downloads/${name}.zip`; $("#dzip").setAttribute("download","");
  $("#dlg").showModal(); $("#dbody").scrollTop = 0;
}
$("#chips").innerHTML = ["All", ...CATS.filter(c=>c!=="Start here")].map(c => `<button class="chip" aria-pressed="${c==="All"}" data-cat="${esc(c)}">${esc(c)}</button>`).join("");
document.addEventListener("click", e => {
  const t = e.target.closest("[data-copy],[data-open],[data-cat],[data-tab],#dclose");
  if (!t) return;
  if (t.id === "dclose") return $("#dlg").close();
  if (t.dataset.copy) return copy(t.dataset.copy);
  if (t.dataset.open) { e.preventDefault(); return open(t.dataset.open); }
  if (t.dataset.cat) { active = t.dataset.cat; document.querySelectorAll(".chip").forEach(c => c.setAttribute("aria-pressed", c===t)); return render(); }
  if (t.dataset.tab) { document.querySelectorAll(".tab").forEach(b => b.setAttribute("aria-selected", b===t)); document.querySelectorAll("[data-panel]").forEach(p => p.hidden = p.dataset.panel !== t.dataset.tab); }
});
$("#dlg").addEventListener("click", e => { if (e.target === $("#dlg")) $("#dlg").close(); });
$("#q").addEventListener("input", render);
render();
if (location.hash.startsWith("#skill-")) open(location.hash.slice(7));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
