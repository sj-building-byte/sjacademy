# Handoff: past papers pages (critical) and the 7 October session

Paste this into a new chat, or tell the new chat to read `claude/past-papers-handoff.md` in the Website Design project. Read `claude/website-rebuild-handoff.md` first for the general build rules; this file adds what changed on 7 October 2026.

---

## 1. Past papers pages: the critical part

### The finding

The subject past papers pages rank for nothing because the paper list is built by a script after the page loads. The HTML that a crawler reads says "Showing 0" and contains no paper links. Confirmed on `/a-level-past-papers/business-9609/` by reading the page source. The other 12 A Level subject pages use the same tool ("Your existing Backblaze tool, modified to lock into [subject]"), so they almost certainly have the same problem. The O Level subject pages have not been checked.

### Why it matters

| Keyword (Pakistan, Semrush, 7 Oct 2026) | Volume | KD |
|---|---|---|
| a level business past papers | 3,600 | 21 |
| business a level past papers | 720 | 17 |
| business studies a level past papers | 90 | 15 |
| a level business topical past papers | 30 | n/a |

This is far larger than any tuition keyword seen so far (the biggest tuition term, "a level tutor in karachi", is 720). The top 10 for the main keyword is weak: number 1 (papacambridge) has Authority Score 9 and one backlink; three of the ten have a score of 0. Neither SJ Academy Business past papers address ranks in the top 100.

Maths has the same shape: "a level maths past papers" 590, "a level maths syllabus" 720, against 20 to 30 for Maths tuition terms.

### What was built

`02 Website/Pages/a-level-business-past-papers-elementor-widget.html` (project: `claude/a-level-business-past-papers-elementor-widget.html`). Version 1.0, on the shared stylesheet, wrapper `sj-p-pp-business`, family Resource.

- All 324 file links are written into the HTML: 2020 to 2025, May/June and Oct/Nov, Papers 1 to 4, variants 1 to 3, question paper and mark scheme, plus the insert for Paper 3.
- Hero: two columns. Left: breadcrumb, pill "Cambridge AS & A Level - 9609", H1 "A Level Business past papers and mark schemes", lead, chips. Right: offset card "Jump to a year" with six year buttons that open the matching tab and scroll to the papers.
- Papers section: paper filter chips (All, Paper 1 to 4), year tabs, one stacking table per series (rows = papers, columns = variants). Link labels are "QP 12", "MS 12", "IN 32".
- Without scripts every year is visible. With scripts on, the page script hides all but the first year and reveals the tabs and filter. This is deliberate so crawlers see everything.
- Then: how to use past papers (four steps and a file-name explainer on exam paper), related Business resources, chips to the other 12 subjects' past papers pages, seven FAQs (four carried from the old page), yellow class-offer band last. No phone bottom bar on this page.
- Structured data: CollectionPage, BreadcrumbList, FAQPage.
- Yoast title: `A Level Business Past Papers (9609) 2020 to 2025 | SJ Academy`
- Yoast meta: `Free A Level Business past papers (9609) with mark schemes and inserts, 2020 to 2025. Papers 1 to 4, May/June and Oct/Nov, all variants. No sign-up.`

### The generator (use this for the other subjects)

`02 Website/Scripts/generate-past-papers-page.py` (project: `claude/generate-past-papers-page.py`) is the Python script that wrote the Business page. It is a single file with the settings at the top:

- `B`: the storage folder for the subject
- `YEARS`, `T` (paper numbers and file types per paper), `PN` (paper names)
- `OUT`: where the widget is written
- `U`: the folder that holds `02 Website/Scripts/sj-page-script.js` (it inlines the standard page script)

The copy, FAQs, wrapper class (`sj-p-pp-business`), IDs (`sjp-`) and resource tiles are written for Business inside the script. For another subject, change the settings and the subject-specific copy, then run it. It asserts the output is plain ASCII.

### Where the files live

