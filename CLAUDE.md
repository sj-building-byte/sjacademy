# SJ Academy: read this first

This folder holds all of SJ Academy's work. Any AI agent (Claude, Codex, Cursor, Antigravity, Gemini) should read this file before doing anything, then read the `START-HERE.md` in the area it is working on.

Last updated: 16 October 2026. Update this file when a fact, rule or priority changes.

## The business

- SJ Academy (sjacademy.pk): Cambridge CAIE O Level and A Level tuition. Campus at Plot 29C, Lane 5, Seher Commercial, DHA Phase 7, Karachi, plus live online classes across Pakistan. May/June and Oct/Nov exam series.
- Owner: Sir Sunyyan Junaid. Teaches A Level Business (9609) and runs content, the website, marketing and edtech product work.
- Instagram: instagram.com/sjacademypk. WhatsApp for demos and enquiries: +92-336-2144454.
- Website stack: WordPress, Educrat theme, Elementor with PRO Elements, Yoast, WPForms, WP-Optimize, Flying Scripts, hosted on Cloudways behind Cloudflare. Take a Cloudways backup before major page changes.
- Approved facts, claims, fees and teacher details: `00 Start Here/FACTS.md`. Never publish a number or claim that is not in that file.
- Anything that teaches, solves or states a fact must pass `00 Start Here/ACCURACY.md` before it is published. That means:
  - solve it twice
  - make sure the question is complete
  - keep the diagram honest
  - review every frame as a student would
  - record the check in the project's BRIEF.md
- What matters right now: `00 Start Here/PRIORITIES.md`.

## Folder map

| Folder | What is in it | Start with |
|---|---|---|
| `✅ Finished/` | Ready-to-post work only: Videos (Ads - vertical, Ads - YouTube, Brand film, Practicals, Reels & teaching, Solve it in your head), Carousels, Posts, Static ads, PDFs & ebooks. One final file per piece, no drafts | Open the subfolder you need |
| `00 Start Here/` | Facts, priorities, move logs | `FACTS.md`, `PRIORITIES.md` |
| `01 Brand/` | Brand system v4: brand book (core), Web, Social and ads, Video and motion, Sound, and PDF and print playbooks; stylesheet, brand kit, voice and copy guides, logos, sound files. The only copy of each | `START-HERE.md` |
| `02 Website/` | Live page widgets, tools, SEO workspace, planning, concepts | `START-HERE.md` |
| `03 Marketing/` | Instagram, ads (static and video), content, audits, metrics | `START-HERE.md` |
| `04 Teaching/` | Academy-wide teaching reference: past papers for all subjects, syllabuses, grade thresholds, IBCC reference. A Level Business is not here (see below) | `START-HERE.md` |
| `05 Strategy/` | Business plan, pitch deck, AI platform, research | `START-HERE.md` |
| `06 Operations/` | Finance, lead tracking, internal tools | `START-HERE.md` |
| `07 AI & Dev/` | Skills, agent personas, Codex and Antigravity projects, dev experiments | `START-HERE.md` |
| `99 Archive/` | Old material kept for reference | |
| `_Inbox/` | Drop new files here; sort them into an area once a week | |
| `_to_delete/` | Created only when needed: duplicates and empty folders waiting for Sunyyan to check. Emptied 16 October 2026 | |

Kept outside this folder on purpose:
- `Documents/A Level Business/`: Sunyyan's own A Level Business (9609) teaching material, kept separate from running the academy since 16 October 2026. It has its own `CLAUDE.md`. Finished products made from it (the Solved Past Papers ebook, definitions ebooks, mock exams) stay in `✅ Finished/`.

Never connect these to an AI session:
- `Documents/SJ Academy - Private/`: API keys, hiring documents and ID scans, student records and lead lists.
- `SJ Academy Media/` (now inside this folder): `Footage & assets/` holds every raw clip, photo and snippet in one flat folder; `Zoom Recordings/` holds class recordings (large files). Finished videos are in `✅ Finished/Videos/`, not here. New footage goes straight into `Footage & assets/`. HyperFrames projects copy the clips they use into their own `assets/`.

Live data that is not in this folder (Google Sheets, reach them through the Google Sheets connector): the Lead Tracker, the finance sheet, the class timetable sheet, and "SJ Academy - Page Rebuild & Marketing Tracker".

## Rules for every piece of work

How Sunyyan works:
- Direct and structured. Complete, publish-ready deliverables, not back-and-forth.
- Ask before setting a new rule or assuming a fact.
- During technical setup: one instruction and the next step, no explanations.
- He reviews on his phone. Design mobile first.
- When a rebuild should change only the copy, keep the design identical to the live version and compare before delivering.

Writing (all copy, posts and pages):
- No em dashes. Active voice. No buzzwords. Sentence case. Bullets use •.
- English only; Karachi and Pakistan details are welcome.
- Dry, sarcastic humour that never offends. No targeting a named place or person. No expletives, even mild or censored ones.
- No unsupported claims ("best", "guaranteed", "highest-rated"). Never name an outside copywriter or brand the voice draws on.
- Instagram captions: plain text, no markdown.
- Landing pages follow `01 Brand/SJ-ACADEMY-LANDING-PAGE-COPY-GUIDELINES.md`; blog posts follow `01 Brand/SJ-ACADEMY-BLOG-VOICE-GUIDELINES.md`.

Design:
- `01 Brand/SJ-ACADEMY-BRAND-BOOK.md` (the core) wins over any other style file; then the playbook for the channel: Web, Social and ads, Video and motion, Sound, or PDF and print. Older guides (anything saying "maximum font weight 400", or `sja_brand_style_guide.md`) are archived and must not be used.
- Colours: yellow #FCE004, brown #453516, orange #FE6100. Fonts: Poppins (all reading text) and Caveat (short handwritten notes) only. Web headings: H1 600, H2 500.
- Every piece starts with the five-line brief in the brand book (section 9). Rotate formats; never repeat the last one.
- No cards with coloured bars on top. Logo sits at the top of ad designs.

Files:
- One current file per thing, with a plain name. Older versions go into that area's `Archive/`.
- Finished work goes into `✅ Finished/` as soon as it is final: one file per piece, a plain name ("May-June 2027 ad.mp4"), no version numbers or words like "final" or "finalest". Source files, assets and drafts stay in the working area.
- HyperFrames: renders stay in the project's `renders/` folder while drafting. Once Sunyyan picks the final, move that one file to the matching `✅ Finished/Videos/` subfolder, renamed plainly, and log it. Never copy finals to the project root.
- At the end of a work session, update the `START-HERE.md` of the area you worked in: what changed, what is live, what is next.
- Never move anything into this folder from `SJ Academy - Private`.

## Starting a new chat

Connect `Documents/SJ Academy` and say: "Read CLAUDE.md, then the START-HERE in [area]. Today I want to [task]."
