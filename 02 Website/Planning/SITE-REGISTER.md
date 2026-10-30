# SJ Academy site register

**Version:** 1.0, 2 October 2026
**Source:** the live sitemap at sjacademy.pk on 2 October 2026 (pages and posts).
**Spreadsheet copy:** `37-site-register.csv` holds the same rows for sorting and filtering.
**Replaces:** the four-row page register in the brand guidelines.

**Read this first**

- Pages are classified **by their address only**. Nobody has opened each page to confirm what it contains. Treat the family and the notes as a first pass to correct.
- The tool that read the page sitemap reported 117 addresses but listed 97. This register holds the 97 it listed. Compare against Yoast's sitemap once to confirm nothing is missing.
- Build priority is by page type, not by traffic. It should be re-ordered using Search Console data.

---

## 1. Summary

| | Count |
|---|---|
| Pages | 97 |
| Blog posts | 74 |
| Rebuilt in the new design | 10 live (see section 9) |
| On the shared stylesheet | 7 live: A Level, O Level, A Level Maths, A Level Business, and Business, Economics and Maths past papers. Homepage, fees and timetable still carry their own CSS |

| Family | Pages |
|---|---|
| Enrol | 24 |
| Resource | 43 |
| Tool | 9 |
| Event | 9 |
| Info | 8 |
| Proof | 1 |
| Utility (forms, confirmations) | 4 |

---

## 2. Rules for every rebuild

1. **The address never changes.** If two pages must merge, the retired one gets a 301 redirect to the kept one, set in Yoast or the redirect plugin, on the same day.
2. Before replacing a page, record its current title, H1, meta description and the queries it ranks for. The new page keeps those keywords.
3. One page at a time. Cloudways backup first. Draft, check on a phone, then replace in place.
4. Update this register when a page ships: status, date, CSS version, lead accent, what is circled.
5. Pages marked "Leave" are functional and are not redesigned.

---

## 3. Build order

| Wave | What | Pages | Approach |
|---|---|---|---|
| Done | Homepage, fees, timetable, A Level Business | 4 | Migrate to the shared stylesheet later, one at a time |
| 1 | Level pages | 3 | Built individually. They feed every subject page |
| 1 | Subject tuition pages | 17 | One Enrol template, based on the A Level Business page, then filled per subject |
| 1 | Lab practicals | 4 | Resolve the overlap first (section 4), then one or two pages |
| 2 | Past papers hubs and subject pages | 31 | One Resource template applied to every subject. The largest group on the site |
| 2 | Tools and quizzes | 8 | Tool family. Each keeps its own logic; only the shell changes |
| 2 | Reference resources | 12 | Resource family |
| 2 | Teachers | 1 | Proof family |
| 2 | Blog | 1 index, 74 posts | See section 5 |
| 3 | Contact and policies | 6 | Info family. Plain |
| 3 | Campaigns and programmes | 7 | Confirm each is still active before spending time on it |
| Leave | Forms and confirmations | 4 | Not redesigned |

---

## 4. Things to resolve before building

These come from the addresses alone and each needs a look at the live page.

| Issue | Pages | Decision needed |
|---|---|---|
| Two A Level Maths pages | `/a-level-maths/`, `/a-level-maths-tuition/` | Keep one, redirect the other, or give them different jobs |
| Two Economics pages | `/economics/`, `/a-level-economics-tuition/` | Same |
| Four practicals pages | `/lab-practicals/`, `/a-level-practicals/`, `/a-level-practical-may-june/`, `/a-level-practical-mock-exams-karachi/` | Which is the main page, which are dated events |
| Three quadratics ebook pages | `/download-quadratics-ebook/`, `/a-level-math-quadratics-ebook/`, `/quadratics-ebook-download/` | Landing page, download page, and likely one duplicate |
| Old and new past paper addresses | `/o-level-math-past-papers/`, `/a-level-business-past-papers/`, `/a-level-mathematics-past-papers/` against the newer `/[level]-past-papers/[subject]/` pages | Redirect the old ones if they duplicate |
| Unclear pages | `/business7081/`, `/physics-and-maths-tutor/` | Confirm what each is for |
| Subject pages with irregular addresses | `/a-level-chemistry/`, `/o-level-biology-sj-academy/`, `/o-level-chemistry-tuitions/` | Keep the addresses. Do not tidy them without redirects |
| Subjects with no tuition page | To be listed against the subjects actually taught | The homepage class finder lists every subject. Any subject without a page is a gap |
| Campaign pages | `/ai-workshop/`, `/paperchase/`, `/justice-for-caie-students/`, internships, referral | Active, archive or retire |
| Confirmation pages in the sitemap | `/thank-you/`, `/payment-confirmation/` | These normally should not be indexed |

