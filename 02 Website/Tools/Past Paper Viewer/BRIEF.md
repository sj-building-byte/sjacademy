# Past paper viewer: brief and audit record

Page: `/past-paper-viewer/` (not live). Widget: `past-paper-viewer-elementor-widget.html`, v2.3, 30 October 2026.

## Five-line brief
• Who: O and A Level students practising past papers, mostly on phones, some on laptops.
• Job: open the right paper and its mark scheme in two taps, try the question first, then check the marks.
• Format: Tool page, one Elementor HTML widget, no libraries.
• Success: `tool_complete` and `mark_scheme_reveal` events; low `paper_unavailable`; WhatsApp leads tagged `PPV-END`.
• Must not: show a broken or blank paper, or offer a paper that does not exist.

## Audit, 30 October 2026

The sandbox cannot reach `sjacademy.pk`, so no live file was opened. Paper structures were checked against public file listings (pastpapers.co, Save My Exams and Cambridge grade threshold tables, through web search). The file host itself still has to be checked with `check-files.py`.

### Why O Level Accounting did not load
1. **Folder name.** The viewer and the O Level hub pages use `Accounting (7707)`. The live O Level directory page (`/o-level-past-papers/`, the older tool) uses `Accounts (7707)`. The older tool's names have the marks of real folder names (`Pakistan studies (2059)` with a small s, `Islamiat`, `Computer`), and Sunyyan's report fits it. Eight O Level subjects have different names in the two places: Accounting, Business Studies, Computer Science, English Language, Islamiyat, Mathematics D, Pakistan Studies, Urdu Second Language.
2. **Variants.** Some Oct/Nov series use variants 2 and 3, not 1 and 2 (Cambridge's November 2024 Accounting thresholds list components 12, 13, 22, 23). The viewer only offered variants 1 and 2.

### Other errors found and fixed in v2.3
| Subject | Was | Now | Evidence |
|---|---|---|---|
| O Level Pakistan Studies 2059 | Paper 1 Variant 1 and so on, files `qp_11` | Paper 1, Paper 2, files `qp_01`, `ms_1`, `in_01` | May/June 2024 listing: `2059_s24_qp_01`, `ms_1`, `in_01`, `qp_02`, `ms_2`, `in_02` |
| O Level Urdu Second Language 3248 | files `qp_11` | `qp_01`, `ms_1`, no insert | May/June 2024 listing: `3248_s24_qp_01`, `ms_1`, `qp_02`, `ms_2` |
| O Level Biology 5090 | Papers 1, 2, 3, 6 every year | Paper 6 up to 2022, Paper 4 from 2023 | 2024 has `5090_s24_qp_41`; Paper 6 only in 2022 and earlier |
| O Level English Language 1123 | insert on both papers | to 2023: insert on Paper 2; from 2024: insert on Paper 1 (new syllabus, Paper 1 Reading) | May/June 2024: `1123_s24_in_11`, Paper 2 Writing has no insert |
| O Level Accounting 7707 | insert on Paper 2 | no insert | May/June 2024 listing has no `in` files |
| O Level Economics 2281 | insert on Paper 2 | no insert | May/June 2024 listing has no `in` files |
| O Level Computer Science 2210 | insert on Paper 2 | no insert | May/June 2024 listing has no `in` files |
| O Level Business Studies 7115 | insert on both papers (hub page) | insert on Paper 2 only | May/June 2024: `in_21`, `in_22` only |
| A Level Biology, Chemistry, Physics | Paper 3 variants 1 to 3, insert listed | Paper 3 variants 1 to 5, confidential instructions only | `9702_s24_qp_34`, `9702/35`, `9701/35` exist; Pakistan often sits 33 to 35 |
| A Level Mathematics 9709 | no Paper 2 | Paper 2 (Pure Mathematics 2) added | Paper 2 is a current component |
| A Level 9695 | shown as "English" | "Literature in English" | 9695 is Literature in English; "English" could be mistaken for General Paper |

Subject names now show their code on screens 768px and wider ("Accounting (7707)"); phones show the name only so it is not cut off.

### Changes to how the viewer works
• **Folder fallback.** Each subject lists folder names to try. If the host answers 404, the viewer tries the next name and keeps the one that works. This needs the host to allow the check (CORS); without it the first name is used.
• **FILES list.** `check-files.py` asks the host for every likely file and writes the list into the widget. A subject in that list shows only the series and papers that exist (including variant 3, 2019 papers and May/June 2026 if uploaded), with no background checks. Subjects not found keep the rules.
• **Phone layout for browsers that cannot show PDFs in a page.** Chrome on Android (phones and tablets) cannot. Before, an Android tablet or a phone turned sideways got blank frames. Now any browser that reports no PDF viewer, and any phone turned sideways, gets the phone layout with "Open ... in new tab".
• **Loading state.** Each pane shows "Loading the paper" until the PDF arrives (or 12 seconds pass).
• **Screen readers.** One short status line announces the loaded paper, instead of the whole stage being read out on every change.
• **Status check.** Only a 2xx answer counts as available; a 403 or 5xx is treated as "cannot tell" and the frame loads as before.

### Tests run
`tests/viewer-test.js`, 44 checks, all passing on 30 October 2026, with the file host mocked: Accounting paper and mark scheme load from `Accounts (7707)`; subject codes; no Insert button where none exists; lock, unlock, toggle; missing paper message; full screen; GA4 events; deep link (with utm kept, Insert opens); no-CORS fallback; Pakistan Studies `qp_01` / `ms_1`; Biology 2024 vs 2021 papers; Physics variant 35 and Confidential; Maths Paper 2; phone bar, lock and open links; sideways phone; browser without PDF viewer; folder fallback; FILES mode (only stored series and papers, missing mark scheme shown, no background checks). `check-files.py` was run against a mock host: it found Accounting under `Accounts (7707)`, Pakistan Studies under its second name, `ms_1` naming, a missing mark scheme, and left a subject with no files on its rules.

Run the tests: `node "02 Website/Tools/Past Paper Viewer/tests/viewer-test.js"` (needs Playwright).

### Still not verified
• The real folder names and file names in storage. `check-files.py` settles this; read `files-report.md` after running it.
• A Level inserts per paper (Business, Economics, Accounting and others follow the old tool). `check-files.py` records what exists.
• iPad Safari and iPhone Safari with the desktop layout (iPad gets it). Test on a device.
• Whether the file host sends `Access-Control-Allow-Origin`. Without it the folder fallback and missing-file message cannot work, which is why the FILES list matters.

### Outside this widget, found during the audit
The live O Level hub pages (`/o-level-past-papers/{subject}/`) were built with the same folder names and file patterns as v2.2. If `check-files.py` confirms `Accounts (7707)` and the `qp_01` naming, those hub pages have broken links for up to eight subjects, including Pakistan Studies and Islamiyat, which almost every O Level student in Pakistan takes. Check them after running the script.
