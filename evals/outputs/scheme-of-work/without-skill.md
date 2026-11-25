# Year 8 Computing: Python Programming Basics (half-term scheme of work)

**6 weeks, 12 lessons, 50 minutes each. Assessment in Week 6.**

## Assumptions

- Pupils know Scratch (sequence, loops, selection, variables, events) but have never typed code.
- Each pupil has a computer. Thonny is the suggested editor (simple, free, built-in debugger). Any browser-based Python editor also works.
- Lesson 12 is the assessment. Lesson 11 is revision and a low-stakes practice task. If your Week 6 has one lesson lost to events, drop Lesson 10 extension work first.
- Mixed ability. Every lesson has a core task, a "challenge" task and a support option.
- Pupils work in pairs for the first half of the unit (driver/navigator), then more independently.

## Unit aims

By the end, pupils can:
1. Write, run and debug short Python programs typed from scratch.
2. Use variables, data types, input and output.
3. Use arithmetic and string operations.
4. Use selection (`if`/`elif`/`else`) with comparison and logical operators.
5. Use iteration (`for`, `while`).
6. Explain how Python concepts link to what they did in Scratch.
7. Read error messages and fix syntax, logic and runtime errors.

## Teaching approach (applies to every lesson)

- **Typing, not copying and pasting.** Pupils have never typed code, so expect slow typing, missed colons, wrong indentation and wrong capitalisation. Build in time for it and praise error-fixing rather than "getting it right first time".
- **Predict, Run, Investigate, Modify, Make.** Pupils predict the output, run it, change one thing, then create their own version.
- **Scratch bridge.** Show the Scratch block next to the Python line in early lessons, then fade it out.
- **Starters** (5 min) are retrieval quizzes on the previous lesson. **Plenaries** (5 min) are exit tickets: a single question, or "write one line that does X".
- **Common errors wall:** keep a running class list of error messages and what they mean.
- **Support:** partially completed code with gaps, Parsons-style problems (reorder jumbled lines), pair work. **Challenge:** open-ended extension tasks and "break my program" tasks for a partner.

## Overview

| Week | Lesson | Topic |
|---|---|---|
| 1 | 1 | From Scratch to text: first Python programs, `print` |
| 1 | 2 | Variables and data types |
| 2 | 3 | Input and string handling |
| 2 | 4 | Arithmetic and converting types |
| 3 | 5 | Errors and debugging |
| 3 | 6 | Selection 1: `if` and `else` |
| 4 | 7 | Selection 2: `elif` and logical operators |
| 4 | 8 | Iteration 1: `for` loops |
| 5 | 9 | Iteration 2: `while` loops |
| 5 | 10 | Putting it together: mini project |
| 6 | 11 | Revision and practice assessment |
| 6 | 12 | Assessment |

---

## Week 1

### Lesson 1: From Scratch to text

**Objectives:** Explain the difference between block-based and text-based languages. Write and run a program using `print()`. Recognise that computers need exact instructions.

- **Starter (5):** Show a Scratch script "say Hello for 2 seconds" and ask pupils how they would tell a computer to do this using only typed words.
- **Teach (10):** Teacher live-codes `print("Hello")` in Thonny. Introduce the editor, Run button, shell/output. Show Scratch block vs Python line side by side. Model typing carefully: brackets, quote marks, lowercase.
- **Main (25):**
  1. Type and run three given `print` lines (predict first).
  2. Deliberately break a line (remove a quote, capitalise `Print`) and record the error message.
  3. Make: a program that prints a 4-line "about me" or a simple ASCII picture.
  4. Challenge: use `\n` and `*` (`"-" * 20`) to format the output.
- **Plenary (5):** Exit ticket: "Write the line that prints your name. What two characters must surround the text?"
- **Key vocabulary:** program, code, syntax, output, string, editor, run.
- **Assessment for learning:** Can they type, save and run a file? Collect a screenshot or saved file named `lesson1.py`.

### Lesson 2: Variables and data types

**Objectives:** Create and use variables. Name three data types: string, integer, float. Choose sensible variable names.

