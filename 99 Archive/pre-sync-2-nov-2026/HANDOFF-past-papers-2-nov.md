# Handoff: past paper viewer and the 25 subject past papers pages

Written 2 November 2026 from the last two cloud chats (29 to 31 October 2026). Use it to bring a local Claude session up to date.

Read order for any agent: `CLAUDE.md`, then `02 Website/START-HERE.md`, then this file. Deeper detail lives in the files listed in section 6.

## 1. State in one paragraph

Two cloud chats built the past paper and mark scheme viewer and rebuilt all 25 subject past papers pages (12 O Level, 13 A Level). Every link in them was checked against the real Backblaze storage. **The viewer is live** at https://www.sjacademy.pk/past-paper-viewer/, but the live copy is v2.4, which is out of date and must be re-pasted. **None of the 25 rebuilt subject pages had been pasted as of 31 October.** Nothing is merged into `main` and no pull request exists. All the work is on the branch `claude/jolly-heisenberg-n87o3o`, which has the same commits as `claude/dreamy-sagan-1akdrp` plus this file.

## 2. Sync your local copy

Your local `Documents/SJ Academy` folder is a git clone of `sj-building-byte/sjacademy`. Run these in that folder.

```bash
git fetch origin
```

```bash
git checkout claude/jolly-heisenberg-n87o3o
```

To put it all on `main` instead, ask Claude to open a pull request (none has been opened, by choice), merge it on GitHub, then `git checkout main && git pull`.

Then start the local session with:

```
Read CLAUDE.md, then 02 Website/START-HERE.md, then 02 Website/Planning/HANDOFF-past-papers-2-nov.md.
Today I want to [task]. Start with the paste order in section 4 unless I say otherwise.
```

## 3. What was done, chat by chat

