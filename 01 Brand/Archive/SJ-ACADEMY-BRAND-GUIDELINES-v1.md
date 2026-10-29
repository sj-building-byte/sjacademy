# SJ Academy brand guidelines

**Version:** 2.0, October 2026
**Status:** Current. For new pages this replaces the visual rules in `AI-LANDING-PAGE-DESIGN-GUIDE.md`.
**Reference build:** the homepage (`24-homepage-elementor-widget.html`)
**Visual reference:** `26-sj-academy-brand-kit.html` shows every element in this guide, live.

Give this file to any designer, developer or AI model before they build a page for sjacademy.pk.

---

## 1. The idea

**SJ Academy looks like a good teacher's notebook.**

The brand promise is "Cambridge doesn't mark effort. It marks method." The design shows that method: highlighted key terms, marked answers, pen notes in the margin, photos taped to the page. Everything decorative is something you would find on a teacher's desk.

Three tests for any page:

1. **Would a teacher have made this mark?** Every circle, note and stamp points at something that matters. If it is only decoration, remove it.
2. **Is there more paper than pen?** Most of the page is calm: off-white, black type, white space. The hand-made marks are rare, which is why they are noticed.
3. **Could you tell it is SJ Academy with the logo covered?** The highlighter, the offset card and the handwriting should make it recognisable.

---

## 2. Colour

| Name | Value | Job |
|---|---|---|
| Yellow | `#FCE004` | Highlight, selected state, final CTA band |
| Light yellow | `#FFF9CC` | Result panels, sticky notes, hover |
| Orange | `#FE6100` | Pen marks and stars only. Never behind white text |
| CTA orange | `#CC4A00` | Primary buttons, handwritten notes |
| Brown | `#453516` | One method band per page, avatars |
| Ink | `#151515` | Headings, outlines |
| Text | `#2B2B2B` | Body copy |
| Muted | `#66625A` | Secondary text |
| Canvas | `#F7F5EF` | Page background |
| Line | `#E2DDD0` | Dividers |
| Kraft | `#E9DFC9` | Tabs, ticket stubs, tape on yellow |
| Pen red | `#D63A2F` | Marks, stamps, margin notes |
| Exam ink | `#1B2A4A` | Text on exam paper |
| WhatsApp | `#25D366` | WhatsApp buttons, black text |

Rules:

- Yellow is a highlighter, not a background, except for the final call-to-action band.
- White text never sits on bright orange (`#FE6100`). Buttons with white text use `#CC4A00`.
- Brown is used for one full-width band per page at most.
- Red pen is for marking only: marks, stamps and margin notes.

```css
/* put on the page wrapper */
--sj-yellow:#FCE004;\n--sj-yellow-light:#FFF9CC;\n--sj-orange:#FE6100;\n--sj-cta:#CC4A00;\n--sj-brown:#453516;\n--sj-ink:#151515;\n--sj-text:#2B2B2B;\n--sj-muted:#66625A;\n--sj-canvas:#F7F5EF;\n--sj-white:#FFFFFF;\n--sj-line:#E2DDD0;\n--sj-kraft:#E9DFC9;\n--sj-whatsapp:#25D366;\n--sj-pen:#D63A2F;\n--sj-exam-ink:#1B2A4A;\n--sj-hand:'Caveat','Segoe Script','Bradley Hand',cursive;\n--sj-font:'Poppins',system-ui,-apple-system,'Segoe UI',sans-serif
```

---

## 3. Type

| Use | Font | Weight | Size (phone / desktop) |
|---|---|---|---|
| H1 | Poppins | 400 | 32px / 54px, line height 1.1 to 1.18, letter spacing -0.4 to -1.4px |
| H2 | Poppins | 400 | 26px / 38px |
| H3, card titles | Poppins | 400 or 500 | 17px |
| Body | Poppins | 400 | 16px minimum, line height 1.6 |
| Buttons, labels, eyebrows | Poppins | 500 | 11px to 15.5px |
| Large numbers | Poppins | 400 | 27px / 36px |
| Handwritten notes | Caveat | 600 | 18px to 30px |

Rules:

- Two families only. Do not load the theme's GT Walsheim on new pages.
- Never above weight 500. Never weight 300 for body text.
- Sentence case everywhere. Uppercase only for the kicker pill, eyebrows and box stamps.
- Load fonts without blocking the page:

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
```

---

## 4. Page families

Pick the family by what the visitor came to do. This is what stops every page looking like the homepage: each family has its own surface, its own hero and its own set of elements.

| Family | Pages | Surface | Hero | Elements to draw from |
|---|---|---|---|---|
| **Enrol** | Homepage, level pages, subject tuition pages | Dotted notebook | Class finder or subject card in an offset card | Polaroid with tape, circle, handwritten note, proof strip, exam paper |
| **Tool** | IBCC calculator, grade strategy, admission criteria, quizzes | Graph paper | The tool itself in an offset card | Index tabs, round stamp for the result, sticky note for caveats, steps |
| **Resource** | Past papers, definitions, ebooks, date sheets | Ruled paper | Search or filter bar | Index tabs, paperclip on downloads, ink tag for "new", soft tiles |
| **Reading** | Blog posts and guides | Plain canvas | Headline and a one-paragraph answer | Margin note, pen underline, sticky note for the takeaway, star |
| **Proof** | Results wall, reviews, teachers | Dotted notebook | A wall of pinned cards | Pinned cards, grade badges, ink tag, polaroids with tape |
| **Event** | Workshops, mock exams, practical batches | Dotted notebook with one brown band | Ticket with the date | Ticket, box stamp, ticks, handwritten note |
| **Info** | Fees, timetable, contact, policies | Plain canvas | A clear table or card | One circle on the key number. Nothing else |

### How to vary pages inside a family

Every page uses all four **signature** elements (highlighter, kicker pill, one offset card, the button set). Beyond that:

- **Choose three accent elements** from the family's list, plus at most one borrowed from another family. Do not use them all.
- **Choose a different lead accent** from the last page built in the same family. If the homepage leads with the polaroid, a subject page leads with the exam paper.
- **Change the handwriting.** Notes are written for that page. Never reuse a note from another page.
- **Change what is circled.** One circle per page, on that page's most important number.
- **Change the section rhythm.** Alternate the family surface with white. Place the brown band where the page shows its proof of method; leave it out if there is none.
- **Keep tilts irregular.** Tilted items sit between 0.6 and 2.2 degrees. Neighbours tilt in opposite directions.

### Density limits

| Per page | Limit |
|---|---|
| Hand-drawn circles | 1 |
| Pen arrows | 1 |
| Sticky notes | 1 |
| Offset cards | 1 per screen |
| Brown bands | 1 |
| Yellow bands | 1, the final call to action |

| Per section | Limit |
|---|---|
| Highlighters | 1, in the heading |
| Handwritten notes | 1 |
| Ink tags | 1 per group of cards |
| Stamps | 1 per card |

---

## 5. Elements

All selectors below are written without a prefix. On a real page, **prefix every selector with the page's wrapper id** (for example `#sjh .sj-hl`) so nothing leaks into the theme.

## Signature

### Highlighter

**Use for:** Every page. The one mark that says SJ Academy.

**Rules:** One per heading, on 1 to 3 words, never split across lines. The band covers the lower half of the letters and stops at the baseline. Never on brown or yellow backgrounds: use yellow text on brown instead.

```html
<h2 class="sj-h2">The teachers behind the <span class="sj-hl">950+ A*s</span></h2>
```

```css
.sj-hl{background-image:linear-gradient(100deg,transparent 0,var(--sj-yellow) .14em,var(--sj-yellow) calc(100% - .14em),transparent 100%);background-repeat:no-repeat;background-size:100% .4em;background-position:0 calc(100% - .31em);padding:0 .14em;margin:0 -.14em;-webkit-box-decoration-break:clone;box-decoration-break:clone;white-space:nowrap}
```

### Kicker pill

**Use for:** Above or inside the H1 to name the page. Put it inside the H1 when it carries the search keyword.

**Rules:** One per page, in the hero only. Uppercase, 11px, weight 500.

```html
<span class="sj-pill"><span>O &amp; A Level coaching center in Karachi</span></span>
```

