# Year 8 Computing: Python Programming Basics (half-term scheme of work)

## Assumptions
- 6 weeks, 2 x 50-minute lessons per week = 12 lessons. No dates given, so weeks are numbered. Add real dates and check them against your school calendar and any INSET or bank holidays.
- Curriculum reference: England KS3 National Curriculum, Computing. Codes used below:
  - **NC-A**: design, use and evaluate computational abstractions that model the behaviour of problems.
  - **NC-B**: use two or more programming languages, at least one textual, to solve problems; use logical reasoning, sequence, selection and repetition, variables and input/output.
  - **NC-C**: understand simple Boolean logic (AND, OR, NOT).
  - **NC-D**: make appropriate use of data structures (lists); detect and correct errors (debugging).
- Students know sequence, loops, selection and variables conceptually from Scratch, but have never typed code. Expect slow, error-prone typing, so every lesson has a debugging element and the early lessons include typing practice.
- Each student has a computer with a Python editor (assumed: Thonny, IDLE or a browser editor such as Trinket or Replit). Use a browser editor if you want zero install and homework access.
- Class of about 20 to 30, mixed ability. Each lesson has a core task and a stretch task.
- Lesson shape throughout: 5 to 8 min retrieval starter, 10 to 15 min teach and model (live code), 20 to 25 min practice (Use, Modify, Create), 5 min plenary or exit ticket.
- Scratch links used in teaching: Scratch "say" is `print`, "ask and wait" is `input`, "set variable" is `=`, "if/else" is `if/else`, "repeat" is `for`, "forever/repeat until" is `while`. Put this table on a slide and refer back to it.

## Dependency chain
print and running code -> variables and types -> input and casting -> arithmetic -> comparisons and if/else -> elif and Boolean operators -> for loops -> while loops -> lists -> combined mini project -> assessment.
Nothing is used before it is taught. Lists come last because looping over a list needs both loops and indexing.

## Scheme of work

