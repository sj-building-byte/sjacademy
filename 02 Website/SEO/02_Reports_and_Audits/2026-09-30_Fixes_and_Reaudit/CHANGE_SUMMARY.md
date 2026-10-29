# SJ Academy SEO Fixes: Change Summary (30 Sep 2026)

**Status:** APPLIED to local files on 30 Sep 2026 (originals in `backup_originals/`). Not yet published to the live site. Note: the folder was reorganised afterwards, so the hubs now live in `01_Website_Pages/Past_Papers/`, the fee and tutor files in `01_Website_Pages/Pages/` and `Blog_Posts/`, new pages in `01_Website_Pages/New_Pages_Drafts/`, and the Yoast sheet in `03_Plans_and_Content/Metadata/`. Paths inside `staged/` and `backup_originals/` still mirror the old layout.

**Data used:** GSC for Jul 1 to Sep 28 2026 (page, query and page+query dimensions; low-CTR, striking-distance and cannibalization audits), GSC URL Inspection on 6 URLs, a GSC health check (last 7 days vs the previous 7), GA4 property 482748209 for Aug 31 to Sep 28 2026, and live crawls of 29 URLs.

## Key findings

| # | Finding | Evidence |
|---|---|---|
| 1 | High-impression pages have weak CTR because titles don't match the query | Beaconhouse: 135.8K impressions, 1.08% CTR. "beaconhouse school fees" sits at position 4.7 with 0.5% CTR. O/A Levels guide: 70.4K impressions, 0.69% CTR. City School: 55.7K impressions, 0.92% CTR. Zone 4 timetable: 36.8K impressions, 0.70% CTR |
| 2 | 52 live pages have nested `<head>` and duplicate `<title>` tags | Root cause: widget files in this folder are full HTML documents pasted into Elementor |
| 3 | Past-paper hubs are indexed but invisible | 25 subject hubs get 6 to 120 impressions each. Their only text is one FAQ sentence, and the paper list is rendered by JavaScript |
| 4 | The homepage and the O Level tuition page compete for "o level tutor in karachi" | 3,617 impressions. The tuition page ranks at 7.3, the homepage at 10.4, and CTR is 0.4% |
| 5 | The tutor-academy post ranks itself #1 and makes claims that can't be verified | 14.4K impressions, 0.64% CTR, position 10.1 |
| 6 | Content gap: A Level grade thresholds | The O Level thresholds page gets 50.3K impressions. The A Level blog post sits at position 12.4 with 0.24% CTR, and subject-code threshold queries have no matching page |
| 7 | Conversions are concentrated in one place | GA4: 87 `generate_lead` events. 84 are attributed to /contact-us/ and 0 to the homepage (6,212 events). 64% of sessions are mobile |
| 8 | Health | Sitemap has no errors, no anomalies, clicks are flat week over week (+0.9%) |

## Changes to existing files (staged)

### A. 25 past-paper hubs + 2 directories (`A_Level_Hubs/`, `O_Level_Hubs/`)
- Removed the doctype, `<html>`, `<head>`, `<meta>`, `<title>` and `<body>` wrappers. This fixes the nested head and duplicate title on these live pages.
- H1 changed, for example from "Business (9609) Past Papers" to "**A Level** Business (9609) Past Papers **& Mark Schemes**". The A Level directory H1 now also includes "& Mark Schemes".
- The one-sentence FAQ became an H2 section. It keeps the syllabus answer and adds H3s on reading file names, choosing variants and using mark schemes, plus a help CTA.
- New internal links: the mark-scheme guide, the grade thresholds page, and the matching subject tuition page. Subjects without a tuition page link to the O or A Level tuition centre with neutral wording, so the copy never claims you teach a subject.
- Internal links changed from `https://sjacademy.pk/` to `https://www.sjacademy.pk/`, which skips a redirect.

### B. `HTML_Tools_and_Drafts/fee_structure.html`
- Removed the document wrappers. /fee-structure/ is on the nested-head list. The description in the file was a duplicate, because Yoast already outputs one.

### C. `HTML_Tools_and_Drafts/top_10_tutor_academies_karachi.html` (live: /blog/the-best-tutor-academy-in-karachi/)
- Added a disclosure box saying SJ Academy publishes the guide.
- H3 changed from "SJ Academy (Center of Excellence) 🏆 Ranked #1" to "SJ Academy, DHA Phase 7 (Physical and Live Online)".
- Removed unverifiable superlatives: "widely recognized as the premier", "highest-rated academy in the region", "perfect formula" and "guarantees results".
- Competitor cons rewritten as neutral "check before enrolling" points. Removed "class sizes extremely large" and the unverified "Rs. 30k+".
- New H2 "Karachi Tuition Options Compared" with a responsive table.
- New H2 FAQ with 4 Q&As targeting "tutor academy in karachi" (3,419 impressions), "tutor academy near me" (567) and fees.
- New internal links to /o-level-tuition-center-karachi/ and /a-level-tuition-center-karachi/ with keyword anchors, which supports finding 4. Also a link to /fee-structure/. All links now use www.

## New files (staged in `staged/New_Pages/`)

| File | Purpose | Ready? |
|---|---|---|
| `o_a_level_class_equivalence_answer_block.html` | Direct answer box and table for the top of /blog/o-levels-and-a-levels-in-pakistan/ (O Level = Matric, A Level = Intermediate, AS/A2 = Class 11/12) | Yes |
| `a_level_grade_thresholds.html` | New page /a-level-grade-thresholds/: explainer, official Cambridge source link, study use and CTA | **No.** The threshold table has `[FILL]` cells that must be copied from the official June 2026 Cambridge PDFs. I did not estimate any figures |
| `Yoast_Metadata_Changes.csv` | New titles and meta descriptions for 10 live pages that aren't in this folder, each with before/after, evidence and conditions | Yes, apart from the per-row conditions (for example, the fee year must match the page) |

## Not changed, and why
- **IBCC calculator files:** the 11 Sep audit (`IBCC_Audit_2026_09_11/AUDIT.md`) found the engine materially inaccurate. The live page still gets 3,500 impressions. The engine needs fixing first. Note that the new answer block links to the live calculator.
- **homepage-preview.html:** this is a draft, not the live homepage. For finding 4, add one homepage link to /o-level-tuition-center-karachi/ in Elementor.
- **Cafes post (45K impressions, 0.12% CTR):** the queries are global "near me" searches with no tuition value, so I recommend no action.
- **Core Web Vitals (0 good URLs):** needs theme and plugin work, which is outside these files. Loading Poppins inside each widget adds requests. If the theme already loads Poppins, remove the `<link>` from the widgets.

## To verify before or after applying
1. Resolved: Cambridge replaces O Level Business Studies 7115 with Business 7081 from June 2027, so `/business7081/` and the 7115 hub are both correct.
2. The "220+ 5-Star Reviews" claim should match the live Google Business Profile count.
3. After pasting the hubs into Elementor, re-crawl one hub and /fee-structure/ to confirm only one `<title>` remains.