---

## 5. The blog

74 posts and the blog index. Posts are WordPress posts, shown through the theme's single-post template, not through an HTML widget. That makes the blog different from every other page:

- **Open decision:** how the new design reaches posts. Either a blog template that styles all posts at once, or leaving posts on the theme's design and applying the new voice only. Rebuilding 74 posts by hand as widgets is not sensible.
- The existing Additional CSS already styles links inside posts (blue, bold, underlined). Any blog template must replace that rule rather than fight it.

| Post type | Count | Note |
|---|---|---|
| Listicle or comparison | 26 | |
| Exam technique or subject guide | 16 | The posts closest to the tuition business |
| System or decision guide | 13 | Need dates and official sources |
| Named school review | 10 | Check each against the blog voice rule: facts and labelled opinion, no ridicule |
| Opinion or news | 5 | Two address Cambridge directly. Review tone, keep the facts |
| News or dated update | 4 | Check accuracy or mark as archived |

No existing post is an entertainment post in the new sense. The one-in-five ratio starts from the next post published.

---

## 6. Pages

### Enrol

| URL | Type | Status | Notes |
|---|---|---|---|
| `/` | Homepage | Live, v1.4 (own CSS `#sjh`, pre-3.0). Checked live 8 Oct 2026 |  |
| `/a-level-practicals/` | Lab practicals | Not rebuilt | Four practical pages exist (lab-practicals, a-level-practicals, a-level-practical-may-june, a-level-practical-mock-exams-karachi). Check for overlap |
| `/lab-practicals/` | Lab practicals | Not rebuilt | Four practical pages exist (lab-practicals, a-level-practicals, a-level-practical-may-june, a-level-practical-mock-exams-karachi). Check for overlap |
| `/a-level-tuition-center-karachi/` | Level page | Live, v1.1 on shared stylesheet 3.1.1. Checked live 8 Oct 2026 | Shared stylesheet 3.1.1. Wrapper `sj-p-a-level`. Lead accent: polaroid with tape. Circled: 5.0. Target keyword: A Level tuition center in Karachi. Title: A Level Tuition Center in Karachi & Online \| SJ Academy |
| `/o-a-level-classes/` | Level page | Not rebuilt |  |
| `/o-level-tuition-center-karachi/` | Level page | Live on shared stylesheet 3.1.1 (wrapper `sj-p-o-level`). Checked live 8 Oct 2026 |  |
| `/a-level-biology-tuition/` | Subject tuition | Not rebuilt |  |
| `/a-level-business-tuition/` | Subject tuition | Live, v2.1 on shared stylesheet 3.1.1, 8 Oct 2026. Copy rewritten to the landing page copy guidelines | Wrapper `sj-p-a-level-business`. Lead accent: sample answer papers. Circled: 6 of the 12. Keyword pass from Semrush: Business Studies, syllabus, past papers anchors. SEO title to set: A Level Business tuition in Karachi & online \| SJ Academy. WhatsApp refs: ALB-AS, ALB-A2, ALB-Q |
| `/a-level-chemistry/` | Subject tuition | Not rebuilt | Slug does not follow the "[level]-[subject]-tuition" pattern. Keep the address; do not rename without a redirect |
| `/a-level-computer-science-tuition/` | Subject tuition | Not rebuilt |  |
| `/a-level-economics-tuition/` | Subject tuition | Not rebuilt | Possible overlap between /economics/ and /a-level-economics-tuition/. Check |
| `/a-level-maths-tuition/` | Subject tuition | Live, v1.0 on shared stylesheet 3.1.1. Checked live 8 Oct 2026 | First page on the shared stylesheet (3.1.1). Wrapper `sj-p-a-level-maths`. Lead accent: pen-marked worked solution with round stamp. Circled: 3 s.f. Target keyword: A Level Maths tuition in Karachi. Title: A Level Maths Tuition in Karachi & Online (9709) \| SJ Academy. Overlap with `/a-level-maths/` still undecided |
| `/a-level-maths/` | Subject tuition | Not rebuilt | Two A Level Maths pages. Check for overlap before rebuilding |
| `/a-level-physics-tuition/` | Subject tuition | Not rebuilt |  |
| `/business7081/` | Subject tuition | Not rebuilt | Slug suggests a different Business syllabus code. Confirm what this page is |
| `/economics/` | Subject tuition | Not rebuilt | Possible overlap between /economics/ and /a-level-economics-tuition/. Check |
| `/o-level-accounting-tuition/` | Subject tuition | Not rebuilt |  |
| `/o-level-biology-sj-academy/` | Subject tuition | Not rebuilt | Slug does not follow the "[level]-[subject]-tuition" pattern. Keep the address; do not rename without a redirect |
| `/o-level-chemistry-tuitions/` | Subject tuition | Not rebuilt | Slug does not follow the "[level]-[subject]-tuition" pattern. Keep the address; do not rename without a redirect |
| `/o-level-islamiat-tuition/` | Subject tuition | Not rebuilt |  |
| `/o-level-math-tuition/` | Subject tuition | Not rebuilt |  |
| `/o-level-pakistan-studies-tuition/` | Subject tuition | Not rebuilt |  |
| `/o-level-physics-tuition/` | Subject tuition | Not rebuilt |  |
| `/physics-and-maths-tutor/` | Subject tuition | Not rebuilt | Confirm purpose: tuition page or a resource comparison |

