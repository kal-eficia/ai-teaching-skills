# Year 9 Computing: How data travels across the internet (packets and packet switching)

50-minute live lesson on Zoom. This pack has five parts, in this order:

1. `teacher-plan.md`
2. `student-page.html` (copy the code block into a file and save it with that name)
3. `homework.md`
4. `mark-scheme.md`
5. `solutions.md` (one-screen key for approving work live)

**Assumptions (you asked me not to ask, so I made these):**
- English KS3 National Curriculum computing, no exam board. Objectives use KS3 wording about how networks and the internet transmit data.
- Students are about 13 to 14, each on their own device with a browser and Zoom chat open.
- You will share the HTML file with students (LMS, email, or any file link). It needs no login and works offline once opened.
- Last lesson (routers, switches, NICs) is the recall material for the starter.
- Question numbers: S1 to S3 (starter), C1 to C3 (check), E1 (exit), H1 to H3 (homework). All 10 multiple-choice questions are in that order in the answer key on the last line.

---

# 1. teacher-plan.md

## Objectives
- Understand how data is split into packets and sent across the internet using packet switching.
- Describe what a packet contains (header: source address, destination address, packet number, hop limit; payload: the data).
- Explain the roles of the sender, routers and receiving device when a message is sent.
- Explain why packets can take different routes and arrive out of order, and how the receiver copes.

## Success criteria (say these aloud at the start)
- I can name the parts of a packet.
- I can explain what a router does with a packet.
- I can explain how a file is put back together at the other end.

## Before the lesson
- Send students the HTML file and ask them to open it **before** the Zoom start time, or paste the link in chat at 0:00.
- Have the Zoom chat open. Students paste a summary from each page into chat (they click "Copy my summary", then paste). Skim for confident-but-wrong answers.
- Have `solutions.md` open on a second screen or device.
- Optional: have a pack of coloured sticky notes or a pen and paper ready for the live demo at 8:00.

## Timeline

| Time | Phase | What happens |
|---|---|---|
| 0:00 to 2:00 | Settle | Share the link, state the three success criteria, cameras/mics as per your rules. |
| 2:00 to 8:00 | Starter (page 1) | Students answer S1 to S3 from memory on last lesson's hardware, with a confidence rating each. They paste the page 1 summary into chat. |
| 8:00 to 21:00 | Learn (page 2) | You explain, they follow on the page. Live demo (below). Students try the "shuffle the packets" widget, then write one sentence about the header. |
| 21:00 to 27:00 | Check (page 3) | Hinge questions C1 to C3. Paste summary. Use the results to decide whether to reteach (see "Decision point"). |
| 27:00 to 42:00 | Apply (page 4) | Sort task (5 min), then the 4-mark written question (8 min). You approve written work live using `solutions.md`. |
| 42:00 to 46:00 | Exit | E1, one question that proves the objective. Paste summary. |
| 46:00 to 50:00 | Wrap | Cold-call two students for the 10-second recap. Set homework (20 min). Say next lesson's topic. |

## What to say at each transition (one line each)
- Into starter: "Two minutes, from memory only. Rate how sure you are before you see if you were right."
- Into learn: "Last lesson you met the hardware. Today we follow one message through it."
- Into check: "Three quick questions. The wrong answers are the ones people really pick, so read all four."
- Into apply: "Now you do the thinking. First sort the jobs, then explain it in your own words."
- Into exit: "One question. If you get this, you got today."
- Closing: "Message in, chopped up, routed, rebuilt. Say it to someone at home tonight."

## Live demo for the learn phase (3 minutes)
Type "Meet me at the park at six" in the Zoom chat or on a shared document. Say you are sending it across the internet. Split it into four packets on screen:

1. Meet me
2. at the
3. park
4. at six

Add a header to each: "From: my laptop, To: your phone, Packet 2 of 4, Hops left: 64". Ask students which router would read the "To" part. Then "post" packets 3, 1, 4, 2 in chat in that order and ask the class how the receiver rebuilds it. The answer they should reach: **the packet number**.

