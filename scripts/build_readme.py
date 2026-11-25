from pathlib import Path
R = Path(__file__).resolve().parent.parent
import json
CATS = [(c["category"], [(s["name"], s["summary"]) for s in c["skills"]]) for c in json.loads((R/"scripts/categories.json").read_text())]
names = [n for _,s in CATS for n,_ in s]
on_disk = sorted(p.name for p in (R/"skills").iterdir() if p.is_dir())
assert sorted(names)==on_disk, (set(names)^set(on_disk))
N=len(names)
sections=[]
for cat, items in CATS:
    rows="\n".join(f"| [**{n}**](skills/{n}/SKILL.md) | {d} |" for n,d in items)
    sections.append(f"### {cat}\n\n| Skill | What it does |\n|---|---|\n{rows}")
body = "\n\n".join(sections)
readme = f'''<p align="center"><img src=".github/banner.png" alt="AI teaching skills" width="100%"></p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-{N}-0f8b8d?style=flat-square" alt="{N} skills">
  <a href="https://github.com/kal-eficia/ai-teaching-skills/actions/workflows/validate.yml"><img src="https://github.com/kal-eficia/ai-teaching-skills/actions/workflows/validate.yml/badge.svg" alt="validate"></a>
  <img src="https://img.shields.io/badge/built%20for-Claude-0c1a30?style=flat-square" alt="Built for Claude">
  <img src="https://img.shields.io/badge/licence-MIT-c99a2e?style=flat-square" alt="MIT">
</p>

<p align="center"><b>{N} Claude skills for teachers, tutors and school leaders.</b><br>Planning, retrieval, assessment, feedback, inclusion, pastoral, parents and AI, written by a working teacher.</p>

Ask Claude for a lesson without any guidance and you get a lesson plan. Ask for a quiz and the answers go A, B, C, D. Ask for reports and all thirty sound the same.

These skills fix that. Each one is a short, opinionated Claude skill that tells Claude how a teaching job is done well: what to ask, what to build, and what to check before handing it over. They're built on what works in classrooms (retrieval practice, worked examples, hinge questions, variation theory) and on how I run my own lessons, tutoring and parent communication.

## Add them to Claude

**The easy way: [kal-eficia.github.io/ai-teaching-skills](https://kal-eficia.github.io/ai-teaching-skills/)** has an **Add to Claude** button on every skill, plus step-by-step set-up. No GitHub or terminal needed.

**Claude app (claude.ai and desktop)**

1. Make sure *Code execution and file creation* is on in Settings, then Capabilities.
2. Download a skill's zip from the site (or zip a folder from `skills/` yourself, keeping the folder as the top level).
3. Go to *Customize, then Skills*, press **+**, then **Create skill**, then **Upload a skill**, and choose the zip. Turn it on.
4. Ask for the job. Claude loads the skill when your request matches.

On a school Team or Enterprise plan, an owner can publish skills to every member of staff, so teachers don't have to upload anything.

**Claude Code plugin**

```
/plugin marketplace add kal-eficia/ai-teaching-skills
/plugin install ai-teaching-skills
```

**Claude Code, by hand**

```bash
git clone https://github.com/kal-eficia/ai-teaching-skills
mkdir -p ~/.claude/skills
cp -r ai-teaching-skills/skills/* ~/.claude/skills/
```

**Claude Projects:** paste a skill's `SKILL.md` into the project instructions and add your `teaching-context.md` as a project file.

## Start with teaching-context

Add **teaching-context** first and ask Claude to set it up. It interviews you once (classes, exam boards and codes, timetable, delivery mode, student needs, house rules like "no answer patterns" or "British spelling") and saves a `teaching-context.md` file. Every other skill reads that file before it starts, so you never explain your classes twice.

## The skills

{body}

## Examples

See real input and output for the core skills in [examples/](examples/), so you can judge the quality before you try one.

## Try it

> Use lesson-pack-builder. Year 10, Cambridge IGCSE Computer Science 0984, topic 3.1 the CPU, 50 minutes, remote. Last lesson was binary addition.

> Here are last week's quiz results. What are they confusing, and what should I reteach first?

> Build a six-week review for this student. Baseline and latest quiz scores attached.

> Plan a 60-minute CPD session for my department on using AI to plan lessons.

> Check this quiz for answer patterns and fix it.

## The principles behind them

- **Recall first.** Lessons open with retrieval from memory, spaced and interleaved.
- **Student pages talk to students.** Teacher notes stay in the teacher plan.
- **Make the thinking visible.** Hinge questions, confidence ratings, summaries after every page.
- **Check with code, not by eye.** Anything that can be verified (answer keys, word counts, numbering) is.
- **House rules win.** Whatever your teaching context says overrides a skill's defaults.
- **Student data stays safe.** Skills that handle student work ask for initials or numbers, not names, and keep health, SEND and safeguarding details out unless your school's policy allows the tool you're using.
- **Make young people love AI, not fear it,** and design tasks so the learning still happens in their heads.

## Companion tools

- [pattern-guard](https://github.com/kal-eficia/pattern-guard): the answer-pattern checker as a CLI and library
- [recall-engine](https://github.com/kal-eficia/recall-engine): spaced-retrieval starters from a question bank and attempts log
- [lesson-page-kit](https://github.com/kal-eficia/lesson-page-kit): the student-page engine the lesson-pack skill can write for
- [mark-point-checker](https://github.com/kal-eficia/mark-point-checker): marks short answers against the mark schemes the exam-question skill writes
- [ai-skills-kit](https://github.com/kal-eficia/ai-skills-kit): skills for AI adoption, creators and builders

## Other assistants

The skills are written for Claude, but they're plain Markdown. Other coding agents can install them with `npx skills add kal-eficia/ai-teaching-skills`, and ChatGPT, Gemini or Copilot users can paste a `SKILL.md` into a custom GPT, a Gem or the chat.

## Contributing

Teachers: if a skill gets something wrong for your subject, country or age group, open an issue with an example. That's the most useful contribution there is.

New skills are welcome. Each lives in `skills/<name>/SKILL.md`, the `name` in its frontmatter matches the folder, the description says when to use it (under 1,024 characters), and it reads `teaching-context.md` first. `python3 scripts/validate_skills.py` checks all of that, and CI runs it on every push. To measure whether a change makes Claude's output better, run it through Anthropic's skill-creator skill.

---

Written by [Kalid Nur](https://github.com/kal-eficia), who teaches Computer Science, ICT and AI to 11 to 18 year olds and trains schools and teams on adopting AI. MIT licence.
'''
assert "—" not in readme
(R/"README.md").write_text(readme); print("README ok", N)
