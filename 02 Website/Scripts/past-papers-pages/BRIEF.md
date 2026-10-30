# Subject past papers pages: brief, order and SEO plan

Started 30 October 2026. Generator: `build.py` (this folder), copy and facts: `subjects.py`, check: `preview.js`.

## Five-line brief
• Who: O and A Level students in Pakistan looking for one subject's past papers, mostly on phones.
• Job: find the right year and paper in two taps, open the paper, mark scheme or insert, or both side by side.
• Format: Resource page on the shared stylesheet, the same design as the live A Level Business, Economics and Maths past papers pages (approved: "the past papers widget and selector is fine").
• Success: Google clicks to each page (Search Console), `resource_download` and `viewer_click` events, WhatsApp leads tagged `PP-O-{code}`.
• Must not: link to a file that is not in storage, or state a paper fact that was not checked against the papers.

## Why these pages, in this order
Checked on 30 October 2026 by testing a link from each live page against storage:

| Order | Page | Live state | Why this place |
|---|---|---|---|
| 1 | O Level Pakistan Studies 2059 | every link 404 (wrong folder and wrong file names) | Compulsory for O Level students in Pakistan, so the widest audience; the most broken page |
| 2 | O Level Islamiyat 2058 | every link 404 (folder) | Compulsory in Pakistan |
| 3 | O Level Mathematics D 4024 | every link 404 (folder) | Taken by almost every O Level student; Maths comes first on general pages |
| 4 | O Level English Language 1123 | every link 404 (folder) | Compulsory; syllabus changed in 2024 (insert moved to Paper 1) |
| 5 | O Level Urdu Second Language 3248 | every link 404 (folder and file names) | Compulsory for most students in Pakistan |
| 6 | O Level Accounting 7707 | every link 404 (folder) | Commerce classes are the revenue priority (PRIORITIES.md) |
| 7 | O Level Business Studies 7115 | every link 404 (folder) | Commerce |
| 8 | O Level Computer Science 2210 | every link 404 (folder) | Elective |
| 9 | A Level Urdu 9686 | every link 404 (file names) | Smallest audience |
| 10 to 13 | O Level Biology, Chemistry, Economics, Physics | links work, but the list is built by script after load, so Google sees no papers | Same rebuild for search, once 1 to 9 are done |
| later | A Level Business, Economics, Maths (already rebuilt) | 30 of 1,395 links broken | Regenerate from the checked file list |

No Semrush data was used. Order is by how many students each page serves and how broken it is.

## SEO approach (without Semrush)
• **Keep every address.** `/o-level-past-papers/{subject}-{code}/` pages are indexed (URL inspection 30 September 2026). Rebuilding in place keeps that.
• **Search engines can read every paper.** The old pages built the list with JavaScript after loading, so Google saw "Showing 0". Every link is now in the HTML, with one year shown at a time for people.
• **Match how students search.** Competitors in the results for "o level pakistan studies past papers" are Save My Exams (split by paper) and pastpapers.co (split by series). Students also search by paper nickname ("pak studies paper 2 geography") and short name ("pak studies"). Each page carries: the full name and code in the title, H1 and lead; the nicknames in the lead, filter buttons and an FAQ; series names written the way Cambridge writes them (May/June 2025, Oct/Nov 2025).
• **Unique content per page, checked against the papers:** a "What is on each paper" table (time, marks, how many questions, answer booklet or question paper), taken from the latest question papers' cover pages. Competitors list files only.
• **Title, meta, keyphrase per page** in the comment at the top of each widget file, for Yoast. Title under 60 characters with the code.
• **Structured data:** CollectionPage, BreadcrumbList and FAQPage in each widget.
• **Internal links:** each page links to the subject tuition page, the viewer (side by side links per paper), grade thresholds, the mark scheme guide and the other subject pages. Still to do after publishing: link each page from its tuition page and from `/o-level-past-papers/`.
• **Fix alongside:** the `/o-level-past-papers/` directory page still carries a wrong embedded canonical (`https://sjacademy.com/o-level-past-papers-faq`, found 30 September). Remove it in Elementor. Old duplicate `/o-level-math-past-papers/` should 301 to `/o-level-past-papers/mathematics-d-4024/`.
• **Measure:** Search Console clicks and impressions per page, 4 and 8 weeks after publishing.

## Accuracy record

### O Level Pakistan Studies 2059 (built 30 October 2026)
• Paper names, times, marks and how to answer: read from the cover pages of 2059_w25_qp_01, 2059_w25_qp_02 and 2059_s25_qp_01 (and 2059_s22_qp_01, same Paper 1 format). Paper 1: The History and Culture of Pakistan, 1 hour 30 minutes, 75 marks, Section A Question 1 compulsory, two of Questions 2 to 5 in Section B, 25 marks each (4, 7 and 14 mark parts), answer booklet, sources in the insert. Paper 2: The Environment of Pakistan, 1 hour 30 minutes, 75 marks, answer three of five questions, answers on the question paper, ruler needed, figures in the insert (checked 2059_w25_in_02) and on the paper.
• File names: qp_01, qp_02, ms_1, ms_2, in_01, in_02 (from storage).
• Teacher: Sir Kashaan Ali, from the O Level tuition page. No affiliation stated (FACTS asks to confirm affiliations first).
• Claims: free demo class (FACTS); DHA Phase 7 and live online (FACTS). No numbers used.
• Links: all 69 file links return 200 through sjacademy.pk (checked with a browser user agent; Cloudflare refuses Python's default one).
• Page checks (`preview.js`): one H1, tabs, filter, structured data, no script errors, no sideways scroll on a phone.
