# Handoff: past paper and mark scheme viewer

Written 30 October 2026. Read `CLAUDE.md`, then `02 Website/START-HERE.md`, then this file.

## 1. State in one paragraph

The viewer is built and tested in a browser but is NOT live. It is one Elementor HTML widget, plain JavaScript, no libraries. It sits on the branch `claude/caie-past-papers-viewer-3plf1s` of `sj-building-byte/sjacademy`. That branch is NOT merged into `main` and no pull request exists. The planned page address is `/past-paper-viewer/`. Nothing has been pasted into WordPress yet.

## 2. Files

| File | What it is |
|---|---|
| `02 Website/Tools/Past Paper Viewer/past-paper-viewer-elementor-widget.html` | The widget. The only file to paste. About 580 lines, no blank lines inside it (blank lines can make WordPress add stray paragraphs), ASCII only. Yoast title, meta, canonical, deep link format and GA4 events are in the comment at the top |
| `02 Website/START-HERE.md` | Session log for the viewer (updates dated 29 October 2026) |
| `02 Website/Planning/SITE-REGISTER.md` | New row for `/past-paper-viewer/` in the Tool family (count now 9) |

To see it on GitHub, switch the branch dropdown from `main` to `claude/caie-past-papers-viewer-3plf1s`.

## 3. What the tool does

- Header: centred H1 "Past Paper & Mark Scheme Viewer" with the yellow highlighter on the lower half, a short subheading ("Open any Cambridge O and A Level past paper next to its mark scheme. Free, no sign-up."), and the Caveat note in `#B54200`: "Read the command word before you look at the answer."
- Four cascading dropdowns: Level, Subject, Year (shown as "2024 May/June"), Paper (shown as "Paper 3, Variant 2").
- Data: A Level (13 subjects, 3 variants) and O Level (12 subjects, 2 variants), 2020 to 2025, May/June and Oct/Nov. File links are built from `https://sjacademy.pk/file/Past-papers-storage/{A+Level|O+Level}/{Subject+%28code%29}/{May+June|October+November}+{year}/{code}_{s|w}{yy}_{qp|ms|in|ci}_{paper}{variant}.pdf`. Subject settings come from the old past papers tool, the live Business and Maths pages, and the O Level hub files in `02 Website/SEO/01_Website_Pages/Past_Papers/`. `BASE` and `LEVELS` are at the top of the script.
- Desktop and tablet (768px and up): paper on the left, mark scheme on the right, in iframes.
  - Question paper header: "Insert", "Confidential" (sciences) and "Back to Paper" buttons.
  - Mark scheme header: a segmented toggle, "Don't cheat | Learn". Selected mode is bold and dark, the other is greyed, no borders.
  - Locked state: the mark scheme is blurred behind a frosted cover with a white card. Heading "Your answer first." Text "Write it out, then check it. A mark scheme feels easy to follow until you have to produce one yourself." Button "I've written my answer. Show the marks." (white on `#CC4A00`). It locks again on every new paper. Frosted glass is an agreed exception to the brand book's "no glass" rule, for this page only.
  - A Full screen button appears above the panes once a paper is loaded. It uses the browser Fullscreen API with a fixed full-window fallback. In full screen the title and the closing band are hidden. Esc exits.
- Phones (under 768px): no iframes. Each view shows an "Open ... in new tab" button. A sticky bottom bar switches Paper, Insert, Confidential and Mark scheme. The mark scheme stays locked until revealed.
- Missing files: before loading a PDF the page sends a background HEAD request. A 404 shows "This question paper isn't available. Try a different variant or year." with a "Choose another paper" button, instead of the host's raw JSON. If the host blocks the request (CORS), the viewer falls back to loading the frame as before and the old 404 text can appear.
- Deep links: `?level=o-level&subject=biology&year=2025-mj&paper=31` (2025-mj is May/June 2025, 2025-on is Oct/Nov 2025, 31 is Paper 3 Variant 1). Any prefix works, utm tags are kept, and the address bar updates as the student picks.
- Closing yellow band: heading "Know the content but still losing marks?", a line about in class at DHA Phase 7 and live online, past-paper practice marked to the mark scheme, feedback on lost marks, free demo class. Two buttons: "Message us on WhatsApp" and "Explore SJ Academy" (homepage, same tab).
- WhatsApp message follows the other pages: "I'd like to book a free demo class.", then Level and Subject once chosen, a Mode line, `(Ref: PPV-END)`, "My name is ". `PPV-END` is a new Ref code.