```css
.sj-pill{display:table;border:1.5px solid var(--sj-ink);border-radius:50px;padding:4px;background:#fff;box-shadow:3px 3px 0 rgba(0,0,0,.14)}
.sj-pill span{display:block;background:var(--sj-yellow);border-radius:40px;padding:6px 14px;font-size:11px;line-height:1.4;font-weight:500;letter-spacing:.7px;text-transform:uppercase;color:var(--sj-ink)}
```

### Offset card

**Use for:** The single most important interactive block on a page: a finder, calculator, form or result.

**Rules:** One per screen at most. Ink outline with a yellow offset shadow. Ordinary content cards do not get this.

```html
<div class="sj-offset"><b>Find your class</b><p>The main tool on the page lives here.</p></div>
```

```css
.sj-offset{background:#fff;border:1.5px solid var(--sj-ink);border-radius:18px;padding:18px;box-shadow:7px 7px 0 var(--sj-yellow),7px 7px 0 1.5px var(--sj-ink)}
```

### Buttons

**Use for:** Primary = the one action the page wants. WhatsApp = talk to us. Ghost = everything else.

**Rules:** One primary per section. Never white text on bright orange (#FE6100): the primary uses the darker #CC4A00. Minimum height 48px. Sentence case.

```html
<a class="sj-btn sj-btn-primary">Book a free demo</a> <a class="sj-btn sj-btn-wa">WhatsApp us</a> <a class="sj-btn sj-btn-ghost">See the timetable</a>
```

```css
.sj-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;padding:12px 22px;border-radius:12px;border:1.5px solid var(--sj-ink);font-size:15.5px;line-height:1.3;font-weight:500;white-space:nowrap;text-decoration:none;cursor:pointer}
.sj-btn-primary{background:var(--sj-cta);color:#fff;box-shadow:4px 4px 0 var(--sj-ink)}
.sj-btn-wa{background:var(--sj-whatsapp);color:#000}
.sj-btn-ghost{background:#fff;color:var(--sj-ink)}
```

## Annotation

### Handwritten note

**Use for:** A short aside in the teacher's voice: a nudge, a reassurance, a label on a photo.

**Rules:** Six words or fewer, lowercase, no full stop. One per section at most. Never for information the reader must not miss. Rotate between -2 and 2 degrees.

```html
<span class="sj-hand" style="transform:rotate(-1.5deg);display:inline-block">pick your subject, try a class free</span>
```

```css
.sj-hand{font-family:var(--sj-hand);font-weight:600;font-size:22px;line-height:1.1;color:var(--sj-cta)}
```

### Hand-drawn circle

**Use for:** Circles the one number or word a teacher would circle: a result, a deadline, a fee.

**Rules:** One per page. Orange pen. Sits behind a number or a single word, never a sentence.

```html
<span class="sj-circled"><svg class="sj-circle" viewBox="0 0 120 70" preserveAspectRatio="none" aria-hidden="true"><path d="M14 38C10 18 40 6 68 7c27 1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30" fill="none" stroke="#FE6100" stroke-width="2.6" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg><b>950+</b></span>
```

```css
.sj-circled{position:relative;display:inline-block;padding:2px 10px}
.sj-circled b{font-weight:400;font-size:32px;color:var(--sj-ink);letter-spacing:-1px;position:relative}
.sj-circle{position:absolute;left:-6px;top:-4px;width:calc(100% + 12px);height:calc(100% + 8px);pointer-events:none}
```

### Pen arrow

**Use for:** Points from a handwritten note to the thing it is about.

**Rules:** Always paired with a handwritten note. One per page.

```html
<span class="sj-hand">start here</span> <svg class="sj-arrow" viewBox="0 0 80 50" aria-hidden="true"><path d="M4 8c22-6 50 2 62 30M66 38l-12-3M66 38l2-12" fill="none" stroke="#CC4A00" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
```

```css
.sj-arrow{width:64px;height:40px;vertical-align:middle}
```

### Pen underline

**Use for:** Underlines one word in body copy or a subheading where the highlighter is already used in the heading.

**Rules:** One per section. Never in the same heading as a highlighter.

```html
<span class="sj-under">never luck<svg class="sj-scribble" viewBox="0 0 200 14" preserveAspectRatio="none" aria-hidden="true"><path d="M3 9c30-6 62-7 96-4s66 2 98-2M12 12c40-4 90-4 170-3" fill="none" stroke="#FE6100" stroke-width="2.4" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg></span>
```

```css
.sj-under{position:relative;display:inline-block;color:var(--sj-ink)}
.sj-scribble{position:absolute;left:-2%;bottom:-.35em;width:104%;height:.5em}
```

### Ink tag

**Use for:** Labels who is speaking or what a card is: "from a parent", "most used", "new for 2027".

**Rules:** Sits on the top edge of a card, tilted about 2 degrees. Three words or fewer. One per group of cards.

```html
<div class="sj-demo-card"><span class="sj-tag">from a parent</span><p>A review card or a featured tile.</p></div>
```

```css
.sj-tag{position:absolute;top:-14px;right:16px;background:var(--sj-ink);color:var(--sj-yellow);font-family:var(--sj-hand);font-weight:600;font-size:18px;line-height:1.2;padding:2px 12px;border-radius:6px;transform:rotate(2deg)}
```

### Pen ticks

**Use for:** Short lists of what the reader gets.

**Rules:** Three to five items, one line each where possible. Orange-brown pen tick.

```html
<ul class="sj-ticks"><li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>Past-paper practice, marked to the mark scheme</span></li><li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>A free demo class before you enrol</span></li></ul>
```

```css
.sj-ticks{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:15px;color:var(--sj-ink)}
.sj-ticks li{display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:start;line-height:1.45;margin:0}
.sj-ticks svg{width:22px;height:22px;fill:none;stroke:var(--sj-cta);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
```

### Margin note

**Use for:** A teacher's comment beside a paragraph in long reading: guides, blog posts, model answers.

**Rules:** Red pen. Two short lines at most. One per screen of reading.

```html
<div class="sj-margin"><p>Analysis means a chain: because, so, which leads to.</p><span class="sj-margin-note">examiners look for this</span></div>
```

```css
.sj-margin{position:relative;border-left:2px solid var(--sj-pen);padding:2px 0 2px 16px}
.sj-margin p{margin:0;color:var(--sj-text)}
.sj-margin-note{display:block;font-family:var(--sj-hand);font-weight:600;font-size:19px;color:var(--sj-pen);margin-top:4px;transform:rotate(-1deg);transform-origin:left}
```

### Pen star

**Use for:** Marks the single best option in a set: a recommended combination, a top tip.

**Rules:** One per set. Never as decoration.

```html
<span class="sj-starred"><svg class="sj-star" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 4l4.2 11.3L36 16l-9.2 7.4L30 35l-10-6.6L10 35l3.2-11.6L4 16l11.800-.7z" fill="none" stroke="#FE6100" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg>Recommended</span>
```

```css
.sj-starred{display:inline-flex;align-items:center;gap:6px;font-weight:500;color:var(--sj-ink)}
.sj-star{width:26px;height:26px}
```

## Paper

### Tape

**Use for:** Holds a photo or a note to the page. Use on photos of real people and places.

**Rules:** Yellow by default, kraft on yellow backgrounds. One or two strips per photo. Tilt 1 to 3 degrees.

```html
<div class="sj-polaroid"><span class="sj-tape"></span><div class="sj-ph">photo</div><span class="sj-hand">Inside a class at DHA Phase 7</span></div>
```

```css
.sj-tape{position:absolute;top:-12px;left:50%;width:96px;height:26px;margin-left:-48px;background:rgba(252,224,4,.78);transform:rotate(2deg);box-shadow:0 1px 2px rgba(0,0,0,.1)}
.sj-tape-kraft{background:rgba(203,180,137,.85)}
.sj-polaroid{position:relative;background:#fff;padding:10px 10px 12px;box-shadow:0 10px 28px rgba(0,0,0,.14);transform:rotate(-1.4deg);max-width:260px}
.sj-polaroid .sj-hand{display:block;text-align:center;color:var(--sj-ink);font-size:19px;margin-top:8px}
```

### Sticky note

**Use for:** One key takeaway, a reminder or a deadline that should stand apart from the text.

**Rules:** One per page. Thirty words or fewer. Body in Poppins, optional heading in handwriting.

```html
<div class="sj-sticky"><span class="sj-hand">remember</span><p>Registration for May/June closes before the exam entry deadline.</p></div>
```

```css
.sj-sticky{background:var(--sj-yellow-light);padding:16px 16px 20px;max-width:240px;transform:rotate(1.2deg);box-shadow:0 8px 18px rgba(0,0,0,.12);border-bottom-right-radius:18px 4px}
.sj-sticky .sj-hand{display:block;color:var(--sj-ink);margin-bottom:6px}
.sj-sticky p{margin:0;font-size:14.5px;line-height:1.5;color:var(--sj-ink)}
```

### Exam paper

**Use for:** Shows real work: a marked answer, a model answer, a question.

**Rules:** Navy exam ink on lined paper with a red margin. Marks in red handwriting. Tilt under 1 degree. Content must be real or clearly labelled as a sample.

```html
<div class="sj-paper"><div class="sj-paper-q"><small>A Level Business 9609</small>Analyse two benefits of job enrichment. [8]</div><div class="sj-paper-a">Job enrichment gives employees more responsibility.<span class="sj-mark">K</span></div></div>
```

```css
.sj-paper{position:relative;overflow:hidden;background:#FFFEF9;color:var(--sj-exam-ink);border-radius:4px;box-shadow:0 14px 34px rgba(0,0,0,.22);transform:rotate(-.6deg);max-width:420px}
.sj-paper::before{content:"";position:absolute;left:34px;top:0;bottom:0;width:1.5px;background:#E9A29C}
.sj-paper-q{padding:14px 16px 12px 46px;border-bottom:1.5px solid var(--sj-exam-ink);font-size:13.5px;line-height:1.5;color:#111}
.sj-paper-q small{display:block;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#666}
.sj-paper-a{padding:8px 16px 8px 46px;font-size:15px;line-height:30px;background:repeating-linear-gradient(transparent 0 29px,#D8E2EE 29px 30px);min-height:90px}
.sj-mark{font-family:var(--sj-hand);font-weight:600;color:var(--sj-pen);font-size:19px;margin:0 3px}
```

### Stamps

**Use for:** A verdict: a score, a status, an outcome.

**Rules:** Round stamp for scores and grades. Box stamp for one or two words such as "free" or "verified". One per card. Red pen colour, tilted 6 to 10 degrees.

```html
<span class="sj-stamp">8/8</span> <span class="sj-stamp-box">first class free</span>
```

```css
.sj-stamp{display:inline-grid;place-items:center;width:74px;height:74px;border:2.5px solid var(--sj-pen);border-radius:50%;font-family:var(--sj-hand);font-weight:600;font-size:30px;color:var(--sj-pen);transform:rotate(-9deg);vertical-align:middle}
.sj-stamp-box{display:inline-block;border:2.5px solid var(--sj-pen);border-radius:6px;padding:4px 12px;font-size:13px;font-weight:500;letter-spacing:1.5px;text-transform:uppercase;color:var(--sj-pen);transform:rotate(-6deg);vertical-align:middle;margin-left:14px}
```

### Grade badge

**Use for:** A real grade achieved, on a result card.

**Rules:** Only for real, named results. Yellow disc, ink letter.

```html
<span class="sj-grade">A*</span>
```

```css
.sj-grade{display:inline-grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--sj-yellow);font-weight:500;font-size:22px;color:var(--sj-ink)}
```

### Index tabs

**Use for:** Switching between sets of the same thing: levels, years, papers, series.

**Rules:** Looks like file dividers. The active tab joins the panel below it. Use for resources and tools, not for marketing sections.

```html
<div class="sj-tabs"><button aria-pressed="false">2024</button><button aria-pressed="true">2025</button><button aria-pressed="false">2026</button></div><div class="sj-tabpanel">Papers for the selected year.</div>
```

```css
.sj-tabs{display:flex;gap:4px;padding-left:12px}
.sj-tabs button{font:inherit;font-size:14px;min-height:44px;padding:8px 18px;border:1.5px solid var(--sj-ink);border-bottom:0;border-radius:10px 10px 0 0;background:var(--sj-kraft);color:var(--sj-ink);cursor:pointer;position:relative;top:1.5px}
.sj-tabs button[aria-pressed="true"]{background:#fff;font-weight:500}
.sj-tabpanel{border:1.5px solid var(--sj-ink);border-radius:12px;background:#fff;padding:16px;font-size:14.5px}
```

### Paperclip

**Use for:** Marks a downloadable file or an attached resource.

**Rules:** Top left of a download card. One per card. Do not mix with tape on the same card.

```html
<div class="sj-demo-card sj-clipped"><svg class="sj-clip" viewBox="0 0 24 56" aria-hidden="true"><path d="M7 14v26a5 5 0 0 0 10 0V10a8 8 0 0 0-16 0v32" fill="none" stroke="#8A8578" stroke-width="2.2" stroke-linecap="round"/></svg><b>9609 definitions (PDF)</b><p>Download card</p></div>
```

```css
.sj-clipped{padding-left:54px}
.sj-clip{position:absolute;left:12px;top:-14px;width:22px;height:52px;transform:rotate(-6deg)}
```

### Ticket

**Use for:** Anything with a date and limited seats: workshops, mock exams, practical batches.

**Rules:** Kraft stub on the left with the date, details on the right, perforated divider. State real dates only.

```html
<div class="sj-ticket"><div class="sj-ticket-stub"><b>14</b>Nov</div><div class="sj-ticket-body"><b>Physics P3 workshop</b><span>DHA Phase 7 · 5 sessions</span></div></div>
```

```css
.sj-ticket{display:grid;grid-template-columns:84px 1fr;border:1.5px solid var(--sj-ink);border-radius:14px;overflow:hidden;background:#fff;max-width:360px}
.sj-ticket-stub{background:var(--sj-kraft);border-right:2px dashed var(--sj-ink);display:grid;place-items:center;align-content:center;padding:12px;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:var(--sj-ink)}
.sj-ticket-stub b{display:block;font-weight:400;font-size:30px;line-height:1;letter-spacing:-1px}
.sj-ticket-body{padding:14px 16px}
.sj-ticket-body b{display:block;font-weight:500;color:var(--sj-ink)}
.sj-ticket-body span{font-size:13.5px;color:var(--sj-muted)}
```

### Pinned card

**Use for:** Pinboard layouts: results walls, review walls, notices.

**Rules:** A pin at the top centre, slight tilt, alternate the tilt direction between neighbours.

```html
<div class="sj-pinned"><span class="sj-pin"></span><b>A* in Chemistry</b><p>May/June 2026</p></div>
```

```css
.sj-pinned{position:relative;background:#fff;border:1px solid var(--sj-line);border-radius:6px;padding:22px 16px 14px;box-shadow:0 8px 18px rgba(0,0,0,.1);transform:rotate(-1deg);max-width:200px;text-align:center}
.sj-pinned b{display:block;font-weight:500;color:var(--sj-ink)}
.sj-pinned p{margin:2px 0 0;font-size:13px;color:var(--sj-muted)}
.sj-pin{position:absolute;top:-8px;left:50%;margin-left:-8px;width:16px;height:16px;border-radius:50%;background:var(--sj-cta);box-shadow:inset -3px -3px 0 rgba(0,0,0,.2),0 3px 4px rgba(0,0,0,.25)}
```

## Structure

### Numbered steps

**Use for:** A process in order: how we teach, how to register, how a tool works.

**Rules:** Handwritten numerals 01, 02, 03. Title in weight 500, one line of explanation.

```html
<ol class="sj-steps"><li><b>Taught to the mark scheme</b><span>You learn what each mark is for.</span></li><li><b>Marked like the real thing</b><span>Timed questions, examiner-style marking.</span></li></ol>
```

```css
.sj-steps{list-style:none;margin:0;padding:0;counter-reset:sj}
.sj-steps li{counter-increment:sj;display:grid;grid-template-columns:44px 1fr;gap:2px 8px;padding:14px 0;border-top:1px solid var(--sj-line);margin:0}
.sj-steps li::before{content:"0" counter(sj);font-family:var(--sj-hand);font-weight:600;font-size:26px;color:var(--sj-cta);line-height:1;grid-row:span 2}
.sj-steps b{font-weight:500;color:var(--sj-ink)}
.sj-steps span{font-size:14px;color:var(--sj-muted);grid-column:2}
```

### Proof strip

**Use for:** Two to four verified numbers under a hero.

**Rules:** Ink rules above and below. Numbers in weight 400. Every number must be one of the approved facts, and should link to its evidence.

```html
<div class="sj-proof"><span><b>950+</b>A*s achieved</span><span><b>4,500+</b>students taught</span><span><b>5.0</b>Google rating</span></div>
```

```css
.sj-proof{display:grid;grid-template-columns:repeat(3,1fr);gap:0 12px;border-top:1.5px solid var(--sj-ink);border-bottom:1.5px solid var(--sj-ink)}
.sj-proof span{padding:14px 6px 14px 0;font-size:13px;color:var(--sj-muted);line-height:1.35}
.sj-proof b{display:block;font-weight:400;font-size:27px;line-height:1.1;color:var(--sj-ink);letter-spacing:-1px}
```

### Section eyebrow

**Use for:** Names a section above its H2.

**Rules:** Uppercase, 12px, with a short ink rule before it.

```html
<div class="sj-eyebrow">How we teach</div>
```

```css
.sj-eyebrow{font-size:12px;font-weight:500;letter-spacing:1.4px;text-transform:uppercase;color:var(--sj-muted);display:flex;align-items:center;gap:10px}
.sj-eyebrow::before{content:"";width:26px;height:2px;background:var(--sj-ink)}
```

### Soft tile and link

**Use for:** Ordinary content cards: tools, audiences, resources.

**Rules:** Canvas fill, no outline, no top bar. Hover turns light yellow. Text links use a yellow underline and an arrow.

```html
<a class="sj-tile"><b>Past papers</b><p>Every subject, by year and series.</p><span class="sj-link">Open past papers</span></a>
```

```css
.sj-tile{display:block;background:var(--sj-canvas);border-radius:16px;padding:18px;text-decoration:none;max-width:280px}
.sj-tile:hover{background:var(--sj-yellow-light)}
.sj-tile b{display:block;font-weight:500;color:var(--sj-ink)}
.sj-tile p{margin:4px 0 10px;font-size:14px;color:var(--sj-muted)}
.sj-link{font-size:14px;font-weight:500;color:var(--sj-ink);border-bottom:2px solid var(--sj-yellow);padding-bottom:2px}
.sj-link::after{content:" \2192"}
```

## Surfaces

### Page surfaces

**Use for:** Each page family has one signature surface. Sections alternate between it and plain white.

**Rules:** Dotted notebook for enrolment pages. Graph paper for tools. Ruled paper for resources. Plain canvas for reading. Brown for one "proof of method" band per page. Yellow for the final call to action only.

```html
<div class="sj-surfaces"><div class="sj-bg-dots">Dotted</div><div class="sj-bg-grid">Graph</div><div class="sj-bg-ruled">Ruled</div><div class="sj-bg-brown">Brown</div><div class="sj-bg-yellow">Yellow</div></div>
```

```css
.sj-bg-dots{background:radial-gradient(#DAD4C3 1.1px,transparent 1.2px) 0 0/22px 22px,var(--sj-canvas)}
.sj-bg-grid{background:linear-gradient(#E6E0D0 1px,transparent 1px) 0 0/22px 22px,linear-gradient(90deg,#E6E0D0 1px,transparent 1px) 0 0/22px 22px,var(--sj-canvas)}
.sj-bg-ruled{background:repeating-linear-gradient(transparent 0 31px,#E2DDD0 31px 32px),var(--sj-canvas)}
.sj-bg-brown{background:var(--sj-brown);color:#EDE6D3}
.sj-bg-yellow{background:radial-gradient(rgba(0,0,0,.12) 1.1px,transparent 1.2px) 0 0/22px 22px,var(--sj-yellow)}
```


---

## 6. Photography

- Real students, real teachers, real classrooms and labs. No stock photos and no AI-generated people.
- Photos of people go in a polaroid frame with tape, or in a rounded card with a 14px radius.
- Every photo has alt text describing the scene, including the place where it helps (for example "A Level Physics students doing a practical at SJ Academy, DHA Phase 7").
- Use the smallest version WordPress made that still looks sharp (usually the 768px version), with width and height set.

---

## 7. Voice

- Plain, direct and specific. Short sentences. Active voice.
- Name the reader's problem before the solution ("That's why hard-working students get stuck at a B").
- Show method through real artefacts (marked answers, timetables, results), not adjectives.
- No em dashes. No buzzwords. Sentence case.
- Handwritten notes sound like a teacher talking: lowercase, six words or fewer.
- Buttons say what happens: "Book a free demo", "WhatsApp us", "Register for a class".

### Facts that may be stated

| Fact | Wording |
|---|---|
| A*s | 950+ A*s |
| Students | 4,500+ students taught |
| Google | Rated 5.0 on Google from 226 reviews. Never "226+ five-star reviews" |
| Faculty | Teachers from LUMS, IBA and KGS |
| Location | Plot 29C, Lane 5, Seher Commercial Area, DHA Phase 7, Karachi |
| WhatsApp | +92-336-2144454 |

### Facts that must not be stated

- A batch size number. Say "small batches".
- One-on-one or home tuition. It is not offered.
- Demo classes for lab practicals. Students join practicals directly.
- Fee figures on marketing pages. Link to the fee page.
- Frequencies or durations that are not confirmed ("weekly", "in six weeks").
- Reviews that are not real, word-for-word quotes with the reviewer's name.

---

## 8. Calls to action

| Situation | Primary | Secondary |
|---|---|---|
| O Level and A Level classes | "Book a free demo" (opens WhatsApp with the level and subject filled in) | "WhatsApp us" |
| Lab practicals | "Join on WhatsApp" | "Register for a class" |
| Ready to enrol | "Register for a class" (opens registration popup 6023) | "or WhatsApp us" as a text link |
| Tools and resources | The tool's own action first; the class offer comes after the result | Text link |

- WhatsApp message pattern: "Hi SJ Academy, I would like to book a free demo class for [level] [subject]. My name is "
- On phones, a bottom bar with the two main actions appears once the hero's main block has scrolled away.
- The registration form is the only form. Do not add new forms without a reason.

---

## 9. Build rules

- One Elementor HTML widget per page, in a full-width section with zero padding and no entrance animation.
- One wrapper element with a unique id per page. Every CSS selector starts with that id. No global resets.
- Reset theme styles on purpose inside the wrapper: headings, links, lists, images and buttons.
- Phone first. Design at 360px, then 390px, then desktop. Content width on desktop is 1550px to line up with the site header.
- Tap targets are at least 44px tall. Body text is at least 16px. Nothing overflows sideways.
- One H1 per page. The kicker pill sits inside the H1 when it carries the search keyword.
- All content that matters for search is in the HTML. JavaScript only shows, hides and enriches.
- FAQ uses native `details` and `summary`, with matching FAQ data in the same widget.
- The first image loads eagerly with `fetchpriority="high"`; the rest are lazy. Requests for extra data (blog posts, timetables) wait until needed.
- No sliders, autoplay carousels, parallax, animated counters or popups on load.
- Respect `prefers-reduced-motion`.
- Scripts are wrapped in a function, use prefixed ids, and never depend on jQuery.

---

## 10. Do not

- Add a coloured bar to the top of cards.
- Use glass effects, gradients between brand colours, or drop shadows heavier than those in this guide.
- Use decorative shapes with no meaning (circles, plus signs, blobs, waves).
- Put more than one tilted element next to another with the same tilt.
- Use handwriting for body text, buttons, navigation or anything the reader must not miss.
- Copy the homepage section by section. Start from the page family, then choose.

---

## 11. Checklist before publishing

- [ ] Page family chosen, with its surface and hero
- [ ] Four signature elements present
- [ ] Three accent elements, different lead accent from the last page in this family
- [ ] Density limits respected
- [ ] One H1, with the keyword
- [ ] Only approved facts stated
- [ ] No sideways scroll at 360px
- [ ] Buttons do what their labels say
- [ ] Tested inside Elementor on a draft
