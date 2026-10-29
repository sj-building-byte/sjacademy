# Website: start here

sjacademy.pk is being rebuilt page by page in one design language without losing Google rankings. Header and footer stay; only page bodies are rebuilt.

## Read first
1. `Planning/HANDOFF-website-rebuild.md`: full state of the rebuild, build rules, testing method, next steps and open items.
2. `Planning/SITE-REGISTER.md` (and `site-register.csv`): every live page, its family, status, keywords and overlaps.
3. `../01 Brand/START-HERE.md` for design and copy rules.
4. For SEO work: `SEO/00_START_HERE/SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md`.
5. Past papers pages: `Planning/HANDOFF-past-papers-and-session-7-oct.md`.

## What is where
- `Pages/`: the current widget for each built page (one Elementor HTML widget per page). The file here is the one that is live, unless its name says otherwise.
  • `homepage-elementor-widget.html` is live (v3.0: v2.0 copy on the shared stylesheet; confirmed live on 16 October 2026). v1.5 is in `Archive/Old widget versions/`.
  • `a-level-business-tuition-elementor-widget.html` is v2.1 (live).
  • `schools-near-me-elementor-widget.html` is v2.0, built 20 October 2026, NOT yet pasted live. Tool page for /schools-near-me-karachi/: every school is written into the HTML (the old page loaded the list with JavaScript). Refresh it with `Scripts/build-schools-near-me.py` when the Google Sheet changes.
  • `a-level-subject-combinations-tool-elementor-widget.html` is v2.0, built 21 October 2026, NOT yet pasted live. Tool page for /a-level-subject-combinations-tool/ with the SEO sections (by degree, subjects list, 9 FAQs) written into the HTML. Rebuild with `Scripts/subject-combinations-tool/build.py`; accuracy record in its BRIEF.md.
  • `Standalone pages/`: the A Level mock landing page and the results wall.
- `Tools/`: interactive tools (Business quiz, grade calculator, class schedule, past papers tool, Quadratics ebook pages).
- `SEO/`: the SEO workspace with its own `00_START_HERE`, audits, plans, data and scripts. Its `venv` needs rebuilding after the move (`python3 -m venv venv`, then reinstall packages) before running its scripts.
- `Concepts/`: homepage design versions and page concept specs (IBCC calculator, career finder, teachers directory and others).
- `Scripts/`: `sj-page-script.js` (standard page script) and the past papers page generators.
- `Archive/`: old widget versions, old drafts from April and July, old exports.

## State on 12 October 2026
- 10 rebuilt pages are live. On the shared stylesheet: A Level, O Level, A Level Maths, A Level Business, and the Business, Economics and Maths past papers pages. Still on their own CSS: fees, timetable. The homepage moved to the shared stylesheet with v3.0.
- Page status, keywords and marketing per page are tracked in the Google Sheet "SJ Academy - Page Rebuild & Marketing Tracker".

## Next
See "What comes next" and "Open items" in `Planning/HANDOFF-website-rebuild.md`. Update this file and the handoff at the end of every website session.

## Update 20 October 2026
- Schools near me page rebuilt on the shared stylesheet (Tool family). Search Console shows the old page gets about 2 clicks a day, so the aim is clicks, then leads. Next: paste it live after a Cloudways backup, set the Yoast title, description and canonical (listed at the top of the widget file), then check Search Console and GA4 events (`tool_complete`, `school_call_click`, `school_map_click`, `whatsapp_click`) after two weeks.
- Traffic and lead analysis of the live schools near me page: `SEO/02_Reports_and_Audits/2026-10-20_Schools_Near_Me_Analysis/schools-near-me-karachi-report.md`. Real traffic is about 56 Google clicks a month (Semrush's 19.5K is wrong), 89% from Karachi, and at most one lead in 90 days. Before the rebuild goes live, remove the UTM tags from the tuition ad card link and mark `submit_lead_form` and `whatsapp_click` as key events in GA4.
- Traffic and lead analysis of the top schools in Karachi blog post: `SEO/02_Reports_and_Audits/2026-10-20_Top_Schools_Karachi_Blog_Analysis/top-schools-karachi-blog-report.md`. It brings 24% of site clicks (5,926 in 3 months), 84% from Karachi, but only 4 key events in 90 days. Clicks are down 53% on last year at the same rankings. Next: fix the 15/10/14 school count in the title, H1 and meta, add a parent-focused tuition call to action, and update the fees for 2026-27.

- Top schools in Karachi blog post (site's biggest page, about 24% of clicks): new body built as `Pages/top-schools-karachi-blog-elementor-widget.html` (v2.0, 20 October 2026), NOT yet live. Snapshot of the live version: `Archive/Live snapshots/`. KAS and BOS fees are official 2026-27; the rest are labelled estimates. Two WhatsApp offers tagged Ref BLOG-T14-TOP and BLOG-T14-END, so you can see which placement brings leads.
- IBCC calculator v2.0 (20 Oct 2026): `Pages/ibcc-calculator-elementor-widget.html`, built from `Scripts/ibcc-calculator/` (`python3 build.py`). Accuracy record in `Scripts/ibcc-calculator/BRIEF.md`. When IBCC publishes the 2027 A* table, update `engine.js` and rerun `ref_check.py`. Traffic analysis: `SEO/02_Reports_and_Audits/2026-10-20_IBCC_Calculator_Analysis/ibcc-calculator-report.md`.

## Update 29 October 2026
- Past paper and mark scheme viewer built: `Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html` (one Elementor HTML widget, vanilla JS, NOT yet pasted live). Level, Subject, Year, Paper dropdowns; paper left, mark scheme right; "Don't cheat / Learn" toggle plus a locked overlay on the mark scheme; insert and confidential instructions swap on the left pane. Under 768px the PDFs open in a new tab and a sticky bottom bar switches Paper, Insert, Mark scheme.
- File links are built from the same storage pattern and subject settings as the old past papers tool (`sjacademy.pk/file/Past-papers-storage`, A Level and O Level, 12 to 13 subjects each, 2020 to 2025). O Level settings come from `SEO/01_Website_Pages/Past_Papers/O_Level/` hubs. `BASE` and `LEVELS` sit at the top of the script. Links were not tested from the sandbox (host blocked). Next: paste into a draft page, check that PDFs show inside the frames (a frame-blocking header on the file host would leave them blank), tap a few links per subject, then decide on the 2026 series.
