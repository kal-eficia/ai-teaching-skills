<p align="center"><img src=".github/banner.png" alt="AI teaching skills" width="100%"></p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-56-0f8b8d?style=flat-square" alt="56 skills">
  <a href="https://github.com/kal-eficia/ai-teaching-skills/actions/workflows/validate.yml"><img src="https://github.com/kal-eficia/ai-teaching-skills/actions/workflows/validate.yml/badge.svg" alt="validate"></a>
  <img src="https://img.shields.io/badge/works%20with-Claude%20%C2%B7%20Codex%20%C2%B7%20Cursor%20%C2%B7%20any%20agent-0c1a30?style=flat-square" alt="Works with any agent">
  <img src="https://img.shields.io/badge/licence-MIT-c99a2e?style=flat-square" alt="MIT">
</p>

<p align="center"><b>56 agent skills for teachers, tutors and school leaders.</b><br>Planning, retrieval, assessment, feedback, inclusion, pastoral, parents and AI, written by a working teacher.</p>

Ask a general AI assistant for a lesson and you get a lesson plan. Ask for a quiz and the answers go A, B, C, D. Ask for reports and all thirty sound the same.

These skills fix that. Each one is a short, opinionated playbook that tells an AI assistant how a teaching job is done well: what to ask, what to build, and what to check before handing it over. They're built on what works in classrooms (retrieval practice, worked examples, hinge questions, variation theory) and on how I run my own lessons, tutoring and parent communication.

## Start with teaching-context

Run **teaching-context** first. It interviews you once (classes, exam boards and codes, timetable, delivery mode, student needs, house rules like "no answer patterns" or "British spelling") and saves a `teaching-context.md` file. Every other skill reads that file before it starts, so you never explain your classes twice.

## Install

**Any agent (Claude Code, Codex, Cursor, Gemini CLI and more)**

```bash
npx skills add kal-eficia/ai-teaching-skills
```

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

**Claude apps (claude.ai, desktop):** zip a skill folder (for example `skills/lesson-pack-builder`) and upload it under *Settings → Capabilities → Skills*.

**Any other assistant:** paste the contents of a `SKILL.md` into the conversation or your project instructions. They are plain Markdown.

## The skills

### Start here

| Skill | What it does |
|---|---|
| [**teaching-context**](skills/teaching-context/SKILL.md) | Records your classes, boards, timetable and house rules once. Every other skill reads it first |

### Planning and curriculum

| Skill | What it does |
|---|---|
| [**lesson-pack-builder**](skills/lesson-pack-builder/SKILL.md) | A full, teachable pack: teacher plan, interactive student page, homework, mark scheme and a solutions sheet |
| [**scheme-of-work-builder**](skills/scheme-of-work-builder/SKILL.md) | A term or year of lessons, sequenced by dependency, with spaced retrieval and assessment points |
| [**learning-objectives-writer**](skills/learning-objectives-writer/SKILL.md) | Turns a spec point into checkable objectives and success criteria at the right level |
| [**curriculum-mapper**](skills/curriculum-mapper/SKILL.md) | Maps taught, planned and assessed against the spec to show gaps and over-taught areas |
| [**knowledge-organiser**](skills/knowledge-organiser/SKILL.md) | A one-page organiser: essential facts, vocabulary, diagrams and common mistakes |
| [**homework-designer**](skills/homework-designer/SKILL.md) | Short, spaced homework nobody at home has to teach, quick to check |
| [**cover-lesson-planner**](skills/cover-lesson-planner/SKILL.md) | A cover lesson a non-specialist can run with zero preparation |
| [**remote-lesson-adapter**](skills/remote-lesson-adapter/SKILL.md) | Adapts a lesson for Zoom or Teams so every student participates and you can see their thinking |

### Memory and retrieval

