# Year 9 Python: First lesson on while loops

**Assumptions (teacher note, remove before sharing):** Python 3 in Thonny or IDLE, a 50 to 60 minute lesson. Students already use variables, `input()`, `int()`, `if/else` and `for` loops. The set is not tied to an exam board. It follows PRIMM (Predict, Run, Investigate, Modify, Make), with a debugging task and a Parsons problem. There is one short pseudocode item so students see the format before GCSE. You do not need to use everything. The core is Tasks 1 to 5, Task 8 and Task 9. Tasks 6, 7 and 10 are for fast finishers or homework. Part 3 is the solutions sheet, so do not share it.

---

# PART 1: Student pages

## Before you start

A `for` loop repeats a set number of times. A `while` loop repeats **for as long as a condition is True**. You use it when you do not know in advance how many times you will need to repeat.

```python
while condition:
    # indented lines here repeat
    # until the condition becomes False
```

**If your program will not stop:** it is stuck in an infinite loop. Press the red Stop button in Thonny, or Ctrl+C in a terminal. It is not broken forever. Fix the code and run it again.

**Every while loop needs three things:**
1. Something set up **before** the loop (a starting value)
2. A **condition** that is checked every time round
3. Something **inside** the loop that eventually makes the condition False

---

## Task 1: Predict, run, investigate (countdown)

Read this code. **Do not run it yet.**

```python
count = 3
while count > 0:
    print(count)
    count = count - 1
print("Liftoff!")
```

**a)** Write down exactly what you think it prints.

**b)** Now run it. Were you right? If not, what did you miss?

**c)** Answer these:
1. What is the condition?
2. How many times does the line `print(count)` run?
3. What is the value of `count` when the loop stops?
4. Why does "Liftoff!" only appear at the end? What is different about that line?

**d)** Put a `#` at the start of the line `count = count - 1` to turn it off, then run the program. What happens? Stop it with the Stop button. Why did it happen?

---

## Task 2: Predict and trace (adding up)

Read this code. **Do not run it yet.**

```python
total = 0
number = 1
while number <= 4:
    total = total + number
    number = number + 1
print(total)
```

**a)** Complete the trace table. Each row is one time the computer **checks the condition**. Stop when the condition is False.

| Check | number | total | number <= 4 ? |
|---|---|---|---|
| 1 | 1 | 0 | True |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

**b)** What will the program print?

**c)** Run it and check.

---

## Task 3: Predict (a loop that never runs)

```python
lives = 0
while lives > 0:
    print("Still alive")
    lives = lives - 1
print("Game over")
```

**a)** Predict the output. Then run it.

**b)** How many times did the loop body run? Why?

**c)** Change the first line to `lives = 2`. Predict what happens now, then run it.

---

## Task 4: Modify (three small changes)

Start with the countdown code from Task 1. Do each change in a **new copy** of the program.

**4A.** Make it count down from **10** to 1, then print "Liftoff!".

**4B.** Make a new program that counts **up in 2s**: `2, 4, 6, ... , 20`. It must include 20.

**4C.** Start from the adding up program in Task 2. Change it so it adds up all the whole numbers from **1 to 10**. What total do you get?

---

## Task 5: Make (the password gate)

Write a program that asks the user for a password and **keeps asking until they get it right**.

- The correct password is `sunrise`
- If they get it wrong, print `Wrong. Try again.` and ask again
- When they get it right, print `Access granted`

**Example run**

```
Enter the password: moon
Wrong. Try again.
Enter the password: Sunrise
Wrong. Try again.
Enter the password: sunrise
Access granted
```

Test your program with the table in Part 2 when you are finished.

---

## Task 6: Debug (the times table)

This program should print the 5 times table from `1 x 5` to `12 x 5`. It has **three bugs**. Find and fix all of them.

```python
number = 1
while number < 12
    print(number, "x 5 =", number * 5)
number = number + 1
```

**Expected output (first and last lines):**

```
1 x 5 = 5
...
12 x 5 = 60
```

For each bug, write down:
- which line it is on
- what is wrong
- how you fixed it

Tip: fix them one at a time and run the program after each fix.

---

## Task 7: Put the lines in order (Parsons problem)

These lines make a program that asks the user for numbers and **adds them up until they type 0**. The lines are jumbled up and the indentation is missing. Put them in the right order and add the correct indentation.

```
A.  print("Total:", total)
B.  total = total + number
C.  number = int(input("Enter a number (0 to stop): "))
D.  total = 0
E.  while number != 0:
F.  number = int(input("Enter a number (0 to stop): "))
```

Notes:
- Lines C and F look the same, but they have different jobs and go in different places.
- Type it out in Python and test it with `4`, `6`, `10`, `0`. You should get `Total: 20`.

---