- Storage base: `https://sjacademy.pk/file/Past-papers-storage` (the bare domain, not `www`; `www` returns 404 for this path).
- Pattern: `{base}/A+Level/{Subject}+%28{code}%29/{May+June|October+November}+{year}/{code}_{s|w}{yy}_{qp|ms|in}_{paper}{variant}.pdf`
- Example: `https://sjacademy.pk/file/Past-papers-storage/A+Level/Business+%289609%29/May+June+2024/9609_s24_qp_12.pdf`
- The old tool's settings for Business: years 2020 to 2025, sessions s and w, variants 1 to 3, papers 1 and 2 (qp, ms), 3 (qp, ms, in), 4 (qp, ms). The new page uses exactly this set.

### Not verified

- **The 324 links were never tested.** The sandbox and the linked computer's shell are both blocked from `sjacademy.pk` (bare domain) by the network allowlist. The links are the same ones the old tool generated. Sunyyan needs to tap a few per year on the draft.
- Whether March series, examiner reports or grade thresholds exist in storage. The old tool did not list them, so the new page does not.
- Exam durations on the page are copied from the Business tuition page.

### State on 7 October, end of session

- Sunyyan pasted the first version into Elementor and saw ruled lines; that was the first paste, not the current file. The file in `05-Elementor Widgets` is correct (dotted surface, "Jump to a year" card, no "Go to the papers" link). **He had not yet confirmed the re-paste.** If he re-pastes and still sees lines, check caching (WP-Optimize, Cloudways, Cloudflare).
- The page has not had its phone check.

### Decisions made

- **Surface:** he rejected the ruled-paper surface ("this design choice doesn't make sense"). This page uses dots. The brand guidelines (section 7) still say Resource = ruled paper. **Open:** he was asked whether all Resource pages should use dots; no answer yet. If yes, update section 7 and the change log.
- He approved the papers table, year tabs and paper filter ("the past papers widget and selector is fine").
- Keep `/a-level-past-papers/business-9609/` as the Business past papers page.

### Still to do, in order

1. Confirm the re-paste shows the current version; phone check; tap-test links.
2. 301 redirect `/a-level-business-past-papers/` to `/a-level-past-papers/business-9609/` on publish day. Neither ranks, so nothing is lost.
3. Get his answer on dots for all Resource pages; update the brand guidelines if yes.
4. Generate the other 12 A Level subject pages from the generator. Needed per subject: years in storage, papers and file types per paper (inserts, practical papers), paper names. Read each live page's source for its `subjectsData` line; it holds exactly this.
5. Check the O Level subject past papers pages for the same script-built list.
6. Resolve the other old flat addresses in the site register (`/a-level-mathematics-past-papers/`, `/o-level-math-past-papers/`) the same way: keep the new-structure page, redirect the old one.
7. Rebuild the hubs (`/a-level-past-papers/`, `/o-level-past-papers/`, `/past-papers/`).
8. Open decision carried from the brand guidelines: hosting Cambridge files versus linking out. The new page hosts, as the old one did, and carries the copyright and independence line.

### Known limits of the Business page

- The widget is about 82KB, over the 60KB budget in the brand guidelines. The links are almost all of it and are the point of the page.
- Link labels are short ("QP 12") inside a row and series heading; there are no per-link aria labels (they would add about 20KB).
- The shared `sj-bg-ruled` surface draws lines that cut through text. If it is ever used again it needs fixing in the stylesheet, not per page.

---

## 2. Other pages built or changed on 7 October

All are in `05-Elementor Widgets` and in the project under `claude/`. All are on the shared stylesheet 3.1.1. He said "Stylesheets are working", so shared-stylesheet pages render on the live site. None of the four has a confirmed phone check or is confirmed live.

| Page | File | State | Yoast title |
|---|---|---|---|
| A Level Maths tuition | `a-level-maths-tuition-elementor-widget.html` | Delivered. First page on the shared stylesheet | A Level Maths Tuition in Karachi & Online (9709) \| SJ Academy |
| Main A Level page | `a-level-tuition-center-karachi-elementor-widget.html` | Delivered. He said "This is fine" | A Level Tutors & A Level Academy in Karachi \| SJ Academy |
| A Level Business tuition | `a-level-business-tuition-elementor-widget.html` | v2.0, migrated from own CSS. v1.3 and v1.4 are in `Archive` | A Level Business Tuition in Karachi & Online (9609) \| SJ Academy |
| Business past papers | see section 1 | Delivered | see section 1 |

Meta descriptions:

- Maths: `A Level Maths (9709) tuition in Karachi with Sir Salman Junaid, ex-KGS faculty. AS and A2 classes at DHA Phase 7 and live online. Book a free demo class.`
- Main A Level: `A Level tutors near you in Karachi. SJ Academy is an A Level academy and coaching center at DHA Phase 7 and online, with a free demo class in 12 subjects.`
- Business: `A Level Business (9609) tuition in Karachi with Sir Sunyyan Junaid. AS and A2 Business Studies classes at DHA Phase 7 and live online. Book a free demo.`

### Standing instructions from this session

- **On general pages, Maths and Sir Salman come first** (first in class finders and selected by default, first subject tile, first teacher card).
- Shared-stylesheet pages are approved for use; the remaining own-CSS pages (homepage, fees, timetable) can migrate.
- He does not like leading with "950+ A*s"; the Business page proof strip now uses "8+ years teaching Business".
- WhatsApp messages name the page ("I saw the A Level Maths page and would like to...") for lead tracking.
- Keyword work is done with his Semrush account: tell him exactly what to search (Pakistan database), he sends screenshots. Positions reports for the page being rebuilt come first.

### Semrush findings to keep

- Main A Level page ranks 7 for "a level tutors near me" (720, KD 13), which is 18 of its 19 estimated visits; 11 for "a level academy" (110). It also sits at 23 to 42 for generic "coaching center" terms, which came from the old H1. The rebuild keeps "tutors", "academy" and "coaching center".
- "a level tutor in karachi" 720, KD 25. "a level tuition karachi" only 30.
- "a level colleges in karachi" 880 and five variants: college-list intent, served by `/blog/top-a-level-colleges-in-karachi/`. Recommended: link from that post to the main A Level page with the anchor "A Level tutor in Karachi". Not done.
- Business: tuition page, definitions page and exam guide post rank for nothing or one keyword. "a level business syllabus" variants 390, 260, 110, 90; "a level business book" variants about 320 in total at KD 9 to 11 (a blog post was recommended, not written).
- Maths tuition terms are 20 to 30; the volume is in "a level maths syllabus" (720) and past papers (590).

### Open items per page

**Maths**
- `/a-level-maths/` is untouched; he chose "decide later". Recommendation given: keep it and rebuild it as a Maths syllabus and resource hub, not a redirect.
- Timings: the loader matches timetable cells containing "math" (not Add or Further Maths); never tested against the real sheet. Falls back to a timetable link.
- Paper routes written as AS = P1 with M1 or S1; A2 = P3 with a second applied paper. Unconfirmed.
- "250+ A*s" used without "in 8+ years" (clashes with "12+ years").
- Shahr Bano's review is from the old Maths page, not checked against Google.
- Two demo video links come from the old page; not played.
- No classroom photo of Sir Salman, so a teacher card is used in place of a polaroid.
- Positions report for the two Maths addresses was requested, not received.

**Main A Level page**
- Dropped from the old page: "450+ A* grades", "300+ students currently enrolled", "10-12 students", "one-on-one guidance", fee figures.
- Law left out (no teacher listed); page says 12 subjects.
- H1 pill "A Level tutors & coaching center, Karachi" wraps to two lines on phones.
- Google Business Profile not reviewed; "near me" rankings depend on it.
- After publishing, watch "a level tutors near me" and "a level academy" for two to three weeks.
- Unconfirmed wording: "evening and weekend classes", "composite classes cover AS and A2 in one run", "after your demo class, fill in the registration form".

**Business**
- The five syllabus areas named on the page were written without looking them up.
- Mark picker chips wrap to two rows on phones.
- Polaroids were not seen with their real photos.

### Testing notes

- Playwright method as in the main handoff. Test files were in the session scratchpad and are gone.
- A stacking table cell with more than one element inside breaks on phones (each child becomes a grid item). Wrap the cell's content in one `span`.
- Inside the brown band, `sj-muted` and `sj-hand` turn pale or yellow, so they are unreadable on a white panel placed inside it. Set the colour in page CSS with one extra class of specificity.
- The Write tool turned `·` in scripts into a literal character once. Run the non-ASCII check on every file before delivery.
- The site register in the local folder was updated for all four pages. **The project copy (`claude/site-register.md`) was not.**
