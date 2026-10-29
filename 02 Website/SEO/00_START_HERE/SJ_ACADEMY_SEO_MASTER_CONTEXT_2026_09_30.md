# SJ Academy SEO: Master Context File

**Last updated:** 30 September 2026
**Website:** https://www.sjacademy.pk/
**Local workspace:** `/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/SEO` (moved 12 Oct 2026)
**Supersedes as the starting point:** `02_Reports_and_Audits/2026-09-11_Handoff/START_HERE_SJ_ACADEMY_SEO_HANDOFF.md` (11 Sep 2026) and `02_Reports_and_Audits/2026-09-22_Progress_Report/SEO_Comprehensive_Progress_Report.md` (22 Sep 2026). Those files remain the source for the deep 10 Sep crawl evidence and the 22 Sep strategy summary. Everything needed for planning is summarised here.

---

## 0. How to use this file (read first)

This file is self-contained for planning in Claude Chat or any new session. Important limits:

- **It is a snapshot.** GSC/GA4 numbers below are from specific date windows (stated on each table). Re-pull live data before making decisions that depend on exact numbers.
- **Claude Chat cannot see the local folder, the live GSC/GA4 accounts, or the WordPress site** unless those are connected there. Upload this file (and optionally `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/CHANGE_SUMMARY.md` and the 11 Sep handoff) to a Claude Project as knowledge.
- **Local files are not the live site.** On 30 Sep changes were applied to local files only. Nothing on sjacademy.pk has been changed by Claude. See section 7 for what still needs publishing.
- Recheck any live URL immediately before editing or reporting on it.

---

## 1. Business context

- SJ Academy: Cambridge (CAIE) O Level and A Level tuition academy, **DHA Phase 7, Karachi** (Plot 29C, Lane 5, Seher Commercial). Physical classes plus **live online classes nationwide** across Pakistan.
- **Dual strategy (confirmed 22 Sep 2026):**
  1. **Tuition track:** tuition leads and brand authority. Local physical demand in Karachi/DHA and nationwide online demand have equal priority. Measured only by qualified leads and demo bookings. The pilot is A Level Business 9609.
  2. **Audience and affiliate track:** high-volume student-lifestyle content (laptops, study apps, educational websites, study spots, school/university guides) builds brand awareness and earns **affiliate income**. Measured by traffic volume and affiliate clicks.
  Judge informational pages against the audience/affiliate track, not only against tuition leads.
- Positioning: exam-focused, structured, teacher-led, deep familiarity with Cambridge expectations. Premium and confident, not arrogant.
- A Level Business pages: emphasise CAIE 9609 exam technique, application to case data, analysis chains, evaluation and recommendations, Papers 1 to 4, **Sir Sunyyan Junaid** as teacher.
- Other named teachers seen on the site: Sir Salman (A Level Maths, ex-KGS), Sir Umair (A Level Biology, LUMS), Sir Muhammad Riza (A Level Computer Science), Zaman (Chemistry). Verify affiliations before using them in new copy.
- Brand colours: Yellow `#FCE004`, Brown `#453516`, Orange `#fe6100`, WhatsApp green `#25D366`.
- **Teachwink is an independent competitor**, not connected to SJ Academy. Its public site listed the same address as SJ Academy. Investigate with evidence (signage, GBP pin, documents) before requesting any correction. Do not claim it copied the address.

## 2. Working rules (user preferences)

- Audit first, recommend second, implement after scope is approved. **Show a summary of every change before finalising.** Stage changes in a separate folder and apply only on approval, with backups.
- Preserve the WordPress header and footer. Stack is WordPress + Elementor + HTML widgets + Yoast.
- Scoped, responsive CSS in widgets. Check mobile first (64% of sessions are mobile).
- Simple solutions, no unnecessary dependencies, fast pages, easy to edit.
- Natural, conversion-focused copy. **No em dashes in user-facing copy.** No generic tuition copy, no unsupported claims ("best", "guaranteed", "highest-rated").
- WhatsApp-first CTAs for cold traffic. Don't force a full enrolment form before the user is ready.
- Preserve UTMs; verify GA4, Meta Pixel, WhatsApp and form events whenever journeys change.
- Educational facts (IBCC, thresholds, syllabus, admissions) must come from official sources. Never estimate figures.

## 3. Timeline of work so far