### Resource

| URL | Type | Status | Notes |
|---|---|---|---|
| `/a-level-math-quadratics-ebook/` | Ebook landing / download | Not rebuilt | Three quadratics ebook pages. Likely a landing page, a download page and a duplicate. Check |
| `/download-quadratics-ebook/` | Ebook landing / download | Not rebuilt | Three quadratics ebook pages. Likely a landing page, a download page and a duplicate. Check |
| `/quadratics-ebook-download/` | Ebook landing / download | Not rebuilt | Three quadratics ebook pages. Likely a landing page, a download page and a duplicate. Check |
| `/a-level-past-papers/` | Past papers hub | Not rebuilt |  |
| `/o-level-past-papers/` | Past papers hub | Not rebuilt |  |
| `/past-papers/` | Past papers hub | Not rebuilt |  |
| `/a-level-business-9609-definitions/` | Resource or reference | Not rebuilt |  |
| `/a-level-business-9609-solved-past-papers-2025/` | Resource or reference | Not rebuilt |  |
| `/a-level-scholarship-requirements/` | Resource or reference | Not rebuilt |  |
| `/caie-2027-pakistan-timeline/` | Resource or reference | Not rebuilt |  |
| `/caie-private-candidate-registration/` | Resource or reference | Not rebuilt |  |
| `/caie-zone-4-timetable/` | Resource or reference | Not rebuilt |  |
| `/ebooks/` | Resource or reference | Not rebuilt |  |
| `/free-caie-resources/` | Resource or reference | Not rebuilt |  |
| `/o-level-grade-thresholds/` | Resource or reference | Not rebuilt |  |
| `/a-level-business-past-papers/` | Subject past papers | Not rebuilt | Older flat address alongside the newer /[level]-past-papers/[subject]/ page. Check for overlap |
| `/a-level-mathematics-past-papers/` | Subject past papers | Not rebuilt | Older flat address alongside the newer /[level]-past-papers/[subject]/ page. Check for overlap |
| `/a-level-past-papers/accounts-9706/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/biology-9700/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/business-9609/` | Subject past papers | Live, v1.0 on shared stylesheet 3.1.1. Checked live 8 Oct 2026 | First Resource page on the shared stylesheet. Wrapper `sj-p-pp-business`. All 324 file links are in the HTML (the old tool built them with script, so Google saw none). Target keyword: a level business past papers (3,600/month, KD 21). Title: A Level Business Past Papers (9609) 2020 to 2025 \| SJ Academy. Redirect `/a-level-business-past-papers/` here with a 301 |
| `/a-level-past-papers/chemistry-9701/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/computer-science-9618/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/economics-9708/` | Subject past papers | Live, v1.0 on shared stylesheet 3.1.1 (wrapper `sj-p-pp-economics`). Checked live 8 Oct 2026 |  |
| `/a-level-past-papers/english-9695/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/law-9084/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/mathematics-9709/` | Subject past papers | Live, v1.0 on shared stylesheet 3.1.1 (wrapper `sj-p-pp-maths`). Checked live 8 Oct 2026 |  |
| `/a-level-past-papers/physics-9702/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/psychology-9990/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/sociology-9699/` | Subject past papers | Not rebuilt |  |
| `/a-level-past-papers/urdu-9686/` | Subject past papers | Not rebuilt |  |
| `/o-level-math-past-papers/` | Subject past papers | Not rebuilt | Older flat address alongside the newer /[level]-past-papers/[subject]/ page. Check for overlap |
| `/o-level-past-papers/accounting-7707/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/biology-5090/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/business-studies-7115/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/chemistry-5070/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/computer-science-2210/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/economics-2281/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/english-language-1123/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/islamiyat-2058/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/mathematics-d-4024/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/pakistan-studies-2059/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/physics-5054/` | Subject past papers | Not rebuilt |  |
| `/o-level-past-papers/urdu-second-language-3248/` | Subject past papers | Not rebuilt |  |

