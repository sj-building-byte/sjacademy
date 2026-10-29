# SJ Academy brand guidelines

**Version:** 3.2, October 2026
**Status:** Current. Replaces v2.0. Where this guide and the handoff file disagree on build rules, this guide wins.
**Owner:** Sunyyan Junaid. Changes need his approval and a change log entry (section 21).
**Stylesheet:** `02-Brand/sj-brand.css` (shared, site-wide, version 3.1.1)
**Visual reference:** `02-Brand/sj-academy-brand-kit-v3.html` shows every element in this guide, live.
**Copy:** landing pages (Enrol and Event families) follow `02-Brand/SJ-ACADEMY-LANDING-PAGE-COPY-GUIDELINES.md`. Blog posts follow `02-Brand/SJ-ACADEMY-BLOG-VOICE-GUIDELINES.md`. Section 14 is the short version of both.
**Standard page script:** `07-Code & Scripts/sj-page-script.js` (tabs, phone bottom bar, video, click tracking)
**Applies to:** every new page on sjacademy.pk. The four pages built before 3.0 keep their own CSS until migrated (section 20).

Give this file, the stylesheet and the brand kit to any designer, developer or AI model before they build a page.

### What changed from 2.0

- One shared stylesheet replaces per-page CSS. This guide no longer carries CSS; the stylesheet is the single source.
- New: logo section, audiences, language policy, design tokens, functional components (forms, tables, FAQ, alerts, cards, search), interaction states, accessibility, consent, facts register, SEO standards, performance budget, page templates, off-site templates, governance.
- Fixed: focus style, link and tile contrast, minimum text sizes, pen colour roles, tab markup, button wrapping, tilt rules.

---

## 1. The idea

**SJ Academy looks like a good teacher's notebook.**

The brand promise is "Cambridge doesn't mark effort. It marks method." The design shows that method: highlighted key terms, marked answers, pen notes in the margin, photos taped to the page. Everything decorative is something you would find on a teacher's desk.

Three tests for any page:

1. **Would a teacher have made this mark?** Every circle, note and stamp points at something that matters. If it is only decoration, remove it.
2. **Is there more paper than pen?** Most of the page is calm: off-white, black type, white space. The hand-made marks are rare, which is why they are noticed.
3. **Could you tell it is SJ Academy with the logo covered?** The highlighter, the offset card and the handwriting should make it recognisable.

### What protects the style from dating

- The **signature set** (highlighter, kicker pill, offset card, buttons) is the brand. The paper and pen elements are seasoning.
- Tool, Resource and Info pages are the calmest on the site. Function first.
- If the style ever needs a refresh, only the Paper and Annotation groups change. Colour, type and the signature set stay.

---

## 2. Positioning and audiences

**Positioning.** SJ Academy teaches Cambridge O Level and A Level students in Karachi and online how marks are actually awarded, so effort turns into grades. It is a tuition centre. It is not a school, not home tuition and not a recorded-course platform.

Every page serves one of two readers. Decide which one leads before writing.

| | Student | Parent |
|---|---|---|
| Wants | Method, past papers, speed, a teacher who explains | Proof, fees, timings, location, a person to talk to |
| Arrives from | Search for a paper, topic or tool | Search for tuition, a referral, WhatsApp |
| Convinced by | A marked answer, a useful tool | Results, teacher credentials, clear costs |
| Next step | Use the resource, then try a class | WhatsApp, then a demo class |
| Tone | Direct, quick, a little dry | Plain, specific, reassuring without fuss |

Rules:

- Enrol pages carry a short "For parents" block. Resource and Tool pages are written for students.
- A parent must reach fees, timetable, teachers, results and location within two taps from any Enrol page.
- Never write to both at once in the same paragraph.

---

## 3. Logo

The logo is an open book whose two pages form the letters S and J, with the wordmark "SJ Academy" and the tagline "Center of Excellence". It was delivered in eight versions. Clean SVG files, exported from the original Illustrator master, are in `Logo & Assets/SVG`.

### Versions and when to use them

| Version | File | Use on |
|---|---|---|
| Horizontal, on light | `sj-academy-logo-horizontal-on-light.svg` | Canvas, white. **The default for the website and documents** |
| Horizontal, on brown | `sj-academy-logo-horizontal-on-brown.svg` | The brown band, dark photos |
| Horizontal, on yellow | `sj-academy-logo-horizontal-on-yellow.svg` | The yellow band, yellow social posts |
| Stacked, on light | `sj-academy-logo-stacked-on-light.svg` | Square or tall spaces: posters, PDF covers, profile headers |
| Stacked, on brown | `sj-academy-logo-stacked-on-brown.svg` | As above, on brown |
| Stacked, on yellow | `sj-academy-logo-stacked-on-yellow.svg` | As above, on yellow |
| Stacked, one-colour black | `sj-academy-logo-stacked-mono-black.svg` | Photocopies, stamps, single-colour print |
| Stacked, one-colour white | `sj-academy-logo-stacked-mono-white.svg` | Black or very dark backgrounds |
| Icon | `sj-academy-icon-on-light.svg`, `-on-brown`, `-on-yellow`, `-mono-black`, `-mono-white` | Favicon, app icon, social avatar, watermark, anywhere under the minimum size |

Older files in `Logo & Assets`, kept for reference:

| File | What it is | Note |
|---|---|---|
| `SJWhite.png` | Horizontal, on light (2758 x 700) | The name is misleading: it is the version for white backgrounds |
| `Yellow w.png`, `Yello logo Website.png` | Horizontal, on brown (yellow wordmark) | Unreadable on white or canvas |
| `Logo Search Engine.png`, `Logo for Search engine.png` | Icon on a yellow square, 512 x 512 | Use for favicon and search engine logo |
| `SJ Logo.png`, `SJ Logo.svg` | Icon, on light | The SVG is an automatic trace with uneven colours. Use the new icon SVG instead |
| `SJ Academy - Logo Delivery.ai` | Illustrator master, all eight versions | The source of truth |