| Date | Work | Output |
|---|---|---|
| 10 Sep 2026 | Full audit: 166 sitemap URLs crawled, 161 extra links checked, GSC + GA4 reviewed, competitor and AI visibility review | `02_Reports_and_Audits/2026-09-10_Full_Site_Audit/` (report, inventory CSV, broken links CSV, evidence) |
| 11 Sep 2026 | Handoff written; IBCC calculator audit (decision: do not publish supplied calculator, engine inaccurate); growth diagnosis refuting a Semrush "traffic drop" (GSC showed organic clicks **+21.4%**, 9,598 vs 7,907, and impressions +28.4% over the latest 28 days) | `02_Reports_and_Audits/2026-09-11_Handoff/START_HERE_SJ_ACADEMY_SEO_HANDOFF.md`, `02_Reports_and_Audits/2026-09-11_IBCC_Calculator_Audit/AUDIT.md`, `02_Reports_and_Audits/2026-09-11_Growth_Diagnosis/SJ_Academy_SEO_Growth_Diagnosis.md` |
| 22 Sep 2026 | Consolidated progress report: dual strategy (tuition + affiliate), two-track KPIs, 90-day roadmap | `02_Reports_and_Audits/2026-09-22_Progress_Report/SEO_Comprehensive_Progress_Report.md` |
| 30 Sep 2026 (later) | Workspace reorganised into numbered folders; blog strategy and Oct to Dec 2026 calendar created (8 pillars, 36 posts, 3/week, Jan to Sep 2027 monthly themes) | `00_START_HERE/README_Folder_Guide.md`, `03_Plans_and_Content/Blog_Content_Plan_2026-27/` |
| 30 Sep 2026 (later) | Instagram analysis of 373 posts (Jan to Sep 2026): carousels drive 78% of organic follows; tech/tools and exam-technique content win saves and follows; memes/results reach far but add few followers; ~19% of follows from ~10 likely boosted posts; organic follows flat while posting rose 40%; Instagram sends traffic but almost no leads (Organic Social 3,095 sessions, 2 key events). Audience: women 35-44 largest group (21.7%), 43.5% aged 35+ (parents; export starts at 18); Karachi 27.2%, rest of Pakistan ~48.5%, abroad ~24%. Stories: 1,042, median reach 616; link stickers on only 10% of stories but 3,683 clicks at 3.8%. Paid (42 ads from screenshots): PKR 319,611 spend; 795 messaging conversations at PKR 232 avg (best PKR 100 to 150 on batch/registration offers); 30% of spend (PKR 95,690) on 'leads via messaging' ads reporting 0 results; website-visitor clicks PKR 3 to 6; no UTMs or enrolment tracking |  `02_Reports_and_Audits/2026-09-30_Instagram_Analysis/Instagram_Analysis_2026-09-30.md` |
| 30 Sep 2026 (later) | Instagram growth playbook and 13-week calendar (7 weekly series: Examiner Mode, Sir Says, Tool Drop, POV, Parent Guide, Comment-to-Get, Sunday Special; daily stories with link sticker + past-paper quiz; collabs, ambassadors, #SJStudyWithMe; Messages-objective boosts) | `03_Plans_and_Content/Instagram_Plan_2026-27/` |
| 30 Sep 2026 | Live GSC/GA4 re-audit, fixes to hub/fee/tutor-post files, new content files, metadata sheet, WordPress API check, past-paper architecture review | `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/`, `01_Website_Pages/New_Pages_Drafts/`, `03_Plans_and_Content/Metadata/Yoast_Metadata_Changes_2026_09_30.csv`, this file |

---

## 4. Data snapshot (30 Sep 2026 session)

### 4.1 GSC site health (19 to 26 Sep vs 11 to 18 Sep 2026)
- Clicks 1,708 (+0.9%), impressions 107,161 (-1.2%), CTR 1.59%, avg position 6.24 (improved from 6.47).
- One sitemap (`/sitemap.xml`), no errors or warnings, last downloaded 24 Sep. No anomalies flagged.
- Bing Webmaster Tools is not connected.

### 4.2 GSC top pages (1 Jul to 28 Sep 2026)

| Page | Clicks | Impressions | CTR | Pos |
|---|---:|---:|---:|---:|
| /blog/top-10-best-schools-in-karachi-with-fee-structures/ | 6,051 | 181,191 | 3.34% | 5.8 |
| /blog/top-schools-in-lahore/ | 2,547 | 161,818 | 1.57% | 6.6 |
| / (homepage) | 2,204 | 32,364 | 6.81% | 6.3 |
| /blog/top-a-level-colleges-in-karachi/ | 1,883 | 66,339 | 2.84% | 5.3 |
| /blog/top-10-universities-in-islamabad/ | 1,648 | 91,727 | 1.80% | 6.0 |
| /blog/beaconhouse-school-system-review/ | 1,463 | 135,806 | 1.08% | 5.4 |
| /blog/karachi-grammar-school-review/ | 969 | 36,530 | 2.65% | 5.8 |
| /blog/best-degrees-in-pakistan/ | 766 | 63,199 | 1.21% | 5.2 |
| /o-level-grade-thresholds/ | 712 | 50,271 | 1.42% | 6.9 |
| /blog/alpha-college-review/ | 590 | 34,825 | 1.69% | 6.2 |
| /blog/city-school-review/ | 515 | 55,692 | 0.92% | 6.3 |
| /blog/o-levels-and-a-levels-in-pakistan/ | 485 | 70,388 | 0.69% | 6.9 |
| /o-level-tuition-center-karachi/ | 393 | 26,629 | 1.48% | 6.4 |
| /caie-zone-4-timetable/ | 256 | 36,833 | 0.70% | 6.8 |
| /blog/the-best-free-english-learning-apps/ | 221 | 27,888 | 0.79% | 7.3 |
| /blog/best-laptop-for-students/ | 214 | 40,959 | 0.52% | 6.5 |
| /blog/best-schools-in-islamabad/ | 210 | 20,099 | 1.04% | 6.3 |
| /a-level-grade-strategy-tool/ | 201 | 3,072 | 6.54% | 7.7 |
| /blog/best-a-level-subjects-combinations/ | 188 | 23,221 | 0.81% | 8.3 |
| /blog/haque-academy-review/ | 166 | 8,721 | 1.90% | 7.0 |
| /schools-near-me-karachi/ | 157 | 13,248 | 1.19% | 6.5 |
| /a-level-tuition-center-karachi/ | 152 | 7,607 | 2.00% | 6.3 |
| /blog/heuser-college-review/ | 141 | 21,155 | 0.67% | 7.3 |
| /blog/top-universities-in-karachi/ | 127 | 19,834 | 0.64% | 5.3 |
| /classes-schedule/ | 127 | 3,282 | 3.87% | 2.5 |
| /blog/lyceum-school-review/ | 125 | 12,138 | 1.03% | 6.9 |
| /blog/cambridge-caie-vs-pearson-edexcel/ | 120 | 9,758 | 1.23% | 7.4 |
| /a-level-subject-combinations-tool/ | 116 | 1,129 | 10.27% | 9.7 |
| /ibcc-equivalence-calculator/ | 97 | 3,500 | 2.77% | 7.1 |
| /university-admission-criteria-tool/ | 95 | 655 | 14.50% | 7.7 |
| /blog/the-best-tutor-academy-in-karachi/ | 92 | 14,369 | 0.64% | 10.1 |
| /blog/best-cafes-in-karachi-for-students/ | 53 | 45,075 | 0.12% | 6.6 |
| /blog/top-universities-in-pakistan/ | 52 | 16,192 | 0.32% | 9.6 |
| /blog/how-to-use-mark-scheme/ | 38 | 11,214 | 0.34% | 6.5 |
| /registration-form/ | 38 | 4,734 | 0.80% | 4.9 |
| /blog/a-level-thresholds-guide/ | 20 | 8,498 | 0.24% | 12.4 |
| /fee-structure/ | 20 | 718 | 2.79% | 3.3 |
| /past-papers/ | 43 | 580 | 7.41% | 6.8 |
| /o-level-past-papers/ | 20 | 1,043 | 1.92% | 9.6 |
| /a-level-past-papers/ | 2 | 175 | 1.14% | 10.3 |
| /a-level-business-9609-definitions/ | 24 | 192 | 12.50% | 7.2 |

**Pattern:** traffic is dominated by informational school/university/fee articles (the Karachi schools article alone is ~25% of clicks). Commercial tuition pages get a small share. Tools convert attention well (high CTR).

### 4.3 Worst high-impression, low-CTR query/page pairs (1 Jul to 28 Sep)

| Query | Page | Impr | Clicks | CTR | Pos |
|---|---|---:|---:|---:|---:|
| beaconhouse school fees | Beaconhouse review | 12,499 (all pages) | 66 | 0.53% | 4.7 |
| beaconhouse school fees | Beaconhouse review | 4,769 | 24 | 0.50% | 3.5 |
| karachi grammar school | KGS review | 3,349 | 11 | 0.33% | 7.1 |
| best cafes for studying | Cafes | 3,074 | 0 | 0% | 8.3 |
| best places to study near me | Cafes | 2,837 | 0 | 0% | 8.0 |
| heuser college | Heuser review | 2,809 | 6 | 0.21% | 8.9 |
| city school fee structure / fees / monthly fees | City School review | ~3,200 to 3,350 each | 35 to 37 each | ~1.1% | 5.9 to 6.6 |
| physics and maths tutor | /physics-and-maths-tutor/ | 1,540 | 1 | 0.06% | 6.5 (navigational for PMT website, low value) |
| mark scheme | Mark scheme guide | 1,100 | 1 | 0.09% | 6.5 |
| o level is equal to which class in pakistan | O/A Levels guide | 1,087 | 3 | 0.28% | 8.9 |
| a level means which class | O/A Levels guide | 672 | 0 | 0% | 9.7 |
| a level is equal to which class in pakistan | O/A Levels guide | 635 | 1 | 0.16% | 10.9 |
| oct nov 2026 timetable zone 4 | Zone 4 timetable | 851 | 6 | 0.70% | 5.5 |
| tutor academy in karachi | Tutor academy post | 3,419 | 5 | 0.15% | 9.9 |
| coaching centre near me | Homepage | 616 | 3 | 0.49% | 6.0 |

### 4.4 Commercial tuition queries (1 Jul to 28 Sep)

| Query | Page | Impr | Clicks | Pos |
|---|---|---:|---:|---:|
| o level tutor in karachi | /o-level-tuition-center-karachi/ | 2,443 | 5 | 7.3 |
| o level tutor in karachi | / (homepage) | 1,044 | 11 | 10.4 |
| o level tuition near me | /o-level-tuition-center-karachi/ | 669 | 5 | 4.0 |
| tutor academy near me | tutor academy post | 567 | 1 | 8.4 |
| best tutor academy in karachi | tutor academy post | 1,422 | 5 | 8.2 |
| karachi tutor academy | tutor academy post | 1,059 | 4 | 10.1 |
| a level tutor | /a-level-tuition-center-karachi/ | 227 | 5 | 9.9 |
| o level coaching near me | /o-level-tuition-center-karachi/ | 185 | 10 | 4.0 |
| best a level coaching in karachi | homepage | 48 | 7 | 2.1 |

**Cannibalisation:** "o level tutor in karachi" (3,617 impressions total) is split between the homepage and the O Level tuition page. Brand queries ("sj academy") also spread across 8 pages, which is normal and low priority.

### 4.5 Threshold and past-paper demand
- O Level threshold queries are strong: dozens of "[subject/code] threshold 2026" variants, all on /o-level-grade-thresholds/.
- A Level: "a level threshold" 613 impr (pos 7.3, 0.3% CTR), "a levels threshold" 209. Subject-code queries ("9700 threshold 2026", "9609 threshold 2026 may june") appear with no dedicated page.
- Past-paper subject hubs: indexed, but only **6 to 120 impressions each** in 3 months. "9609 past papers" had 1 impression.

### 4.6 GA4 (property 482748209, 31 Aug to 28 Sep 2026)
- Devices: mobile 7,513 sessions (49.5% engagement), desktop 3,862 (52.2%), tablet 198.
- Countries (sessions): Pakistan 9,342; UAE 248; Indonesia 239; US 234; Saudi Arabia 227; Singapore 205; India 127; UK 123; Bangladesh 108.
- Avg session duration 138 s, engagement rate 50.6%.
- Key event `generate_lead`: 87. **84 attributed to /contact-us/**, 1 each to /contact, /contact_us, /contactus. Homepage: 0 key events from 6,212 events.
- Other events: form_start 855, submit_lead_form 263, whatsapp_click 104, file_download 525, click 357, form_submit 5, contact_link_click 3. Revenue $0.
- Earlier (13 Aug to 9 Sep, from 11 Sep handoff): 18,217 sessions; Organic 60.7%; AI Assistant 307 sessions (chatgpt.com 296), 4 key events.
- **Measurement caveat:** lead events are fragmented (generate_lead vs submit_lead_form vs form_submit). Events are not qualified leads or enrolments.

### 4.7 URL inspection (30 Sep)
- /o-level-past-papers/accounting-7707/, /a-level-past-papers/business-9609/, /o-level-past-papers/mathematics-d-4024/, /blog/the-best-tutor-academy-in-karachi/, /blog/a-level-thresholds-guide/: all "Submitted and indexed", Google canonical = user canonical.
- Breadcrumb rich results detected but items show as **"Unnamed item"** (Yoast breadcrumb naming issue).
- /chemistry-5070/ is "unknown to Google" but 301-redirects to /o-level-past-papers/chemistry-5070/ (fine).

### 4.8 Older data still relevant (from 10/11 Sep audit)
- GSC 8 Jun to 7 Sep: 24.6K clicks, 1.43M impressions, 1.7% CTR. Generative AI features report: 429K impressions.
- Indexing: 189 indexed / 313 not indexed across all known URLs; submitted set ~92.6% indexed.
- Core Web Vitals: **0 good URLs** on mobile or desktop. Mobile: 67 poor, 45 need improvement; CLS > 0.1 on 112 URLs; LCP > 4 s on 67.
- Backlinks sample: 151 external links, Reddit 113 of them.
- Schema: custom `TutoringService` type on all pages is not a valid Schema.org type. FAQ rich results were retired by Google from 7 May 2026.

---

## 5. Key findings (consolidated)

### Technical
1. **Nested `<head>`/`<body>` and duplicate `<title>` on 52 live pages.** Root cause: widget files were full HTML documents pasted into Elementor. Fixed locally for 25 hubs, 2 directories and fee structure on 30 Sep. Not yet published. Other affected pages (tuition pages, tools, quizzes) have no local source files.
2. **Conflicting embedded canonicals still live (rechecked 30 Sep):**
   - /a-level-past-papers/ contains `rel="canonical" href="https://sjacademy.com/a-level-past-papers-faq"`
   - /o-level-past-papers/ contains `rel="canonical" href="https://sjacademy.com/o-level-past-papers-faq"`
   - /a-level-subject-combinations-tool/ contains `rel="canonical" href="https://www.sjacademy.pk/career-finder/"` (career-finder 301s back to the tool)
   These are in Elementor widgets on the live pages, not in local files. Remove them in Elementor.
3. **Seven broken content links** (10 Sep list, not rechecked since): /contact (from /contact-us/), three /a-level-*-practicals/ (from /lab-practicals/), /career-finder/ (from subject-combinations tool), /a-level-practical-e-book (from physics practical blog), sjacademy.pk/register (from Haque Academy review). GA4 also shows people landing on /contact, /contact_us, /contactus.
4. **Missing meta descriptions** on priority pages: /blog/top-schools-in-lahore/ (161.8K impressions), /registration-form/, /meet-the-teachers/, plus ~34 others from the 10 Sep inventory.
5. **Core Web Vitals all failing.** Likely factors: Slider Revolution, hero images, fonts (Poppins loaded inside many widgets), popups, Elementor output, third-party scripts.
6. **Duplicate legacy past-paper URLs** still live with self-canonicals: /a-level-business-past-papers/, /a-level-mathematics-past-papers/, /o-level-math-past-papers/. They compete with the hubs and need 301 redirects.
7. Many internal links use `https://sjacademy.pk/` (non-www), which causes a redirect hop. Fixed in the local files that were edited.

### Content and CTR
1. The biggest CTR losses are **title/intent mismatches** on high-impression articles (Beaconhouse, City School = fees intent; O/A Levels guide = "which class" intent; Zone 4 = session/year intent).
2. **Tutor academy post** (highest commercial intent with a local file) ranked SJ Academy "#1" in its own list, with unverifiable superlatives and negative claims about named competitors (Anees Hussain, Students' Inn, Valeem/Maqsad). Rewritten locally on 30 Sep.
3. **Past-paper hubs are thin:** one FAQ sentence each, paper list built by JavaScript (0 static PDF links in HTML), all 25 hubs are the same template.
4. **Content gap: A Level grade thresholds.** The O Level page earns 50K impressions; the A Level post sits on page 2.
5. The cafes post (45K impressions, 0.12% CTR) has global "near me" intent with no tuition value. Under the affiliate track it is a low-CTR audience page. Improve it only if it can carry affiliate value; its searchers are mostly outside Karachi.
6. Audience/affiliate pages with weak CTR that are worth title work for the affiliate track: best laptop for students (40,959 impr, 0.52%), English learning apps (27,888, 0.79%), top universities in Pakistan (16,192, 0.32%).

### Conversion and trust (from 11 Sep, still open)
- Conversions come almost entirely from /contact-us/. The homepage has no attributed key events.
- The mobile registration popup asks for too much too early. Recommend a WhatsApp/demo-first path, collecting level/subject/mode first.
- Inconsistent facts across the site: fees, batch dates, A* counts, review counts (e.g. "220+ 5-star reviews"). A single source of truth is needed.
- **IBCC calculator (live)** has accuracy risks (A* auto-converted to 90, weak group rules). Needs fixing before promotion. Note: the new O/A Levels answer block links to it.
- **Drafted replacement IBCC calculator (blocked, 11 Sep):**
  - A* hard-coded to 100, but IBCC's July 2026 notification sets A* per subject and year (e.g. Physics = 94).
  - Letter grades inflated by 5 marks. Blank/U grades were silently counted as zero while still producing a result.
  - Ignored the February 2026 IBCC notice for science students. Conflated local SSC (/800), overseas SSC (/500) and overseas HSSC scales.
  - Switching routes wiped the grades already entered.
- **Accessibility:** white text on brand orange `#FE6100` fails WCAG contrast (3.03:1). Use dark text on orange, or a darker orange, for CTAs.
- The A Level subject-combinations article has accuracy issues (pre-medical Physics requirement, FAST computing eligibility, mixing IBCC and university rules).
- Cambridge O Level Business Studies **7115 becomes Business 7081** from June 2027. `/business7081/` is the new-syllabus page. Keep 7115 papers labelled as historical.

---

## 6. Changes made on 30 Sep 2026 (local files only, applied with backups)

Backups of all 29 originals: `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/backup_originals/`. Full diff-level summary: `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/CHANGE_SUMMARY.md`. Script: `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/scripts/fix_hubs.py`.

1. **25 subject hubs + 2 directory pages** (`01_Website_Pages/Past_Papers/A_Level/`, `O_Level/`):
   - Removed doctype/html/head/meta/title/body wrappers (fixes nested head and duplicate title once published).
   - H1 now reads, for example, "A Level Business (9609) Past Papers & Mark Schemes" (was "Business (9609) Past Papers"). A Level directory H1 gained "& Mark Schemes".
   - FAQ block is now an H2 section with 4 extra H3 Q&As (file naming, variants, using mark schemes, help CTA).
   - New internal links: /blog/how-to-use-mark-scheme/, thresholds page (O Level page or A Level guide), and the subject tuition page. Subjects without a tuition page use neutral wording linking to the O or A Level tuition centre.
   - Non-www links changed to www.
2. **`01_Website_Pages/Pages/fee_structure.html`:** wrappers removed.
3. **`01_Website_Pages/Blog_Posts/top_10_tutor_academies_karachi.html`** (live post ID 6716, /blog/the-best-tutor-academy-in-karachi/):
   - Added a disclosure box saying SJ Academy publishes the guide. Removed "Ranked #1" and unverifiable superlatives.
   - Neutral competitor cons. Added a comparison table and a 4-question FAQ.
   - Keyword-anchored links to the O and A Level tuition centre pages and /fee-structure/.
4. **New files in `01_Website_Pages/New_Pages_Drafts/`:**
   - `o_a_level_class_equivalence_answer_block.html`: answer box for the top of /blog/o-levels-and-a-levels-in-pakistan/. Ready.
   - `a_level_grade_thresholds.html`: draft for a new /a-level-grade-thresholds/ page. **Not ready: `[FILL]` cells must be copied from official Cambridge June 2026 threshold tables.** Then 301 /blog/a-level-thresholds-guide/ to it.
5. **`03_Plans_and_Content/Metadata/Yoast_Metadata_Changes_2026_09_30.csv`:** new titles/metas for 10 live pages (Beaconhouse, O/A Levels guide, City School, Zone 4 timetable, O Level tuition centre, Lahore schools, A Level thresholds guide, registration form, meet the teachers, mark scheme guide), with evidence and pre-publish conditions.

Not changed: IBCC calculator (accuracy issues first), homepage-preview.html (a draft, not the live homepage), cafes post.

---

## 7. Pending: needs manual publishing in WordPress

1. Paste each updated hub file into its Elementor HTML widget (replace existing code). Same for /fee-structure/ and the tutor academy post.
2. Apply Yoast titles/metas from the CSV, respecting each row's condition (e.g. only say "2026 fees" if the fee table shows 2026 figures).
3. Insert the answer block at the top of the O/A Levels guide.
4. Add one homepage link to /o-level-tuition-center-karachi/ with the anchor "O Level tutors in Karachi".
5. Remove the three embedded conflicting canonicals (section 5, technical item 2).
6. 301-redirect the legacy past-paper URLs to the matching hubs.
7. Fix Yoast breadcrumb names ("Unnamed item").
8. After publishing: re-crawl to confirm a single `<title>` per page, then request indexing in GSC. Compare CTR after 3 to 4 weeks against section 4.

---

## 8. Decisions made by the user

- **Past-paper setup:** keep the current structure for now. No per-session pages, no static-HTML paper list rebuild at this stage. (Analysis in section 9 is kept for future reference.)
- **Backend publishing:** interested in pushing pages from a backend instead of copy-paste. A proposal was made (section 10) but **not built yet**.
- Changes are staged for review first, then applied locally with backups on approval.
- Two-track measurement (22 Sep): `generate_lead` for tuition, and a separate `affiliate_click` event for monetised content (not yet implemented).

## 9. Past-paper architecture analysis (reference, deferred)

- The hubs are connected: the site menu links every hub from every page (30 past-paper links per page). Discovery is not the problem.
- Ranking limits:
  - No static paper links in the HTML (the JavaScript builds the list).
  - Near-duplicate template pages.
  - Legacy duplicate URLs.
  - The breadcrumb is plain text, not a link.
  - Few contextual links from related content.
  - Head terms ("9609 past papers") are usually won by long-established past-paper sites.
- Realistic wins: session-specific long-tail queries, and unique content (solved papers, definitions, teacher commentary). The /a-level-business-9609-solved-past-papers-2025/ page logged 657 events in 4 weeks; /a-level-business-9609-definitions/ has a 12.5% CTR.
- Options if revisited:
  - **A)** Update the current hub files: static HTML paper lists (generated by script from each file's `subjectsData`), a clickable breadcrumb, unique paper-structure tables and teacher tips.
  - **B)** Add per-session pages (e.g. /a-level-past-papers/business-9609/2025-may-june/). Pilot with Business 9609 and Maths 9709 only, and measure for 6 to 8 weeks.
  - Either way: 301 the legacy URLs, fix Yoast breadcrumbs, and link the hubs from solved papers, notes, thresholds and tuition pages.

## 10. WordPress technical facts and backend-publishing proposal

- REST API reachable at `https://www.sjacademy.pk/wp-json/` (checked 30 Sep). Authentication: **application-passwords** enabled.
- Namespaces present: `wp/v2`, `yoast/v1`, `elementor/v1`, `elementor-pro/v1`, `elementor-one/v1`, `elementor-ai/v1`.
- Yoast title/meta fields are **not exposed** in REST post meta by default (they need `register_post_meta` with `show_in_rest`).
- Elementor stores layouts in `_elementor_data` post meta (JSON), not `post_content`. Editing it via the API is fragile.
- Plugins seen: Educrat theme, Elementor + Pro Elements, Yoast, WPForms, WPCode, Site Kit, PixelYourSite, Joinchat, Slider Revolution, WP-Optimize. Past-paper PDFs are served from `sjacademy.pk/file/Past-papers-storage/...` (Backblaze-backed).
- **Proposal (not built):**
  1. A WPCode PHP snippet registers a private "SJ Blocks" post type and a `[sj_block slug="..."]` shortcode that outputs the stored HTML raw. It also exposes Yoast title/meta to REST.
  2. Each Elementor widget holds only its shortcode (a one-time swap on about 30 pages).
  3. A local `push.py --dry-run` / `push.py` creates or updates blocks and Yoast fields from local files, saving the live version before overwriting.
  4. The application password is stored in the macOS Keychain, not in the folder.
  - Blog posts not built with Elementor can be updated directly via `wp/v2/posts`.

---

## 11. Open questions for the owner

1. Is "220+ 5-star Google reviews" still accurate? (Used in hubs and the tutor post.)
2. Which fee, batch-date, A* count and review figures are the current source of truth?
3. Which subjects are actually taught (needed for tuition links: A Level Law, Psychology, Sociology, Urdu, English, Accounting; O Level CS, English, Urdu)?
4. Exact address details and the GBP pin (Teachwink discrepancy).
5. Who reviews educational accuracy (IBCC, thresholds, subject combinations)?

## 12. Candidate backlog for the next big SEO plan (ranked by evidence)

| Priority | Item | Why (evidence) |
|---|---|---|
| P0 | Publish the 30 Sep fixes + Yoast CSV | Largest CTR gaps: Beaconhouse 135.8K impr at 1.08%, O/A guide 70.4K at 0.69%, City School 55.7K at 0.92%, Zone 4 36.8K at 0.70% |
| P0 | Remove the 3 conflicting canonicals, 301 legacy past-paper URLs, fix 7 broken links | Live technical errors, confirmed 30 Sep (canonicals) |
| P0 | Fix IBCC calculator and subject-combination accuracy | Trust risk; the calculator gets 3.5K impressions and is linked from new content |
| P0 | Reconcile fees, dates, review counts, A* counts | Conflicting facts across pages hurt trust and AI citations |
| P1 | Core Web Vitals programme per template | 0 good URLs; 64% of traffic is mobile |
| P1 | Lead measurement cleanup (one lead event, test journeys, admissions matching) | 87 generate_lead, almost all from /contact-us/; fragmented events |
| P1 | Mobile enquiry journey (WhatsApp/demo first) | Homepage has 0 key events from 6,212 events |
| P1 | Resolve "o level tutor in karachi" cannibalisation and strengthen tuition pages | 3,617 impressions at 0.4% CTR, split across 2 pages |
| P1 | A Level grade thresholds page (fill with official data) | O Level equivalent gets 50K impressions |
| P1 | Business 9609 pilot (tuition track): topic-level paper index, answer frameworks, teacher evidence, clear tuition path | Chosen pilot on 22 Sep; the 9609 solved-papers and definitions pages already show strong engagement |
| P1 | Affiliate track setup: `affiliate_click` event, affiliate links on laptop/apps/resources posts, CTR work on those titles | Confirmed business goal 22 Sep; laptop post 40,959 impr at 0.52% CTR |
| P2 | Contextual links from high-traffic school/university articles to tuition and online offer | Informational traffic dominates; few tuition paths |
| P2 | Replace invalid `TutoringService` schema with `EducationalOrganization` / `Service` / `Course` | Invalid type on every page |
| P2 | Past-paper upgrade (option A or B, section 9) | Hubs get 6 to 120 impressions each |
| P2 | Local SEO: address/NAP consistency, GBP, honest reviews | Teachwink address issue, local intent queries |
| P2 | AI visibility: question panel, teacher-reviewed reference content, source citations | 429K AI-feature impressions; ChatGPT referrals convert at ~1% |
| P1 | Instagram: useful-carousel backbone, named teacher reels, parent-focused content, online-class messaging for the ~73% outside Karachi, daily UTM link stickers, comment-to-get with lead capture, link-in-bio page + GA4 tracking, blog/Instagram pipeline; ads: drop the lead-messaging objective, UTMs, label ad conversations, track cost per enrolment | Instagram analysis 30 Sep (section 2 of that report) |
| P3 | Backend publishing system (section 10) | Removes copy-paste for ~30+ widget pages |
| P3 | Add Bing Webmaster Tools | Bing organic 474 sessions/month; not connected |

## 13. File map (reorganised 30 Sep 2026)

Full guide: `00_START_HERE/README_Folder_Guide.md`. Old to new paths: `00_START_HERE/move_log_2026-09-30.csv`.

- `00_START_HERE/`: this file, the folder guide, the move log
- `01_Website_Pages/`: HTML that goes on the site
  - `Past_Papers/A_Level/`, `Past_Papers/O_Level/` (hubs + directories), `Past_Papers/Template/`
  - `Pages/` (fee structure, homepage draft, tuition/landing pages, resources vault, `Policies/`)
  - `Blog_Posts/` (tutor academies post, O Level guide)
  - `Tools/` (IBCC calculator, career finder, scholarship tools, `IBCC_Calculator_Widget/` with official IBCC source PDFs)
  - `New_Pages_Drafts/` (answer block, A Level thresholds draft)
- `02_Reports_and_Audits/`: dated folders: 30 Sep fixes (CHANGE_SUMMARY, backups, scripts), 22 Sep progress report, 11 Sep handoff, 11 Sep growth diagnosis, 11 Sep IBCC audit, 10 Sep full site audit (report, `page_inventory.csv`, `broken_links.csv`, `evidence/`), older audits
- **Live content calendar (single source of truth for blog + Instagram):** Google Sheet "SJ Academy Content Calendar 2026-27", https://docs.google.com/spreadsheets/d/14wakCHfKvBj02zeMzSMQKMwFKaIcDiBwEOoj4Ix2ly0/edit (owner sjacademypk@gmail.com). The CSVs in 03_Plans_and_Content are the original build inputs only; `05_Scripts/build_content_calendar.py` rebuilt the .xlsx that was imported.
- `03_Plans_and_Content/`: `Blog_Content_Plan_2026-27/` (strategy + dated calendar CSV + `Instagram_to_Blog_Plan.csv`: 18 top Instagram posts mapped to blog posts, swaps proposed but not yet applied to the calendars), `Instagram_Plan_2026-27/` (growth playbook + 91-post calendar 5 Oct 2026 to 3 Jan 2027), `Metadata/` (Yoast sheet), `Blog_Drafts/`, `Old_Plans_Outdated/`
- `04_Data/`: Search Console/GA4 CSV exports, `Instagram/` post export (30 Sep 2026), scholarship data, resources database, SEO tracker
- `05_Scripts/`: `Analysis/`, `Archive_One_Off_Scripts/` (archived; contain pre-reorganisation absolute paths)
- `99_Archive/`: old hub backups (Aug 2026)

Note: the 11 Sep and 22 Sep documents cite pre-reorganisation paths. Use the move log to translate them.

## 14. Ready-to-paste prompt for a new conversation

```text
We are continuing the SJ Academy SEO project (sjacademy.pk, O/A Level tuition academy in DHA Phase 7 Karachi plus live online across Pakistan). The attached file SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md is the complete, latest context. Read it fully first. Treat all numbers as dated snapshots. Nothing in section 6 is live on the website yet; section 7 lists what still needs publishing.

Goal for this conversation: build the next big SEO plan for SJ Academy. Use the ranked backlog in section 12 as the starting point, respect the working rules in section 2 and the decisions in section 8, and ask me the open questions in section 11 where they block decisions. Give me a prioritised 90-day plan with owners, acceptance tests and how we will measure results against the section 4 baselines.
```
