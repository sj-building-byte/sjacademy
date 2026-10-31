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

### The other eight pages (built 30 October 2026, approved template)
Paper names, times, marks and how to answer were read from each subject's question paper cover pages in storage. Where a syllabus changed, the older papers were read too and each year on the page shows the names used that year.

| Page | Papers read | Facts on the page | Syllabus change shown |
|---|---|---|---|
| Islamiyat 2058 | 2058_w25_qp_11, qp_21; 2058_s25_qp_12, qp_22; 2058_s20_qp_11 | Both papers 1 hour 30 minutes, 50 marks; five questions, answer four (Questions 1 and 2, then two others); Question 1 on Qur'an passages (Paper 1) or Hadiths (Paper 2); written on the question paper | None |
| Mathematics D 4024 | 4024_w25_qp_11, qp_21; 4024_s25_qp_12; 4024_s23, s24, w24 qp_11 and qp_21 | 2025: Paper 1 Non-calculator and Paper 2 Calculator, 2 hours, 100 marks each. Up to 2024: Paper 1 2 hours, 80 marks, no calculator; Paper 2 2 hours 30 minutes, 100 marks | 2025 |
| English Language 1123 | 1123_w25_qp_11, qp_21; 1123_s24_qp_11; 1123_s23_qp_11, qp_21, in_21 | 2024 on: Paper 1 Reading, 2 hours, 50, insert; Paper 2 Writing, 2 hours, 50, Section A Directed Writing, Section B Composition (one question). Up to 2023: Paper 1 Writing 1 hour 30 minutes, 60; Paper 2 Reading 1 hour 45 minutes, 50, insert | 2024 |
| Urdu Second Language 3248 | 3248_w25_qp_01, qp_02; 3248_s24_qp_01; 3248_w24_qp_02; 3248_s23 and s20 qp_01, qp_02 | 2024 on: Paper 1 Reading and Writing 1 hour 45 minutes, 50; Paper 2 Grammar, Writing and Translation 1 hour 30 minutes, 50, no dictionaries. Up to 2023: Composition and Translation 2 hours, 55; Language Usage, Summary and Comprehension 1 hour 45 minutes, 55 | 2024 |
| Accounting 7707 | 7707_w25_qp_12, qp_22, ms_22; 7707_s20_qp_21 | Paper 1 Multiple Choice, 1 hour 15 minutes, 35 questions, 35 marks, calculator allowed; Paper 2 Structured Written Paper, 1 hour 45 minutes, 100 marks. "Own figure rule" confirmed in the mark scheme. 7707 replaced 7110 from 2020 (web sources agree) | None |
| Business Studies 7115 | 7115_w25_qp_11, qp_21; 7115_s22_qp_11, qp_21 | Paper 1 Short Answer and Data Response, Paper 2 Case Study (insert), both 1 hour 30 minutes, 80 marks | None |
| Computer Science 2210 | 2210_w25_qp_12, qp_22; 2210_s23_qp_11; 2210_s22_qp_11, qp_21 | 2023 on: Computer Systems and Algorithms, Programming and Logic, 1 hour 45 minutes, 75 each. Up to 2022: Theory (75) and Problem-solving and Programming (50), 1 hour 45 minutes each | 2023 |
| A Level Urdu 9686 | 9686_w25_qp_02, qp_03, qp_04; 9686_s15_qp_2 | Paper 2 Reading and Writing 1 hour 45 minutes, 70, insert; Paper 3 Essay 1 hour 30 minutes, 40 (16 content, 24 language); Paper 4 Texts 2 hours 30 minutes, 75, three questions on different texts. Only Papers 2, 3 and 4 (Cambridge threshold tables list components 02, 03, 04) | None |

Teachers in the closing bands come from the live O and A Level tuition pages: Sir Kashaan Ali (Islamiyat), Sir Salman Junaid (Maths), Miss Tayyaba Yaseen (English), Miss Asmat Zafar (both Urdu pages), Sir Saifullah (Accounting), Sir Aaliyan (Business Studies), Sir Riza Walji (Computer Science). No affiliations stated. Subjects with no own tuition page link to the O Level or A Level tuition page.

Checks on all nine pages, 30 October 2026:
• 871 PDF links, all 200 through sjacademy.pk.
• 397 "Side by side" links opened in the real viewer widget, each loads the same question paper as its row (`check-side-links.js`).
• `preview.js` on each: one H1, tabs, filter, structured data, no script errors, no sideways scroll on a phone.

Storage gaps seen while building: O Level storage starts in 2020; May/June 2026 is not in storage for these subjects (Cambridge has published A Level Urdu June 2026 thresholds, so the papers exist). Upload them and run `check-files.py`, then `build.py`.

