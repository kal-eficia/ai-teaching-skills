# Year 9 Python: First Lesson on While Loops (Programming Tasks)

**Assumptions:** Students are working in IDLE, Thonny or similar. Lesson is about 50-60 minutes, with roughly 35-40 minutes of coding time. Tasks 1-5 are core; Task 6 is a stretch for fast finishers. Each task builds on the last, and each one introduces exactly one new idea. Expected solutions are at the end for you.

**Key idea to teach first (2 minutes):** A `for` loop repeats a *set number of times*. A `while` loop repeats *for as long as a condition is True*. Use `while` when you don't know in advance how many repeats you need.

---

## Task 1: Predict, run, explain (warm-up, 5 min)

Do **not** run this yet. Read it and write down what you think the output will be.

```python
count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1
print("Finished")
```

1. Write your prediction. Then run it and check.
2. How many times did the loop body run?
3. Which line stops the loop going on forever?

**Now break it on purpose.** Delete the line `count = count + 1` and run it again. Press **Ctrl+C** (or the Stop button) to halt it. In one sentence, explain what happened. This is called an *infinite loop*.

---

## Task 2: Counting loops (10 min)

Write these three programs. Each must use a `while` loop, not a `for` loop.

**a)** Print the numbers 1 to 10.

**b)** Print the numbers 10 down to 1, then print `"Lift off!"`.

**c)** Print the 5 times table (5, 10, 15 ... up to 60).

**Extension:** Change (c) so it asks the user which times table they want and prints it up to 12 times that number.

---

## Task 3: Keep asking until it's right (10 min)

This is where `while` earns its place, because we can't know how many attempts the user will need.

Write a program that:

- Sets a secret password, e.g. `"python"`
- Asks the user to enter the password
- Keeps asking, with the message `"Wrong, try again"`, until they get it right
- Finally prints `"Access granted"`

**Starter code:**

```python
password = "python"
guess = input("Enter the password: ")

while guess != password:
    # your code here

print("Access granted")
```

**Think about it:** Why do we ask for input *before* the loop and again *inside* it?

**Extension:** Count how many attempts it took and print `"You got it in 4 attempts"` at the end.

---

## Task 4: Running total (10 min)

Write a program that keeps asking the user to enter a number and adds each one to a running total. It stops when the user enters `0`. At the end, print the total.

Example run:

```
Enter a number (0 to stop): 7
Enter a number (0 to stop): 12
Enter a number (0 to stop): 3
Enter a number (0 to stop): 0
The total is 22
```

**Hints:** You need a variable `total` that starts at 0. Remember `input()` gives a string, so you need `int()`.

**Extension:** Also print how many numbers were entered, and the average. (Careful: what happens if the user enters 0 straight away? Fix it so your program doesn't crash.)

---

## Task 5: Spot and fix the bugs (5-8 min)

Each program below has one bug. Predict the problem, then fix it.

**Program A** (never stops)

```python
number = 10
while number > 0:
    print(number)
    number = number + 1
```

**Program B** (never runs at all)

```python
lives = 0
while lives > 3:
    print("You are still alive")
    lives = lives - 1
```

**Program C** (runs one time too few)

```python
n = 1
while n < 5:
    print("Hello", n)
    n = n + 1
```
*It should print Hello 1 to Hello 5.*

**Program D** (crashes)

```python
age = input("Enter your age: ")
while age < 18:
    print("Too young")
    age = input("Enter your age: ")
```

---

## Task 6: Stretch challenge, Guess the Number (15 min, fast finishers)

Build a number guessing game.

1. Use `import random` and `secret = random.randint(1, 50)` to pick a hidden number.
2. Ask the player to guess.
3. After each wrong guess, tell them `"Too high"` or `"Too low"`.
4. Keep going until they get it right, then print how many guesses it took.

**Level up (choose one or more):**
- Limit the player to 7 guesses. Print `"Game over, the number was ..."` if they run out. (You will need a condition with `and`.)
- Ask `"Play again? (y/n)"` at the end and wrap the whole game in another `while` loop.
- Add a "hot/cold" hint depending on how close the guess is.

---

## Plenary (3 min): exit questions

1. In one sentence, when would you choose `while` over `for`?
2. What two things must every working `while` loop have? *(A condition that can become False, and something inside the loop that changes it.)*
3. What does an infinite loop look like, and how do you stop it?

---

## Teacher solutions

**Task 1:** Output is `Count is 1` through `Count is 5`, then `Finished`. The body runs 5 times. `count = count + 1` moves towards the condition becoming False. Without it, `count` stays 1 and the loop never ends.

**Task 2:**
```python
# a
n = 1
while n <= 10:
    print(n)
    n = n + 1

# b
n = 10
while n >= 1:
    print(n)
    n = n - 1
print("Lift off!")

# c
n = 5
while n <= 60:
    print(n)
    n = n + 5

# c extension
table = int(input("Which times table? "))
i = 1
while i <= 12:
    print(table * i)
    i = i + 1
```

**Task 3:**
```python
password = "python"
guess = input("Enter the password: ")
attempts = 1
while guess != password:
    print("Wrong, try again")
    guess = input("Enter the password: ")
    attempts = attempts + 1
print("Access granted")
print("You got it in", attempts, "attempts")
```
The first input gives the loop something to test; the input inside gives the user a chance to change the answer.

**Task 4:**
```python
total = 0
count = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total = total + number
    count = count + 1
    number = int(input("Enter a number (0 to stop): "))
print("The total is", total)
if count > 0:
    print("Numbers entered:", count)
    print("Average:", total / count)
```

**Task 5:**
- **A:** `number` goes up, so it never reaches 0. Change to `number = number - 1`.
- **B:** The condition is False from the start, so the loop body never runs. Start `lives` at a value above 3 (or change the condition to `lives > 0` with `lives = 3`).
- **C:** Off-by-one. Use `n <= 5`.
- **D:** `age` is a string, and comparing a string to an integer causes a `TypeError`. Use `int(input(...))` in both places.

**Task 6:**
```python
import random
secret = random.randint(1, 50)
guess = int(input("Guess the number (1-50): "))
guesses = 1
while guess != secret:
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))
    guesses = guesses + 1
print("Correct! It took you", guesses, "guesses.")
```

Limited-guesses version (key change):
```python
while guess != secret and guesses < 7:
    ...
if guess == secret:
    print("Correct!")
else:
    print("Game over, the number was", secret)
```

---

## Common misconceptions to watch for

- Students forget to change the variable inside the loop (infinite loops). Keep reminding them: "What makes this condition eventually False?"
- Using `=` instead of `==` in conditions.
- Forgetting `int()` around `input()` when comparing numbers.
- Putting the `input()` only inside the loop and getting a `NameError` on the first check.
- Off-by-one errors with `<` versus `<=`. Get them to trace the last iteration by hand.
- Thinking the loop stops the instant the condition becomes False mid-body. It only re-checks at the top of each pass.
