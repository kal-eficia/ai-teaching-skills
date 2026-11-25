# Year 8 Computing: Python Programming Basics
**Half-term scheme of work: 6 weeks, 2 x 50-minute lessons per week (12 lessons)**

## Assumptions
- Pupils have used Scratch in Year 7 (sequences, loops, selection, variables, events) but have never typed code.
- Each pupil has a computer with Python 3 and a simple editor (IDLE, Thonny or Mu). Thonny is recommended because it shows variables and has a gentle debugger. A browser-based option (Trinket, Replit) works as a fallback.
- Mixed ability. Each lesson has a core task, a "stretch" extension and a support option.
- The assessment is in Week 6, Lesson 12: a 50-minute practical plus short written section. Lesson 11 is revision and a practice paper.
- Pupils do not need to type fast. Typing accuracy, case sensitivity and indentation are taught explicitly.

## Overall aims
By the end of the half-term, pupils can:
1. Write and run short Python programs in a text editor.
2. Use variables, data types, input and output.
3. Use arithmetic and string operations.
4. Use selection (`if / elif / else`) with comparison and logical operators.
5. Use iteration (`for` and `while`).
6. Read error messages, debug, and test their programs.
7. Link each idea back to its Scratch equivalent.

## Bridge from Scratch to Python
Use this table throughout. Put it on the wall and in pupils' books.

| Scratch | Python |
|---|---|
| say [Hello] | `print("Hello")` |
| ask [] and wait / answer | `name = input("...")` |
| set [score] to 0 | `score = 0` |
| if / else | `if ... :` / `else:` |
| repeat 10 | `for i in range(10):` |
| forever / repeat until | `while ...:` |
| join | `+` (concatenation) |

## Week-by-week overview

| Week | Lesson | Topic |
|---|---|---|
| 1 | 1 | Meeting Python: from blocks to text |
| 1 | 2 | Variables and data types |
| 2 | 3 | Input and building programs |
| 2 | 4 | Arithmetic and strings |
| 3 | 5 | Selection 1: `if` and `else` |
| 3 | 6 | Selection 2: `elif`, `and`, `or` |
| 4 | 7 | Iteration 1: `for` loops |
| 4 | 8 | Iteration 2: `while` loops |
| 5 | 9 | Debugging and testing |
| 5 | 10 | Mini-project: putting it all together |
| 6 | 11 | Revision and practice assessment |
| 6 | 12 | Assessment |

## Lesson-by-lesson plan

Each lesson follows the same rhythm so pupils feel safe: **Starter (5-8 min) / Teach and model (10-12 min) / Guided practice (10-15 min) / Independent task (15 min) / Plenary (5 min).**

### Week 1

**Lesson 1: Meeting Python**
- *Objectives:* Explain the difference between block-based and text-based languages. Write, save and run a first program using `print()`.
- *Starter:* Show a three-block Scratch script and the equivalent Python. Ask: what is the same, what is different?
- *Teach:* Open the editor, type `print("Hello, world")`, run it. Cover: what an editor and interpreter are, why spelling, brackets and quote marks matter, and what a syntax error looks like. Teacher live-codes and deliberately makes one typo.
- *Practice:* Print a name, a favourite food and a joke on separate lines. Introduce `#` comments.
- *Independent:* "Typing accuracy challenge": copy a short program exactly, then fix a version containing 5 planted errors (missing quote, `Print` with a capital, missing bracket).
- *Plenary:* Exit ticket: "Name two things that Python is strict about."
- *Stretch:* Use `\n` and `print("a", "b", sep="-")`. *Support:* Provide a printed code card with fill-in-the-blank lines.