- **Starter (5):** Quiz: what does `print` do? What must go around text? Then: "In Scratch, what is a variable block?"
- **Teach (10):** Variables as labelled boxes. `name = "Sam"`, `age = 13`. Show `print(name)` vs `print("name")`. Introduce `type()` and the three types plus Boolean (briefly). Link to Scratch "set [score] to 0".
- **Main (25):**
  1. Predict-and-run: short snippets that reassign variables (`score = score + 1`).
  2. Sort cards: value to data type (`"7"`, `7`, `7.0`, `True`).
  3. Make: a "character profile" program that stores name, age, height and favourite game in variables and prints a sentence about them using commas in `print`.
  4. Challenge: swap the values of two variables.
- **Plenary (5):** Mini whiteboards: "What type is `3.5`? Which of `my score`, `my_score`, `2score` are valid names?"
- **Key vocabulary:** variable, assign, integer, float, string, Boolean, identifier.

---

## Week 2

### Lesson 3: Input and string handling

**Objectives:** Use `input()` to get data from the user. Join strings (concatenation). Use `len()` and simple string methods.

- **Starter (5):** Retrieval: write a line that stores your age in a variable. What type is it?
- **Teach (10):** `name = input("What is your name? ")`. Compare to Scratch "ask and wait / answer". Concatenation with `+` and with commas. `len()`, `.upper()`, `.lower()`.
- **Main (25):**
  1. Guided: greeting program asking for name and favourite food.
  2. Investigate: what does `len(name)` return? What does `name.upper()` do?
  3. Make: a "mad libs" story generator that asks for 4 words and prints a story.
  4. Challenge: print the first letter and last letter of a word using indexing (`word[0]`, `word[-1]`).
- **Plenary (5):** "Write one line that asks for the user's town and stores it."
- **Key vocabulary:** input, prompt, concatenate, index, method.

### Lesson 4: Arithmetic and converting types

**Objectives:** Use arithmetic operators (`+ - * / // % **`). Convert between types using `int()`, `float()`, `str()`. Understand why `input()` returns a string.

- **Starter (5):** Quick quiz on lesson 3 plus "What is `"5" + "5"`?" (leads into the problem).
- **Teach (10):** Operators table. Demonstrate the classic bug: `age = input(...)`, then `age + 1` fails. Introduce `int()`. Explain `//` and `%` with a sharing-sweets story.
- **Main (25):**
  1. Operator investigation table: predict then run.
  2. Make a calculator that asks for two numbers and prints sum, difference, product.
  3. Make: a "pocket money" or "pizza party" program (cost per head, total, change).
  4. Challenge: a program that converts minutes into hours and minutes using `//` and `%`.
- **Plenary (5):** Exit ticket: "Why does `input("Age")` need `int()` before you add 1 to it?"
- **Key vocabulary:** operator, integer division, modulus, type conversion (casting).

---

## Week 3

### Lesson 5: Errors and debugging

**Objectives:** Identify syntax, runtime and logic errors. Read an error message and locate the line. Use a systematic approach to fix bugs.

- **Starter (5):** Show a program with one obvious error. "What do you think went wrong?"
- **Teach (10):** Three error types with examples (missing bracket, dividing by zero or converting text to int, wrong operator giving wrong answer). Introduce Thonny's line numbers and the "read the last line first" routine. Add a debugging checklist: read error, go to line, check brackets/quotes/colons/indentation, change one thing at a time.
- **Main (25):**
  1. "Bug hunt": five short broken programs, each with one bug. Pupils fix and classify each error.
  2. Peer swap: each pupil writes a short working program, introduces one bug, and swaps with a partner to fix it.
  3. Challenge: a program with a logic error (no error message, wrong answer) that needs test data to spot.
- **Plenary (5):** Match each error name to a description. Add to the class common errors wall.
- **Key vocabulary:** syntax error, runtime error, logic error, debug, trace, test.
- **Note:** This lesson is deliberately placed before selection so pupils have the skills to cope with indentation errors.

### Lesson 6: Selection 1, `if` and `else`

**Objectives:** Use comparison operators. Write `if` and `if/else` statements with correct indentation.

