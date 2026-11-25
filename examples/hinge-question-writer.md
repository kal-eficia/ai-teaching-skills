# Example: hinge-question-writer

## The request

> Use hinge-question-writer. IGCSE CS, 15 year olds. Three hinge questions for a lesson on the fetch-decode-execute cycle, buses, and clock speed. Students answer on their lesson page and I see the spread live.

## What the skill produced

### Hinge 1: fetch stage

**An instruction has just been read from memory. Which register does it go into first?**

A. Program Counter (PC)
B. Memory Address Register (MAR)
C. Current Instruction Register (CIR)
D. Memory Data Register (MDR)

**Correct: D.** Everything read from memory arrives in the MDR first, then it's copied to the CIR.

| Option | What it reveals |
|---|---|
| A | Thinks the PC holds instructions, not addresses |
| B | Mixes up the address with the thing stored at that address |
| C | Knows the instruction ends up in the CIR but skips the MDR step |

**Decision rule:** 80%+ on D: move on to decode. Many on C: draw the route memory → MDR → CIR again and ask "what's the only register that talks to memory for data?" Many on A or B: go back to *address versus contents* with the pigeonhole analogy before anything else.

### Hinge 2: buses

**The CPU needs the instruction stored at address 150. What travels along the address bus?**

A. The instruction stored at address 150
B. The number 150
C. A signal telling memory to read
D. The next address, 151

**Correct: B.**

| Option | What it reveals |
|---|---|
| A | Confuses the address bus with the data bus |
| C | Confuses the address bus with the control bus |
| D | Mixes the PC being incremented with what's sent on the bus |

**Decision rule:** 80%+ on B: move on. Split between A and C: one slide with all three buses, what each carries and its direction, then re-ask with address 200.

### Hinge 3: clock speed

**A computer's clock speed is doubled and nothing else changes. What is most likely?**

A. It can run twice as many programs at the same time
B. Its storage capacity doubles
C. It can carry out more instructions per second
D. Its RAM capacity doubles

**Correct: C.**

| Option | What it reveals |
|---|---|
| A | Confuses clock speed with number of cores |
| B | Mixes up speed with storage |
| D | Mixes up speed with memory size |

**Decision rule:** 80%+ on C: move on to cores and cache. Many on A: contrast "faster worker" (clock) with "more workers" (cores) before teaching cores.

Key across the set: D, B, C. Checked: clean.