### Colours in the logo

| Colour | Value | Note |
|---|---|---|
| Logo yellow | `#FCE004` | Same as brand yellow |
| Logo brown | `#463613` | Visually identical to brand brown `#453516`. Do not try to match one to the other; leave both as they are |
| Black, white | `#231F20`, `#FFFFFF` | One-colour versions only |

### Rules

- **Pick the version by background.** Never place the on-light version on brown, or the yellow wordmark on white.
- **Clear space:** one quarter of the logo's height on every side (for the stacked logo and icon, one quarter of the icon's height). Nothing enters it.
- **Minimum size:** horizontal 160px wide, stacked 110px wide, icon 24px. Below the minimum for a full logo, use the icon. In print: horizontal 35mm wide.
- **The tagline stays** with the full logo. If it would be too small to read, use the icon instead of removing the tagline.
- **Backgrounds:** canvas, white, brand yellow, brand brown, black. On photos only over a calm area, never over faces. On the dotted, graph or ruled surfaces, put a solid white or canvas patch behind it.
- **The wordmark is artwork.** Never retype "SJ Academy" in Poppins or any other font as a substitute for the logo.
- **Do not** stretch, rotate, tilt, recolour, outline, add a shadow or glow, rearrange the icon and wordmark, or crop the icon.
- **The logo is never tilted, taped, stamped or circled.** Paper effects apply to content, not to the mark.
- **One logo per screen.** The site header already carries it, so page content almost never needs another. Exceptions: share images, PDFs, print.
- The site header and footer belong to the theme and are outside this guide.

---

## 4. Colour

| Name | Token | Value | Job |
|---|---|---|---|
| Yellow | `--sj-yellow` | `#FCE004` | Highlighter, selected state, final call-to-action band |
| Light yellow | `--sj-yellow-light` | `#FFF9CC` | Result panels, sticky notes, key table rows, deadline alerts |
| Orange | `--sj-orange` | `#FE6100` | Pen strokes only: circle, underline, star. Never text, never behind white text |
| CTA orange | `--sj-cta` | `#CC4A00` | Primary buttons, pen ticks, pen arrow |
| CTA orange, dark | `--sj-cta-dark` | `#B54200` | Handwriting addressed to the visitor, step numbers, primary button hover |
| Brown | `--sj-brown` | `#453516` | One method band per page, avatars |
| Ink | `--sj-ink` | `#151515` | Headings, outlines, focus ring |
| Text | `--sj-text` | `#2B2B2B` | Body copy |
| Muted | `--sj-muted` | `#66625A` | Secondary text |
| Canvas | `--sj-canvas` | `#F7F5EF` | Page background |
| Line | `--sj-line` | `#E2DDD0` | Dividers only. Never input borders |
| Kraft | `--sj-kraft` | `#E9DFC9` | Unselected tabs, ticket stubs, tape on yellow |
| Pen red | `--sj-pen` | `#D63A2F` | Strokes and borders of marks and stamps |
| Pen red, text | `--sj-pen-text` | `#B92F25` | Any red pen that is text: marks, stamp text, margin notes |
| Exam ink | `--sj-exam-ink` | `#1B2A4A` | Text on exam paper |
| WhatsApp | `--sj-whatsapp` | `#25D366` | WhatsApp buttons, black text |
| Success | `--sj-ok` | `#1F7A3D` | Confirmations only |
| Error | `--sj-err` | `#B3261E` | Form and system errors only |

### The pen rule

- **Orange-brown pen** (`--sj-cta` for strokes, `--sj-cta-dark` for handwriting) is the teacher talking to the visitor: notes, arrows, ticks, step numbers.
- **Red pen** (`--sj-pen`, `--sj-pen-text`) is the teacher marking work: marks, stamps, margin notes. Never used for errors.
- **Bright orange** (`--sj-orange`) is for strokes only. It is decorative and never the only carrier of meaning.

### Other rules

- Yellow is a highlighter, not a background, except the final call-to-action band.
- White text never sits on bright orange. Buttons with white text use CTA orange.
- Brown is used for one full-width band per page at most.
- Selected states always carry a second signal besides yellow: a tick, a bolder weight or an edge.
- Error and success colours appear only in forms, alerts and tool results.
- There is no dark mode. Pages render the same in light and dark system settings.

### Checked contrast (WCAG 2.1 AA)

| Pair | Ratio | Use |
|---|---|---|
| Text on canvas | 12.99 | Any size |
| Muted on canvas | 5.57 | Any size |
| White on CTA orange | 4.62 | Any size |
| Dark CTA orange on canvas | 5.14 | Handwriting, any size from 20px |
| CTA orange on canvas | 4.24 | Strokes and icons only, not text |
| Pen red text on canvas | 5.51 | Any size |
| Error on error background | 5.69 | Any size |
| Success on success background | 4.76 | Any size |
| Cream text on brown | 9.50 | Any size |
| Black on WhatsApp green | 10.59 | Any size |

---

## 5. Type

Two families only: **Poppins** (400, 500, 600) and **Caveat** (600). Do not load the theme's GT Walsheim on new pages.

| Use | Class | Font and weight | Size (phone to desktop) | Line height |
|---|---|---|---|---|
| H1 | `sj-h1` | Poppins 600, letter spacing -0.03em | 32 to 54px, fluid | 1.08 |
| H2 | `sj-h2` | Poppins 500, letter spacing -0.025em | 26 to 38px, fluid | 1.15 |
| H3, card titles | `sj-h3` | Poppins 500 | 18 to 21px | 1.3 |
| H4, labels in cards | `sj-h4` | Poppins 500 | 16px | 1.4 |
| Lead paragraph | `sj-lead` | Poppins 400, same colour as body text | 17 to 19px | 1.6 |
| Body | default | Poppins 400 | 16px | 1.6 |
| Long-form body | `sj-prose` | Poppins 400 | 17px | 1.7 |
| Small | `sj-small` | Poppins 400 | 14px | 1.5 |
| Caption | `sj-caption` | Poppins 400 | 13px | 1.45 |
| Buttons | `sj-btn` | Poppins 500 | 16px (15px small) | 1.3 |
| Eyebrow, pill | `sj-eyebrow`, `sj-pill` | Poppins 500 uppercase | 12px | 1.4 |
| Handwriting | `sj-hand` | Caveat 600 | 20 to 30px | 1.1 |

