---
description: Build a full lesson pack (teacher plan, interactive student page, homework, mark scheme, solutions) and check it
argument-hint: <year group, course, topic, length, e.g. "Y10 IGCSE CS 0984, the CPU, 50 min, remote">
---

Build a complete lesson pack for: $ARGUMENTS

1. Read `teaching-context.md` if it exists and follow its house rules. Ask only for what is missing and would change the lesson.
2. Follow the `lesson-pack-builder` skill. Use `recall-starter` for the opening and `hinge-question-writer` for the hinge questions.
3. Save the pack in a new folder named after the topic: `teacher-plan.md`, `lesson.json` (lesson-page-kit format), `homework.md`, `mark-scheme.md`, `solutions.md`.
4. Call the `validate_lesson` tool on `lesson.json` and fix every error and every warning about teacher voice.
5. Call `build_lesson_page` to write `student-page.html` in the same folder.
6. Call `check_answer_key` on any multiple-choice set in the homework, and `fix_answer_key` if it finds a pattern.
7. Finish with the folder path, a one-line summary of each file, and anything I should check before teaching it.
