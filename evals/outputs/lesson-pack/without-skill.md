# Year 9 Computing: How Data Travels Across the Internet (Packets and Packet Switching)

**Length:** 50 minutes, taught online over Zoom
**Previous lesson:** Network hardware (routers, switches, NICs)

**Assumptions (stated briefly):**
- Students have Zoom with chat, and either a pen and paper or a blank document to hand.
- You can share your screen and use polls or the chat. Nothing needs installing.
- No prior knowledge of IP addresses beyond "every device has one".
- The pack includes a no-tech "Packet Post" activity that works over Zoom using the chat and paper.
- Where I describe a typical trace (tracert), I've given sample output so the lesson still works if the school network blocks it.

---

## 1. Learning objectives

By the end of the lesson, students can:
1. Explain why data is split into packets before it is sent.
2. Name the main parts of a packet (header, payload, trailer) and say what the header holds.
3. Describe packet switching: packets take different routes and are reassembled at the destination.
4. Explain the roles of routers (and a simple view of switches and NICs) in moving packets.
5. Describe what happens when a packet is lost, late or out of order.

**Success criteria (put on the first slide):**
- I can say what a packet is.
- I can say what is in a header and why.
- I can explain how a message gets from A to B in packets.

**Key vocabulary:** packet, header, payload, trailer, packet switching, router, IP address, MAC address, hop, TTL (time to live), sequence number, reassemble, latency, packet loss, protocol (TCP/IP).

---

## 2. Lesson at a glance

| Time | Phase | What happens |
|---|---|---|
| 0:00 to 0:08 | Starter | Recall quiz on last lesson (2 MCQs) plus link to today |
| 0:08 to 0:16 | Teach 1 | Why packets? What is inside one? |
| 0:16 to 0:30 | Activity | Packet Post (breakout rooms or chat) |
| 0:30 to 0:40 | Teach 2 | Packet switching, routers, hops, TTL, reassembly |
| 0:40 to 0:47 | Check | Six-question MCQ quiz (Zoom poll or chat) |
| 0:47 to 0:50 | Plenary | Exit ticket and homework set |

---

## 3. Teacher script and plan

### Before the lesson (5 minutes)
- Open the slides (outline in Section 4) and the Packet Post cards (Section 5).
- Create 4 breakout rooms (or plan to use chat if you have a small class).
- Prepare the poll for Section 7 if you want automatic results. If not, students type letters in chat.
- Optional: have a command prompt ready to run `tracert bbc.co.uk` (Windows) or `traceroute bbc.co.uk` (Mac/Linux). Sample output is in Section 4, slide 11.

### Starter (0:08): Recall and link
**Say:** "Last lesson we met the hardware that moves data about. Two quick questions to wake the brain up, then we find out what is actually being moved."

Post these in chat or as a poll. Students answer with a letter. Reveal answers after both. Full list of MCQs is in Section 7, but these two go first.

**Starter Q1.** Which device connects different networks together and decides where to send data next?
- A. Switch
- B. Network interface card (NIC)
- C. Router
- D. Monitor

**Starter Q2.** What does a NIC do?
- A. It lets a device connect to a network
- B. It stores web pages for faster loading
- C. It sends data to the correct network based on IP address
- D. It boosts the Wi-Fi signal across a house

(Answers in Section 9.)

**Link to today:** "Routers move 'things'. What are those things? Not whole files. Today: packets."

**Hook question (30 seconds, chat):** "You send a 5 MB photo to a friend. Do you think it travels as one big lump, or in pieces? Type your guess."

Take 3 or 4 answers and say "Let's find out."

### Teach 1 (0:08 to 0:16): Why packets, and what is in one

**Key points to deliver:**
1. **Data is split into small chunks called packets.** A photo, an email or a video call is broken up before it leaves your device.
2. **Why bother?**
   - **Fairness / sharing:** one big file would hog a line. Small packets let many people's data share the same cables.
   - **Reliability:** if one packet is lost or damaged, only that packet is sent again, not the whole file.
   - **Efficiency / routing:** packets can use whichever routes are free, so the network is used well and keeps working if one link fails.
3. **Inside a packet** (draw as three coloured blocks on the slide):
   - **Header:** source IP address, destination IP address, packet number (sequence number), protocol, TTL.
   - **Payload:** the actual piece of data.
   - **Trailer / footer:** error-checking information (for example, a checksum) so the receiver can spot damage.