Rules:

- **Weight follows rank.** H1 is 600, H2 is 500, card titles are 500, body is 400. The heaviest text on a screen is always the headline.
- 600 is for H1 only. Nothing is ever 700. Never weight 300.
- **Big type is set tight.** Letter spacing and line height both tighten as size grows, so a headline reads as one block.
- **Paragraph colour does not change.** The lead paragraph stays the same colour as body text. The headline leads through weight and size, not by greying the text under it.
- **Headline line breaks are chosen.** Each line is a phrase. Use a manual break where the automatic one splits a phrase badly.
- Sentence case everywhere. Uppercase only for the kicker pill, eyebrows, table headings and box stamps.
- **16px is the floor for anything the reader must read.** 14px is for secondary text (help text, metadata, dates). 13px is for captions and table headings only. Nothing is below 12px.
- Handwriting is never below 20px and never carries information the reader must not miss.
- Text lines never run longer than 68 characters (`sj-measure`, `sj-prose`).
- Load fonts without blocking the page, once per page:

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>
```

---

## 6. Layout tokens

All values live in the stylesheet as variables. Use the variable, never a new number.

| Set | Values |
|---|---|
| Spacing (`--sj-s1` to `--sj-s9`) | 4, 8, 12, 16, 24, 32, 48, 72, 96px |
| Section padding (`sj-section`) | 48px phone, 72px from 600px, 96px from 1200px |
| Side gutter (`sj-wrap`) | 16px phone, 24px from 900px |
| Content width | 1550px maximum, to line up with the site header |
| Text measure | 68 characters maximum |
| Radius | 6px (tags, stamps), 12px (buttons, inputs, tabs), 18px (cards), pill |
| Photo radius | 14px |
| Shadows | soft (cards), lift (paper), offset (signature card) |
| Breakpoints | 360 (design base), 600, 900, 1200 |
| Grid (`sj-grid`) | 1 column phone, 2 from 600px, 3 or 4 from 900px |
| Tap target | 48px minimum. Buttons 52px |
| Motion | 120ms (press), 200ms (hover, open). Ease-out. Nothing longer |
| Layers | raised content 2, phone bottom bar 900. Theme header and popups sit above |

Tilt, by element:

| Element | Tilt |
|---|---|
| Exam paper | under 1 degree |
| Handwritten notes, polaroids, sticky notes, pinned cards | 0.6 to 2.2 degrees |
| Tape, ink tag | 1 to 3 degrees |
| Stamps | 6 to 10 degrees |
| Logo, buttons, forms, tables, body text | never |

Neighbours tilt in opposite directions. Tilted and offset elements carry their own margin in the stylesheet so they never cause sideways scroll.

---

## 7. Page families

Pick the family by what the visitor came to do.

| Family | Pages | Leads for | Surface | Hero | Accent elements |
|---|---|---|---|---|---|
| **Enrol** | Homepage, level pages, subject tuition pages | Parent and student | Dotted notebook | Class finder or subject card in an offset card | Polaroid with tape, circle, handwritten note, proof strip, exam paper |
| **Tool** | IBCC calculator, grade strategy, admission criteria, quizzes | Student | Graph paper | The tool itself in an offset card | Index tabs, round stamp for the result, sticky note for caveats, steps |
| **Resource** | Past papers, definitions, ebooks, date sheets, subject hubs | Student | Ruled paper | Search or filter bar | Index tabs, paperclip on downloads, ink tag for "new", soft tiles |
| **Reading** | Blog posts and guides | Student or parent | Plain canvas | Headline and a one-paragraph answer | Margin note, pen underline, sticky note for the takeaway, star |
| **Proof** | Results wall, reviews, teachers | Parent | Dotted notebook | A wall of pinned cards | Pinned cards, grade badges, ink tag, polaroids with tape |
| **Event** | Workshops, mock exams, practical batches | Student | Dotted notebook with one brown band | Ticket with the date | Ticket, box stamp, ticks, handwritten note |
| **Info** | Fees, timetable, contact, policies | Parent | Plain canvas | A clear table or card | One circle on the key number. Nothing else |

### Section order per family

Start from the template, then vary. Sections alternate the family surface with white.

| Family | Order |
|---|---|
| Enrol | Hero with offset card, proof strip, the problem, method (brown band), teacher, what you get, for parents, reviews, resources, FAQ, final band |
| Tool | Hero with the tool, result, how it works (steps), caveats, related tools, class offer, FAQ |
| Resource | Breadcrumb, hero with search or filters, results, how to use it, related resources, class offer |
| Reading | Breadcrumb, headline, short answer, body, takeaway, related reading, class offer |
| Proof | Hero, filters, wall, how results are verified, final band |
| Event | Ticket hero, what happens, who it is for, schedule, how to join, FAQ, final band |
| Info | Headline, the table or card, notes, contact, FAQ |

### How to vary pages inside a family

Every page uses all four signature elements. Beyond that:

- **Choose three accent elements** from the family's list, plus at most one borrowed from another family.
- **Choose a different lead accent** from the last page built in the same family. Check the page register (section 20).
- **Write new handwriting.** Never reuse a note from another page.
- **Circle something different.** One circle per page, on that page's most important number.
- **Place the brown band** where the page shows its proof of method. Leave it out if there is none.

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
| Free handwritten notes | 1 |
| Ink tags | 1 per group of cards |
| Stamps | 1 per card |

**What counts as a handwritten note:** only a free-standing `sj-hand` note. Polaroid captions, step numbers, ink tags, sticky note headings and marks on exam paper use the handwriting font but do not count.

---

## 8. Elements

The stylesheet holds the CSS. Copy markup from the brand kit. Classes below are used inside the `#sj` wrapper.

