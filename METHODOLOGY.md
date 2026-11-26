# METHODOLOGY — how the one-line roast was written and chosen

## The entry

> **My smartwatch congratulates me for standing up, as if sitting down was the one job I had and I failed it.**

105 characters, 105 bytes — under the bounty gate of 1–200
characters. Single line, no trailing newline in `entry.txt`, so the
judged text is exactly this line.

## The judge this entry is built for

The bounty is judged pairwise by a house judge (z-ai/glm-5.3-flash)
briefed as a comedy editor who has read a thousand one-line jokes
and can tell a fresh roast from a reheated one. Each pair is judged
in both orders, no ties, margin 1–5, over three blind rounds. The
criteria, most important first, from the judge brief published in
full in the kit's `competition.yaml`:

1. Roasts a gadget or app people use every day in a single line; a
   line that never names or clearly targets a daily gadget or app
   loses to any line that roasts one.
2. Is actually funny: the joke lands on a first read, with a sting
   of recognition rather than a mild grumble.
3. Feels fresh: an angle, comparison or detail not seen before, not
   the obvious complaint everyone makes about that product.
4. Is neatly worded: tight, well timed, no wasted words, and
   comfortably inside the character limit.
5. Sounds like one person's specific gripe, with a concrete detail
   about how the thing actually behaves, not a generic complaint
   that could be about anything.

Crudeness for its own sake does not count. Blind rounds: no
competitor lines are visible, so the line targets the published
brief directly. The field at build time was about 4,167 entries,
and only the top 500 on the development board reach the final heat
— so the line has to beat the house anchors and rungs in
development, not just be charming. An exact tie on judge win rate
goes to the smaller text (fewer bytes) before the earlier receipt,
so a short line carries a real tie-break advantage: 105 characters
is comfortably short.

The design rule that follows from that brief: the line must name
one daily gadget in its first words, roast one precise, lived-in
failure of it (not "technology bad"), find an angle other than the
brief's own examples (the phone dying at 4 p.m., the rating-prompt
app, the firmware-update kettle — all three will be heavily used by
the field, so none of them is the entry), and save its turn for the
last few words.

## Step 1 — 30 candidates, drafted in-session