- **Starter (5):** Scratch recall: show an "if/else" block in Scratch and ask what it does.
- **Teach (10):** Comparison operators (`== != < > <= >=`), with emphasis on `==` versus `=`. Show Scratch if/else next to Python. Teach the colon and indentation. Live-code a password check.
- **Main (25):**
  1. Parsons problem: reorder lines to make a working age-check program.
  2. Make: "Guess my number" with a fixed secret number (higher/lower/correct feedback).
  3. Make: a cinema ticket program (child/adult price by age).
  4. Challenge: an even/odd checker using `%`.
- **Plenary (5):** "What is the difference between `=` and `==`?" Mini whiteboards.
- **Key vocabulary:** selection, condition, comparison operator, indentation, Boolean.

---

## Week 4

### Lesson 7: Selection 2, `elif` and logical operators

**Objectives:** Use `elif` for multiple branches. Combine conditions using `and`, `or`, `not`.

- **Starter (5):** Retrieval quiz on `if/else` (three questions, mixed formats).
- **Teach (10):** Why a chain of `if` statements can misbehave compared with `elif`. Truth table for `and`/`or`/`not` using real-life examples ("it is raining AND I have no umbrella"). Live-code a grade calculator.
- **Main (25):**
  1. Trace table: pupils predict outputs for a set of test values.
  2. Make: grade boundaries program (score to grade 9 to 1, or A to E).
  3. Make: a "theme park ride" checker (height and age conditions using `and`/`or`).
  4. Challenge: a rock-paper-scissors judge for two typed choices.
- **Plenary (5):** Exit ticket: "Write a condition that is true when a number is between 1 and 10 inclusive."
- **Key vocabulary:** elif, logical operator, AND, OR, NOT, test data.

### Lesson 8: Iteration 1, `for` loops

**Objectives:** Explain what iteration is. Use `for i in range()` to repeat code a set number of times.

- **Starter (5):** "Draw a square in Scratch using the fewest blocks." Lead into "repeat 4".
- **Teach (10):** Show 10 identical `print` lines versus a loop. Introduce `range(5)`, `range(1, 6)`, `range(0, 20, 5)`. Explain indentation defines the loop body. Show the loop variable `i` and how to use it.
- **Main (25):**
  1. Predict-run-modify: three loops with different `range` settings.
  2. Make: a times table generator (user picks the number).
  3. Make: a countdown timer that ends with "Blast off!".
  4. Challenge: print a triangle of stars, or total up the numbers 1 to 100.
- **Plenary (5):** "How many times will `for i in range(2, 9):` run?" Mini whiteboards.
- **Key vocabulary:** iteration, loop, range, loop variable, count-controlled.

---

## Week 5

### Lesson 9: Iteration 2, `while` loops

**Objectives:** Use `while` loops for condition-controlled repetition. Avoid infinite loops. Combine loops with selection.

- **Starter (5):** Retrieval: write a `for` loop that prints 1 to 5.
- **Teach (10):** `while` as "repeat until" (Scratch link). Compare with `for` (known number of repeats vs unknown). Demo a password-retry loop and an accidental infinite loop; show how to stop it (Stop button in Thonny).
- **Main (25):**
  1. Guided: "keep asking until the user types `quit`".
  2. Upgrade last week's "Guess my number" so the player keeps guessing until correct, and count the guesses.
  3. Make: a running total (user keeps adding numbers until they enter 0).
  4. Challenge: add a random secret number with `import random` and `random.randint(1, 10)`.
- **Plenary (5):** Sorting task: which scenario needs `for` and which needs `while`?
- **Key vocabulary:** while, condition-controlled, infinite loop, counter, import, random.

### Lesson 10: Putting it together, mini project

**Objectives:** Plan and build a program combining input, variables, selection and iteration. Test and improve it.

- **Starter (5):** Show the project brief and success criteria.
- **Teach (5):** Model planning: write what the program must do in plain English or pseudocode first. Show a short test table.
- **Main (35):** Pupils choose one project:
  - A quiz game with 5 questions and a final score.
  - A text-based adventure with at least 3 choices.
  - A simple shop or café ordering program with a running total.
  - A number guessing game with levels.
  
  Success criteria: uses input, at least 2 variables, `if/elif/else`, at least one loop, comments, tested with at least 3 sets of test data. Teacher circulates and does verbal feedback with 2 stars and a wish per pupil.
