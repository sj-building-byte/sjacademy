# SJ Academy video and motion playbook

**Version:** 1.2, October 2026
**Builds on:** `SJ-ACADEMY-BRAND-BOOK.md` (the core). Sound has its own playbook: `SJ-ACADEMY-SOUND-PLAYBOOK.md`.
**Covers:** ads and motion graphics, teacher reels and lesson clips, student and campus videos, long-form YouTube and brand films.
**Visual reference:** `sj-academy-brand-book.html`, "Motion" section, where every move below plays live.

### The short version

1. **Hook in 2 seconds, brand in 3** through yellow, the highlighter or a face. Never open on a logo.
2. **It must work on mute.** Captions on everything, checked by hand.
3. **Things move like they would on a desk:** paper slides, pens draw, stamps land. Nothing floats, spins or glows.
4. **Two speeds:** Teach (calm, cuts every 2 to 4 seconds) and Hype (on the beat).
5. **Real footage beats graphics.** Shoot with HDR off, a lapel mic and window light.

---

## 1. What this playbook fixes

Before this playbook, each video project made up its own rules. The May/June reel used a serif and gold gradients. The video folder's `frame.md` set Poppins 800 in lowercase on flat orange and brown. The practicals reel used 3D objects on graph paper. Some of those choices were good, but none were written down, so the next video started from zero again.

This playbook sets one motion language that every video shares, and a clear recipe for each kind of video. **`frame.md` in the video ads folder (the "Broadside" preset) is retired.** New HyperFrames projects take their tokens from section 11 of this file.

---

## 2. Five principles

1. **Hook in 2 seconds.** Viewers decide within about two seconds whether to keep watching. Open on a face mid-sentence, a marked paper, a number or a question, never on a logo.
2. **Brand within 3 seconds, through assets.** Yellow, the highlighter, a teacher's face or a small logo should appear in the first three seconds. A logo-only intro card wastes the opening; the full logo belongs on the end card.
3. **Works on mute, rewards sound.** Most feed viewers start with sound off. Every video must make sense with captions and on-screen text alone. Sound then adds energy, timing and the sonic logo.
4. **Show the work.** Marked papers, real classes, real labs, real teachers. A marked answer on screen beats any claim.
5. **Real people, real voices.** Teachers and students speak in their own words. Nobody is scripted to say something they would not say.

---

## 3. Formats and specs

| Type | Aspect | Size | Length | Speed |
|---|---|---|---|---|
| Ad, motion graphic | 9:16 (plus 4:5 and 16:9 cuts) | 1080 x 1920 | 9, 15 or 30 seconds | Hype |
| Teacher reel | 9:16 | 1080 x 1920 | 20 to 60 seconds | Teach, with a Hype opening |
| Lesson clip | 9:16 or 16:9 | 1080 x 1920 or 1920 x 1080 | 45 to 90 seconds | Teach |
| Testimonial | 9:16 and 16:9 | as above | 30 to 60 seconds | Teach |
| Results day, events, behind the scenes | 9:16 | 1080 x 1920 | 10 to 30 seconds | Hype |
| YouTube lesson, past paper walkthrough | 16:9 | 1920 x 1080 or 3840 x 2160 | 8 to 40 minutes | Teach |
| YouTube Short | 9:16 | 1080 x 1920 | 20 to 60 seconds | Teach or Hype |
| Brand film | 16:9 and 9:16 | as above | 45 to 90 seconds | Builds from Teach to Hype |

### Export settings

| Setting | Value |
|---|---|
| Frame rate | 30fps for everything (60fps only for slow-motion shots inside a 30fps edit) |
| Video | H.264 High, SDR (Rec. 709). 15 to 20 Mbps for 1080p, 40 Mbps or more for 4K |
| Audio | AAC, 48kHz, 320kbps, stereo. Loudness per the Sound playbook (about -14 LUFS, peaks at -1 dBTP) |
| Captions | Burned in for social. A separate `.srt` file for YouTube |
| File name | `sj_[type]_[topic]_[aspect]_v[n]_[YYYY-MM-DD].mp4`, for example `sj_ad_a-level-commerce_9x16_v3_2026-10-12.mp4` |

### Safe zones

