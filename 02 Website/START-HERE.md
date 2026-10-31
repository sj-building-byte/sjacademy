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

- Past paper viewer v2 (29 October 2026): centred title, "Don't cheat / Learn" segmented control in the Mark scheme header, frosted cover with the message "Your answer first.", Insert / Confidential / Back to Paper buttons in the Question paper header, yellow closing band with a WhatsApp button (prefilled with the chosen level and subject) and an Instagram button. Tracking matches the other pages: `whatsapp_click` and `instagram_click`, `data-loc="viewer_band"`, `data-family="Tool"`. Mark `instagram_click` as an event in GA4 if you want it reported.
- Past paper viewer v2.1 (29 October 2026): missing files show "This question paper isn't available" with a "Choose another paper" button, instead of the host's raw 404 JSON. Each file is checked with a background HEAD request first; if the file host blocks that request (CORS) the viewer falls back to loading the frame as before. Closing band: new heading "Know the content but still losing marks?", WhatsApp button and an "Explore SJ Academy" button to the homepage (event `homepage_click`, replaces `instagram_click`).
- Past paper viewer WhatsApp message now follows the other pages: free demo request, Level and Subject lines, Mode line, `(Ref: PPV-END)` and "My name is". `PPV-END` is a new Ref code (past paper viewer, closing band); add it to the lead tracker's Ref list.
- Past paper viewer: added a Full screen button (above the panes, desktop and tablet only). It uses the browser's Fullscreen API, with a full-window fallback where that is blocked. In full screen the title and the closing band are hidden so the two panes get the whole screen. Esc exits.
- Past paper viewer: the Don't cheat / Learn toggle is hardened against the site theme's button styles (they were turning the clicked button black and adding black outlines). Selected mode is bold and dark, the other is greyed, no borders; keyboard focus shows an orange ring only.

## Update 29 October 2026 (past paper viewer, search and measurement)
- Past paper viewer v2.2, `Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html`, planned address `/past-paper-viewer/`. Added to `Planning/SITE-REGISTER.md` (Tool family, now 9). Still NOT live. Yoast title, meta and canonical are in the comment at the top of the widget file. Focus keyphrase is left empty until the keyword research is done.
- Deep links: `?level=o-level&subject=biology&year=2025-mj&paper=31` opens that paper (year 2025-mj is May/June, 2025-on is Oct/Nov; paper 31 is Paper 3, Variant 1). Any prefix works and utm tags are kept. The address bar updates as the student picks, so any paper can be shared. Next: add "View with mark scheme" links from the subject hub pages, the past papers directories, the homepage resources and the mark scheme blog post.
- GA4 events (matching the other pages): `tool_start`, `tool_complete`, `mark_scheme_reveal`, `insert_view`, `fullscreen_open`, `paper_unavailable` (shows broken or missing files), `open_in_new_tab` (phones), `whatsapp_click`, `homepage_click`. Parameters: level, subject, series, paper, entry, method, type, file, link_location, page_family. To see them in reports, register these as custom dimensions in GA4 (Admin, Custom definitions): level, subject, series, paper, entry, method, type, file.
- Before going live: set the canonical to the clean address in Yoast, test a deep link on the draft page, and take a Cloudways backup.
- Full handoff for the past paper viewer (state, decisions, open items): `Planning/HANDOFF-past-paper-viewer-30-oct.md`.

