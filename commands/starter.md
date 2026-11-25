---
description: Build today's retrieval starter, from your question bank and attempts log if you keep them
argument-hint: [student id or class] [bank.csv] [attempts.csv]
---

Build a retrieval starter. $ARGUMENTS

- Look for a question bank (`bank.csv` or `bank.json`) and an attempts log (`attempts.csv`) in this folder or the paths I gave. If they exist, call `recall_starter` (one call per student if I named several) and present each starter with a teacher key that says why each question was chosen.
- If there is no bank, follow the `recall-starter` skill: ask what the last four lessons covered and what the class found hard, then write the starter. Offer to save the questions as `bank.csv` so the next starter can be chosen automatically.
- Any multiple-choice questions must pass `check_answer_key`.
- After the lesson, if I give you the results, call `log_attempts` to record them.