### Signature (every page)

| Element | Class | Use | Rules |
|---|---|---|---|
| Highlighter | `sj-hl` | The one mark that says SJ Academy | One per heading. 1 to 3 words, 18 characters at most, never split across lines. On brown it becomes yellow text automatically |
| Kicker pill | `sj-pill` | Names the page, in the hero | One per page. Sits inside the H1 when it carries the search keyword |
| Offset card | `sj-offset` | The most important interactive block: finder, calculator, form, result | One per screen. Ordinary content cards do not get this |
| Buttons | `sj-btn` with `sj-btn-primary`, `sj-btn-wa`, `sj-btn-ghost` | Primary = the one action the page wants. WhatsApp = talk to us. Ghost = everything else | One primary per section. Labels of four words or fewer. Sentence case |
| Text link | `sj-link`, `sj-link-go` | Links in text and at the foot of tiles | Ink underline plus highlighter band. `sj-link-go` adds an arrow |

### Annotation

| Element | Class | Use | Rules |
|---|---|---|---|
| Handwritten note | `sj-hand` | A short aside in the teacher's voice | Six words or fewer, lowercase, no full stop. One per section |
| Hand-drawn circle | `sj-circled`, `sj-circle` | The one number a teacher would circle | One per page. A number or a single word |
| Pen arrow | `sj-arrow` | Points from a note to its subject | Always with a note. One per page |
| Pen underline | `sj-under`, `sj-scribble` | One word in body copy or a subheading | One per section. Never in a heading that has a highlighter |
| Ink tag | `sj-tag` inside `sj-tagged` | Labels who is speaking or what a card is | Three words or fewer. One per group of cards |
| Pen ticks | `sj-ticks` | Short lists of what the reader gets | Three to five items |
| Margin note | `sj-margin`, `sj-margin-note` | A teacher's comment beside a paragraph | Red pen. Two short lines at most. One per screen of reading |
| Pen star | `sj-starred`, `sj-star` | The single best option in a set | One per set |

### Paper

| Element | Class | Use | Rules |
|---|---|---|---|
| Polaroid and tape | `sj-polaroid`, `sj-tape`, `sj-tape-kraft` | Photos of real people and places | One strip of tape. Kraft tape on yellow backgrounds |
| Sticky note | `sj-sticky` | One takeaway, reminder or deadline | One per page. Thirty words or fewer |
| Exam paper | `sj-paper`, `sj-paper-q`, `sj-paper-a`, `sj-mark`, `sj-paper-note` | Shows real work: a question, a marked answer | Real, or labelled "sample". `sj-paper-full` for the model answer template |
| Stamps | `sj-stamp`, `sj-stamp-box` | A verdict: a score, a status | Round for scores. Box for one to three words. One per card |
| Grade badge | `sj-grade` | A real grade on a result card | Only for verified results (section 13) |
| Index tabs | `sj-tabs`, `sj-tabpanel` | Switching between sets of the same thing | Resources and tools, not marketing sections. Scrolls sideways when there are many |
| Paperclip | `sj-clipped`, `sj-clip` | Marks a downloadable file | One per card. Never with tape |
| Ticket | `sj-ticket` | Anything with a date and limited seats | Real dates only |
| Pinned card | `sj-pinned`, `sj-pin` | Results walls, review walls, notices | Tilt alternates automatically |

### Structure

| Element | Class | Use | Rules |
|---|---|---|---|
| Numbered steps | `sj-steps` | A process in order | Title plus one line |
| Proof strip | `sj-proof` | Two or three verified numbers under a hero | Only facts from the register (section 14) |
| Section eyebrow | `sj-eyebrow` | Names a section above its H2 | Optional. Two or three words |
| Soft tile | `sj-tile` | Ordinary content cards that link somewhere | White on canvas sections, canvas on white sections. The stylesheet handles this |
| Plain card | `sj-card` | Any boxed content | White with a thin line border |
| Breadcrumb | `sj-crumbs` | Resource, Reading and subject pages | Matches the BreadcrumbList data |
| Chip | `sj-chip`, `sj-chip-yellow` | Short status: days to exam, syllabus years | One yellow chip per screen |
| Updated line | `sj-updated` | "Updated October 2026" on resources and guides | Required on Resource and Reading pages |
| Surfaces | `sj-bg-dots`, `sj-bg-grid`, `sj-bg-ruled`, `sj-bg-canvas`, `sj-bg-white`, `sj-bg-brown`, `sj-bg-yellow` | Section backgrounds | One family surface per page, alternating with white |

---

## 9. Functional components

### Forms

| Part | Class | Rules |
|---|---|---|
| Field wrapper | `sj-field` | Label above, help below, error last |
| Label | `sj-label` | Always visible. Never a placeholder used as a label |
| Text input | `sj-input` | 52px tall, 16px text (stops phones zooming), ink outline |
| Select | `sj-select` | Native select. No custom dropdowns |
| Text area | `sj-textarea` | |
| Help text | `sj-help` | One line |
| Error | `sj-error`, with `is-error` on the field | Says what to do, not what went wrong: "Enter all 11 digits" |
| Choice chips | `sj-choices`, `sj-choice` | For 2 to 6 options. Raised pills that look tappable. Selected = yellow plus a tick |
| Checkbox row | `sj-check` | For consent and optional extras |
| Search | `sj-search` | Has a visually hidden label |
| Filter bar | `sj-filterbar` | Search first, then filters. Stacks on phones |

Rules:

- The registration popup is the only enrolment form. Other forms exist only inside tools.
- Ask for the fewest fields possible. Set `autocomplete`, `inputmode` and `type` on every input.
- Validate when the visitor leaves a field or submits, never while typing.
- On error set `aria-invalid="true"` and link the message with `aria-describedby`.
- Anything interactive must look tappable. Instructions are never buried in a paragraph.

### Tables

| Pattern | Class | When |
|---|---|---|
| Stacking table | `sj-table sj-table-stack` inside `sj-table-wrap` | Up to four columns: fees, timetable. Each cell needs `data-label` |
| Scrolling table | `sj-table` inside `sj-table-wrap`, with `sj-table-cue` after it | Five or more columns: grade thresholds. The wrapper gets `tabindex="0"`, `role="region"` and a label |

Rules: one key row at most (`is-key`). Numbers right-aligned with `sj-num`. Column headings use `scope="col"`. No tilt, no tape, no decoration on tables.

### FAQ

`sj-faq` with native `details` and `summary`, answers in `sj-faq-a`. Matching FAQPage data in the same widget. Five to nine questions. The first may be open.

### Alerts

| Type | Class | Use |
|---|---|---|
| Notice | `sj-alert` | Closures, changes |
| Deadline | `sj-alert sj-alert-deadline` | Registration and exam dates |
| Success | `sj-alert sj-alert-ok` | After an action worked |
| Error | `sj-alert sj-alert-err` | Something failed, with what to do next |

One alert per screen. A bold title of four words or fewer plus one sentence. Real dates only.

### Content cards

| Card | Class | Must contain |
|---|---|---|
| Teacher | `sj-card sj-teacher` | Real photo, name, subject and level, qualification, years teaching |
| Review | `sj-card sj-review` | Word-for-word quote, name as consented, source |
| Result | `sj-card sj-result` | Grade badge, name as consented, subject with code, series |
| Download | `sj-card sj-clipped sj-download` | Title, file type, size, updated date, a "Download" button |
| Video | `sj-video` with `data-src` | A cover image and play button. The player loads only after a tap |

### Phone bottom bar

`sj-bar` with two small buttons: the page's primary action and WhatsApp. Rules:

- Appears on phones once the element marked `data-sj-hero` has scrolled away.
- 68px tall plus the phone's safe area. The stylesheet adds matching space under the page.
- Hide the theme's `.joinchat` bubble and `#back-to-top` on phones in the page's own CSS.
- Not used on Info pages that are a single table, or inside tool flows where it would cover a result.

### Pagination and loading

- Lists of more than 12 items use a "Show more" ghost button. Use `sj-pager` only where pages have their own addresses.
- While data loads, show `sj-skel` lines in the shape of the content.
- No results: `sj-empty` with what happened, what to try and one button.
- Data failed to load: an error alert with a "Try again" button and a WhatsApp fallback.

### Not in the system

Header, footer and navigation (theme), the registration popup (Elementor popup 6023), custom dropdowns, carousels, modals, tooltips, toasts. Ask before adding any of them.

### Icons

Line icons only: 24px grid, 2.2 to 2.6px stroke, round caps and joins, ink or CTA orange, inline SVG with `aria-hidden="true"`. No icon fonts, no emoji as icons, no filled or two-tone sets. An icon never replaces a text label.

---

## 10. States

Every interactive element has all of these. They are built into the stylesheet.

| State | Treatment |
|---|---|
| Default | As drawn |
| Hover (mouse only) | Buttons: light yellow fill, primary darkens and lifts 1px. Tiles: ink outline and light yellow. Links: highlighter grows |
| Focus | 3px ink outline, 3px away from the element. Yellow on brown. Never removed |
| Pressed | Moves down and right; the shadow shrinks |
| Selected | Yellow plus a second signal (tick, weight or top edge) |
| Disabled | Grey fill, muted text, no shadow. Say why nearby ("Batch full") |
| Busy | `aria-busy="true"` shows a spinner; the label says what is happening |
| Error | Red border, tinted field, message below |
| Empty | `sj-empty` |
| Loading | `sj-skel` |

---

## 11. Accessibility

Target: WCAG 2.1 AA.