### Tool

| URL | Type | Status | Notes |
|---|---|---|---|
| `/a-level-business-quiz/` | Tool or quiz | Not rebuilt |  |
| `/a-level-grade-strategy-tool/` | Tool or quiz | Not rebuilt |  |
| `/a-level-subject-combinations-tool/` | Tool or quiz | Rebuilt v2.0 (21 Oct 2026), not yet live | Wrapper `sj-p-subject-combos`. Target keywords: a level subjects combination (70, KD 14), a level subjects combination in pakistan (40, KD 6). Title to set: A Level subjects combination tool for Pakistan \| SJ Academy. Ref TL-COMBOS. Owns "best a level subject combination" (decided 21 Oct 2026); the blog `/blog/best-a-level-subjects-combinations/` must be retargeted and link here. See `Scripts/subject-combinations-tool/BRIEF.md` |
| `/chapter-17-quiz/` | Tool or quiz | Not rebuilt |  |
| `/ibcc-equivalence-calculator/` | Tool or quiz | Rebuilt v2.0 (20 Oct 2026), not yet live |  |
| `/past-paper-viewer/` | Tool or quiz | New page, widget built v2.3 (30 Oct 2026), not yet live | Widget `02 Website/Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html`. Title to set: Past Paper & Mark Scheme Viewer \| O and A Level \| SJ Academy. Canonical: the clean address. Focus keyphrase to be set after keyword research. Deep links by query string. Ref PPV-END |
| `/periodic-table-of-elements/` | Tool or quiz | Not rebuilt |  |
| `/schools-near-me-karachi/` | Tool or quiz | Not rebuilt |  |
| `/university-admission-criteria-tool/` | Tool or quiz | Not rebuilt |  |

### Event

| URL | Type | Status | Notes |
|---|---|---|---|
| `/ai-workshop/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/internship-singapore/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/internships-in-pakistan/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/justice-for-caie-students/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/online-teaching-jobs/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/paperchase/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/referral-program/` | Campaign or programme | Not rebuilt | Confirm whether still active. If not, decide: keep, update or retire with a redirect |
| `/a-level-practical-may-june/` | Lab practicals | Not rebuilt | Four practical pages exist (lab-practicals, a-level-practicals, a-level-practical-may-june, a-level-practical-mock-exams-karachi). Check for overlap |
| `/a-level-practical-mock-exams-karachi/` | Lab practicals | Not rebuilt | Four practical pages exist (lab-practicals, a-level-practicals, a-level-practical-may-june, a-level-practical-mock-exams-karachi). Check for overlap |

### Info

