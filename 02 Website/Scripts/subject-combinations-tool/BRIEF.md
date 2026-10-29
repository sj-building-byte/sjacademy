# A Level Subject Combinations Tool v2.0: brief and accuracy check

Page: /a-level-subject-combinations-tool/ (address unchanged). Widget: `02 Website/Pages/a-level-subject-combinations-tool-elementor-widget.html`.
Rebuild: `python3 build.py` (needs node; reads `source.html` and `../sj-page-script.js`). Tests: `python3 test.py` (Playwright; set `SJ_CSS` to the path of `01 Brand/sj-brand.css`), `python3 ref_check.py`.
Family: Tool (graph-paper hero, tool in the offset card). Shared stylesheet 3.1.1. Wrapper `sj-p-subject-combos`. WhatsApp ref: TL-COMBOS.

## Decisions (Sunyyan, 21 Oct 2026)
- Recommend every subject. No "not at SJ" tags or mentions anywhere.
- Further Maths is not taught at SJ. It stays as a route option and in the subjects list.
- PDF export removed (html2pdf, the old Free Expert Help form and the old script are gone).
- No phone bottom bar (it would cover the result). Registration popup 6023 is the only enrolment form.

## Keywords (Semrush screenshots, 21 Oct 2026)
- Primary: a level subjects combination (70/month, KD 14) and a level subjects combination in pakistan (40, KD 6).
- Where they sit: Yoast title, meta, H1 pill, lead ("in Pakistan"), the "A Level subjects list for Pakistan" H2, FAQ.
- Long tail: "A Level subject combination for medicine / engineering / computer science / business and finance / law / architecture and design" are six H3s written into the HTML from the same ROUTES data the tool uses (build.py). "A Level subjects list" and "cie / cambridge a level subjects" are served by the 18-row subjects table with syllabus codes.
- Question keywords ("best subject combination for a levels", how many, compulsory, easiest or hardest) are FAQ questions, 9 in total, with matching FAQPage JSON-LD (built from the same list, so they cannot drift apart).
- The screenshots showed only the top rows of the keyword lists. A Semrush CSV export would let us add anything below them.
- Yoast: title `A Level subjects combination tool for Pakistan | SJ Academy`; meta in the file header (143 characters); focus keyphrase `a level subjects combination`.
- Overlap: /blog/best-a-level-subjects-combinations/ and /blog/choosing-your-path-a-level-subjects-selection-guide/ cover the same topic. The tool links to the first. Decision (Sunyyan, 21 Oct 2026): the tool page owns "best a level subject combination". When the blog is rebuilt, retarget it away from that phrase, link it to the tool near the top, and check Search Console for cannibalisation before deciding whether to merge or redirect.

## Accuracy check (21 October 2026)
- Second solve: `ref_check.py` is a separate Python version of the ranking, written from the rules (direction +10 each, undecided +2 per tag, no direction hit -20, style +5, coverage x10 minus 2 per weak core subject, one best route per chosen direction, then fill to three). It matches the JavaScript on 5,000 random answer sets: 0 differences in the three routes, the removed routes and the fallback flag.
- 12 scenarios in `test.py` (medicine, no Physics, business, no Maths, CS, law, no essay subjects, creative, undecided, engineering and medicine, engineering with no Maths, everything banned): three routes each, except "ban everything" (one route and a notice). No script errors, no sideways scroll at 320, 360, 390 px. With JavaScript off the page still holds 6 degree cards, 18 list rows, 9 FAQ answers and the H1.
- FAQ and JSON-LD compared programmatically: identical text.

## Facts checked against sources
| Fact | Source |
|---|---|
| Pre-Medical = Physics, Chemistry, Biology, plus SSC Science with Biology | IBCC equivalence guidance, Eduvision |
| Pre-Engineering = Physics, Chemistry, Mathematics | IBCC |
| Computer Science group = Physics, Computer Science, Mathematics | IBCC |
| General Science accepts Maths + Economics + CS, Maths + Physics + Statistics, among others | IBCC |
| Humanities = any three subjects | IBCC |
| No compulsory A Level subjects; typically four at AS and three at A Level; more than 50 subjects | Cambridge factsheet, British Council |
| Syllabus codes: Maths 9709, Further Maths 9231, Physics 9702, Chemistry 9701, Biology 9700, CS 9618, Economics 9708, Business 9609, Accounting 9706, English Language 9093, Literature 9695, History 9489, Sociology 9699, Psychology 9990, Law 9084, Art and Design 9479, Geography 9696, Urdu 9686 | Cambridge syllabus list, British Council components list |
| MDCAT run by PMDC; UCAT replaced BMAT | PMDC, UCAT |

## Please skim (from general knowledge, not a primary source)
University and entry-test lines inside ROUTES (NED, GIKI, PIEAS, FAST-NUCES, LUMS, IBA, Habib, NCA, LAT, LNAT), the three one-line descriptions of the related tools, and the "Often chosen for" column of the subjects list. Entry-test names and formats change each year.

## Before going live
- Record the old page's title, H1, meta and top ranking queries from Search Console, then replace.
- Cloudways backup first. Clear Elementor, plugin and server caches after pasting.
- Elementor: Full Width, Hide Title = Yes, one HTML widget, zero padding, no entrance animation.
- 7 chips in the "dealbreaker" group is above the 2 to 6 guideline. The yellow band sits right before the FAQ. Both are deliberate and open to change.