| Wk | Lesson | Objective (spec ref) | Starter draws from | Main task type | Check | Resources |
|---|---|---|---|---|---|---|
| 1 | **1. Hello, Python** | Run a Python program, use `print()`, identify and fix syntax errors (NC-B, NC-D) | Scratch recall: name 3 Scratch blocks and what they do (Y7) | Typing and modelling: type, run and tweak 5 short programs; "spot the typo" debugging cards. **Baseline quiz (10 questions)** held for the six-week review | Baseline quiz (not graded) | Editor set up, Scratch-to-Python table, typo cards, baseline quiz |
| 1 | **2. Variables and data types** | Store values in variables; know str, int, float; choose sensible variable names (NC-B) | L1: print, syntax errors | Use/Modify/Create: Mad Libs story generator using variables and `print` (creative) | Exit ticket: what type is `"7"`, `7`, `7.0`? | Mad Libs starter code, data types mini-poster template |
| 2 | **3. Input and casting** | Use `input()`; convert with `int()` and `float()`; explain why `"5" + "5"` gives `55` (NC-B) | L2 (1 back): types; L1 (2 back): print | Build "Name and age" greeting bot; fix the broken calculator that joins numbers instead of adding | Mini-quiz of 5 questions, marked in lesson | Broken-code worksheet, TypeError error-message cheat sheet |
| 2 | **4. Arithmetic and operators** | Use `+ - * / // % **`, and brackets; apply BIDMAS in code (NC-B, NC-A) | L3 (1 back): casting; L2 (2 back): variables; L1 (3 back): print | Practical: tip calculator, change-maker (uses `//` and `%`), area and perimeter program | **Check 1** (written, 15 min): print, variables, types, input, operators | Check 1 paper, operator reference sheet |
| 3 | **5. Selection: if and else** | Use comparison operators and `if/else`; understand indentation (NC-B) | L4 (1 back): operators; L3 (2 back): casting; L1 (4 back): syntax errors | Convert a Scratch if/else to Python; build "Guess the number" and age-check programs (creative) | Exit ticket: predict the output of 3 `if` snippets | Scratch-to-Python side-by-side slide, indentation error cards |
| 3 | **6. elif, and, or, not** | Use `elif`; combine conditions with `and`, `or`, `not`; trace a program with a trace table (NC-B, NC-C, NC-A) | L5 (1 back): if/else; L4 (2 back): operators; L2 (4 back): variables | Build a quiz game with scoring OR a grade calculator using `elif`; trace-table practice | Hinge question on `and` vs `or` | Boolean truth-table mat, trace-table template |
| 4 | **7. FLEX: consolidate selection and debugging** | Fix gaps from Checks and from L5 and L6; find and fix logic errors (NC-D) | L1 to L6 (mixed retrieval grid: one question from each lesson, 1, 3 and 6 lessons back) | Reteach by misconception (use Check 1 results); "Debug the bug" station tasks at three levels; extension: add a feature to the quiz game | **Check 2** (short written, 15 min): selection and Booleans | Marked Check 1 scripts, debug task cards, Check 2 paper |
| 4 | **8. Iteration: for loops** | Use `for` with `range()`; explain what a counted loop does; combine with selection (NC-B) | L6 (1 back): elif/Booleans; L4 (3 back): operators; L1 (6+ back): print | Times-table printer; countdown timer; pattern-printer (text shapes) (creative); stretch: FizzBuzz | Exit ticket: how many times does `range(5)` run? | Range reference slide, FizzBuzz stretch card |
| 5 | **9. Iteration: while loops** | Use `while` with a condition; avoid infinite loops; choose `for` vs `while` (NC-B, NC-A) | L8 (1 back): for loops; L5 (4 back): if/else; L2 (7 back): types | Password-checker (repeat until correct); guessing game with "higher/lower" and attempt counter | Mini-quiz of 5 questions: for or while? | Infinite loop "emergency stop" slide (Ctrl+C or stop button) |
| 5 | **10. Lists** | Create, index and append to lists; loop through a list; `len()` (NC-D) | L9 (1 back): while; L8 (2 back): for; L3 (7 back): input and casting | Shopping-list or "favourite things" builder using `append` and a loop; "random name picker" (creative); stretch: find the highest number in a list | **Check 3** (practical, 15 min) on loops and lists | Index diagram (list as boxes numbered from 0), practical check sheet |
| 6 | **11. Mini project and revision (flex)** | Combine print, input, variables, selection, loops and lists in one program; plan, build, test (NC-A, NC-B, NC-D) | Mixed retrieval grid L1 to L10, with extra weight on content from 6+ lessons ago (L1 to L5) | Creative: text adventure OR quiz game OR budget helper (student choice), with a planning template, then peer testing; gaps from Check 3 reteached to a small group | Peer test using a checklist | Project planner template, testing checklist, revision mat |
| 6 | **12. End-of-unit assessment** | Show independent skill across the unit (NC-A to NC-D) | Light retrieval only (3 questions) before the assessment | Assessment: 20 min written (reading and predicting code, spotting errors, one trace table) plus 25 min practical (write a program from a spec). Includes **repeated baseline questions** for the six-week review | **Summative assessment** | Assessment paper, mark scheme, practical spec, grade boundaries |

Flex lessons: L7 and L11 (2 in 12, meeting "one in every six"). If you lose a lesson to absence or an event, merge L11 into L12's revision and drop the project to a shorter version.

## Retrieval map (what each starter pulls from)
Covered in the table above. Each topic is retrieved at least twice. A quick check: `print` (L1) is retrieved in L2, L4 and L8. Variables (L2) are retrieved in L3, L4, L6 and L9. Selection (L5/L6) is retrieved in L7, L9 and L11.

## Assessment calendar