## Task 8: Make (guess the number)

Write a game where the computer has a secret number and the player keeps guessing until they get it.

- Set `secret = 7` at the start
- After each wrong guess, print `Too low` or `Too high`
- Count how many guesses the player takes
- When they get it right, print `Correct! It took you X guesses.`

**Example run**

```
Guess the number (1-10): 3
Too low
Try again: 9
Too high
Try again: 7
Correct! It took you 3 guesses.
```

---

## Task 9: Pseudocode check

Pseudocode is a way of writing a program without worrying about exact Python rules. Read this one.

```
total ← 0
WHILE total < 20
    total ← total + 5
ENDWHILE
OUTPUT total
```

**a)** Complete a trace table for `total`.

**b)** What is output?

**c)** Write the same program in Python.

---

## Task 10: Stretch (only accept a sensible answer)

Websites and apps use while loops to check what you type. Write a program that asks for the user's age and **keeps asking until it is between 11 and 16 (including 11 and 16)**.

- If the age is not allowed, print `Not valid.` and ask again
- When it is allowed, print `Thanks`

---

# PART 2: Test cases (students run these)

How to use these: run your program, type the inputs in the order shown, and check the output matches. Tick each row when it passes.

## Task 4 tests

| Task | What to check | Expected output |
|---|---|---|
| 4A | Whole output | `10` down to `1` on separate lines, then `Liftoff!`. The 10 must be there and there must be no `0`. |
| 4B | First and last lines | First line `2`, last line `20`. There are 10 lines. |
| 4C | Final line | `55` |

## Task 5 tests (password gate)

| Type | Inputs, in order | Expected output |
|---|---|---|
| Normal | `moon`, `sunrise` | `Wrong. Try again.` once, then `Access granted` |
| Boundary | `sunrise` | `Access granted` straight away, with no wrong message |
| Normal (several wrong) | `a`, `b`, `c`, `sunrise` | `Wrong. Try again.` three times, then `Access granted` |
| Invalid (wrong case) | `Sunrise`, `SUNRISE`, `sunrise` | `Wrong. Try again.` twice, then `Access granted` |
| Invalid (nothing typed) | press Enter on its own, then `sunrise` | `Wrong. Try again.` once, then `Access granted` |

## Task 6 tests (times table)

| Check | Expected |
|---|---|
| Runs without a syntax error | Yes |
| Program stops by itself | Yes |
| First line | `1 x 5 = 5` |
| Last line | `12 x 5 = 60` |
| Number of lines printed | 12 |

## Task 7 tests (adding numbers)

| Type | Inputs, in order | Expected output |
|---|---|---|
| Normal | `4`, `6`, `10`, `0` | `Total: 20` |
| Boundary | `0` straight away | `Total: 0` |
| Normal (negative number) | `5`, `-2`, `0` | `Total: 3` |

## Task 8 tests (guess the number)

| Type | Inputs, in order | Expected output |
|---|---|---|
| Boundary (first guess) | `7` | `Correct! It took you 1 guesses.` (the wording is not fussy, the number must be 1) |
| Normal | `3`, `9`, `7` | `Too low`, `Too high`, then `Correct! It took you 3 guesses.` |
| Normal | `1`, `2`, `3`, `4`, `5`, `6`, `7` | six `Too low` lines, then `Correct! It took you 7 guesses.` |
| Invalid (outside 1 to 10) | `50`, `-4`, `7` | `Too high`, `Too low`, then `Correct! It took you 3 guesses.` |

## Task 9 check

Your Python version should print `20`. Change `5` to `7` and `20` to `30`. It should now print `35`. Work out why before you run it.

## Task 10 tests (age check)

| Type | Inputs, in order | Expected output |
|---|---|---|
| Normal | `13` | `Thanks` |
| Boundary (lowest allowed) | `11` | `Thanks` |
| Boundary (highest allowed) | `16` | `Thanks` |
| Boundary (just too low) | `10`, `11` | `Not valid.` once, then `Thanks` |
| Boundary (just too high) | `17`, `16` | `Not valid.` once, then `Thanks` |
| Invalid | `-3`, `200`, `14` | `Not valid.` twice, then `Thanks` |

---

# PART 3: Hints (reveal one at a time)

Try the task first. Open **one hint at a time**, and only when you are stuck.

**Task 4**

<details><summary>Hint 1</summary>Look at where the number starts, which way it moves, and the value in the condition. One of those needs to change.</details>
<details><summary>Hint 2 (4B)</summary>The step is the number on the end of the line that updates the variable.</details>
<details><summary>Hint 3 (4B)</summary>If the last number is missing, look at your condition. Should it be `<` or `<=`?</details>

**Task 5 (password)**