### Chat 1: "CAIE past papers viewer tool" (29 to 30 October)
Branch `claude/caie-past-papers-viewer-3plf1s` (now included in this branch).
- Built the viewer: one Elementor HTML widget, plain JavaScript, no libraries. Level, Subject, Year, Paper dropdowns. Paper on the left, mark scheme on the right (768px and up). Phones get "Open in new tab" buttons and a sticky bottom bar.
- Redesign after your "AI slip" feedback: centred title, "Don't cheat | Learn" segmented toggle in the mark scheme header (selected bold and dark, other greyed, no borders, hardened against the theme's black button styles), frosted lock card ("Your answer first."), Insert / Confidential / Back to Paper buttons in the paper header. Frosted glass is an agreed exception to the "no glass" rule, for this page only.
- Friendly missing-file message ("This question paper isn't available") instead of raw 404 JSON.
- Closing yellow band: "Know the content but still losing marks?", WhatsApp demo button (Ref `PPV-END`) and "Explore SJ Academy" to the homepage. You chose no push after a mark scheme reveal.
- Full screen button. The white bar you saw was a Code Beautify ad, not the site.
- Deep links, the subheading ("Open any Cambridge O and A Level past paper next to its mark scheme. Free, no sign-up.") and GA4 events.
- SEO plan: Yoast title, meta and canonical in the widget's top comment. Keyword research postponed by you.
- Wrote `HANDOFF-past-paper-viewer-30-oct.md`.

### Chat 2 (30 to 31 October)
Branch `claude/dreamy-sagan-1akdrp`.
- **Viewer v2.3 to v2.4.** Fixed O Level folder and file names (for example `Accounts (7707)`, `qp_01` for Pakistan Studies and Urdu), removed wrong inserts, added practical variants and A Level Maths Paper 2. Removed the Caveat note line at your request. Share links switched from `year=` to `series=` because WordPress 404s any address with `year=`. Added a "Share this paper" button and `marks=show`.
- **Real file list.** `check-files.py` checked Backblaze directly and wrote the actual file list into the widget. Storage widened to 2010 to 2026: A Level goes back to 2015, O Level starts at 2020. Computer Science 2015 to 2021 files are the old 9608 syllabus and are labelled "(old 9608)". Viewer now holds 8,201 links, 0 wrong.
- **Found live breakage.** Every link 404s on 9 live pages: O Level Pakistan Studies, Islamiyat, Maths D, English Language, Urdu Second Language, Accounting, Business Studies, Computer Science, and A Level Urdu. O Level Biology, Chemistry, Economics and Physics worked but built their lists by script, so Google saw no papers. The live A Level Chemistry page was loading Business (9609) papers with a Business H1.
- **Rebuilt all 25 subject pages** with a shared generator (`Scripts/past-papers-pages/build.py`). You approved the Pakistan Studies page as the template, including the "What is on each paper" table, "Side by side" buttons into the viewer and Sir Kashaan Ali in the band. Each page has every paper in the HTML, a Yoast title, meta and keyphrase in its top comment, CollectionPage, BreadcrumbList and FAQ schema, a teacher-named closing band and a WhatsApp Ref `PP-O-{code}` / `PP-A-{code}`. Paper names, times and marks were read from the papers' cover pages, year by year where syllabuses changed.
- **A Level Business, Economics and Maths** (already live, hand-written copy): only the paper tables were refreshed, using the live code because the repo copies were older. Business keywords and copy are untouched. Maths extended to 2015 to 2026 with Paper 2 and "Old numbering" labels before 2020 (you approved). Business breadcrumb schema added back (you approved).
- **Law:** there is no Law teacher listed, so its band offers A Level classes in general.
- Empty cells on every page say "Not available" (was "Not set").
- **SEO and UX audit:** you asked for a full audit, then interrupted it to fix Chemistry first. Partial findings are in section 5.

## 4. Paste order (take a Cloudways backup first)

1. **Viewer:** re-paste `02 Website/Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html` over the live `/past-paper-viewer/` widget. The live v2.4 only knows papers from 2019 on, so Side by side links to older A Level papers would open an empty viewer.
2. **A Level Chemistry** (`Pages/a-level-chemistry-past-papers-elementor-widget.html`): the live page shows Business papers.
3. **The 9 broken pages** (every link 404 now): O Level Pakistan Studies, Islamiyat, Maths D, English Language, Urdu Second Language, Accounting, Business Studies, Computer Science, A Level Urdu.
4. **A Level Business, Economics, Maths:** paste over their live widgets.
5. **The rest:** the other 8 A Level pages (Accounting, Biology, Computer Science, Literature in English, Law, Physics, Psychology, Sociology), then O Level Biology, Chemistry, Economics, Physics.

All page files are in `02 Website/Pages/` as `{o|a}-level-{subject}-past-papers-elementor-widget.html`. For each page, set the Yoast title, meta and keyphrase from the comment at the top of its file. The live addresses stay the same; the full list with titles and Ref codes is in `Planning/SITE-REGISTER.md`.

Test totals from the chats: every PDF link returned 200 and every Side by side link loaded the right paper (9 broken pages: 871 and 397; O Level sciences and Economics: 691 and 331; A Level Business, Economics, Maths: 1,822 and 884; other 9 A Level pages: 4,783 and 2,666). Layout checks passed on laptop and phone.

## 5. Open items

**Admin, for you**
- Add `PPV-END` and the 25 `PP-O-` / `PP-A-` Ref codes to the Lead Tracker Ref list.
- GA4 custom dimensions (Admin, Custom definitions): `level`, `subject`, `series`, `paper`, `entry`, `method`, `type`, `file`.
- Viewer Yoast: canonical set to the clean `https://www.sjacademy.pk/past-paper-viewer/`. Focus keyphrase stays empty until keyword research.
- Upload the 16 missing mark schemes (list in `Tools/Past Paper Viewer/BRIEF.md`, "Mark schemes to upload"), plus May/June 2026 papers where Cambridge has published them. Then run `check-files.py`, then `build.py` and `refresh-tables.py`, and re-paste.

**Site fixes found (partial audit, not yet acted on)**
- `/o-level-past-papers/` carries a second canonical pointing to `sjacademy.com`. Remove it in Elementor.
- `/a-level-mathematics-past-papers/` and `/o-level-math-past-papers/` still load and are in the sitemap. `/a-level-business-past-papers/` redirects but is still in the sitemap. 301 them to the subject pages and drop them from the sitemap.
- Every past papers page has two breadcrumb schemas (Yoast's and the widget's) with different names. Keep one. This includes the one added to Business.
- The invalid "TutoringService" schema is on every page.
- Live Yoast descriptions promise "examiner reports", which the pages do not offer.
- The Pakistan Studies and Islamiyat tuition pages link to the old `/past-papers/` tool, not their subject pages.
- The O Level tuition page lists Business as "7081". The code is 7115.
- The science pages are about 250KB each (700 to 850 files). They work but are heavy on mobile data. Handle this with the speed items.

**Next build work**
- Finish the SEO and UX audit as a full report with a 30/60/90-day plan (your prompt is in chat 2, 31 October 07:46).
- Rebuild the directories: `/o-level-past-papers/`, `/a-level-past-papers/`, `/past-papers/`.
- Internal links: "View with mark scheme" deep links from the tuition pages, directories, homepage resources and the mark scheme blog post. Plus an Instagram "Tool Drop" post.
- Viewer checks on the live page: iPad Safari (if PDFs show only page 1, raise the phone breakpoint to 1024px for touch), and confirm GA4 events arrive.
- Two weeks after pages go live: Search Console and GA4 check.
- Merge into `main`: ask before opening a pull request.

**Facts still to confirm**
- Maths Paper 3 insert: the live page lists none, an older config lists one. The viewer follows the live page.
- The band says "Book a free demo class". FACTS says the demo covers every class except lab practicals; this is not qualified on the science pages.
- "AS is Papers 1 and 2 (1 to 3 for the sciences)" on the A Level pages follows Cambridge's paper titles. Confirm against each syllabus if challenged.
- Teacher names in the bands come from the live tuition pages. No affiliations stated.

**Housekeeping**
- `Tools/Past Paper Viewer/__pycache__/check-files.cpython-313.pyc` was committed by mistake. Delete it and add `__pycache__/` to `.gitignore`.

## 6. Key files

| File | What it is |
|---|---|
| `02 Website/Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html` | The viewer widget (paste this). Yoast, deep link format and GA4 events in its top comment |
| `02 Website/Tools/Past Paper Viewer/check-files.py` | Checks Backblaze and writes the real file list into the widget and `files-report.md`. Needs `sjacademy.pk` and `f006.backblazeb2.com` reachable. Use `--workers 3` if the host refuses requests |
| `02 Website/Tools/Past Paper Viewer/BRIEF.md` | Viewer brief, audit record, mark schemes to upload |
| `02 Website/Tools/Past Paper Viewer/tests/` | Playwright tests (`viewer-test.js`, `list-links.js`) |
| `02 Website/Scripts/past-papers-pages/build.py`, `subjects.py` | Generator and checked copy and facts for the 22 generated pages |
| `02 Website/Scripts/past-papers-pages/refresh-tables.py` | Refreshes only the tables in A Level Business, Economics and Maths |
| `02 Website/Scripts/past-papers-pages/BRIEF.md` | Five-line brief, order, SEO approach and the accuracy record for every page |
| `02 Website/Scripts/past-papers-pages/preview.js`, `check-side-links.js` | Page checks and Side by side link checks |
| `02 Website/Pages/*-past-papers-elementor-widget.html` | The 25 page widgets |
| `02 Website/Planning/SITE-REGISTER.md` | Status, title and Ref per page |
| `02 Website/Planning/HANDOFF-past-paper-viewer-30-oct.md` | Detailed viewer handoff from chat 1 (design, GA4, SEO decisions) |
| `02 Website/START-HERE.md` | Dated log of every change |

Update after new uploads: upload to Backblaze, run `check-files.py`, then `build.py` and `refresh-tables.py`, then re-paste the changed widgets.

## 7. Reference

**Deep links.** `/past-paper-viewer/?level=o-level&subject=biology&series=2025-mj&paper=31&marks=show`. `2025-mj` is May/June, `2025-on` is Oct/Nov. `31` is Paper 3, Variant 1. Any prefix works, utm tags are kept, and the address bar updates as students pick. Never use `year=`, because WordPress returns a 404 for it.

**File host.** `sjacademy.pk/file/Past-papers-storage/...` is a Cloudflare 302 to `f006.backblazeb2.com/file/...` with no CORS header. Cloudflare refuses Python's default user agent, so use a browser user agent for link checks.

**GA4 events.** Viewer: `tool_start`, `tool_complete` (`entry`), `mark_scheme_reveal` (`method`), `insert_view` (`type`), `fullscreen_open`, `paper_unavailable` (`file`), `open_in_new_tab`, `share_click`, `whatsapp_click`, `homepage_click`. Subject pages: `resource_download`, `viewer_click`, `whatsapp_click`. All carry `link_location` and `page_family`.

## 8. How Sunyyan worked in these chats

- Reviews on his phone. Wants professional design, not "AI slip": no yellow label fills, no black borders, no heavy black blocks.
- Says "discuss before you code" when he wants a proposal first. Otherwise, complete and publish-ready deliverables.
- Expected all related pages to be done in one pass. Do not stop at a subset without saying why.
- Protect existing keywords and copy on live pages. Change only what was asked.
- No pushing students to book after a mark scheme reveal.
- SEO must be done properly even without Semrush data.