| Canvas | Keep text, faces and the logo inside |
|---|---|
| 9:16 (1080 x 1920) | Below the top 270px, above the bottom 670px, and clear of the right 230px in the lower half. The usable area is roughly the middle 950 x 980px |
| 9:16 cover frame | The middle 1080 x 1440, so the profile grid crop keeps the title |
| 16:9 (1920 x 1080) | 5% from each edge for text. The bottom-right corner stays clear for the YouTube interface |

---

## 4. The motion language

**Everything moves the way it would on a teacher's desk.** Paper slides and settles. Pens draw. Highlighters swipe. Stamps land with a thud. Nothing floats, spins, glows or bounces like jelly.

### The desk moves

Five moves, and only these. Use them on purpose; each one has a job and a sound (Sound playbook, section 3).

| Move | What it looks like | Job | Timing at 30fps |
|---|---|---|---|
| **Highlighter swipe** | A yellow band grows left to right across the lower half of a word | Marks the key word | 8 frames for a short word, 12 for a longer one. Starts 4 frames after the word lands |
| **Highlighter wipe** | A full-height yellow band sweeps across the frame and reveals the next scene | The signature transition | 12 to 15 frames. At most twice per video |
| **Pen write-on** | Ticks, circles, arrows and underlines draw themselves as strokes | Marks the work, points at proof | Tick 6 frames, arrow 10, circle 14 to 18. Circles start at about 10 o'clock and overshoot slightly, like a real hand |
| **Stamp** | Lands from 130% scale to 100% in 4 frames, rotated 6 to 10 degrees, with a 2px shake for 4 frames | A verdict: a score, a date, "seats full" | 4 frames in, 4 frames of shake |
| **Paper drop** | Paper slides in from the edge, tilted 3 to 6 degrees, and settles to under 1 degree | Brings in an exam paper, a card or a ticket | 18 frames |

### Timing tokens

| Token | Frames at 30fps | Milliseconds | Use |
|---|---|---|---|
| `tick` | 4 | 133 | Stamp hit, cuts on emphasis |
| `quick` | 8 | 267 | Short highlighter, small elements, exits |
| `base` | 12 | 400 | Text entering, most movement |
| `settle` | 18 | 600 | Paper drop, large elements |
| `linger` | 30 | 1000 | Slow reveals, end card logo |

Exits take about two thirds of the time of the matching entrance.

### Easing

| Curve | Value | GSAP equivalent | Use |
|---|---|---|---|
| Enter | `cubic-bezier(0.16, 1, 0.3, 1)` | `expo.out` | Anything arriving: text, paper, cards |
| Move | `cubic-bezier(0.4, 0.14, 0.3, 1)` | `power2.inOut` | Anything moving while it stays on screen |
| Exit | `cubic-bezier(0.7, 0, 0.84, 0)` | `expo.in` | Anything leaving |
| Stamp | `cubic-bezier(0.34, 1.56, 0.64, 1)` | `back.out(1.7)` | Stamps only |
| Pen | `cubic-bezier(0.45, 0, 0.55, 1)` | `sine.inOut` | Strokes drawing on |

Never use elastic or bounce easing on text, and never spin anything.

### Type in motion

- Text arrives by word or by phrase, not letter by letter. A mask-up reveal over `base`, with 70 to 90ms between words.
- Typing letter by letter is allowed only inside a phone format (Notes app, search bar, chat).
- The key word gets the highlighter after the line lands, not at the same time.
- **Hold text long enough to read:** at least 1 second, plus 0.3 seconds per word. Never move text while it is being read.
- Count-ups only for real numbers from `FACTS.md`, and in 1 second or less.

### Two speeds

| | Teach (Level 2) | Hype (Level 3) |
|---|---|---|
| Used for | Lessons, teacher reels, testimonials, YouTube | Ads, results day, events, brand film peaks, the first 3 seconds of a reel |
| Cuts | Every 2 to 4 seconds, on sentences | On the beat, every 1 or 2 beats (about every 0.5 to 1 second at 120 to 140 BPM) |
| Moves | One at a time, `base` and `settle` | Overlapping, `tick` and `quick` |
| Camera | Slow push from 100% to 104% over a shot | Punch-ins to 110% on emphasis, whip pans between shots |
| Music | 80 to 100 BPM, or none under explanation | 120 to 140 BPM |

### Camera on footage and photos

- Slow pushes on stills and talking heads (100% to 104%) keep the frame alive.
- Punch-in cuts (a jump to 110 to 115%) mark emphasis in Hype edits. Use the 4K source so they stay sharp.
- Whip pans are Hype only.
- No 3D parallax on photos, no shaky-cam filters.