<details><summary>Hint 1</summary>You must ask for the password before the loop starts, so the loop has something to check.</details>
<details><summary>Hint 2</summary>The loop should keep running while the attempt is NOT the password. In Python, "not equal" is `!=`.</details>
<details><summary>Hint 3</summary>Inside the loop, print the message, then ask again. If you do not ask again inside the loop, it will repeat forever.</details>

**Task 6 (debug)**

<details><summary>Hint 1</summary>Run it. Python will show you the first problem for you. Read the error message and look at the end of the `while` line.</details>
<details><summary>Hint 2</summary>After that is fixed, the program prints the same line forever. Look at which lines are indented. Which line is supposed to be part of the loop?</details>
<details><summary>Hint 3</summary>When it finally stops, how many lines did it print? Compare the last line with the expected output. Check the condition.</details>

**Task 7 (Parsons)**

<details><summary>Hint 1</summary>Variables need a starting value before they are used in the loop.</details>
<details><summary>Hint 2</summary>The loop needs a number to check before it starts. Which of C or F goes first, before the loop?</details>
<details><summary>Hint 3</summary>The last line inside the loop should get the next number, so the loop can finish. Only the lines inside the loop are indented.</details>

**Task 8 (guess the number)**

<details><summary>Hint 1</summary>Take the first guess before the loop. Use `int()` around `input()` so you can compare numbers.</details>
<details><summary>Hint 2</summary>The loop should run while the guess is not equal to the secret.</details>
<details><summary>Hint 3</summary>Inside the loop you need three things: an if/else to say Too low or Too high, a new guess, and the guess counter going up by 1.</details>
<details><summary>Hint 4</summary>Think about what the counter should be after the very first guess, before the loop starts.</details>

**Task 10 (age check)**

<details><summary>Hint 1</summary>Think about when the age is NOT allowed. Is it too low, or too high? Two different checks.</details>
<details><summary>Hint 2</summary>You can join two conditions with `or`. The loop keeps going while the age is too low OR too high.</details>

---
---

# PART 4: TEACHER SOLUTIONS SHEET (do not share with students)

## Suggested lesson flow (about 55 minutes)

| Time | Activity |
|---|---|
| 0 to 5 | Starter: ask "How would you write a program that keeps asking until the password is right, if you don't know how many tries it will take?" Show why a `for` loop does not fit. Introduce `while`. |
| 5 to 15 | Tasks 1 and 2 (predict, run, investigate, trace). Tasks 1d and 2 are where the idea lands. |
| 15 to 20 | Task 3 (never runs), quick whole-class discussion |
| 20 to 30 | Task 4 (modify) |
| 30 to 45 | Task 5, then Task 8 (make) |
| 45 to 55 | Task 6 (debug) or Task 7, then plenary with Task 9 as an exit check |
| Fast finishers | Tasks 7, 9, 10 |

## Quick-check answers

**Task 1**
a) `3`, `2`, `1`, `Liftoff!` each on its own line.
c) 1. `count > 0`  2. Three times.  3. `count` is 0.  4. The "Liftoff!" line is not indented, so it is not part of the loop. It runs once, after the loop ends.
d) Without the line `count = count - 1`, the value of `count` stays at 3 so the condition is always True. It prints `3` forever (infinite loop). Make sure they know about the Stop button.

**Task 2**

| Check | number | total | number <= 4 ? |
|---|---|---|---|
| 1 | 1 | 0 | True |
| 2 | 2 | 1 | True |
| 3 | 3 | 3 | True |
| 4 | 4 | 6 | True |
| 5 | 5 | 10 | False |

Output: `10`. Common error: students stop the table at row 4 and write 6. The condition is checked a fifth time, and the body runs 4 times.

**Task 3**
a) `Game over`. b) Zero times. The condition is False the first time it is checked, so the body is skipped. A `while` loop can run zero times. c) `Still alive`, `Still alive`, `Game over`.

**Task 4**
```python
# 4A
count = 10
while count > 0:
    print(count)
    count = count - 1
print("Liftoff!")

# 4B
number = 2
while number <= 20:
    print(number)
    number = number + 2

# 4C
total = 0
number = 1
while number <= 10:
    total = total + number
    number = number + 1
print(total)   # 55
```
Common wrong attempts:
- 4B with `< 20`: the 20 is missing because the condition is False when `number` is 20. Off-by-one.
- 4A starting at `count = 10` but leaving `count > 0` as `count > 10`. The loop never runs.
- 4C changing only the condition to `<= 10` and getting a wrong total because the starting `total` was changed. Or leaving `<= 4` unchanged and getting 10.