- **Plenary (5):** Pupils swap and play each other's programs; write one piece of positive feedback and one suggestion.
- **Key vocabulary:** decomposition, pseudocode, comment, test data.
- **Note:** This is the best formative evidence you will have before the assessment. Use it to decide who needs support in Lesson 11.

---

## Week 6

### Lesson 11: Revision and practice assessment

**Objectives:** Consolidate learning. Identify and address gaps.

- **Starter (10):** Retrieval grid covering all topics (print, variables/types, input, arithmetic, errors, selection, loops).
- **Main (30):**
  1. 15-minute practice paper in the same format as the assessment (mix of short questions and one short coding task). Self-mark or peer-mark with a mark scheme.
  2. Targeted intervention stations based on Lesson 10 and the practice paper: (a) types and input, (b) selection, (c) loops, (d) debugging. Pupils pick or are directed to a station.
- **Plenary (10):** "One thing I will remember, one thing I'll check before the assessment." Share the format, timing and what is allowed in Lesson 12.

### Lesson 12: Assessment

**Format (50 minutes total, suggested):**

- **Part A: Knowledge and reading code (15 min, about 20 marks), on paper or an online form.**
  - Multiple choice and short answer: data types, operators, what a given program outputs, identify error types, spot the difference between `=` and `==`, which loop to use.
  - Trace table for a short loop.
  - Fix a bug in a printed program.
- **Part B: Practical programming (30 min, about 30 marks), on computer, no help from notes or the internet.**
  - Task 1 (core, about 10 marks): input, variable and arithmetic (e.g., a cost calculator).
  - Task 2 (about 10 marks): selection (e.g., a ticket price or grade program).
  - Task 3 (about 10 marks, stretch): use a loop (e.g., repeat until the user enters a valid answer, or a times table).
  - Comments and sensible variable names earn marks.
- **Wrap-up (5 min):** Save and submit, with a quick self-reflection question ("Which task felt easiest? Which would you like more practice on?").

**Suggested mark scheme and grade descriptors (50 marks):**

| Level | Marks | Description |
|---|---|---|
| Working towards | 0 to 17 | Can print, use variables and input with support. Struggles with selection and loops. |
| Secure | 18 to 34 | Writes programs with input, arithmetic and selection. Can trace simple loops and fix some errors. |
| Strong | 35 to 44 | Writes working programs using selection and loops independently. Identifies error types accurately. |
| Mastery | 45 to 50 | Confidently combines all constructs, tests and improves code, explains reasoning. |

Adjust the boundaries to match your school's reporting system.

---

## Resources and preparation

- Thonny installed (or a browser editor) and tested before Lesson 1. Check that pupils can save to the right folder.
- A one-page "Python cheat sheet" given from Lesson 2 and updated each week (print, variables, input, int(), operators, if/elif/else, for, while). Pupils may use it in lessons, but not in the assessment unless you decide otherwise.
- Pre-prepared bug-hunt sheets (Lesson 5), Parsons problems (Lessons 6 and 7), starter quizzes and exit tickets.
- Code-along starter files for any pupil who falls behind. Consider "scaffolded" versions where the structure is given and pupils fill in the blanks.

## Differentiation and inclusion

- **Typing barriers:** allow shorter task versions, pair programming, and reduce the amount of text needed. Provide gapped code for pupils with significant typing or literacy needs.
- **EAL and SEND:** use the Scratch bridge visually, keep a glossary with images, give sentence starters for explaining code, and allow oral explanations for the written parts of the assessment.
- **Stretch:** lists (`my_list = []`), functions (`def`), the `random` module, and turtle graphics for pupils who finish early. Do not introduce these to the whole class this half-term.

## Tracking progress

Record a quick 1 to 4 score per pupil after Lessons 4, 7, 9 and 10 on: writes code independently, uses selection, uses loops, debugs effectively. This gives you a view of progress and informs groupings for Lesson 11.

## Possible next unit

Lists and functions, followed by a larger project (e.g. a text adventure or quiz app), then a link to data handling or turtle graphics.