### Transitions

| Allowed | Not allowed |
|---|---|
| Hard cut (the default, most of the cuts) | Cross-dissolves, except to show time passing in long-form |
| Highlighter wipe (twice per video at most) | Cube, spin, zoom-blur and glitch transitions |
| Paper slide | Light leaks, lens flares, film burns |
| Whip pan (Hype only) | Preset transitions from editing apps |
| Match cut on a gesture or object | Star, heart or shape wipes |
| J and L cuts (sound leads or trails the picture) | Page turns, tape, sticker effects |

---

## 5. Graphics in video

| Element | Look | Rules |
|---|---|---|
| **Logo** | Horizontal logo, on-light, on-brown or on-yellow to suit the background | 9:16: top of the frame, just below the 270px band, 200 to 260px wide. 16:9: top-left, 5% margin. Fades or slides in as one piece over `base` |
| **Name tag** | White card, 1.5px ink outline, tilted 1 to 2 degrees. Name in Poppins 600, subject and code in Poppins 400 ("Sir Salman, A Level Maths 9709") | Enters with a paper slide, holds 3 seconds, exits `quick`. Once per person per video. 9:16: lower third, above the bottom 670px. 16:9: lower left |
| **Subject chip** | Yellow pill, Poppins 500 uppercase: "9609 · PAPER 3" | Top area. One per video |
| **Chapter card** | Canvas or yellow ground. Chapter title in Poppins 600 | 1.5 seconds. Long-form only |
| **Exam paper** | Off-white paper, exam navy type, red margin line, slight tilt (as on the website) | The main proof device. Text must be readable on a phone |
| **Pen marks on footage** | Red ticks, circles and margin notes drawn over a paper in shot | Only on what matters. One circle per shot |
| **End card** | See section 9 | Every video over 10 seconds |

Graphics stay inside the safe zones. Never place text, tags or stamps over a face.

---

## 6. Captions

Captions are on every video. Three styles, one per job.

| Style | Use | Look | Rules |
|---|---|---|---|
| **Clean** | Lessons, testimonials, long-form, teacher reels | Poppins 500, canvas text on a 70% ink box with 12px corners. 46 to 52px on 9:16, 40 to 46px on 16:9 | Up to 2 lines, 42 characters per line. No faster than 17 characters per second. Each caption on screen 0.8 to 7 seconds. Break lines at natural phrases; keep the bottom line longer |
| **Punch** | Ads, hype reels, the first 3 seconds of any reel | Poppins 700, 64 to 84px, 1 to 4 words at a time. Canvas or ink text with a thin outline for contrast. The key word gets the yellow highlighter | Timed to the speech, word group by word group. Centred, in the lower-middle of the safe area |
| **Note** | Asides, jokes, the teacher's side comment | Caveat 600, orange-brown on light, yellow on dark | Never carries information the viewer needs. One per scene at most |

**Translation rule:** when speech mixes Urdu and English, captions give the meaning in natural English. Do not write Roman Urdu on screen. Keep the speaker's tone and humour. Keep subject terms exactly as spoken: "A*", "Paper 3", "9609", "evaluate".

**Always check automatic captions by hand,** especially names (Kashaan), subject codes and numbers.

---

## 7. Shooting standards

| Area | Standard |
|---|---|
| **Camera** | A recent phone is enough. 4K at 30fps. **Turn HDR and Dolby Vision off** (HDR footage looks washed out or over-bright on Instagram and needs converting). Lock focus and exposure on the face |
| **Orientation** | Shoot vertical for reels. If one shoot serves both YouTube and reels, shoot 4K horizontal with the teacher in the centre third, so a vertical crop still works |
| **Light** | Face the window, or one soft LED panel at 45 degrees. Ceiling tube lights alone turn skin green; set white balance by hand (around 5000K) or fix it in the grade |
| **Sound** | A wireless lapel mic on every speaker. Record 10 seconds of room silence at each setup. Fans and AC off while recording if possible |
| **Framing** | Talking heads: eyes on the upper third line, a little headroom, chest up. Leave space at the bottom for captions |
| **Background** | Real classroom: whiteboard with writing, past papers, shelves. Not a blank wall. No other brands' logos in shot |
| **B-roll** | For every talking-head shoot, 10 extra shots: hands writing, marking, the board, students working (with consent), the corridor, the sign |
| **Grade** | Warm and true to life. No teal-and-orange look, no heavy filters, no LUT presets. Skin looks like skin |