**Task 5 (password gate) model solution**
```python
password = "sunrise"
attempt = input("Enter the password: ")      # first attempt, before the loop
while attempt != password:                   # keep going while it is wrong
    print("Wrong. Try again.")
    attempt = input("Enter the password: ")  # ask again, so the loop can end
print("Access granted")
```
Common wrong attempts:
1. **`if` instead of `while`.** Asks at most twice. If the second answer is also wrong, it prints Access granted anyway or just stops. It is not repeating.
2. **No second `input()` inside the loop.** `attempt` never changes, so it prints `Wrong. Try again.` forever.
3. **Condition the wrong way round (`while attempt == password:`).** A wrong first answer skips the loop and prints `Access granted`. A correct first answer loops forever.

**Task 6 (debug) solution**
```python
number = 1
while number <= 12:                       # fixed bugs 1 and 3
    print(number, "x 5 =", number * 5)
    number = number + 1                   # fixed bug 2: indented into the loop
```

| Bug | Type | Line | Fix |
|---|---|---|---|
| Missing colon after the condition | Syntax | `while number < 12` | Add `:` |
| `number = number + 1` is not indented, so it is outside the loop | Logic | last line | Indent it so it runs every time round. Without this, infinite loop printing `1 x 5 = 5`. |
| `< 12` stops before 12 | Off-by-one | `while number < 12` | Change to `<= 12` (or `< 13`) |

The bugs appear one at a time: the syntax error first, then the infinite loop, then the missing last line. Expect the infinite loop to surprise some students. Remind them of the Stop button.

**Task 7 (Parsons) solution**
```python
total = 0                                                # D
number = int(input("Enter a number (0 to stop): "))     # C
while number != 0:                                       # E
    total = total + number                               # B
    number = int(input("Enter a number (0 to stop): "))  # F
print("Total:", total)                                   # A
```
Order: D, C, E, B, F, A. D and C can be swapped, because they do not depend on each other. Accept either. B before F is not optional. If F goes first, the first number entered is thrown away. The `0` is the "sentinel" value that ends the loop and is never added.

Common wrong attempts:
- Putting F straight after C. The first number is overwritten and never added.
- Putting `total = 0` inside the loop. It resets every time, so the total is only the last number.
- Putting `print` inside the loop (indented), so it prints a running total every time.

**Task 8 (guess the number) model solution**
```python
secret = 7
guess = int(input("Guess the number (1-10): "))
guesses = 1                                  # the first guess is already counted
while guess != secret:
    if guess < secret:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Try again: "))
    guesses = guesses + 1
print("Correct! It took you", guesses, "guesses.")
```
Common wrong attempts:
1. **No new `input()` inside the loop.** The guess never changes, so it prints `Too low` or `Too high` forever.
2. **`guesses = 0` at the start.** Every answer is one too low, because the first guess was not counted. This is an off-by-one counting error.
3. **Forgetting `int()`.** Comparing text with numbers raises a `TypeError`. (In text comparison, `"10" < "7"` is True, which gives wrong hints, so converting matters.)

Note: "1 guesses" is a grammar issue. Let students fix it if they want to, but do not make it part of the success criteria.

**Task 9 (pseudocode)**
a)

| total | total < 20 ? |
|---|---|
| 0 | True |
| 5 | True |
| 10 | True |
| 15 | True |
| 20 | False |

b) `20`.
c)
```python
total = 0
while total < 20:
    total = total + 5
print(total)
```
Check task: with 7 and 30, `total` goes 0, 7, 14, 21, 28, 35 and stops at 35, because 28 is still below 30. It overshoots, so the output is 35. This is a good talking point: the loop checks only at the top.

**Task 10 (age check) model solution**
```python
age = int(input("Enter your age (11 to 16): "))
while age < 11 or age > 16:
    print("Not valid.")
    age = int(input("Enter your age (11 to 16): "))
print("Thanks")
```
Common wrong attempts:
1. **`and` instead of `or`.** No number is both below 11 and above 16, so the condition is always False and nothing is ever rejected.
2. **`age <= 11 or age >= 16`.** Rejects 11 and 16, which should be allowed (boundaries).
3. **No second `input()` in the loop.** Infinite `Not valid.`

If students have not met `or` yet, treat this task as a teacher-led demo, not independent work. Typing letters instead of a number crashes at `int()`. That is an invalid-data topic for a later lesson (try/except). Say so if it comes up.

## Misconceptions to watch for

- **Believing the loop stops as soon as the condition becomes False in the middle of the body.** It does not. The condition is only checked at the top. The rest of the body still runs. (Task 9 check shows this.)
- **Thinking `while` is checked only once.** The trace table in Task 2 fixes this.
- **Mixing up the three jobs of variable lines**: set up before, update inside the loop, check in the condition.
- **`=` and `==`.** `while count = 3:` is a syntax error. Remind them that `=` assigns and `==` compares.
- **Treating an infinite loop as "the computer is broken".** Normalise it and show the Stop button before Task 1d.
