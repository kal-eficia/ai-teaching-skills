---
description: Check a quiz or sort task for answer patterns students can guess, and fix them
argument-hint: <path to a quiz file, or paste the quiz or the key>
---

Check this for answer patterns: $ARGUMENTS

- If I gave a bare key (letters), call `check_answer_key` with it.
- If I gave a JSON file, call `check_answer_key` with `quiz_path`. If it finds a pattern, call `fix_answer_key` with `write: true` and check again.
- If I pasted a quiz as text, turn it into `{q, options, answer}` questions, call `fix_answer_key`, and give me the quiz back in my original layout with the options reordered. Never change the wording.

Show the key before and after, and say plainly whether it is now clean.