**Analogy (use it, then link it back):** "A packet is like a letter in an envelope. The header is the address and 'page 3 of 10' on the front. The payload is the page inside. The checksum is like a note saying 'this page should have 120 words', so the receiver can check nothing got smudged."

**Quick check (cold-call, 30 seconds):** "Which part tells the router where the packet is going?" (Header.)

### Activity (0:16 to 0:30): Packet Post (14 minutes)

**Aim:** students experience splitting, numbering, different routes, and reassembly.

**Setup (2 minutes):**
- Put students in breakout rooms of 3 or 4 (or do it as one class via chat if small).
- Each room is given a short message (see cards in Section 5), for example "MEET AT THE LIBRARY AT NINE".
- Roles: **Sender** (splits the message into packets), **Router A / Router B** (choose a route), **Receiver** (reassembles).

**Round 1 (5 minutes), splitting and numbering:**
1. Sender splits the message into packets of 2 or 3 words, and writes a header for each: `From: Sender | To: Receiver | Packet: 2 of 4`, then the payload.
2. Sender posts the packets one at a time to the next role in the room chat, **in a mixed-up order** (the rule: do not send them in order).

**Round 2 (4 minutes), routing:**
1. Routers each receive some packets and must forward them. Use the route card: odd-numbered packets go via Router A, even-numbered via Router B.
2. Router B is "slow" (waits 10 seconds before forwarding). Router A forwards at once.

**Round 3 (3 minutes), reassembly and loss:**
1. Receiver rebuilds the message using the packet numbers.
2. Teacher secretly tells one room that one packet "was lost". Receiver must notice which number is missing and request it again.

**Debrief (back in main room, 3 minutes), questions to ask:**
- "Did the packets arrive in order? Why not?" (Different routes, different speeds.)
- "How did the receiver put them back together?" (Packet numbers in the header.)
- "How did you know one was missing?" (A gap in the numbering.)
- "What would happen without numbers?" (Scrambled message.)

**Chat-only version (no breakouts):** you act as the sender. Type packets into chat out of order and have 4 volunteers (unmuted) call out each packet's number, then ask the class to rebuild the message in chat.

### Teach 2 (0:30 to 0:40): Packet switching, routers, TTL

**Key points:**
1. **Packet switching:** each packet is treated separately. At each router, the router reads the destination IP in the header and forwards the packet to the next router that gets it closer. Each step is a **hop**.
2. **Different routes:** packets from the same message may take different paths, depending on traffic and broken links. This is what you saw in Packet Post.
3. **Out of order is normal:** the receiving device uses the packet numbers to **reassemble** the data in the right order. If packets are missing, the receiver asks for them again (TCP handles this).
4. **TTL (time to live):** a number in the header (for example, 64) that drops by 1 at each router. If it reaches 0, the packet is thrown away. This stops packets circling the internet forever if there is a routing error.
5. **Link to hardware from last lesson:**
   - **NIC:** converts your device's data to signals and attaches your device's MAC address on the local network.
   - **Switch:** moves frames between devices inside one local network using MAC addresses.
   - **Router:** connects networks and forwards packets using IP addresses. This is the packet-switching device.
6. **Contrast (one line only):** older phone calls used **circuit switching**: one dedicated line for the whole call. The internet uses packet switching because it shares lines far more efficiently.

**Show it:** run `tracert` (or show slide 11 sample) and point out the hops and times.

**Misconceptions to pre-empt:**
- "A packet is a whole file." (No, it is a small piece, often around 1,500 bytes at most on Ethernet.)
- "All packets take the same route." (No, not necessarily.)
- "Packets arrive in order." (Not guaranteed, hence numbering.)
- "The switch routes packets across the internet." (No, switches work inside a local network; routers connect networks.)

### Check (0:40 to 0:47): MCQ quiz
Run Questions 3 to 8 from Section 7 as a Zoom poll, or ask students to answer in chat with a letter on your "go". Give 45 seconds per question, then reveal and give a one-line reason each time.

### Plenary (0:47 to 0:50): Exit ticket and homework
**Exit ticket (type in chat, one sentence):** "Packets are numbered because ..."

Look for: "so the receiver can put them back in the right order, even if they arrive out of order or one is lost."

**Set homework** (Section 8).

### Differentiation
- **Support:** give students a header template to fill in; pre-split the message in Packet Post; sentence starters for the exit ticket.
- **Stretch:** ask what happens if a router fails mid-message; ask why a smaller packet size is not always better (more headers means more overhead); introduce TCP (reliable, numbered, acknowledged) versus UDP (fast, no resend) for video calls like the one you are on right now.

