# Do the skills make Claude better at teaching work?

Tested on 25 November 2026. Short answer: yes, on these tasks, by a clear margin.

| | With the skill | Without |
|---|---|---|
| Criteria met (blind graded) | **96.4%** | 81.2% |
| Graders' preferred answer (48 judgements) | **44** | 4 |
| Checks done by code passed (5 tasks) | **5 of 5** | 1 of 5 |
| Tasks where it scored higher | **21** | 1 (2 level) |

Browse the results at [kal-eficia.github.io/ai-teaching-skills/results.html](https://kal-eficia.github.io/ai-teaching-skills/results.html). Every answer from both arms is in [outputs/](outputs/).

## How it was tested

1. **24 tasks** a real teacher might send, one per skill, across computing, maths, science, English, history, geography, French, pastoral and leadership ([cases.json](cases.json)). Each task has six criteria written before any answer was produced.
2. **Two answers per task**, each from a separate Claude Sonnet agent that saw only that task. One was told to read the skill first. The other was told to answer from its own knowledge. Neither could ask questions.
3. **Blind grading.** The two answers were labelled X and Y at random. Two independent Claude Opus graders per task scored each criterion 0, 1 or 2 without knowing which answer used the skill, reading the pair in opposite orders, and said which they would rather be handed.
4. **Checks by code** where a criterion can be measured: answer keys for guessable patterns, report batches for repeated wording and length, message length, and reading age.

Run it yourself: `python3 evals/prepare.py WORKDIR`, run each prompt in `WORKDIR/prompts/` and each `grader_*.md` with an agent, then `python3 evals/score.py WORKDIR`.

## What stood out

- **Answer patterns.** Without the skill, the 12-question quiz and the lesson pack both came back with a guessable key. With it, every key was clean.
- **Reports.** Without the skill, the batch failed the wording and length checks. With it, all six passed.
- **Biggest gains:** quiz building, AI-proof tasks, reports, worked examples and programming exercises.
- **Where the skill lost:** the exam question. Its mark scheme rejected "sugar" and wanted "maltose", which is stricter than the foundation specification, and it left out temperature.

## Limits, stated plainly

- **The rubrics were written by the skills' author side.** They describe good practice, but they are not neutral. The graders' overall preference and the code checks are the fairer measures.
- **One run per task.** Model output varies, so single-task differences are indicative, not proof. The overall pattern across 24 tasks is the result.
- **Graders are AI, not teachers.** They can miss classroom realities. A panel of teachers is the next step.
- **Ceiling effect.** Many answers scored 11 or 12 out of 12, so the rubric cannot show how much better the best answers are.
- **Blinding was imperfect at first.** Nine skill-arm answers named the skill ("checked with the no-answer-patterns script"). Those phrases were made neutral in the copies the graders saw. The published outputs are the originals.
- **The baseline may have been helped.** Both arms ran inside the author's workspace, which carries his house style. That would shrink the gap, not grow it.
- **Sonnet only.** Other models may differ.

## What changed because of this, and the re-test

Eight skills were tightened after reading the graders' notes. Each was then re-tested the same day: fresh answers from both arms, new random labels, two new blind graders. Scores are skill v plain, out of 12.

| Skill | First run | Re-test | Graders preferred skill |
|---|---|---|---|
| exam-question-writer | 11 v 12 | 12 v 10.5 | 2 of 2 |
| parent-message | 10.5 v 9 | 11 v 9 | 2 of 2 |
| explanation-crafter | 11 v 10 | 12 v 9.5 | 2 of 2 |
| whole-class-feedback | 11.5 v 10 | 11.5 v 12 | 1 of 2 |
| homework-designer | 11.5 v 11 | 12 v 9.5 | 2 of 2 |
| tutoring-session-planner | 9.5 v 7.5 | 12 v 8 | 2 of 2 |
| knowledge-organiser | 11 v 9.5 | 12 v 9.5 | 2 of 2 |
| scheme-of-work-builder | 11 v 10 | 12 v 8.5 | 2 of 2 |

Across the re-test: 98.4% of criteria met with the skill against 79.7% without, and 15 of 16 blind judgements for the skill answer. The exam-question skill, the one loss in the first run, now wins. whole-class-feedback is the one that came out level or just behind: its model paragraph used a quotation it wasn't sure of.

The same limits apply, and a re-test is still one run per task. Answers are in [retest-outputs/](retest-outputs/) and grading files in [retest-grades/](retest-grades/). In the re-test, both arms were told not to mention any files or rules, so no answers needed editing before grading.