---

## 8. Recipes by video type

### 8.1 Ads and motion graphics

**Job:** get a student (or parent) to book a free demo class.
**Built in:** HyperFrames (the `ads`, `practicals-p34` and `brand-film` projects are the templates), or a footage editor for footage-led ads.

**Beat sheet (15 seconds):**

| Time | Beat | Example |
|---|---|---|
| 0 to 2s | **Hook.** Name the viewer's situation, or show the surprising thing | "Started A Levels this year?" over a marked paper landing |
| 2 to 8s | **Proof.** Show the method or the place | Answer marked 6/12, pen circles the lost marks, rewrite gets 12/12 |
| 8 to 12s | **Offer.** The free demo class | Teacher's face, name tag, "One class free. Then decide." |
| 12 to 15s | **End card** with the sonic logo | Logo, CTA, WhatsApp |

**Rules:**

- Make three or four versions per campaign, each with a different hook or format: footage-led, graphics-led, teacher-led, phone-format.
- Cut every ad into 9, 15 and 30 seconds. The 9-second version is the hook, one proof and the end card.
- Footage-led ads beat graphics-only ads for trust. Use real class and lab footage whenever it exists.
- Do not open on the logo. Do not use a stock music bed that sounds like every other ad (Sound playbook).

### 8.2 Teacher reels and lesson clips

**Job:** teach one thing well, so students follow, save and trust the teacher.

**Series to rotate:**

| Series | Idea | Length |
|---|---|---|
| **Examiner trap** | One mistake the mark scheme punishes, and the fix | 20 to 40s |
| **Mark this** | The teacher marks a sample answer live, out loud | 30 to 60s |
| **One-minute method** | One technique: an 8-mark structure, a calculator trick | 45 to 60s |
| **Myth vs mark scheme** | A common belief, then what actually gets marks | 20 to 30s |
| **From the DMs** | A real student question (anonymous), answered | 20 to 45s |
| **Exam countdown** | One tip a day before a paper | 15 to 30s |

**Layouts for 9:16:**

| Layout | What it is | When |
|---|---|---|
| **Face** | Full-frame teacher, captions in the lower safe area | Opinions, myths, quick tips |
| **Split** | Paper or board on top, teacher's face on the bottom half | Marking, worked examples |
| **Paper cam** | Overhead shot of the paper and hands, voice over | Step-by-step solutions |
| **Board** | Teacher at the whiteboard, wide enough to read | Diagrams, definitions |

**Structure:** hook (2s, Punch captions) > the problem (5s) > the method, shown on paper (most of the video) > the one-line takeaway > soft end card ("More in class. Book a free demo on WhatsApp.").

**Rules:** one idea per video. Teach speed after the opening. One dry joke at most. Teachers speak naturally; captions in English.

### 8.3 Students and campus

**Job:** prove that real students are here, working and getting results.

| Type | Recipe |
|---|---|
| **Testimonial** (30 to 60s) | Student or parent, framed slightly off-centre, looking just past the camera at the interviewer. Ask, do not script: "What was hard before?", "What changed in class?", "What would you tell a friend?". Cut to B-roll of their real class. Name tag with first name and last initial, subject and series |
| **Results day** (10 to 30s) | Reactions as they happen, flash photos, result slips (checked against the statement, with consent). Hype speed, the celebratory sonic logo |
| **A day at SJ** (30 to 60s) | Behind the scenes from arrival to the last class. Hard cuts on the beat, natural sound in between |
| **Lab and practicals** (15 to 30s) | Hands, apparatus, colour changes, close-ups. Real lab footage first, 3D only where footage does not exist |

**Rules:** written consent for every student who appears, speaks or is named (Web playbook, section 13). Never put words in a student's mouth. Never show a result that has not been checked.

### 8.4 Long-form YouTube and brand films

**Job (lessons):** be the video a student finds when they search for that paper or topic, then trust the teacher enough to join.

**Structure of a lesson or past paper walkthrough:**

| Part | Length | What happens |
|---|---|---|
| Cold open | 10 to 20s | The question on screen, and the trap most students fall into. No intro yet |
| Bumper | 3s | The short sonic logo with the logo and the subject chip |
| Chapters | Most of the video | One chapter per question part. Chapter cards in Poppins 600. Paper on screen with live pen marking |
| A mid-video surprise | Around minute 3 to 4 | The examiner's comment, a common wrong answer, a shortcut. It keeps people watching |
| Recap | 30s | The method in three lines on one card |
| End screen | 20s | Two video links, subscribe, the class offer, the full sonic logo |