| URL | Type | Status | Notes |
|---|---|---|---|
| `/contact-us/` | Contact or policy | Not rebuilt |  |
| `/fee-payments-policy/` | Contact or policy | Not rebuilt |  |
| `/privacy-policy/` | Contact or policy | Not rebuilt |  |
| `/referral-terms/` | Contact or policy | Not rebuilt |  |
| `/refund-policy/` | Contact or policy | Not rebuilt |  |
| `/terms-and-conditions/` | Contact or policy | Not rebuilt |  |
| `/classes-schedule/` | Fees / timetable | Live, v1.0 (own CSS `#sjt`, pre-3.0). Checked live 8 Oct 2026 |  |
| `/fee-structure/` | Fees / timetable | Live, v1.3 (own CSS `#sjf`, pre-3.0). Checked live 8 Oct 2026 |  |

### Proof

| URL | Type | Status | Notes |
|---|---|---|---|
| `/meet-the-teachers/` | Teachers | Not rebuilt |  |

### Utility

| URL | Type | Status | Notes |
|---|---|---|---|
| `/demo-class-registration/` | Form or confirmation | Not rebuilt | Functional page. Do not redesign. Thank-you and confirmation pages should normally be noindex |
| `/payment-confirmation/` | Form or confirmation | Not rebuilt | Functional page. Do not redesign. Thank-you and confirmation pages should normally be noindex |
| `/registration-form/` | Form or confirmation | Not rebuilt | Functional page. Do not redesign. Thank-you and confirmation pages should normally be noindex |
| `/thank-you/` | Form or confirmation | Not rebuilt | Functional page. Do not redesign. Thank-you and confirmation pages should normally be noindex |

---

## 7. Blog posts