- **Contrast:** 4.5:1 for text, 3:1 for large text (24px and above) and for the edges of controls. Use the pairs in section 4.
- **Focus:** always visible. Never write `outline:none`.
- **Keyboard:** everything works with Tab, Enter, Space and arrow keys. Tab order follows reading order.
- **Tap targets:** 48px. Links inside sentences are exempt.
- **Zoom:** pages work at 200% zoom and at 320px wide with no sideways scroll.
- **Headings:** one H1, then H2 and H3 in order. Never skip a level for looks; use the type classes.
- **Links and buttons:** the text says where it goes. Never "click here". A link goes somewhere; a button does something.
- **Images:** alt text describes the scene. Decorative SVG gets `aria-hidden="true"`.
- **Colour:** never the only signal.
- **Handwriting and tilt:** decoration only. A page must make full sense with every `sj-hand` note removed.
- **Motion:** honoured through `prefers-reduced-motion`. No autoplay, no parallax.
- **Tabs:** `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, and panels with `role="tabpanel"`.
- **Language:** `lang="en"` is inherited from the site.

---

## 12. Photography

- Real students, real teachers, real classrooms and labs. No stock photos and no AI-generated people.
- Photos of people go in a polaroid with tape, or a rounded frame (`sj-photo`, 14px radius).
- Every photo has alt text describing the scene, with the place where it helps.
- WebP or AVIF where WordPress offers it. Use the smallest version that stays sharp (usually 768px), with width and height set. Content photos stay under 120KB.
- The first image loads eagerly with `fetchpriority="high"`. The rest use `loading="lazy"`.
- Faces are never cropped by tape, tags or stamps.

---

## 13. Consent and verification

Most students are minors. Permission has been verbal so far. From v3.0:

- **No new student photo, name, result or review goes on the site without written consent** from a parent or guardian (or the student, if 18 or over).
- **Default naming:** first name and last initial ("Ayesha K."). Full names only where the consent form says so.
- **Results:** a grade badge is used only after the grade has been checked against the statement of results.
- **Reviews:** word-for-word, with the reviewer's name as shown publicly on Google, or as consented.
- **Existing content:** collect consent for people already on the site as they are next contacted. Remove anything on request within 48 hours.
- **Record:** keep a simple sheet with name, what was consented to, date, and who collected it.

Consent wording (WhatsApp or paper):

> I give SJ Academy permission to use my child's [first name and last initial / full name], [photo], [exam results] and [written feedback] on its website and social media. I understand I can withdraw this permission at any time by messaging SJ Academy, and the content will be removed.
> Student: ____ Parent or guardian: ____ Date: ____

This wording is a practical starting point, not legal advice.

---

## 14. Voice and facts

### Voice

**Landing pages** (homepage, level pages, subject tuition pages, events) are written to `02-Brand/SJ-ACADEMY-LANDING-PAGE-COPY-GUIDELINES.md`: the section formula, headline patterns, proof ladder, objections, fees and WhatsApp wording, and a checklist. **Blog posts** are written to `02-Brand/SJ-ACADEMY-BLOG-VOICE-GUIDELINES.md`. The rules below apply to every page.

- Plain, direct and specific. Short sentences. Active voice.
- Name the reader's problem before the solution.
- Show method through real artefacts (marked answers, timetables, results), not adjectives.
- No em dashes. No buzzwords. Sentence case.
- Handwritten notes sound like a teacher talking: lowercase, six words or fewer.
- Buttons say what happens: "Book a free demo on WhatsApp", "WhatsApp us", "Register for a class".
- Error messages say what to do next.

### Language

**English only.** All page copy, handwritten notes, button labels and pre-filled WhatsApp messages are in English. No Roman Urdu and no Urdu script on the site.

### Humour

Blog posts follow `02-Brand/SJ-ACADEMY-BLOG-VOICE-GUIDELINES.md`, which sets the full sarcasm rules: targets, placement and volume. Landing pages follow section 14 of the landing page copy guidelines: at most one dry line per section, never on facts, fees, buttons or the WhatsApp message. Other page copy outside the blog stays lighter still: dry, never offensive, and it must add value or be relatable. When in doubt, cut the line.

### Naming Cambridge

- First mention: "Cambridge International" or "Cambridge O Level" and "Cambridge International AS and A Level". "CAIE" is fine after that, since it is the term people search for.
- Subjects carry the syllabus code on first mention: "A Level Business (9609)".
- Exam series: "May/June 2027", "Oct/Nov 2026".
- Never imply affiliation. No Cambridge logos. Pages with past papers or syllabus material carry this line: "SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge."
- **Open point:** Cambridge past papers are Cambridge's copyright. Whether the site hosts files, links out, or does both needs a decision from the owner, ideally after a check with someone qualified.

### Facts register

The only numbers and claims that may be stated. One source of truth: when a fact changes, change it here first, then on the pages listed in the register.

| Fact | Approved wording | Source | Last confirmed | Review |
|---|---|---|---|---|
| A*s | 950+ A*s | Internal results record | Carried from v2.0, not re-checked | After each results day (August, January) |
| Students | 4,500+ students taught | Internal record | Carried from v2.0, not re-checked | Yearly |
| Google rating | Rated 5.0 on Google from 226 reviews. Never "226+ five-star reviews" | Google Business profile | Carried from v2.0, not re-checked | Quarterly |
| Faculty | Teachers from LUMS, IBA and KGS | Internal | Carried from v2.0 | Yearly |
| Location | Plot 29C, Lane 5, Seher Commercial Area, DHA Phase 7, Karachi | | Carried from v2.0 | On change |
| WhatsApp | +92-336-2144454 | | Carried from v2.0 | On change |
| Registration popup | Elementor popup 6023 | | Carried from v2.0 | On change |

### Facts that must not be stated

- A batch size number. Say "small batches".
- One-on-one or home tuition. It is not offered.
- Demo classes for lab practicals. Students join practicals directly.
- Full fee tables on marketing pages. Enrol pages may state the monthly "from" figure ("From Rs. 10,500 a month per subject"), taken from the live fee page and linked to it. Everything else stays on the fee page.
- Frequencies or durations that are not confirmed.
- Reviews that are not real, word-for-word quotes.
- Sample content presented as real. Label it "sample".

---

## 15. Calls to action and measurement

| Situation | Primary | Secondary |
|---|---|---|
| O Level and A Level classes | "Book a free demo on WhatsApp" (opens WhatsApp with the level and subject filled in) | "Register for a class" as a text link under the button |
| Lab practicals | "Join on WhatsApp" | "Register for a class" |
| Ready to enrol | "Register for a class" (opens popup 6023) | "or WhatsApp us" as a text link |
| Tools and resources | The tool's own action first. The class offer comes after the result | Text link |

- WhatsApp message pattern, one field per line: "Hi SJ Academy, I'd like to book a free demo class. / Level: [level] / Subject: [subject] / Session: [series] / Mode (in class or online): / (Ref: [page code]) / My name is ". Full rules in section 13 of the landing page copy guidelines.
- Every resource has a "Share on WhatsApp" text link.
- The class offer never interrupts a tool or a resource. It follows the result.

### Events

The standard page script sends these. Every tracked link carries `data-loc` (for example `hero`, `bottom_bar`, `final_band`).

| Event | Fires on | Marked by |
|---|---|---|
| `whatsapp_click` | Any WhatsApp link | Automatic |
| `register_open` | Registration popup link | Automatic |
| `resource_download` | A file download | `download` attribute on the link |
| `tool_complete` | A tool shows its result | `data-event="tool_complete"` |
| `resource_share` | A share link | `data-event="resource_share"` |

Never write the literal analytics function name in inline scripts; the standard script already avoids it so Flying Scripts does not delay the page.

---

## 16. SEO and content standards

| Family | Title pattern | Structured data |
|---|---|---|
| Enrol (subject) | `[Level] [Subject] Tuition in Karachi & Online ([code]) \| SJ Academy` | Course, FAQPage, BreadcrumbList |
| Enrol (level, home) | `[Level] Tuition in Karachi & Online \| SJ Academy` | LocalBusiness on the homepage, FAQPage |
| Tool | `[Tool name]: [what it does] \| SJ Academy` | WebApplication or FAQPage |
| Resource | `[Subject] ([code]) [resource] [years] \| SJ Academy` | BreadcrumbList, CollectionPage |
| Reading | `[Question or topic] \| SJ Academy` | Article with author and dates, BreadcrumbList |
| Proof | `[What it shows] \| SJ Academy` | No review markup written by the business about itself |
| Event | `[Event], [date] \| SJ Academy` | Event |
| Info | `SJ Academy [page name]` | FAQPage where it has one |

Rules:

- One H1 with the keyword. The kicker pill sits inside it when it carries the keyword.
- Meta description: 140 to 155 characters, states who, what, where and the next step.
- All content that matters for search is in the HTML. JavaScript only shows, hides and enriches.
- **Never change a live address** without a redirect. The rebuild must not lose rankings.
- **Internal links:** every page links to its level page, its subject page and one tool or resource. Subject pages do not link to the teachers page.
- **Freshness:** Resource and Reading pages show `sj-updated` and the syllabus years they cover.
- **Short answer first:** guides open with a one-paragraph answer (`sj-answer`). This serves readers and AI search.
- Structured data must match what is visible on the page.

---

## 17. Performance budget

The audience is largely on mid-range Android phones and mobile data.

| Measure | Budget |
|---|---|
| Largest Contentful Paint on 4G | under 2.5 seconds |
| Layout shift | under 0.1 |
| Interaction to Next Paint | under 200ms |
| Page widget (HTML, page CSS, script) | under 60KB |
| Images above the fold | one, under 120KB |
| Fonts | two families, four weights in total |

Rules:

- No sliders, autoplay carousels, parallax, animated counters or popups on load.
- Extra data (timetables, blog posts) is requested only when needed and cached in `sessionStorage`.
- Video loads only after a tap.
- Every image has width and height.
- Later improvement: self-host the two fonts and move the stylesheet from Additional CSS to a cached file.

---

## 18. Build rules

### The shared stylesheet

- `sj-brand.css` (in `02-Brand`) is pasted once into **Appearance > Customize > Additional CSS**, after the site's older custom CSS. Paste the minified version, `sj-brand.min.css`. To update, replace the whole block from its first line (`/*! sj-brand.css ...`) to the end.
- Every rule in it starts with `#sj`. It cannot affect the theme, header, footer or older pages.
- The first line carries the version. To check a live site, view source and search for `sj-brand.css`.
- After any change: clear WP-Optimize, Cloudways and Cloudflare caches.
- A staging copy of the site needs the stylesheet too, or new pages will look unstyled.

### Page skeleton

```html
<!-- fonts: the three link lines from section 5 -->
<div id="sj" class="sj-p-[page-name]" data-family="[family]">
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap"> ... </div>
  </section>
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap"> ... </div>
  </section>
  <div class="sj-bar"> ... two buttons ... </div>
</div>
<style>/* page-only CSS. Every selector starts with #sj.sj-p-[page-name] */</style>
<script>/* standard page script, copied unchanged from sj-page-script.js */</script>
<script type="application/ld+json"> ... </script>
```

### Rules

- One Elementor HTML widget per page, in a full-width section with zero padding and no entrance animation. Page layout "Elementor Full Width", Hide Title = Yes.
- One wrapper per page: `id="sj"` plus a page class. Page-only CSS is for layout unique to that page and stays under 40 lines. If a pattern is needed on a second page, it moves into the shared stylesheet with a version bump.
- **Never restyle a shared class in page CSS.** If an element looks wrong, fix the stylesheet.
- No new colours, sizes, radii or shadows in page CSS. Use the tokens.
- Files are plain ASCII: HTML entities in markup, `\XXXX` in CSS, `\uXXXX` in scripts. Check before delivery.
- Do not use `blockquote` or `footer` tags; the theme styles them. Use `div` with `sj-quote`.
- Grid children already get `min-width:0` from `sj-grid`. Custom grids must set it.
- Phone first: design at 360px, check 320, 390, 768 and 1440.
- Scripts are wrapped in a function, never depend on jQuery, and never use IDs without the page prefix.
- Test in a page that mimics the theme's styles, then in Elementor on a draft, then on a real phone.

### Print

The stylesheet prints Resource and Reading pages cleanly: white background, no buttons, no bottom bar, no tilt, link addresses shown. Add `sj-noprint` to anything else that should not print, and `sj-printonly` for a printed footer with the page address. Hiding the theme header and footer in print is a later task in the theme, not in this file.

---

## 19. Templates that make the site a resource

### Subject hub (Resource family)

One page per subject and level. The page a student opens every week.

1. Breadcrumb, H1 with subject and code, syllabus years chip, updated line
2. Filter bar: paper, year, series
3. Past papers as download cards in index tabs by year
4. Definitions and notes as soft tiles
5. Model answers (two or three, linking to the full set)
6. Exam dates chip and timetable link
7. The teacher and the class offer, after the resources
8. FAQ

### Model answer (Reading family)

1. Breadcrumb, H1 with the question topic and marks
2. `sj-paper sj-paper-full`: question, answer with marks in red pen, examiner note
3. Round stamp with the mark
4. "Why it scored": steps
5. One margin note per screen
6. Related answers, then the class offer

Only real marked answers, or answers labelled "sample".

### Resource finder (Resource family)

Search plus choice chips for level, subject, year and series. Results as download cards. Empty state with a "Clear filters" button. Each result has a share link.

### Parent path

A "For parents" block on every Enrol page with five soft tiles: fees, timetable, teachers, results, location. The Info pages they lead to:

- **Fees:** what is included, how and when to pay, what is not included.
- **Teachers:** teacher cards with qualification, subjects and years teaching.
- **Results:** verified results wall, filterable by subject.
- **Contact:** address, map link, class hours, who answers WhatsApp and when.
- **Policies:** refunds, attendance, communication with parents, photo consent.

---

## 20. Off-site templates

The site, Instagram and PDFs should read as one brand.

| Item | Size | Rules |
|---|---|---|
| Share image (Open Graph) | 1200 x 630 | Canvas background, one headline with one highlighter, logo bottom left, no more than one paper element |
| Instagram post or carousel cover | 1080 x 1350 | Same type and highlighter. One handwritten note. Dotted surface |
| Instagram story, WhatsApp status | 1080 x 1920 | Keep text inside the middle 1080 x 1420 |
| PDF handout | A4 | Poppins, ink on white, yellow highlighter on headings, footer with sjacademy.pk and the page address. No tilt in print |
| Favicon | 32, 180 and 512 | Icon on the yellow square (`Logo Search Engine.png`) |

Logo placement on all of the above: horizontal version, bottom left, inside the clear space rule. Detailed social templates are a separate piece of work, not yet built.

---

## 21. Governance

- **Owner:** Sunyyan Junaid approves all changes to this guide and the stylesheet.
- **Versions:** patch (3.0.1) for fixes with no visual change, minor (3.1) for new elements or tokens, major (4.0) for anything that changes existing pages.
- **Review:** twice a year, after each exam series (July and December). Check facts, links, dates and syllabus years.
- **Adding an element:** it must pass the three tests in section 1, have one stated job, a rule, a density limit and all states. It goes into the stylesheet, the brand kit and this guide in the same change.
- **Retiring an element:** mark it "retired" here, list the pages using it in the register, remove it from the stylesheet once those pages are updated.

### Page register

Record every page here when it ships.

| Page | Family | Wrapper | CSS | Lead accent | Circled | Status |
|---|---|---|---|---|---|---|
| Homepage | Enrol | `#sjh` | Own (pre-3.0) | To record | To record | Live |
| Fee structure | Info | `#sjf` | Own (pre-3.0) | To record | To record | Delivered |
| Class timetable | Info | `#sjt` | Own (pre-3.0) | To record | To record | Delivered |
| A Level Business tuition | Enrol | `sj-p-a-level-business` | Shared 3.1.1 | Sample answer papers | 6 of the 12 | Live, v2.1 (copy rewritten to the landing page copy guidelines, 8 October 2026) |