| Skill | What it does |
|---|---|
| [**recall-starter**](skills/recall-starter/SKILL.md) | A spaced, interleaved retrieval starter built from what students got wrong |
| [**low-stakes-quiz-builder**](skills/low-stakes-quiz-builder/SKILL.md) | A 5 to 15 question quiz mixing recent and older topics, with confidence ratings |
| [**flashcard-deck-builder**](skills/flashcard-deck-builder/SKILL.md) | One fact per card, precise answers, ordered for spaced practice |
| [**interleaved-practice-builder**](skills/interleaved-practice-builder/SKILL.md) | Mixed problem sets that make students choose the method, not repeat the last one |
| [**no-answer-patterns**](skills/no-answer-patterns/SKILL.md) | Checks and fixes MCQ and sort-task keys so students can't guess the pattern. Bundles a checker script |

### Explaining and modelling

| Skill | What it does |
|---|---|
| [**explanation-crafter**](skills/explanation-crafter/SKILL.md) | A clear explanation for a specific age: known to new, concrete before abstract, checks built in |
| [**worked-example-builder**](skills/worked-example-builder/SKILL.md) | Worked examples with faded guidance, from fully worked to independent |
| [**modelling-sequence**](skills/modelling-sequence/SKILL.md) | An I do, we do, you do sequence with live thinking aloud |
| [**questioning-planner**](skills/questioning-planner/SKILL.md) | Hinge questions, cold-call sequences, probing follow-ups and responses to wrong answers |
| [**dual-coding-designer**](skills/dual-coding-designer/SKILL.md) | The diagram, flow chart or timeline that pairs with your explanation |
| [**vocabulary-builder**](skills/vocabulary-builder/SKILL.md) | Explicit teaching of the subject words that matter, with student-friendly definitions |

### Assessment and feedback

| Skill | What it does |
|---|---|
| [**exam-question-writer**](skills/exam-question-writer/SKILL.md) | Original exam-style questions and mark schemes in the board's command words and mark allocations |
| [**hinge-question-writer**](skills/hinge-question-writer/SKILL.md) | Single MCQs where every wrong option reveals a specific misconception |
| [**diagnostic-test-builder**](skills/diagnostic-test-builder/SKILL.md) | A baseline test that finds what students know and the exact gaps to fix first |
| [**misconception-finder**](skills/misconception-finder/SKILL.md) | Groups wrong answers by the idea behind them and plans the fix, confident-but-wrong first |
| [**question-level-analysis**](skills/question-level-analysis/SKILL.md) | Mock results question by question: which topics and skills lost the most marks |
| [**script-marker**](skills/script-marker/SKILL.md) | Consistent marking against a scheme, every mark with its evidence, borderline cases flagged |
| [**whole-class-feedback**](skills/whole-class-feedback/SKILL.md) | Turns marked work into one feedback sheet, model answers and an improvement task |
| [**essay-feedback**](skills/essay-feedback/SKILL.md) | Level-based feedback on extended writing with one priority and a rewrite task |
| [**peer-assessment-designer**](skills/peer-assessment-designer/SKILL.md) | Peer review that works: calibration first, structured prompts, accuracy checks |
| [**exam-technique-coach**](skills/exam-technique-coach/SKILL.md) | Command words, marks as a guide to length, planning and timing |
| [**coursework-guide**](skills/coursework-guide/SKILL.md) | Stages, deadlines and what each criterion rewards, inside the board's rules on help |

### Inclusion and adaptation

| Skill | What it does |
|---|---|
| [**send-adaptations**](skills/send-adaptations/SKILL.md) | Adapts lessons and tests for dyslexia, ADHD, autism and processing needs without lowering the bar |
| [**eal-support**](skills/eal-support/SKILL.md) | Vocabulary, visuals and scaffolds for students learning English |
| [**text-leveller**](skills/text-leveller/SKILL.md) | Rewrites a text up or down a reading level, keeping every key fact |
| [**stretch-and-challenge**](skills/stretch-and-challenge/SKILL.md) | Deeper thinking for high attainers, not more of the same |

### Pastoral and behaviour

| Skill | What it does |
|---|---|
| [**behaviour-plan**](skills/behaviour-plan/SKILL.md) | Routines, expectations and responses for a class or a situation |
| [**restorative-conversation**](skills/restorative-conversation/SKILL.md) | A calm, structured conversation after an incident |
| [**mentoring-session-planner**](skills/mentoring-session-planner/SKILL.md) | A one-to-one mentoring session with coaching questions and a target |
| [**form-time-planner**](skills/form-time-planner/SKILL.md) | Purposeful tutor time for a term |
| [**study-skills-coach**](skills/study-skills-coach/SKILL.md) | Teaches students retrieval, spacing, planning and managing phones and distractions |