| URL | Type | Modified | Notes |
|---|---|---|---|
| `/blog/` | Blog index | 2026-09-30 | Needs the new blog list design |
| `/blog/a-comprehensive-guide-to-a-level-practical-physics-chemistry-and-biology/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/a-level-business-exam-guide/` | Exam technique or subject guide | 2025-09-29 |  |
| `/blog/a-level-physics-practical-your-ultimate-guide/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/a-level-practical-exam-uncovered-things-you-need-to-know/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/a-level-thresholds-guide/` | Exam technique or subject guide | 2025-08-28 |  |
| `/blog/caie-exam-day-guide/` | Exam technique or subject guide | 2026-09-30 |  |
| `/blog/how-to-answer-20-mark-business-question-a-level/` | Exam technique or subject guide | 2026-08-17 |  |
| `/blog/how-to-get-an-a-in-o-level-math-advice-from-a-teacher-with-10-years-of-experience/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/how-to-prepare-for-a-level-practicals/` | Exam technique or subject guide | 2025-07-15 |  |
| `/blog/how-to-study-effectively-for-o-a-level-exams/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/how-to-use-mark-scheme/` | Exam technique or subject guide | 2026-04-19 |  |
| `/blog/lab-practical-exams-bridging-theory-and-practice/` | Exam technique or subject guide | 2025-07-27 |  |
| `/blog/o-a-level-success-guide/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/o-level-cheat-codes/` | Exam technique or subject guide | 2026-01-29 |  |
| `/blog/tips-and-tricks-to-conquering-exam-stress/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/why-are-physics-practical-important-for-your-overall-a-level-grade/` | Exam technique or subject guide | 2025-07-11 |  |
| `/blog/best-a-level-subjects-combinations/` | Listicle or comparison | 2026-09-09 |  |
| `/blog/best-cafes-in-karachi-for-students/` | Listicle or comparison | 2025-11-12 |  |
| `/blog/best-degrees-in-pakistan/` | Listicle or comparison | 2025-09-14 |  |
| `/blog/best-education-youtube-channels/` | Listicle or comparison | 2025-07-11 |  |
| `/blog/best-laptop-for-students/` | Listicle or comparison | 2026-02-11 |  |
| `/blog/best-physics-tuition-karachi/` | Listicle or comparison | 2025-07-24 |  |
| `/blog/best-schools-in-islamabad/` | Listicle or comparison | 2025-12-05 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/free-ai-courses-for-o-a-level-students/` | Listicle or comparison | 2026-07-01 |  |
| `/blog/free-certifications/` | Listicle or comparison | 2026-07-08 |  |
| `/blog/in-demand-skills/` | Listicle or comparison | 2026-07-03 |  |
| `/blog/notability-vs-goodnotes/` | Listicle or comparison | 2025-09-05 |  |
| `/blog/papacambridge-vs-savemyexams/` | Listicle or comparison | 2026-08-17 |  |
| `/blog/the-best-free-english-learning-apps/` | Listicle or comparison | 2026-07-08 |  |
| `/blog/the-best-tutor-academy-in-karachi/` | Listicle or comparison | 2026-09-04 |  |
| `/blog/top-10-best-schools-in-karachi-with-fee-structures/` | Listicle or comparison | 2026-08-20 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-10-free-educational-websites-for-students/` | Listicle or comparison | 2025-07-11 |  |
| `/blog/top-10-universities-in-islamabad/` | Listicle or comparison | 2025-09-05 |  |
| `/blog/top-5-tips-on-how-to-revise-for-exams/` | Listicle or comparison | 2025-07-11 |  |
| `/blog/top-5-websites-to-hone-your-english-grammar-skills/` | Listicle or comparison | 2025-07-11 |  |
| `/blog/top-a-level-colleges-in-islamabad/` | Listicle or comparison | 2026-08-20 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-a-level-colleges-in-karachi/` | Listicle or comparison | 2026-08-20 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-a-level-colleges-in-lahore/` | Listicle or comparison | 2026-08-20 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-o-level-schools-in-lahore/` | Listicle or comparison | 2026-08-21 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-schools-in-lahore/` | Listicle or comparison | 2026-02-10 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/top-universities-in-karachi/` | Listicle or comparison | 2026-02-12 |  |
| `/blog/top-universities-in-pakistan/` | Listicle or comparison | 2026-01-05 |  |
| `/blog/alpha-college-review/` | Named school review | 2026-08-17 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/beaconhouse-school-system-review/` | Named school review | 2026-08-13 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/beaconhouse-university-review/` | Named school review | 2026-03-27 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/city-school-review/` | Named school review | 2025-08-19 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/haque-academy-review/` | Named school review | 2026-09-21 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/heuser-college-review/` | Named school review | 2026-01-27 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/karachi-grammar-school-review/` | Named school review | 2026-04-16 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/lyceum-school-review/` | Named school review | 2026-08-17 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/mok-school-of-law-review/` | Named school review | 2026-04-29 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/titan-college-review/` | Named school review | 2026-06-21 | Names a school. Check against the blog voice rule: facts and labelled opinion only, no ridicule |
| `/blog/caie-retake-policy-2026/` | News or dated update | 2026-08-29 | Dated. Check it is still accurate or mark it as archived |
| `/blog/gates-cambridge-scholarship-applications-now-open/` | News or dated update | 2025-09-19 | Dated. Check it is still accurate or mark it as archived |
| `/blog/uol-announces-scholarships/` | News or dated update | 2025-09-19 | Dated. Check it is still accurate or mark it as archived |
| `/blog/winter-vacation-school-holidays-in-pakistan/` | News or dated update | 2025-12-15 | Dated. Check it is still accurate or mark it as archived |
| `/blog/apple-event-iphone-duo-a-level-business-lessons/` | Opinion or news | 2026-09-10 |  |
| `/blog/caie-paper-leak/` | Opinion or news | 2026-05-21 | Addresses Cambridge directly. Review tone against the "no named targets" rule; keep the facts |
| `/blog/iran-israel-war-impact-on-education-prices/` | Opinion or news | 2026-04-16 |  |
| `/blog/open-letter-to-cambridge/` | Opinion or news | 2026-05-16 | Addresses Cambridge directly. Review tone against the "no named targets" rule; keep the facts |
| `/blog/the-truth-about-o-level-tuitions-in-karachi/` | Opinion or news | 2025-07-11 |  |
| `/blog/cambridge-caie-vs-pearson-edexcel/` | System or decision guide | 2026-08-17 |  |
| `/blog/cambridge-modular-a-level-maths/` | System or decision guide | 2026-09-10 |  |
| `/blog/choosing-your-path-a-level-subjects-selection-guide/` | System or decision guide | 2025-07-11 |  |
| `/blog/how-to-learn-english-speaking/` | System or decision guide | 2025-07-15 |  |
| `/blog/ielts-fees-in-pakistan/` | System or decision guide | 2025-07-15 |  |
| `/blog/internships-in-pakistan/` | System or decision guide | 2025-09-08 |  |
| `/blog/o-a-level-colleges-fees-coaching-karachi/` | System or decision guide | 2026-09-02 | Ranks named schools and may quote fees. Facts need a source and a date |
| `/blog/o-level-in-pakistan/` | System or decision guide | 2026-08-25 |  |
| `/blog/o-levels-and-a-levels-in-pakistan/` | System or decision guide | 2026-08-17 |  |
| `/blog/understanding-ai-for-studies/` | System or decision guide | 2025-10-07 |  |
| `/blog/university-admissions-guide/` | System or decision guide | 2025-09-07 |  |
| `/blog/what-is-igcse/` | System or decision guide | 2026-03-27 |  |
| `/blog/why-extracurricular-activities-are-essential-for-students/` | System or decision guide | 2025-07-11 |  |

