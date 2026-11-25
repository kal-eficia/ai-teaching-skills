# Example: worked-example-builder

## The request

> Use worked-example-builder. IGCSE CS, converting negative denary numbers to 8-bit two's complement. Students keep forgetting a step.

## What the skill produced

**The same three steps every time:**
1. Write the **positive** number in 8-bit binary (pad with 0s to 8 bits).
2. **Flip** every bit (0 becomes 1, 1 becomes 0).
3. **Add 1.**

### 1. Fully worked: −12

| Step | Working | Why |
|---|---|---|
| 1 | 12 = 0000 1100 | Start from the positive. It must be 8 bits, so pad with 0s on the left |
| 2 | 1111 0011 | Flip every bit |
| 3 | 1111 0100 | Add 1. **Most marks are lost here:** students stop after flipping |

Check: 1111 0100 = −128 + 64 + 32 + 16 + 4 = −12 ✓

### 2. Paired example: −40 (the carry ripples)

| Step | Working | Why |
|---|---|---|
| 1 | 40 = 0010 1000 | |
| 2 | 1101 0111 | Flip |
| 3 | 1101 1000 | Adding 1 to ...0111 carries along three places. Same rule, it just ripples |

Check: −128 + 64 + 16 + 8 = −40 ✓

### 3. Faded: −25 (you do step 3)

| Step | Working |
|---|---|
| 1 | 25 = 0001 1001 |
| 2 | 1110 0110 |
| 3 | ____________ |

### 4. Faded: −50 (you do steps 2 and 3)

| Step | Working |
|---|---|
| 1 | 50 = 0011 0010 |
| 2 | ____________ |
| 3 | ____________ |

### 5. Faded: −9 (only step 1 is set up for you)

| Step | Working |
|---|---|
| 1 | 9 = ____________ (8 bits) |
| 2 | ____________ |
| 3 | ____________ |

### 6. On your own

a) −3  b) −100  c) What denary number is 1111 1010?  d) **Twist:** can you write −130 in 8-bit two's complement? Explain.

### Answers (teacher)

- Faded −25: 1110 0111
- Faded −50: 1100 1101 then 1100 1110
- Faded −9: 0000 1001, 1111 0110, 1111 0111
- a) 1111 1101  b) 1001 1100  c) −6
- d) No. 8-bit two's complement only covers −128 to +127, so −130 needs more bits.

All answers checked with code.