### Zoom tips
- Use the chat for all quick-fire answers so everyone responds at once.
- Post the Packet Post cards in chat when students enter breakout rooms, as they cannot see your screen there.
- Ask students to keep cameras on during the debrief if your school policy allows it, otherwise use reactions (thumbs up for "got it").
- Set a visible timer for each phase.

---

## 4. Slide outline (11 slides)

1. **Title:** "How does data travel across the internet?" plus success criteria.
2. **Recall:** Starter Q1 and Q2.
3. **Hook:** "Photo of a cat, 5 MB. One lump or many pieces?"
4. **What is a packet?** Definition and envelope analogy.
5. **Why packets?** Three reasons: fair sharing, resend only what was lost, flexible routes.
6. **Anatomy of a packet:** header / payload / trailer diagram. Header contents: source IP, destination IP, packet number, protocol, TTL.
7. **Activity instructions:** Packet Post roles and timings.
8. **Packet switching:** diagram with 4 routers and two possible routes from A to B.
9. **Reassembly and loss:** numbered packets arriving 3, 1, 4, 2 and being put back in order; a gap showing a missing packet.
10. **TTL:** counter dropping 64, 63, 62 ... 0 and the packet being discarded.
11. **Trace demo:** sample output below.

```
Tracing route to bbc.co.uk [151.101.0.81]
  1     2 ms     1 ms     2 ms  home-router [192.168.1.1]
  2    11 ms    10 ms    12 ms  isp-gateway-1 [82.x.x.x]
  3    14 ms    13 ms    15 ms  core-london-2 [195.x.x.x]
  4    17 ms    16 ms    18 ms  peering-exchange [193.x.x.x]
  5    19 ms    18 ms    20 ms  151.101.0.81
```
*(Illustrative example. Real output will differ.)* Ask: "How many hops? Where is the time added?"

12. **Hardware link-up:** NIC, switch, router: which job in the journey?
13. **Quiz slides:** Questions 3 to 8.
14. **Exit ticket and homework.**

---

## 5. Packet Post: resource cards

**Message cards (give one per room):**
1. MEET AT THE LIBRARY AT NINE TOMORROW
2. BRING YOUR LAPTOP AND CHARGER TO ROOM TWELVE
3. THE QUIZ HAS BEEN MOVED TO FRIDAY AFTERNOON
4. PLEASE SEND THE FINAL DESIGN BEFORE LUNCH

**Header template (students copy):**
```
From: ________   To: ________   Packet: ___ of ___   TTL: 5
Payload: ____________________
```

**Route card:**
- Odd packet numbers go via **Router A** (forward immediately).
- Even packet numbers go via **Router B** (wait 10 seconds, then forward).
- Each router lowers TTL by 1 before forwarding. If TTL hits 0, the packet is dropped. (Challenge: give a room TTL: 1 to see what happens. The packet is dropped at the first router.)

**Loss card (teacher gives secretly to one room):** "Packet 3 is lost in transit. Do not deliver it."

**Receiver checklist:**
- Put the packets in number order.
- Check no numbers are missing.
- Read the message back aloud.
- If a number is missing, request it and write which number you asked for.

---

## 6. Worked examples for the board

**Example 1: Splitting.** Message: "HELLO FROM LONDON TODAY" split into packets of 2 words:
- Packet 1 of 2: "HELLO FROM"
- Packet 2 of 2: "LONDON TODAY"

**Example 2: Arrival out of order.** Packets arrive as 3, 1, 4, 2. The receiver sorts them to 1, 2, 3, 4.

**Example 3: Missing packet.** Packets arrive as 1, 2, 4, 5. The gap shows 3 is missing, so the receiver asks the sender to resend packet 3 only.

**Example 4: TTL.** A packet leaves with TTL 3. After router 1, TTL is 2. After router 2, it is 1. After router 3, it is 0 and it is discarded.

---

## 7. Multiple-choice questions (8 in total)

Questions 1 and 2 are for the starter. Questions 3 to 8 are the check quiz. Answers are in Section 9 and in the key on the last line of this file.

**Question 1.** Which device connects different networks together and decides where to send data next?
- A. Switch
- B. Network interface card (NIC)
- C. Router
- D. Monitor

**Question 2.** What does a NIC do?
- A. It lets a device connect to a network
- B. It stores web pages for faster loading
- C. It sends data to the correct network based on IP address
- D. It boosts the Wi-Fi signal across a house