---

## 8. Columns to fill as pages ship

For each rebuilt page, add: date built, stylesheet version, wrapper class, lead accent, accents used, what is circled, target keyword, title tag.

## 9. Keyword targets for live rebuilt pages

Checked against the live site on 8 October 2026. The primary keyword sits in the H1 pill. "Secondary" comes from the Semrush pass where one was run; where none was run, the column says so. Titles are as live.

| Page | Primary keyword (H1 pill) | Secondary keywords | Live title | Copy guide status |
|---|---|---|---|---|
| `/` | O & A Level coaching center in Karachi | Not researched yet | The Best O & A Level Coaching Center in Karachi \| SJ Academy | Not yet rewritten. Title uses "Best" (banned) and the H1 still uses "Cambridge doesn't mark effort. It marks method." which is due to change |
| `/a-level-tuition-center-karachi/` | A Level tutors & tuition academy, DHA Karachi | A Level tuition center in Karachi | A Level Tutors & Tuition Academy in DHA, Karachi \| SJ Academy | Not yet rewritten. H1 "We teach the method that gets you A*s" reads as a promised result: review against the guide |
| `/o-level-tuition-center-karachi/` | O Level tutors & tuition center, DHA Karachi | Not researched yet | O Level Tutor & Tuition Center in Karachi (DHA) \| SJ Academy | Not yet rewritten |
| `/a-level-maths-tuition/` | A Level Maths tuition in Karachi & online | 9709 | A Level Maths Tuition in Karachi & Online (9709) \| SJ Academy | Not yet rewritten |
| `/a-level-business-tuition/` | A Level Business tuition in Karachi & online | business studies a level (170/mo), 9609 business (170), a level business syllabus (390 + 260), A Level Business Studies | A Level Business tuition in Karachi & online \| SJ Academy | Rewritten, v2.1 |
| `/a-level-past-papers/business-9609/` | A Level Business past papers and mark schemes | a level business past papers (3,600/mo, KD 21), business a level past papers (720), business studies a level past papers (90) | A Level Business (9609) Past Papers & Mark Schemes | Resource page, not covered by the copy guide |
| `/a-level-past-papers/economics-9708/` | A Level Economics past papers and mark schemes | Not researched yet | A Level Economics Past Papers (9708) 2020 to 2025 \| SJ Academy | Resource page |
| `/a-level-past-papers/mathematics-9709/` | A Level Maths past papers and mark schemes | Not researched yet | A Level Mathematics (9709) Past Papers & Mark Schemes | Resource page |
| `/fee-structure/` | O & A Level tuition fees in Karachi | Not researched yet | SJ Academy Fee Structure - O & A Level Tuition Fees in Karachi | Info page |
| `/classes-schedule/` | O & A Level class schedule | Not researched yet | SJ Academy Class Timetable - O & A Level Classes in Karachi | Info page |

**Next keyword work:** run the same Semrush and Search Console check done for Business on the homepage, both level pages and A Level Maths before their copy is rewritten.