### Tutoring and progress

| Skill | What it does |
|---|---|
| [**tutoring-session-planner**](skills/tutoring-session-planner/SKILL.md) | A 1:1 or small-group session built from what the tutee got wrong last time |
| [**six-week-review**](skills/six-week-review/SKILL.md) | Compares now with the baseline topic by topic and sets the next three priorities |
| [**revision-timetable-builder**](skills/revision-timetable-builder/SKILL.md) | A realistic, spaced revision plan worked back from exam dates |
| [**intervention-planner**](skills/intervention-planner/SKILL.md) | Short, specific, measured catch-up for a group with the same gap |

### Parents and communication

| Skill | What it does |
|---|---|
| [**parent-message**](skills/parent-message/SKILL.md) | Short, plain-language messages with one clear call to action |
| [**parent-evening-prep**](skills/parent-evening-prep/SKILL.md) | A phone-sized brief per student: a strength, a priority and one home action |
| [**student-report-writer**](skills/student-report-writer/SKILL.md) | Reports that are honest, specific and kind, worded differently for every student |
| [**newsletter-writer**](skills/newsletter-writer/SKILL.md) | A parent newsletter short enough to read on a phone |
| [**difficult-conversation-prep**](skills/difficult-conversation-prep/SKILL.md) | Facts, goal, opening line and likely responses for a hard conversation |

### AI in the classroom

| Skill | What it does |
|---|---|
| [**ai-proof-tasks**](skills/ai-proof-tasks/SKILL.md) | Redesigns homework and coursework so students still learn when AI is available |
| [**ai-literacy-lesson**](skills/ai-literacy-lesson/SKILL.md) | Lessons that teach students to use AI to think more, not less |

### Leadership and CPD

| Skill | What it does |
|---|---|
| [**cpd-session-designer**](skills/cpd-session-designer/SKILL.md) | Training that changes one thing teachers do on Monday, with follow-up |
| [**lesson-observation-feedback**](skills/lesson-observation-feedback/SKILL.md) | Observation notes turned into strengths, one action step and a rehearsal |

### Subject packs

| Skill | What it does |
|---|---|
| [**code-exercise-builder**](skills/code-exercise-builder/SKILL.md) | Predict, run, investigate, modify, make: programming tasks with tests, hints and solutions |
| [**problem-set-builder**](skills/problem-set-builder/SKILL.md) | Maths practice built on variation theory, from fluency to problem solving |
| [**practical-lesson-planner**](skills/practical-lesson-planner/SKILL.md) | Practicals with safety, method, results tables and the exam questions that follow |

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
- **Make young people love AI, not fear it,** and design tasks so the learning still happens in their heads.

## Companion tools

- [pattern-guard](https://github.com/kal-eficia/pattern-guard): the answer-pattern checker as a CLI and library
- [recall-engine](https://github.com/kal-eficia/recall-engine): spaced-retrieval starters from a question bank and attempts log
- [lesson-page-kit](https://github.com/kal-eficia/lesson-page-kit): the student-page engine the lesson-pack skill can write for
- [mark-point-checker](https://github.com/kal-eficia/mark-point-checker): marks short answers against the mark schemes the exam-question skill writes
- [ai-skills-kit](https://github.com/kal-eficia/ai-skills-kit): skills for AI adoption, creators and builders

## Contributing

Teachers: if a skill gets something wrong for your subject, country or age group, open an issue with an example. That's the most useful contribution there is.

New skills are welcome. Each lives in `skills/<name>/SKILL.md`, the `name` in its frontmatter matches the folder, the description says when to use it (under 1,024 characters), and it reads `teaching-context.md` first. `python3 scripts/validate_skills.py` checks all of that, and CI runs it on every push.

---

Written by [Kalid Nur](https://github.com/kal-eficia), who teaches Computer Science, ICT and AI to 11 to 18 year olds and trains schools and teams on adopting AI. MIT licence.