## 4. GA4 events

Same style as the other pages (`link_location`, `page_family` = Tool). Events: `tool_start`, `tool_complete` (param `entry` = manual or link), `mark_scheme_reveal` (param `method` = button or toggle), `insert_view` (param `type`), `fullscreen_open`, `paper_unavailable` (param `file`, shows broken or missing files), `open_in_new_tab` (phones), `whatsapp_click`, `homepage_click`. Most events also carry `level`, `subject`, `series`, `paper`.

To see these in GA4 reports, register `level`, `subject`, `series`, `paper`, `entry`, `method`, `type` and `file` as custom dimensions (Admin, Custom definitions). `instagram_click` is no longer used. `homepage_click` is a new event name.

## 5. SEO decisions

- Address: `/past-paper-viewer/`. Family: Tool.
- Yoast title: `Past Paper & Mark Scheme Viewer | O and A Level | SJ Academy`
- Yoast meta: `View Cambridge O and A Level past papers and mark schemes side by side. Try the question first, then check the marks. Free, no sign-up.`
- Canonical: the clean address `https://www.sjacademy.pk/past-paper-viewer/`, so deep-link versions are not indexed on their own.
- Focus keyphrase: NOT set. Keyword research was postponed by Sunyyan. Candidate phrases: past paper and mark scheme viewer, past papers with mark scheme side by side, cambridge past papers viewer, view past paper and mark scheme online. Do not target the head terms ("a level business past papers" and so on). The 25 subject hub pages own those.
- Sunyyan chose a short subheading only, no long wrapper content, FAQs or subject chips. Elementor setup: Full Width, Hide Title = Yes, one HTML widget, zero padding, no entrance animation.

## 6. Open items, in order

1. Create the page `/past-paper-viewer/` as a draft, paste the widget, and test: PDFs show inside the frames, a deep link, a missing-file case (for example O Level Biology Paper 6 in a series that lacks it), full screen, the toggle, and a phone check. Take a Cloudways backup first.
2. Frames and 404s: the live file host is untested. If the panes stay blank, a frame-blocking header may be the cause. If the old JSON 404 text still appears, ask for `Access-Control-Allow-Origin: https://www.sjacademy.pk` on the `/file/` path (Cloudflare or the WordPress file plugin) so the missing-file check can read the status.
3. Tap a few links per subject. None of the links have been tested from the sandbox because it cannot reach `sjacademy.pk`.
4. Check iPad Safari. It gets the desktop layout. If a PDF only shows page 1 there, raise the phone breakpoint to 1024px for touch devices.
5. Set Yoast title, meta and canonical. Leave the keyphrase until the research is done.
6. Add `PPV-END` to the lead tracker Ref list. Register the GA4 custom dimensions.
7. Internal links so students can find it: "View with mark scheme" links (using deep links) from the 25 subject hub pages, the A Level and O Level past papers directories, the homepage resources, the tuition pages and the "how to use a mark scheme" blog post. Also an Instagram "Tool Drop" post and story link sticker.
8. Merge: ask Sunyyan before opening a pull request into `main`.
9. After two weeks live, check Search Console and GA4 events, as planned for the schools tool.

## 7. Known facts and caveats

- Maths Paper 3: the live Maths page lists no insert, but the older hub config lists one. The viewer follows the live page (no insert). Confirm which is right.
- May/June 2026 is not in the data (the old tool stopped at 2025).
- Copy check against `00 Start Here/FACTS.md`: the band says "Book a free demo class". FACTS says the free demo covers every class except lab practicals. Not qualified in the band yet.
- Theme button styles (the site's Elementor and theme CSS) turned clicked buttons black and added black outlines. The toggle is hardened with `!important` rules and `.sjpv button:focus:not(:focus-visible)` is reset. If similar black fills show on other buttons on the live page, apply the same hardening to those classes.
- Preview sites such as Code Beautify add their own sticky ad bar at the bottom. That is not part of the widget. Preview on the draft page instead.
- The test scripts (Playwright) lived in a temporary folder and are not saved in the repo.

## 8. Sunyyan's preferences seen in this session

Review is on a phone. Design should look professional, not "AI slip": no yellow label fills, no black borders, no heavy black blocks. He wants discussion before code when he says so. Complete, publish-ready deliverables, one instruction at a time. No em dashes. No pushing students after a mark scheme reveal (he removed an optional "book a demo" line for that reason).
