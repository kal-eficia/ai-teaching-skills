# Example: exam-question-writer

## The request

> Use exam-question-writer. Cambridge IGCSE Computer Science 0984, Topic 3 (data storage and network hardware). One structured question, about 10 marks, Paper 1 style, with a full mark scheme.

## What the skill produced

### Question

A school is buying new laptops for its students.

**(a)** Give **two** differences between RAM and ROM. **[2]**

**(b)** A student opens several large applications at once and the laptop's RAM becomes full.
Explain how virtual memory allows the student to keep working. **[3]**

**(c)** The school chooses solid-state drives (SSDs) instead of magnetic hard disk drives.
Explain **two** reasons why SSDs are suitable for students' laptops. **[4]**

**(d)** State the purpose of a MAC address. **[1]**

### Mark scheme

**(a)** 1 mark per difference, max 2. Each point must refer to both, or clearly imply the comparison.
- RAM is volatile; ROM is non-volatile (1)
- RAM can be read from and written to; ROM can only be read (1)
- RAM stores data, programs and the OS currently in use; ROM stores the start-up instructions / BIOS / bootstrap (1)
- RAM contents change constantly; ROM contents are fixed (1)

*Do not accept:* "ROM stores files", "RAM is faster" (not a defining difference at this level), a point about one memory only.

**(b)** 1 mark per point, max 3.
- Part of secondary storage (hard drive / SSD) is used as if it were RAM (1)
- Data / pages not currently needed are moved from RAM to virtual memory (1)
- ...freeing space in RAM for the data or program needed now (1)
- Pages are swapped back into RAM when they're needed (1)

*Do not accept:* "memory in the cloud", "extra RAM is downloaded".

**(c)** 2 marks per reason (1 for the reason, 1 for the linked expansion), max 4.
- No moving parts (1) ...so less likely to be damaged if the laptop is dropped or carried around (1)
- Faster access/read speeds (1) ...so the laptop starts up and opens files and programs quickly (1)
- Lighter / smaller (1) ...so the laptop is easier for students to carry (1)
- Uses less power (1) ...so the battery lasts longer through the school day (1)

*Do not accept:* "more storage" (SSDs aren't necessarily bigger), "cheaper".

**(d)** 1 mark.
- To uniquely identify a device (its network interface card) on a network (1)

*Accept:* "a unique hardware address given by the manufacturer". *Do not accept:* "to give the device an IP address".

### Model answer (10/10)

(a) RAM is volatile so its contents are lost when the power is off, whereas ROM is non-volatile. RAM can be written to, but ROM can only be read.
(b) Part of the SSD is set aside to act as RAM. Data that isn't being used is moved out of RAM into this area, freeing RAM for the program the student needs, and it's swapped back when needed.
(c) SSDs have no moving parts, so they're less likely to break when students carry or drop the laptop. They also have faster access speeds, so the laptop boots and loads programs quickly.
(d) To uniquely identify the device's network interface card on a network.

### Checks

- [x] Command words match the marks: "give" and "state" are recall, "explain" needs linked reasons.
- [x] Each mark can be awarded on its own.
- [x] Everything is within the syllabus's data storage and network hardware content.
- [x] Difficulty rises from (a) to (c). (d) is a short recall item to finish.
- [x] Original question; no past-paper wording reused.