## Misconceptions to listen for
1. **"The router puts the packets back in order."** Routers only read the destination and pass packets on. The **receiving device** reassembles using packet numbers. Fix: ask "Does a postbox sort your jigsaw, or do you?"
2. **"All packets from one message take the same route."** They may not. Each router decides the next hop based on what is quickest right now. Fix: use the shuffle widget and point out "route" is not part of the packet.
3. **"If a packet is lost, the whole file is sent again."** Only the missing packet is requested again. Fix: C2 and H3 target this.
4. **Mixing up devices from last lesson.** A switch sends data within one network to the right device; a router connects different networks and picks routes between them; a NIC connects one device to a network. Fix: S1 to S3 show who is shaky, and you reteach in 60 seconds.
5. **"The header is the title of the message."** It is addressing and control information, not content. Fix: say "label on the envelope, not the letter inside".

## Decision point at 27:00
Look at the page 3 summaries in chat. If more than a third of the class chose the wrong answer on C2 (the order question), spend 2 minutes redoing the live demo with packet numbers before moving on, and shorten the sort task to the first four items.

## Differentiation
- **Support:** Give a sentence starter for the written question: "First the file is split into ... Each packet has a header that contains ... Routers ...". Let them use the word bank on page 4.
- **Stretch:** Ask "What would happen if a router could not reach the next router on the best route?" (It chooses another route, which is why the internet is hard to break.) Or ask them to compare with a dedicated line between two places and say what the downside is (one broken or busy line stops everything, and the line sits unused between messages).

## Zoom tips
- Use chat for summaries, not the microphone, so every student answers every time.
- Ask for a thumbs-up reaction after the starter to show they finished.
- If a student cannot open the HTML, share your screen and read the questions aloud; they answer in chat as A, B, C or D.

## For next lesson's starter
Note which of S1 to S3 and C1 to C3 had the most wrong answers. Use those as the first recall questions next lesson. Good bank: "What does a header contain?", "Who reassembles the packets?", "What is a hop?"

---