**Rules:**

- Title and thumbnail must match what the first minute delivers.
- Add chapters in the description, and an `.srt` caption file.
- Cut three Shorts from every long video: the trap, the method, the takeaway.
- **Thumbnails:** the teacher's face with a clear expression, 2 to 4 words in Poppins 700, one paper element (a circled score, a red tick), the subject code chip, yellow present. It must read at 160px wide. Each series keeps one thumbnail layout.

**Brand films** (45 to 90s): footage first. They start at Teach speed with real moments and natural sound, build to a Hype section cut on the beat, and close on the end card with the full sonic logo. The 44-second "Meet the squad" film is the model for structure.

---

## 9. End card

| | 9:16 | 16:9 |
|---|---|---|
| Ground | Yellow, brown or ink (match the video's last scene) | Same |
| Logo | Horizontal or stacked, centred in the safe area, at least 420px wide | Horizontal, centred, at least 560px wide |
| Line | One line: the offer or the next step ("One class free. Then decide.") | Same |
| CTA | Button shape: "Book a free demo on WhatsApp" | Same, plus the YouTube end screen elements |
| Contact | WhatsApp +92-336-2144454 and sjacademy.pk | Same |
| Sound | The full sonic logo, starting as the logo lands | Same |
| Length | 2.5 to 3 seconds (20 seconds on YouTube end screens) | |

---

## 10. Tools

- **HyperFrames** for motion graphics and ads. Copy the tokens in section 11 into every new project. Read each project's `BRIEF.md` before editing.
- **A footage editor** (CapCut, Premiere, DaVinci Resolve or Final Cut) for footage-led videos. Install Poppins and Caveat. Do not use the app's preset fonts, transitions, stickers or filters.
- **Templates to build next** (in order): caption styles, name tag, end card (9:16 and 16:9), subject chip, highlighter wipe, thumbnail layout per series.

---

## 11. Video tokens

Paste into any HTML or HyperFrames composition. Sizes in `cqw` scale with the frame.

```css
:root{
  /* colour */
  --sj-yellow:#FCE004; --sj-yellow-light:#FFF9CC; --sj-ink:#151515; --sj-canvas:#F7F5EF;
  --sj-brown:#453516; --sj-navy:#1B2A4A; /* navy: exam paper text only */
  --sj-cta:#CC4A00; --sj-pen:#D63A2F; --sj-pen-text:#B92F25; --sj-pen-note:#B54200;
  --sj-scrim:rgba(21,21,21,.7);
  /* type */
  --sj-font:"Poppins",sans-serif; --sj-hand:"Caveat",cursive;
  /* timing (30fps) */
  --t-tick:133ms; --t-quick:267ms; --t-base:400ms; --t-settle:600ms; --t-linger:1000ms;
  /* easing */
  --e-enter:cubic-bezier(.16,1,.3,1); --e-move:cubic-bezier(.4,.14,.3,1);
  --e-exit:cubic-bezier(.7,0,.84,0); --e-stamp:cubic-bezier(.34,1.56,.64,1);
  --e-pen:cubic-bezier(.45,0,.55,1);
}
/* the highlighter: lower half of the letters, soft ends */
.sj-hl{background:linear-gradient(100deg,transparent 0,var(--sj-yellow) .14em,var(--sj-yellow) calc(100% - .14em),transparent 100%) no-repeat 0 calc(100% - .31em)/100% .4em;padding:0 .14em;margin:0 -.14em}
```

---

## 12. Checklist before publishing

- [ ] Hook in the first 2 seconds; no logo-only opening
- [ ] Yellow, highlighter, a teacher's face or the logo in the first 3 seconds
- [ ] Makes sense on mute; captions checked by hand
- [ ] Only Poppins and Caveat; only brand colours; no gradients except the photo scrim
- [ ] Desk moves only; no preset transitions
- [ ] Text inside the safe zones, held long enough to read
- [ ] Facts from `FACTS.md`; sample work labelled
- [ ] Written consent for every student shown, heard or named
- [ ] Music licensed for this use; sonic logo on the end card
- [ ] Exported at 30fps, SDR, about -14 LUFS, file named to the pattern