Each candidate was scored 1–10 on five axes matching the judge's
criteria: **specific** (names one daily gadget and one precise
failure), **funny** (lands in one read, sting of recognition),
**original** (fresh angle, not the obvious complaint),
**tight** (neatly worded, no wasted words), **fresh** (a detail or
comparison not seen before). Lengths are characters including
spaces. All 30 were drafted fresh in this session (see
`candidates.txt`), each a different gadget/app with a different
specific grievance; none copies the sibling one-line entries (#3 /
#7 / #8 / #9 / #10 / #11 / #12 / #13) or the brief's three examples.

| # | Gadget / app | Line (short form) | Chars | Spec | Funny | Orig | Tight | Fresh | Total /50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Phone Face ID | stranger in my own bed | 125 | 9 | 9 | 8 | 8 | 8 | 42 |
| 2 | Printer | boarding pass at 6 a.m. | 96 | 9 | 8 | 7 | 9 | 7 | 40 |
| 3 | Robot vacuum | mapped the flat, eats the cable | 115 | 9 | 8 | 8 | 8 | 8 | 41 |
| 4 | **Smartwatch** | **congratulates me for standing up** | **105** | **9** | **9** | **9** | **9** | **9** | **45** |
| 5 | Earbuds | left side filed for divorce | 104 | 8 | 8 | 8 | 8 | 7 | 39 |
| 6 | Laptop fan | numbers personally offended it | 105 | 8 | 8 | 7 | 8 | 7 | 38 |
| 7 | Microwave | beeps again an hour later | 106 | 8 | 7 | 6 | 8 | 6 | 35 |
| 8 | Autocorrect | love letters to my manager | 112 | 9 | 8 | 7 | 8 | 7 | 39 |
| 9 | Password manager | forgot the one password | 103 | 9 | 8 | 8 | 9 | 8 | 42 |
| 10 | Streaming app | "Are you still watching?" | 103 | 8 | 8 | 6 | 8 | 6 | 36 |
| 11 | Smart fridge | holding the milk | 99 | 9 | 8 | 8 | 9 | 8 | 42 |
| 12 | Wi-Fi router | restart during a video call | 115 | 8 | 7 | 6 | 7 | 6 | 34 |
| 13 | Smart speaker | ignores the one I shouted | 96 | 8 | 7 | 6 | 8 | 6 | 35 |
| 14 | Smart lock | wet, cold, or, apparently, mine | 108 | 9 | 9 | 8 | 9 | 9 | 44 |
| 15 | Bluetooth | neighbour's speaker first | 90 | 9 | 8 | 9 | 9 | 9 | 44 |
| 16 | TV remote | the button that does nothing | 102 | 8 | 7 | 6 | 8 | 6 | 35 |
| 17 | Washing machine | sock + little song | 99 | 8 | 8 | 6 | 9 | 6 | 37 |
| 18 | Alarm | snooze nine times, betrayed | 102 | 8 | 8 | 7 | 8 | 7 | 38 |
| 19 | Fitness app | a gym that never lets you leave | 103 | 8 | 7 | 7 | 8 | 7 | 37 |
| 20 | Coffee machine | tiny landlord, rent in vinegar | 97 | 8 | 8 | 8 | 8 | 8 | 41 |
| 21 | GPS | road closure it knew about | 91 | 8 | 7 | 7 | 9 | 7 | 38 |
| 22 | Phone storage | never when I photograph lunch | 110 | 8 | 7 | 7 | 8 | 7 | 37 |
| 23 | Banking app | password I set in 2019 | 99 | 8 | 8 | 7 | 8 | 7 | 38 |
| 24 | Doorbell | films the postman, the cat, a leaf | 94 | 9 | 8 | 8 | 9 | 8 | 42 |
| 25 | Spacebar | takes the day off | 96 | 7 | 7 | 6 | 8 | 6 | 34 |
| 26 | Earbuds case | one day longer than the earbuds | 104 | 8 | 7 | 7 | 8 | 7 | 37 |
| 27 | Thermostat | heats the house when I'm away | 98 | 8 | 7 | 8 | 8 | 8 | 39 |
| 28 | Calendar | confidence of a man on time | 107 | 8 | 8 | 7 | 8 | 7 | 38 |
| 29 | Dishwasher | cooked dinner and wants applause | 93 | 8 | 8 | 7 | 9 | 7 | 39 |
| 30 | Charger cable | charging is now a yoga pose | 88 | 8 | 8 | 7 | 9 | 7 | 39 |

Why the low scorers lost: #7, #10, #12, #13, #16, #17 are the
most-told complaints about their gadgets (beeping microwaves,
"Are you still watching?", Wi-Fi dropping on calls, speakers
mishearing, remote buttons, sock-eating washers) — fresh (criterion
3) is their weakest axis, and in a 4,167-entry field the obvious
complaint is the one a hundred other entries already make. #12
also repeats the Wi-Fi angle a sibling bounty (#11) already used.
#2, #6, #21, #22 are solid but single-beat: one observation, no
turn in the last words.

## Step 2 — head-to-heads among the top three

- **#4 smartwatch (45) vs #14 smart lock (44):** #14's twist is a
  three-item list ending on "mine" — very neat, and the wet-hands
  failure is universally recognised. But it is one beat. #4 has
  two: the congratulation itself is the insult, and the second
  clause reframes sitting as a job failed. #4 wins on funny and
  on freshness (praise-as-insult is an angle nobody frames that
  way; fingerprint-failing-when-wet is a known complaint).
- **#4 smartwatch (45) vs #15 Bluetooth (44):** #15 is the
  shortest (90 chars) and the freshest single observation —
  connecting to the neighbour's speaker before your own car. But
  again one beat, and its sting is mild. #4's second clause
  ("the one job I had and I failed it") is the sharper sting of
  recognition, and it lands last. #4 wins.
- **#4 vs #1 Face ID (42):** #1's last line ("a stranger in my
  own bed") is a strong image, but Face ID failing in the morning
  is a familiar complaint; #4's angle is fresher and its two-beat
  structure survives a first read better.

## Step 3 — refinement of the winner

- **4a (chosen, 105 chars):** "My smartwatch congratulates me for
  standing up, as if sitting down was the one job I had and I failed
  it."
- **4b (101):** "…as if sitting was the one job I had, and I failed
  it." — "sitting" without "down" reads thinner; the comma breaks
  the run-up to the punch. Rejected.
- **4c (100):** "My smartwatch applauds me for standing up, …" —
  "applauds" is showier, but "congratulates" is the watch's own
  formal language for a stand goal, which is what makes the praise
  funny. Rejected.
- **4d (116):** "…for standing up at 10 a.m., …" — a timestamp adds
  a detail but no laugh, and costs tightness. Rejected.
- **4e (95):** "…like sitting down was my one job and I blew it."
  — "blew it" is punchier in isolation, but "failed it" keeps the
  job-performance register ("the one job I had") that the joke is
  built on. Rejected.

Final line verified programmatically: 105 characters, 105 bytes,
one line, no trailing newline, inside the 1–200 gate.

## Why this line maps to the judge's criteria

1. **Names a daily gadget:** "My smartwatch" in the first two
   words; the stand congratulation is a behaviour every smartwatch
   owner recognises.
2. **Funny on first read:** the praise is the insult, and the
   second clause delivers the sting ("the one job I had and I
   failed it") in the last words.
3. **Fresh:** not the obvious smartwatch complaint (battery,
   nagging, step counts) and not any of the brief's three examples;
   the angle is the watch congratulating you, not failing you.
4. **Neatly worded:** 105 characters, two clauses, no wasted
   words; short enough to carry the smaller-text tie-break.
5. **One person's specific gripe:** the concrete behaviour is the
   stand-up congratulation itself, not a generic "technology bad".