| When | What | Purpose |
|---|---|---|
| Wk 1, L1 | Baseline quiz (10 questions, ungraded) | Starting point; kept for six-week comparison |
| Wk 2, L4 | Check 1 (written, 15 min) | Catch early misconceptions before selection |
| Wk 4, L7 | Check 2 (written, 15 min) | Selection and Booleans, informs the flex lesson |
| Wk 5, L10 | Check 3 (practical, 15 min) | Loops and lists |
| Wk 6, L12 | End-of-unit assessment (45 min) | Summative; repeat of baseline questions gives the six-week review |
| Following half-term | Return and go over assessment (first lesson back) | Feedback, then move to the next unit |

## Key vocabulary by unit
- **Getting started (L1 to L2):** program, code, syntax, error, run, output, print, string, integer (int), float, variable, assign, data type.
- **Input and operators (L3 to L4):** input, cast/convert, operator, concatenate, modulus, integer division, BIDMAS.
- **Selection (L5 to L6):** condition, comparison, selection, if, elif, else, indentation, Boolean, AND, OR, NOT, trace table.
- **Iteration (L8 to L9):** iteration, loop, for, while, range, counter, infinite loop.
- **Lists (L10):** list, element, index, append, length, `len`.
- **Project (L11 to L12):** decomposition, test, debug, logic error, syntax error, runtime error.

## Common misconceptions by unit
Pass these to the `misconception-finder` skill if you use it.
- **L1 to L2:** Python ignores capital letters (it does not: `Print` fails); `=` means "equals" like in maths rather than "assign"; quotes are optional around text; a variable name with a space works; a variable "remembers" its old value after being reassigned.
- **L3:** `input()` returns a number if the user types a number (it always returns text); `"5" + "5"` gives 10.
- **L4:** `/` and `//` are the same; `%` means percent; Python does the sum left to right, ignoring BIDMAS; `^` means power (it is `**`).
- **L5 to L6:** `=` and `==` are interchangeable; `if x == 5 or 6` means "x is 5 or 6" (it does not); `elif` and a second `if` behave the same; indentation is just for looks; `and` is the same as `or` in everyday speech.
- **L8:** `range(5)` goes 1 to 5 (it goes 0 to 4); the loop variable must be named `i`; the loop body runs once.
- **L9:** `while` loops always run at least once; changing the condition variable inside the loop is optional; "it crashed" when the program is in an infinite loop.
- **L10:** list indexes start at 1; `append` returns a new list; `len(list)` is the last index (it is one higher).
- **General:** red error text means "I broke the computer"; the program "doesn't work" without reading the error message line number; copying code character by character without thinking about what it does.

## Home heads-up list

| When | What families need to know |
|---|---|
| Before Wk 1 (now) | Students will start typing Python. If they want to practise at home, they can use a free browser editor (give the link); no install or purchase needed. Nothing is compulsory. Give a printable offline version of the starter tasks for any student without a device. |
| Wk 1 | Optional practice task: type and run the five "Hello" programs at home. Login for the browser editor sent home (if you use one). |
| Wk 3 | Heads up: Check 1 results and first look at progress. Practical tasks may include simple text games, so parents may hear "guess the number" at home. |
| Wk 4 | Check 2 is next lesson. Students may be asked to revise using their lesson notes and Python reference sheet. |
| Wk 5 | End-of-unit assessment is in Week 6, Lesson 12. Tell students the date and format (written and practical, no notes except the reference sheet). |
| Wk 6 | Mini project: students may want to keep working on their text adventure or quiz at home. Fine to share, but the assessment is individual and in class. |

## Final check against the SKILL checklist
- [x] Every KS3 point in range (sequence, selection, repetition, variables, input/output, lists, debugging, Boolean) is taught once and retrieved at least twice.
- [x] No lesson depends on something taught later.
- [x] Creative (Mad Libs, quiz game, patterns, project) and exam-style (checks, trace tables, assessment) lessons both appear every fortnight.
- [x] Flex lessons exist: L7 and L11.
- [ ] Dates: not checked, because no calendar was supplied. Please add real dates and holidays.