Migration: the four pages above move to the shared stylesheet one at a time, after the first new page built on 3.0 has been checked on a real phone.

### Change log

| Version | Date | Change | Pages to update |
|---|---|---|---|
| 2.0 | October 2026 | Notebook design language, page families, element set | |
| 3.0 | 2 October 2026 | Shared stylesheet, tokens, functional components, states, accessibility, consent, registers, templates, governance | None. Older pages keep their own CSS |
| 3.0.1 | 2 October 2026 | Logo section completed from the delivered artwork. Clean SVG set exported from the Illustrator master. No stylesheet change | None |
| 3.0.2 | 2 October 2026 | Humour note now points to the blog voice guidelines. No stylesheet change | None |
| 3.1 | 3 October 2026 | Heading weights: H1 600, H2 500, tighter letter spacing and line height. Paragraph colours unchanged. Poppins 600 added to the font link. Stylesheet 3.1.1. File names updated for the reorganised folder | All four built pages: re-paste the updated widgets |
| 3.2 | 8 October 2026 | Landing page copy guidelines added as the copy standard for Enrol and Event pages. Enrol pages may show the monthly "from" fee, linked to the fee page. Demo button reads "Book a free demo on WhatsApp", with "Register for a class" as a text link. New WhatsApp message pattern with a page reference. No stylesheet change | Enrol pages: apply when each is next rebuilt. A Level Business is done |

