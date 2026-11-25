# Example: no-answer-patterns

## The request

> Use no-answer-patterns. Here's a 6-question CPU quiz I wrote quickly. Check it and fix it. ([cpu-quiz.json](files/cpu-quiz.json))

## What the skill did

**1. Checked the key with the bundled script**

```
$ python3 scripts/check_key.py cpu-quiz.json
MCQ  ABCDAB  PATTERN
  x staircase   Q1-Q4         key climbs in order: A B C D
```

The first four answers go A, B, C, D. Students who spot that get Q5 and Q6 free.

**2. Fixed it**

```
$ python3 scripts/check_key.py cpu-quiz.json --fix --seed 7
$ python3 scripts/check_key.py cpu-quiz.json
MCQ  DBCACD  clean
```

| Q | Before | After |
|---|---|---|
| 1 ALU | **A** | **D** |
| 2 Program Counter | **B** | **B** |
| 3 One-directional bus | **C** | **C** ("All of them" stays last) |
| 4 Cache | **D** | **A** |
| 5 Embedded system | **A** | **C** |
| 6 MAC address | **B** | **D** |

Question wording didn't change, every answer is still correct, and "All of them" stayed as the last option. Result: [cpu-quiz.fixed.json](files/cpu-quiz.fixed.json).

## Found in testing

The first version of the fixer moved "All of them" into the middle of the options, which the skill itself says not to do. The fixer now keeps options like "All of the above", "None of these" and "A and B" in place, and if one of them is the correct answer, that question keeps its slot and the rest of the key is planned around it. This is covered by tests in [pattern-guard](https://github.com/kal-eficia/pattern-guard).