**Lesson 2: Variables and data types**
- *Objectives:* Create variables, name them sensibly, and recognise `str`, `int`, `float` and `bool`.
- *Starter:* "Variables as labelled boxes": link to Scratch "set score to 0".
- *Teach:* `name = "Aisha"`, `age = 13`. Print variables, change a variable, and print more than one. Introduce `type()`. Naming rules (no spaces, can't start with a number, be descriptive).
- *Practice:* Predict-then-run: pupils write what a short program will output before running it.
- *Independent:* Build a "Character card" that stores and prints name, age, height and whether they like football.
- *Plenary:* Quick quiz: sort five values into the four data types.
- *Stretch:* Swap two variables without losing a value. *Support:* Sentence starters and a partly completed program.

### Week 2

**Lesson 3: Input and building programs**
- *Objectives:* Use `input()` to get data from a user and store it.
- *Starter:* Scratch "ask and wait" next to Python `input()`.
- *Teach:* `name = input("What is your name? ")`. Discuss why input is always a string, and introduce `int()` and `float()`.
- *Practice:* Write a greeting program, then an "age in 10 years" program (shows why `int()` is needed).
- *Independent:* "Chatbot v1": asks name, favourite subject and hobby, then replies in full sentences.
- *Plenary:* Spot the bug: `age = input(...)` then `age + 1`. What goes wrong and why?
- *Stretch:* Make the chatbot use at least three stored answers in one sentence.

**Lesson 4: Arithmetic and strings**
- *Objectives:* Use `+ - * / // % **`. Join strings and use simple string functions.
- *Starter:* "Maths with a twist": predict `7 / 2`, `7 // 2`, `7 % 2`.
- *Teach:* Operators, order of operations, `+` for joining text vs adding numbers, `len()`, `.upper()`, `.lower()`. Use f-strings as a clean way to build output (`f"Hello {name}"`).
- *Practice:* Pocket-money calculator and tip calculator.
- *Independent:* "Shop receipt": the user enters price and quantity, and the program prints the total with a message.
- *Plenary:* Mini whiteboard questions on `%` and `//`.
- *Stretch:* Convert minutes into hours and minutes using `//` and `%`.

### Week 3

**Lesson 5: Selection 1: `if` and `else`**
- *Objectives:* Use comparison operators and `if / else` with correct indentation.
- *Starter:* Scratch "if / else" block and a real-world rule ("If it's raining, take an umbrella").
- *Teach:* `==`, `!=`, `<`, `>`, `<=`, `>=`. The colon, and why indentation is a part of the code. Warn about `=` versus `==`.
- *Practice:* Age checker ("Are you old enough?") and password check.
- *Independent:* "Guess my number" (a fixed secret number): tell the user whether they were right.
- *Plenary:* Indentation hunt: find the error in three printed snippets.
- *Stretch:* Add a different message depending on how close the guess is.

**Lesson 6: Selection 2: `elif`, `and`, `or`**
- *Objectives:* Build multi-branch decisions and combine conditions.
- *Starter:* Flowchart-to-code matching (cards).
- *Teach:* `elif` chains, `and`, `or`, `not`. Trace through a grade-boundary program with different inputs.
- *Practice:* Grade calculator (score to grade) and a rollercoaster entry checker (height and age).
- *Independent:* "Text adventure fork": a two-level decision story with at least three endings.
- *Plenary:* Trace table on the board: what will print if `x = 15`?
- *Stretch:* Handle invalid input with a final `else`.

### Week 4

**Lesson 7: Iteration 1: `for` loops**
- *Objectives:* Use `for` and `range()` to repeat code a set number of times.
- *Starter:* Scratch "repeat 10" and its Python equivalent.
- *Teach:* `for i in range(5):`, using the loop variable, `range(start, stop, step)`. Indentation shows what is inside the loop.
- *Practice:* Print a times table, count down from 10, and print a row of stars.
- *Independent:* "Times table trainer": the user picks a number and the program prints its full table.
- *Plenary:* Predict the output of three loops with different `range()` values.
- *Stretch:* Add up the numbers 1 to 100 using a running total.

**Lesson 8: Iteration 2: `while` loops**
- *Objectives:* Use `while` loops for repetition that depends on a condition, and avoid infinite loops.
- *Starter:* "Repeat until" in Scratch. When would you use it instead of "repeat 10"?
- *Teach:* `while` syntax, loop conditions, updating the variable, and what to do if a program hangs (Ctrl+C or the stop button). Compare `for` and `while`.
- *Practice:* Password retry program, and a "keep asking until positive number" validator.
- *Independent:* "Guess my number v2": the user keeps guessing until correct, and the program counts the attempts.
- *Plenary:* Decide: `for` or `while`? Five quick scenarios.
- *Stretch:* Limit to 5 guesses using `and` in the condition.

### Week 5

**Lesson 9: Debugging and testing**
- *Objectives:* Identify syntax, runtime and logic errors. Test with normal, boundary and erroneous data.
- *Starter:* "Spot the bug" gallery of six short broken programs.
- *Teach:* Three error types, how to read a traceback (look at the last line and the line number), testing strategy, and simple test tables.
- *Practice:* Pupils fix a bank of broken programs (one error per program, increasing difficulty).
- *Independent:* Write a test table for their grade calculator from Lesson 6 and fix any bugs found.
- *Plenary:* "Bug bounty": pairs swap programs and try to break each other's.
- *Stretch:* Predict which of two programs has a logic error without running them.

**Lesson 10: Mini-project**
- *Objectives:* Plan, build, test and evaluate a small program using several concepts.
- *Starter:* Show a finished example, with a checklist of what it uses (input, variables, selection, loop).
- *Task:* Choose one project: quiz game (5 questions with score), number guessing game with hints, simple calculator menu, or "Choose your own adventure". Success criteria: uses input, a variable, selection and a loop, and has comments.
- *Teach:* A short planning step first (write in plain English or pseudocode before typing).
- *Plenary:* Peer feedback using "two stars and a wish".
- *Stretch:* Add a high-score feature or input validation. *Support:* Project starter templates with gaps.

### Week 6

**Lesson 11: Revision and practice assessment**
- Starter: retrieval quiz covering each topic (low-stakes, whole class).
- Stations or rotating tasks: trace tables, predict the output, fix the bug, complete the code.
- Pupils complete a 20-minute practice paper, then self- and peer-mark using a mark scheme. Identify one personal target.
- Plenary: "I can" checklist against the assessment objectives.

**Lesson 12: Assessment** (see below)

## Assessment (Lesson 12)

**Format (50 minutes, individual, no internet).**
- **Section A: Written, 15 minutes, 15 marks.** Data types, predict the output, spot the error, trace a loop, `for` versus `while`.
- **Section B: Practical, 35 minutes, 25 marks.** Pupils complete a short programming task set in stages.

**Example practical task: "Ticket machine".**
1. Ask the user for their name and age; print a greeting. (variables, input, output: 5 marks)
2. Decide the ticket price by age band using `if / elif / else`. (selection: 6 marks)
3. Ask how many tickets they want, using a loop to ensure the number is between 1 and 10. (iteration and validation: 6 marks)
4. Calculate and print the total cost. (arithmetic, formatted output: 4 marks)
5. Add comments and use meaningful variable names. (good practice: 4 marks)

**Grading bands (adjust to your school's system):** Working towards / Secure / Mastering.

**Assessment objectives:**
- Understand and use variables, data types, input and output.
- Use selection and iteration correctly.
- Detect and correct errors.
- Write readable, commented code.

**Differentiation for the assessment:** Support pupils receive a partially completed starter file and a syntax reference sheet. Stretch pupils get an optional bonus step (e.g. a loop that lets another customer buy tickets).

## Teaching approach and tips
- **Live coding:** Narrate your thinking and make errors deliberately. It normalises mistakes.
- **Pair programming (driver and navigator):** Swap roles every 10 minutes. This helps first-time typers.
- **Parson's problems:** Give mixed-up lines of code to reorder, a bridge between dragging blocks and typing.
- **Error messages are friends:** Create a class "error dictionary" of common messages and their causes.
- **Keep a reference sheet:** One page of syntax for every pupil, to cut anxiety about remembering.
- **Low-stakes retrieval:** Open every lesson from Week 2 with 3 questions from earlier lessons.
- **Formative checks:** Mini whiteboards for predictions, and a "red, amber, green" cup or card on the desk during practice.
- **Common misconceptions to address:** `=` versus `==`; `input()` always returns text; indentation changes meaning; Python is case sensitive; a loop variable is not a counter you must declare separately.

## Resources needed
- Thonny (or alternative) installed, and student login access.
- Python-to-Scratch bridge poster.
- Syntax reference sheet and printed code cards (Lessons 1, 6, 9).
- Broken-code bank for Lesson 9.
- Mini-project template files and assessment paper with a mark scheme.

## Homework (optional, short, one per week)
1. Re-type and annotate a program (typing practice).
2. Write down five real-life examples of data and its type.
3. Pseudocode a decision from daily life.
4. Predict-the-output sheet with loops.
5. Plan the mini-project on paper.
6. Revision flashcards.