---

## 22. Do not

- Add a coloured bar to the top of cards.
- Use glass effects, gradients between brand colours, or shadows heavier than the three tokens.
- Use decorative shapes with no meaning (circles, plus signs, blobs, waves).
- Put two tilted elements side by side with the same tilt.
- Use handwriting for body text, buttons, navigation or anything the reader must not miss.
- Copy the homepage section by section. Start from the page family, then choose.
- Restyle shared classes in page CSS, or invent a new value outside the tokens.
- Remove the focus outline.
- Publish a student's name, photo or result without written consent.
- Present sample content as real.

---

## 23. Checklist before publishing

**Design**

- [ ] Page family chosen, with its surface, hero and lead reader
- [ ] Four signature elements present
- [ ] Three accent elements, with a different lead accent from the last page in this family
- [ ] Density limits respected
- [ ] No new colours, sizes or radii outside the tokens

**Content**

- [ ] One H1, with the keyword
- [ ] Only facts from the register
- [ ] Landing pages: the landing page copy checklist (section 21 of that guide) passed
- [ ] English only, no em dashes, sentence case
- [ ] Sample content labelled, real content consented
- [ ] Updated line and syllabus years on Resource and Reading pages

**Function**

- [ ] Buttons do what their labels say
- [ ] Every link and field reachable by keyboard, with a visible focus ring
- [ ] Forms show clear errors; tools have empty, loading and error states
- [ ] No sideways scroll at 320 and 360px
- [ ] Tap targets 48px or more
- [ ] Tracked links carry `data-loc`

**Build**

- [ ] Wrapper is `id="sj"` with a page class and `data-family`
- [ ] Page CSS under 40 lines and scoped to the page class
- [ ] File is plain ASCII
- [ ] Structured data matches the visible page
- [ ] First image eager, the rest lazy, all with width and height
- [ ] Tested in Elementor on a draft and on a real phone
- [ ] Page register updated