# 2. student-page.html

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>How data travels across the internet</title>
<style>
  body{font-family:system-ui,-apple-system,Segoe UI,Arial,sans-serif;margin:0;background:#f3f6fb;color:#1c2a3a;line-height:1.5}
  .wrap{max-width:760px;margin:0 auto;padding:16px}
  h1{font-size:1.5rem;margin:8px 0 4px}
  h2{font-size:1.2rem;margin-top:0}
  .bar{display:flex;gap:6px;margin:10px 0}
  .bar span{flex:1;height:8px;border-radius:4px;background:#cdd7e5}
  .bar span.on{background:#1f7a8c}
  .card{background:#fff;border-radius:12px;padding:18px;margin:12px 0;box-shadow:0 1px 4px rgba(0,0,0,.08)}
  .tip{background:#fff6dc;border-left:5px solid #e0a800;padding:10px 12px;border-radius:6px;margin:12px 0}
  .q{margin:16px 0;padding-top:10px;border-top:1px solid #e3e9f1}
  .q:first-of-type{border-top:0}
  .opt{display:block;width:100%;text-align:left;margin:6px 0;padding:10px 12px;border:2px solid #cdd7e5;background:#fff;border-radius:8px;font-size:1rem;cursor:pointer}
  .opt:hover{border-color:#1f7a8c}
  .opt.right{border-color:#2e9e5b;background:#e6f6ec}
  .opt.wrong{border-color:#d1495b;background:#fde8eb}
  .fb{font-weight:600;margin:4px 0 0}
  button.main{background:#1f7a8c;color:#fff;border:0;border-radius:8px;padding:10px 16px;font-size:1rem;cursor:pointer;margin:4px 6px 4px 0}
  button.alt{background:#fff;color:#1f7a8c;border:2px solid #1f7a8c;border-radius:8px;padding:8px 14px;font-size:1rem;cursor:pointer;margin:4px 6px 4px 0}
  textarea{width:100%;box-sizing:border-box;min-height:110px;font:inherit;padding:8px;border:2px solid #cdd7e5;border-radius:8px}
  textarea.short{min-height:60px}
  select{font-size:1rem;padding:6px;border-radius:6px;border:2px solid #cdd7e5}
  .pk{display:inline-block;background:#e8f3f6;border:2px solid #1f7a8c;border-radius:8px;padding:8px 12px;margin:4px;min-width:90px;text-align:center}
  .pk b{display:block;font-size:.8rem;color:#1f7a8c}
  .sortrow{display:flex;gap:10px;align-items:center;margin:8px 0;flex-wrap:wrap}
  .sortrow .t{flex:1;min-width:220px}
  .summary{background:#eef2f8;border-radius:8px;padding:12px;margin-top:16px}
  .summary pre{white-space:pre-wrap;font-family:inherit;margin:6px 0}
  .hidden{display:none}
  table{border-collapse:collapse;width:100%}
  td,th{border:1px solid #cdd7e5;padding:6px 8px;text-align:left}
  th{background:#e8f3f6}
</style>
</head>
<body>
<div class="wrap">
<h1>How data travels across the internet</h1>
<div class="bar" id="bar"><span></span><span></span><span></span><span></span></div>

<!-- PAGE 1 -->
<div class="page" id="p1">
  <div class="card">
    <h2>Page 1: Warm-up</h2>
    <p>Answer from memory, no peeking at your notes. Pick how sure you are first, then choose your answer.</p>
    <div id="qs-p1"></div>
    <div class="summary">
      <b>Your page 1 summary</b>
      <pre id="sum1"></pre>
      <button class="main" onclick="copySum(1)">Copy my summary</button>
      <span id="cp1"></span>
      <p>Paste it into the Zoom chat, then move on.</p>
    </div>
    <button class="main" onclick="go(2)">Next page</button>
  </div>
</div>

<!-- PAGE 2 -->
<div class="page hidden" id="p2">
  <div class="card">
    <h2>Page 2: Following a message across the internet</h2>
    <p>Imagine you send a photo to a friend. That photo is far too big to squeeze down the internet in one go, so your device does something clever.</p>
    <p><b>Step 1. Chop it up.</b> Your device splits the photo into lots of small chunks called <b>packets</b>.</p>
    <p><b>Step 2. Label each one.</b> Every packet gets a label called a <b>header</b>, like the address on an envelope. The chunk of photo inside is called the <b>payload</b>.</p>
    <table>
      <tr><th>Header (the label)</th><th>Payload (the contents)</th></tr>
      <tr><td>Where it came from (sender's IP address)<br>Where it is going (destination IP address)<br>Packet number (for example 2 of 4)<br>Hop limit (a countdown, explained below)</td><td>A small piece of your photo</td></tr>
    </table>
    <p><b>Step 3. Pass it along.</b> The packets travel through routers. A router reads the <b>destination address</b> and passes the packet on to the next router. Each jump from one router to the next is called a <b>hop</b>. Every router picks the quickest way onwards at that moment, so packets from the same photo can take <b>different routes</b>.</p>
    <p><b>Step 4. Rebuild it.</b> Packets can arrive in the wrong order. Your friend's device uses the <b>packet numbers</b> to put them back together. If a number is missing, it asks for <b>just that packet</b> to be sent again.</p>
    <p>Sending data this way is called <b>packet switching</b>.</p>
    <div class="tip"><b>Hop limit:</b> every router takes 1 off the hop limit. If it reaches 0 the packet is thrown away, so a lost packet cannot wander around the internet forever.</div>
    <div class="tip"><b>Exam tip:</b> Say that the <b>receiving device</b> puts packets back in order, not the router. Routers only pass packets on.</div>

    <h2>Try it: shuffle the packets</h2>
    <p>This message has been split into 4 packets. Press Send to see them arrive in a random order, then press Rebuild.</p>
    <div id="pkts"></div>
    <button class="main" onclick="sendPk()">Send</button>
    <button class="alt" onclick="rebuildPk()">Rebuild</button>
    <p id="pkmsg" class="fb"></p>

    <h2>Your turn</h2>
    <p>In one sentence: what does a packet's header contain?</p>
    <textarea class="short" id="w0" oninput="upd(2)"></textarea>

    <div class="summary">
      <b>Your page 2 summary</b>
      <pre id="sum2"></pre>
      <button class="main" onclick="copySum(2)">Copy my summary</button>
      <span id="cp2"></span>
      <p>Paste it into the Zoom chat, then move on.</p>
    </div>
    <button class="alt" onclick="go(1)">Back</button><button class="main" onclick="go(3)">Next page</button>
  </div>
</div>

<!-- PAGE 3 -->
<div class="page hidden" id="p3">
  <div class="card">
    <h2>Page 3: Quick check</h2>
    <p>Read all four options. Some wrong answers are tempting.</p>
    <div id="qs-p3"></div>
    <div class="summary">
      <b>Your page 3 summary</b>
      <pre id="sum3"></pre>
      <button class="main" onclick="copySum(3)">Copy my summary</button>
      <span id="cp3"></span>
      <p>Paste it into the Zoom chat, then move on.</p>
    </div>
    <button class="alt" onclick="go(2)">Back</button><button class="main" onclick="go(4)">Next page</button>
  </div>
</div>

<!-- PAGE 4 -->
<div class="page hidden" id="p4">
  <div class="card">
    <h2>Page 4: Put it to work</h2>
    <h3>Task A: Who does the job?</h3>
    <p>Each of these jobs is done by the sender's device, a router, or the receiving device. Choose who, then press Check.</p>
    <div id="sortbox"></div>
    <button class="main" onclick="checkSort()">Check</button>
    <p id="sortfb" class="fb"></p>

    <h3>Task B: Explain it</h3>
    <p>A friend sends you a 2 MB photo. Explain how it gets from their laptop to your phone. Use these words: <b>packets</b>, <b>header</b>, <b>router</b>, <b>reassembled</b>. (4 marks)</p>
    <textarea id="w1" oninput="upd(4)"></textarea>

    <h3>Task C: Last question</h3>
    <div id="qs-p4"></div>

    <div class="summary">
      <b>Your page 4 summary</b>
      <pre id="sum4"></pre>
      <button class="main" onclick="copySum(4)">Copy my summary</button>
      <span id="cp4"></span>
      <p>Paste it into the Zoom chat. Well done!</p>
    </div>
    <button class="alt" onclick="go(3)">Back</button>
  </div>
</div>
</div>

<script>
var QS = [
 {id:"S1",page:1,conf:true,q:"Which device passes data between different networks, such as your home network and the internet?",
  o:["Switch","NIC","Router","Wireless keyboard"],a:2},
 {id:"S2",page:1,conf:true,q:"A switch receives data from a laptop that is meant for a printer on the same network. What does the switch do?",
  o:["Sends it only to the printer","Sends it to every device on the network","Sends it out to the internet","Deletes it"],a:0},
 {id:"S3",page:1,conf:true,q:"What is a NIC?",
  o:["A cable that joins two routers","A program that blocks viruses","A type of web address","A part that lets a device connect to a network"],a:3},
 {id:"C1",page:3,conf:false,q:"Why is a big file split into packets before it is sent?",
  o:["Packets are encrypted automatically, so the file is safe","Small packets can share the network and use different routes, so one big file does not block everyone else","Routers can only store text, not pictures","Smaller files always travel faster than the speed limit of the cable"],a:1},
 {id:"C2",page:3,conf:false,q:"Packets from one message arrive in a different order from the one they were sent in. What happens?",
  o:["The message is deleted and sent again from the start","The first router fixes the order","The message is shown in whatever order the packets arrived","The receiving device uses the packet numbers to put them back in order"],a:3},
 {id:"C3",page:3,conf:false,q:"Which of these is found in the header of a packet?",
  o:["The destination IP address and the packet number","The whole file being sent","The sender's password","A copy of the router's list of routes"],a:0},
 {id:"E1",page:4,conf:false,q:"Which list shows what happens to an email in the correct order?",
  o:["Reassembled, sent across routers, split into packets","Sent across routers, split into packets, reassembled","Split into packets, sent across routers, reassembled","Split into packets, reassembled, sent across routers"],a:2}
];
var L=["A","B","C","D"];
var res={};     // id -> {pick, ok, conf}
var conf={};
function build(){
  QS.forEach(function(q){
    var box=document.getElementById("qs-p"+q.page);
    var d=document.createElement("div"); d.className="q";
    var h='<p><b>'+q.id+'.</b> '+q.q+'</p>';
    if(q.conf){
      h+='<p>How sure are you? <select id="cf'+q.id+'" onchange="conf[\''+q.id+'\']=this.value;upd('+q.page+')">'+
         '<option value="">Choose...</option><option>Guessing</option><option>Think so</option><option>Certain</option></select></p>';
    }
    q.o.forEach(function(t,i){
      h+='<button class="opt" id="'+q.id+'_'+i+'" onclick="pick(\''+q.id+'\','+i+')">'+L[i]+'. '+t+'</button>';
    });
    h+='<p class="fb" id="fb'+q.id+'"></p>';
    d.innerHTML=h; box.appendChild(d);
  });
}
function pick(id,i){
  if(res[id]) return;
  var q=QS.filter(function(x){return x.id===id})[0];
  var ok=(i===q.a);
  res[id]={pick:i,ok:ok};
  document.getElementById(id+"_"+i).className="opt "+(ok?"right":"wrong");
  if(!ok) document.getElementById(id+"_"+q.a).className="opt right";
  document.getElementById("fb"+id).textContent = ok ? "Correct." : "Not quite. The right answer is " + L[q.a] + ".";
  upd(q.page);
}
// sort task: bucket order is Sender, Router, Receiver
var BK=["Sender's device","Router","Receiving device"];
var ITEMS=[
 {t:"Reads the destination IP address and decides where to send the packet next",b:1},
 {t:"Uses the packet numbers to put the packets back in order",b:2},
 {t:"Splits the file into packets",b:0},
 {t:"Passes the packet on to the next router along the route",b:1},
 {t:"Adds a header with the addresses and packet number to each packet",b:0},
 {t:"Notices a packet is missing and asks for it to be sent again",b:2}
];
var sortDone=false, sortScore="";
function buildSort(){
  var h="";
  ITEMS.forEach(function(it,i){
    h+='<div class="sortrow"><span class="t">'+(i+1)+'. '+it.t+'</span><select id="so'+i+'" onchange="upd(4)"><option value="">Choose...</option>';
    BK.forEach(function(b,j){h+='<option value="'+j+'">'+b+'</option>';});
    h+='</select><span id="sr'+i+'"></span></div>';
  });
  document.getElementById("sortbox").innerHTML=h;
}
function checkSort(){
  var right=0, filled=0;
  ITEMS.forEach(function(it,i){
    var v=document.getElementById("so"+i).value, r=document.getElementById("sr"+i);
    if(v===""){r.textContent="";return;}
    filled++;
    if(parseInt(v,10)===it.b){right++;r.textContent=" correct";}
    else{r.textContent=" try again";}
  });
  sortScore=right+"/"+ITEMS.length;
  document.getElementById("sortfb").textContent = filled<ITEMS.length ? "Choose an answer for every job first." : ("You got "+right+" out of "+ITEMS.length+".");
  upd(4);
}
// packet demo
var base=[{n:1,t:"Meet me"},{n:2,t:"at the"},{n:3,t:"park"},{n:4,t:"at six"}];
var cur=base.slice(), sentOnce=false;
function drawPk(){
  var h="";
  cur.forEach(function(p){h+='<div class="pk"><b>Packet '+p.n+' of 4</b>'+p.t+'</div>';});
  document.getElementById("pkts").innerHTML=h;
}
function sendPk(){
  var a=base.slice();
  do{ a.sort(function(){return Math.random()-0.5;}); }
  while(a.every(function(p,i){return p.n===i+1;}));
  cur=a; sentOnce=true; drawPk();
  document.getElementById("pkmsg").textContent="They arrived in a muddled order. Can your friend's device read the message like this?";
}
function rebuildPk(){
  if(!sentOnce){document.getElementById("pkmsg").textContent="Press Send first.";return;}
  cur=base.slice(); drawPk();
  document.getElementById("pkmsg").textContent="The packet numbers let the receiving device put the message back together: Meet me at the park at six.";
}
// pages, summaries
function go(n){
  for(var i=1;i<=4;i++){document.getElementById("p"+i).className="page"+(i===n?"":" hidden");}
  var s=document.querySelectorAll("#bar span");
  for(var j=0;j<s.length;j++){s[j].className=(j<n?"on":"");}
  window.scrollTo(0,0);
}
function upd(p){
  var lines=["Page "+p+" summary"];
  QS.filter(function(q){return q.page===p}).forEach(function(q){
    var r=res[q.id];
    var l=q.id+": "+(r?L[r.pick]+" ("+(r.ok?"correct":"not yet")+")":"not answered");
    if(q.conf) l+=", confidence: "+(conf[q.id]||"not chosen");
    lines.push(l);
  });
  if(p===2){ lines.push("Header sentence: "+(document.getElementById("w0").value||"(blank)")); }
  if(p===4){
    lines.push("Task A: "+(sortScore||"not checked"));
    lines.push("Task B: "+(document.getElementById("w1").value||"(blank)"));
  }
  document.getElementById("sum"+p).textContent=lines.join("\n");
}
function copySum(p){
  upd(p);
  var txt=document.getElementById("sum"+p).textContent, el=document.getElementById("cp"+p);
  function done(){el.textContent=" Copied!";}
  if(navigator.clipboard&&navigator.clipboard.writeText){
    navigator.clipboard.writeText(txt).then(done,function(){fallback();});
  } else {fallback();}
  function fallback(){
    var t=document.createElement("textarea"); t.value=txt; document.body.appendChild(t);
    t.select(); try{document.execCommand("copy");done();}catch(e){el.textContent=" Select the text above and copy it.";}
    document.body.removeChild(t);
  }
}
build(); buildSort(); drawPk();
for(var k=1;k<=4;k++){upd(k);}
go(1);
</script>
</body>
</html>
```

---

# 3. homework.md

## Homework: How data travels (20 minutes)

Do these from memory first, then check your notes. Write your answers in your book or a document and bring them to the next lesson.

### Part 1: Quick-fire (5 minutes)

**H1.** What is a "hop"?

A. One step of a packet from one router to the next
B. A packet that has been lost on the way
C. The part of a packet that holds the data
D. A copy of the file kept by the sender

**H2.** Why does every packet carry a hop limit that counts down?

A. So the receiver knows how fast it travelled
B. So a packet stuck going round in circles is eventually thrown away
C. So the receiver knows how long the message is
D. So the sender's address stays secret

**H3.** A message is sent as 10 packets. Packet 6 never arrives. What happens?

A. Everything is sent again from packet 1
B. The receiving device guesses what was in packet 6
C. The routers delete the other nine packets
D. The receiving device notices packet 6 is missing and asks for just that packet again

### Part 2: Recall from last lesson and today (8 minutes)

4. Give **two** jobs of a router. (2 marks)
5. Explain the difference between a switch and a router. (2 marks)
6. What is the job of a NIC? (1 mark)
7. Name the two main parts of a packet and say what each one holds. (2 marks)

### Part 3: Stretch (7 minutes)

8. Imagine the internet sent every message down one single dedicated line between two places and held that line for the whole time, instead of using packets. Give **two** problems with this, and explain how packet switching solves each. (4 marks)

---

# 4. mark-scheme.md

## Student page (marked live or afterwards)

**Starter and check (S1 to S3, C1 to C3, E1):** one mark each. Answers are on `solutions.md`.

**Sort task (Task A):** 6 items, one mark each.

**Task B (written, 4 marks).** Credit one mark for each point, up to four:
1. The file/photo is split (broken up) into small packets.
2. Each packet has a header containing the addresses (sender and destination) and a packet number.
3. Routers read the destination address and pass each packet on towards it (accept "hop by hop" or "choose the best route").
4. Packets may take different routes and arrive out of order, so the receiving device **reassembles** them using the packet numbers.

Also credit (but still within the maximum of 4): a missing packet is requested again.

**Answers that do not get the mark:**
- "The router puts them back in order" (the receiving device does this).
- "The packets all take the same route" or "they travel in a line".
- "The whole photo is sent in one piece" or "the photo is compressed" with no mention of packets.
- Using the word "packets" without saying what happens to them (for example "the photo is sent in packets" alone gets point 1 only).

**Model answer.** The photo is split into small packets. Each packet gets a header with the sender's and destination's IP addresses and a packet number. The packets go through routers, which read the destination address and pass each packet on to the next router. Packets may take different routes and arrive out of order, so my phone uses the packet numbers to reassemble the photo. If any packet is missing, it asks for that one to be sent again.

## Homework

| Q | Answer | Marks | Do not accept |
|---|---|---|---|
| H1 | A | 1 | |
| H2 | B | 1 | |
| H3 | D | 1 | |
| 4 | Any two: reads the destination address; chooses the next hop / best route; passes packets on; connects different networks (for example home network to internet). 1 mark each. | 2 | "Sends the internet to your house"; "makes Wi-Fi" alone |
| 5 | Switch: connects devices **within** one network and sends data only to the intended device (1). Router: connects **different** networks and chooses the route between them (1). | 2 | "A router is bigger"; "a switch is wireless" |
| 6 | Lets a device connect to a network (accept: network interface card; connects a computer to a network with a cable or wirelessly). | 1 | "The wire"; "boosts the signal" |
| 7 | Header: addresses (sender and destination), packet number, hop limit (1). Payload: the actual chunk of data being sent (1). | 2 | "Header is the top of the file"; "payload is the password" |
| 8 | Up to 4 marks, 2 per problem. Problem: one line used by one conversation means everyone else waits or is blocked (1); packet switching lets many messages share the same lines at once (1). Problem: if the line breaks or is busy, the whole message fails (1); packets can be sent a different way and only missing ones are resent (1). Also accept: the line is wasted while nobody is sending (1); packet switching fills the gaps with other people's packets (1). | 4 | Answers about speed only, with no reason |

**Total for homework: 15 marks** (3 + 2 + 2 + 1 + 2 + 1 + 4 = 15).

---

# 5. solutions.md

One-screen answer key for approving work in class. Numbers match the student page.

**Page 1: Warm-up**
- S1: **C** (Router)
- S2: **A** (Only to the printer)
- S3: **D** (Lets a device connect to a network)

Look at the confidence column: "Certain" with a wrong answer means reteach that device.

**Page 2**
- Header sentence: accept sender's and destination IP addresses, packet number, hop limit. Header does **not** hold the data.

**Page 3: Check**
- C1: **B** (small packets share the network and use different routes)
- C2: **D** (receiving device uses the packet numbers)
- C3: **A** (destination IP address and packet number)

**Page 4**
- Task A (sort): 1 Router, 2 Receiving device, 3 Sender's device, 4 Router, 5 Sender's device, 6 Receiving device.
- Task B (4 marks): split into packets, header with addresses and packet number, routers read destination and pass on, receiving device reassembles using packet numbers (also accept missing packet resent). Watch for "router puts them in order".
- E1: **C** (split, sent across routers, reassembled)

**Homework**
- H1 **A**, H2 **B**, H3 **D**. Short answers are in `mark-scheme.md`.

**Answer-pattern check (run with the no-answer-patterns script):**
- Multiple-choice key across the whole pack (S1 S2 S3 C1 C2 C3 E1 H1 H2 H3): `CADBDACABD`, checker result: clean (no repeats, runs, staircases, alternation, repeating blocks, or lopsided letters; A 3, B 2, C 2, D 3).
- Sort task bucket order (Sender = A, Router = B, Receiver = C): `BCABAC`, checker result: clean.

ANSWER KEY: C A D B D A C A B D
