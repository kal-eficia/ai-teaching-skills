# Example: recall-starter

## The request

> Use recall-starter. Year 10, Cambridge IGCSE Computer Science 0984, live online. Today is the second lesson on the fetch-decode-execute cycle. The last four lessons were: CPU components and registers, buses, and the start of the FDE cycle. Last week's quiz showed they mix up the MAR and MDR. Two's complement (taught three weeks ago) and parity checks (taught a week ago) were weak too. I can see their answers live, so add confidence ratings.

## What the skill produced

### Starter (student-facing)

**From memory. No notes, no searching, no AI. 6 minutes.**

1. Which register holds the address of the memory location being read from or written to?
   A. MDR   B. PC   C. MAR   D. CIR
   *How sure are you? Guessing / Think so / Certain*
2. Write −12 as an 8-bit two's complement binary number.
3. Which bus carries signals in one direction only?
   A. Address bus   B. Data bus   C. Control bus   D. All three
   *How sure are you? Guessing / Think so / Certain*
4. A system uses even parity. Which byte has arrived with an error?
   A. 10110100   B. 01110011   C. 11000011   D. 00000000
   *How sure are you? Guessing / Think so / Certain*
5. During the fetch stage, what happens to the Program Counter?
6. Convert the hexadecimal number 3F to denary.
7. What does the ALU do?
8. Give one reason serial transmission is used over long distances instead of parallel.

### Teacher key

| # | Answer | Topic | Why it's here |
|---|---|---|---|
| 1 | C (MAR) | 3.1 Registers | Got wrong last week. Confident-wrong answers here are the priority |
| 2 | 11110100 | 1.1 Two's complement | Taught 3 weeks ago and weak. Due a check |
| 3 | A (Address bus) | 3.1 Buses | Last lesson, keeps the thread |
| 4 | B (five 1s, so odd) | 2.2 Parity | Taught 7 days ago and weak |
| 5 | Its address is copied to the MAR, then it is incremented by 1 | 3.1 FDE | Last lesson, and today builds on it |
| 6 | 63 | 1.1 Hexadecimal | 30-day check |
| 7 | Carries out arithmetic and logic operations | 3.1 CPU components | 3-day check |
| 8 | Bits can't arrive out of sync (no skew); fewer wires, so cheaper | 2.1 Serial vs parallel | Not asked in a starter yet |

MCQ key: C, A, B. Checked with `check_key.py`: clean. No two neighbouring questions share a topic.

## Why it's useful

- Built from what this class got wrong, not a random topic list.
- Spaced at 3, 7, 21 and 30 days, and interleaved across three units.
- Confidence ratings show who is confident and wrong (the MAR/MDR mix-up) so the teacher can deal with it first.
