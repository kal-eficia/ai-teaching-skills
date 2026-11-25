# Example: misconception-finder

## The request

> Use misconception-finder. Year 10 IGCSE CS quiz on data storage, 14 students (S01 to S14). Here are the wrong answers with confidence ratings.

| Question | Wrong answers (students, confidence) |
|---|---|
| Q2 Why does a computer need ROM? | "To save your files when the computer is off" (S03, S05, S08, S11 *Think so*; S06, S13 *Certain*) |
| Q4 What is virtual memory? | "Memory stored in the cloud" (S02, S04, S07, S12 *Certain*; S09 *Think so*) |
| Q5 RAM is volatile. Explain what this means. | "RAM is unstable and can crash" (S01, S10 *Guessing*); "RAM is slow" (S05, S14 *Guessing*) |
| Q7 How does an SSD store data? | "On a spinning disk" (S08 *Certain*; S03, S11 *Guessing*) |

## What the skill produced

### 1. Virtual memory means the cloud (fix first)

- **The wrong idea:** "Virtual means online, so virtual memory is memory in the cloud."
- **Evidence:** Q4, 5 of 14 students, 4 of them *Certain*.
- **Why it's appealing:** "virtual" is used for online things everywhere else (virtual meetings, virtual tours).
- **The fix:** contrast "virtual = acting like something it isn't" with "online". Show RAM full → part of the SSD or hard drive is used as if it were RAM, then pages swap back and forth, and that's why it's slow. Five minutes, with a diagram of RAM and secondary storage swapping pages.
- **Hinge check:** *A laptop's RAM is full and the user opens another app. Where is virtual memory created?* A. In the cloud  B. On the hard drive or SSD  C. In ROM  D. In the CPU's cache. (Correct: B)
- **Revisit:** next two starters.

### 2. ROM stores your files

- **The wrong idea:** "ROM keeps things when the power's off, so it's where my files go."
- **Evidence:** Q2, 6 students, 2 *Certain*.
- **Why it's appealing:** they've correctly learned that ROM is non-volatile, but applied it to the wrong job. It's mixing up ROM with secondary storage.
- **The fix:** sort task with three buckets: ROM, RAM, secondary storage. Items: start-up instructions, your homework file, the app you have open, saved photos, the operating system while it runs. The key point: ROM holds a small, fixed set of start-up instructions, and you can't save to it.
- **Hinge check:** *Which of these is stored in ROM?* A. A document the user saved  B. The operating system while it is running  C. Photos on the phone  D. The instructions that start the computer. (Correct: D)
- **Revisit:** next two starters, as the sort task.

### 3. SSDs spin

- **The wrong idea:** "All storage spins."
- **Evidence:** Q7, 3 students, 1 *Certain* (S08, who also got Q2 wrong).
- **The fix:** side by side, a hard drive (moving read/write head, spinning platters) and an SSD (no moving parts, data stored as trapped charge in flash memory). Ask "what happens to each if you drop the laptop?"
- **Hinge check:** *How does an SSD store data?* A. In flash memory chips with no moving parts  B. On a spinning magnetic disk  C. As pits and lands read by a laser  D. In chips that lose data when the power is off. (Correct: A)

### Slip, not a misconception: "volatile"

Q5's wrong answers were all *Guessing* and scattered between two different ideas. That's a vocabulary gap, not a belief. Fix it with one flashcard (*volatile: loses its data when the power is turned off*) and a starter question, not a reteach.

**Fix first:** virtual memory. Most students, most of them certain, and they won't drop it without being shown why it's wrong.

Hinge key across the set: B, D, A. Checked: clean.