**Question 3.** What is a packet?
- A. A complete file stored on a server
- B. A cable that links two routers
- C. A password used to join a network
- D. A small chunk of data with extra information added so it can be delivered

**Question 4.** Which of these is normally found in a packet's header?
- A. The whole file being sent
- B. The destination IP address
- C. The sender's web browser history
- D. The speed of the user's broadband

**Question 5.** Why is data split into packets before it is sent across the internet?
- A. So it can be hidden from hackers completely
- B. So that files become smaller for ever
- C. So that every packet must follow exactly the same route
- D. So that lost or damaged pieces can be re-sent without sending everything again

**Question 6.** In packet switching, what can happen to packets that belong to the same message?
- A. They can take different routes and arrive in a different order
- B. They always arrive in the order they were sent
- C. They must all travel through the same router
- D. They are joined into one large packet at every router

**Question 7.** What is the purpose of the TTL (time to live) value in a packet header?
- A. It records how long the user has been online
- B. It stops packets travelling around the network forever by discarding them when it reaches zero
- C. It tells the receiver how many seconds to wait before opening the file
- D. It measures the size of the payload

**Question 8.** How does the receiving device put the data back in the right order?
- A. It guesses using the file name
- B. It asks the router to sort the packets
- C. It uses the packet (sequence) numbers in the headers
- D. It waits until the packets arrive in order by luck

---

## 8. Homework (about 20 minutes)

**Task A: Explain it (short answer).** In 4 to 6 sentences, explain to a Year 7 student how a photo gets from your phone to a friend's phone using the words *packet*, *header*, *router* and *reassemble*.

**Task B: Draw it.** Draw a labelled diagram of a packet showing header, payload and trailer. List at least four items stored in the header.

**Task C: What would happen if...?** Answer in 2 or 3 sentences each:
1. Packets had no sequence numbers.
2. A packet's TTL was never reduced.
3. One link between two routers was suddenly cut during a download.

**Task D (stretch):** Find out what the difference is between **TCP** and **UDP**. Which would you choose for (a) downloading a document and (b) a live video call, and why?

**Mark scheme for homework (teacher):**
- A: 1 mark each for correct use of packet (small chunk of data), header (addressing and numbering information), router (forwards packets towards destination), reassemble (put back in order using numbers); 1 mark for a clear, logical explanation. Total 5.
- B: 1 mark for the three labelled parts; 1 mark each for four correct header items (source IP, destination IP, packet number, TTL, protocol). Total 5.
- C: 1 mark each for a clear consequence. (1) Receiver could not reorder packets or detect missing ones. (2) Packets could circle forever and clog the network. (3) Packets are rerouted another way, so the download continues, possibly a little slower. Total 3.
- D: TCP is reliable (numbered, checks, resends); UDP is faster with no resending. Document: TCP. Video call: UDP, because a late packet is no use and speed matters more than perfection. Total 4.

---

## 9. Teacher solutions and explanations

**MCQ answers (with the reason to give out loud):**
1. **C. Router.** Routers connect networks and forward packets using IP addresses. A switch works inside one network.
2. **A.** A NIC connects a device to a network. Choice C describes a router; D describes a Wi-Fi extender.
3. **D.** A packet is a small chunk of data plus header information.
4. **B.** The header holds addressing and control information such as source and destination IP, packet number and TTL.
5. **D.** Only the lost or damaged packet needs resending, and sharing the lines is fairer.
6. **A.** Packets are routed individually, so routes and arrival order may differ.
7. **B.** TTL falls at each hop and the packet is discarded at zero.
8. **C.** Sequence numbers in headers let the receiver reassemble in order.

**Starter and plenary expected answers:** see Sections 3 and 6.

**Packet Post debrief answers:** out of order because different routes and speeds; numbers allow reassembly; a gap in the numbers reveals loss; without numbers the message is scrambled.

**Common errors to listen for:**
- "The header is the first packet." (No, it is the first part of every packet.)
- "Routers store the packets permanently." (They forward them quickly.)
- Mixing MAC and IP addresses. (MAC: identifies the NIC on the local network. IP: identifies the device for routing across networks.)

---

## 10. Quick timing safety net
- Running late: shorten Packet Post to two rounds (drop the loss round), and set the quiz to four questions (3, 4, 6, 8).
- Running early: run the loss round in the main room as a class, or use the TCP versus UDP stretch question.

ANSWER KEY: C A D B D A B C