## Update 30 October 2026 (past paper viewer v2.3, audit)
- Audit of the viewer: `Tools/Past Paper Viewer/BRIEF.md`. O Level Accounting failed because storage most likely uses `Accounts (7707)`; the viewer now tries both names. Pakistan Studies and Urdu Second Language use `qp_01` / `ms_1` file names, Biology has Paper 4 from 2023, English Language moved its insert in 2024, wrong inserts removed, A Level practical variants 1 to 5, A Level Maths Paper 2 added.
- New `Tools/Past Paper Viewer/check-files.py`: run it on your own computer before pasting. It writes the real file list into the widget so students only see papers that exist, and `files-report.md` shows what is missing in storage.
- Android Chrome and sideways phones get the phone layout (no blank PDF frames). Browser tests in `Tools/Past Paper Viewer/tests/`.
- Live O Level hub pages use the same folder names and file patterns as the old viewer and probably have broken links for several subjects. Check them with the script's report.
- Still NOT live. Next: run `check-files.py`, then open item 1 in `Planning/HANDOFF-past-paper-viewer-30-oct.md` (draft page test).
- Share links: the address now uses `series=` (WordPress shows a 404 for any page address containing `year=`) and `marks=show` opens the mark scheme too. New "Share this paper" button. Example: `/past-paper-viewer/?level=o-level&subject=biology&series=2025-mj&paper=31&marks=show`.
- `sjacademy.pk/file/` only redirects to `f006.backblazeb2.com`. `check-files.py` needs that host reachable (from your Mac, or allow it in the Claude environment).
- Past paper viewer v2.4: real file list from Backblaze written into the widget; all 6,200 links checked, 0 wrong. 16 mark schemes need uploading (list in `Tools/Past Paper Viewer/BRIEF.md`).
- LIVE PROBLEM: 8 of 12 O Level subject past papers pages and the A Level Urdu page have links that all return 404 (wrong storage folder or file names). Next job.


## Update 30 October 2026 (broken past papers pages)
- Checked every live subject past papers page against storage. Broken now (every link 404): O Level Accounting, Business Studies, Computer Science, English Language, Islamiyat, Mathematics D, Pakistan Studies, Urdu Second Language, and A Level Urdu. A Level Business, Economics and Maths pages: 30 of 1,395 links broken.
- New generator for all subject past papers pages: `Scripts/past-papers-pages/build.py` (copy and checked facts in `subjects.py`, plan and accuracy record in `BRIEF.md`). It reads the checked file list from the past paper viewer widget, so every link exists.
- First page built: `Pages/o-level-pakistan-studies-past-papers-elementor-widget.html` (v1.0), NOT live. Waiting for Sunyyan's review before the other eight. Order and reasons in `Scripts/past-papers-pages/BRIEF.md`.
- Storage check widened to 2010 to 2026: A Level papers go back to 2015, now in the viewer. Computer Science 2015 to 2021 files are the old 9608 syllabus and are labelled so.
- All nine broken past papers pages rebuilt (v1.0, 30 October 2026), NOT live: O Level Pakistan Studies, Islamiyat, Mathematics D, English Language, Urdu Second Language, Accounting, Business Studies, Computer Science, and A Level Urdu. Files in `Pages/` (`o-level-{subject}-past-papers-elementor-widget.html`, `a-level-urdu-past-papers-elementor-widget.html`). Yoast title, meta and keyphrase at the top of each file. 871 file links and 397 side by side links checked. Publish the past paper viewer first (the side by side links go to it). Next: O Level Biology, Chemistry, Economics and Physics (links work but Google cannot read them), then regenerate A Level Business, Economics and Maths from the checked list.
- 31 October 2026: O Level Biology, Chemistry, Physics and Economics past papers pages rebuilt on the same template (v1.0, NOT live). All 12 O Level subject pages and A Level Urdu are now built. Next: regenerate A Level Business, Economics and Maths from the checked file list, then the other 9 A Level subject pages, then the `/o-level-past-papers/` and `/a-level-past-papers/` directories.
- 31 October 2026: A Level Business, Economics and Maths past papers pages fixed. The repo copies were older than the live pages, so the live code was used (old copies in `Archive/Old widget versions/`). Only the paper tables changed (`Scripts/past-papers-pages/refresh-tables.py`); keywords and copy are untouched. 32 broken links removed, 52 missing files added, Side by side links added. Paste the three files over the live widgets.