### O Level Biology, Chemistry, Physics and Economics (built 31 October 2026)
Their old pages worked but built the paper list with JavaScript, so Google saw no papers. Rebuilt on the same template.

| Page | Papers read | Facts on the page | Change shown |
|---|---|---|---|
| Biology 5090 | 5090_w25 qp_11, qp_21, qp_31, ci_32, qp_41; 5090_s23 qp_21, qp_31, qp_41; 5090_s22 qp_11, qp_21, qp_31, qp_61 | From 2023: Paper 1 Multiple Choice 1 hour, 40 questions, 40; Paper 2 Theory 1 hour 45 minutes, 80; Paper 3 Practical Test 1 hour 30 minutes, 40; Paper 4 Alternative to Practical 1 hour, 40. Up to 2022: Paper 6 was the alternative to practical (1 hour, 40), Paper 3 was 1 hour 15 minutes, Paper 2 had a choice in Section C | 2023 |
| Chemistry 5070 | 5070_w25 qp_11, qp_21, qp_31, ci_31, qp_41; 5070_s23 qp_21, qp_41; 5070_s22 qp_11, qp_21, qp_31, ci_31, qp_41 | From 2023: as Biology. Up to 2022: Paper 2 1 hour 30 minutes, 75, Section B choose three; Paper 4 60 marks | 2023 |
| Physics 5054 | 5054_w25 qp_11, qp_21, qp_31, qp_41; 5054_s23 qp_21, qp_31, qp_41; 5054_s22 qp_11, qp_21, qp_31, qp_41 | From 2023: as Biology. Up to 2022: Paper 2 75 with a choice in Section B; Paper 3 2 hours, 30; Paper 4 30 | 2023 |
| Economics 2281 | 2281_w25 qp_12, qp_22; 2281_s22 qp_11, qp_21 | Paper 1 Multiple Choice 45 minutes, 30 questions, 30; Paper 2 Structured Questions 2 hours 15 minutes, 90, Section A Question 1, Section B three questions | None |

"You sit Paper 1, Paper 2 and either Paper 3 or Paper 4": Cambridge syllabus wording, found in the 5054 syllabus through web search. Teachers from the O Level tuition page: Sir Umair (Biology), Sir Abdullah Zaman (Chemistry), Sir Basharat in class and Sir Salman Junaid online (Physics; FACTS confirms Sir Salman online), Sir Aaliyan (Economics).
Checks, 31 October 2026: 691 PDF links all 200; 331 side by side links all load the right paper; `preview.js` passes on each.

### A Level Business, Economics and Maths (fixed 31 October 2026)
These pages were already rebuilt and live, with hand-written copy and keywords (Business especially). The repo copies were older than the live pages, so the live widget code was taken from the live pages, the old repo copies moved to `Archive/Old widget versions/`, and only the paper tables were refreshed with `refresh-tables.py`. Headings, copy, keywords, FAQs and structured data are unchanged (diff checked). Changed outside the tables: the hero file count and "all three variants" to "every variant"; one sentence on "Side by side"; a style line and a script selector so Side by side links open normally; en dashes in Economics written as hyphens.

| Page | Broken links removed | Missing files added | Notes |
|---|---|---|---|
| Business 9609 | 22: Paper 3 inserts for 2016 to 2019 (not in storage), ms_22 May/June 2022, ms_13 Oct/Nov 2017 | 6: variant 4 of Papers 1 to 3, May/June 2021 | No insert in storage for May/June 2021 Paper 3 Variant 4. Live page has no BreadcrumbList schema (as before) |
| Economics 9708 | 8: qp and ms 12 May/June 2024, ms_21 and ms_32 Oct/Nov 2017, qp and ms 43 Oct/Nov 2021 and 2022 | 26: variant 4 in May/June 2022, 2025, 2026 and Oct/Nov 2025 | |
| Maths 9709 | 2: ms_11 May/June 2025, ms_12 Oct/Nov 2025 (question papers kept, mark schemes not uploaded) | 20: variant 5, 2025 | Page keeps its own years (2020 to 2025) and papers (P1, P3, M1, S1, S2) to match its copy. Storage also has 2015 to 2019, May/June 2026 and Paper 2 |

Checks: 1,415 PDF links all 200; 683 side by side links all load the right paper; `preview.js` passes (Business: 2 structured data blocks, as live).

## How to update a page
1. Upload new papers to Backblaze.
2. `python3 "02 Website/Tools/Past Paper Viewer/check-files.py"` (writes the file list into the viewer).
3. `python3 "02 Website/Scripts/past-papers-pages/build.py"` (rebuilds the generated pages) and `python3 "02 Website/Scripts/past-papers-pages/refresh-tables.py"` (refreshes the tables in A Level Business, Economics and Maths).
4. Re-paste the changed widgets.

