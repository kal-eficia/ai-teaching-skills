---
description: First-pass marking of short answers against a mark scheme, with class feedback
argument-hint: <question and mark scheme, then the answers, or paths to them>
---

Mark these answers: $ARGUMENTS

1. Turn the mark scheme into marking points (`id`, `label`, `accept`, and `forbid` for answers that look right but aren't), then call `mark_answers`.
2. Read every answer flagged `teacher_check`, and any answer where the tool's mark looks wrong, and correct the mark with a reason. The tool matches wording; you judge meaning.
3. Give me a table (student, mark, what was missing), then follow the `whole-class-feedback` skill using the most-missed points.
4. List the answers I should look at myself.
