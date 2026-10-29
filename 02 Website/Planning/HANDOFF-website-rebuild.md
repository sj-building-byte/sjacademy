> **Paths updated 12 October 2026** after the move into `Documents/SJ Academy`. Live homepage widget: `02 Website/Pages/homepage-elementor-widget.html` (v3.0, confirmed live 16 October 2026). v1.5 is in `Archive/Old widget versions/`.

# SJ Academy website rebuild: start here (updated 8 October 2026)

Paste this into a new chat, or tell the new chat to read `claude/website-rebuild-handoff.md` in the Website Design project. This version replaces the handoff written earlier the same day, which described per-page CSS. That method is retired for new pages.

## Who and what

- Sunyyan Junaid runs SJ Academy (sjacademy.pk), a CAIE O and A Level tuition centre in DHA Phase 7, Karachi, with live online classes. He teaches A Level Business (9609).
- Stack: WordPress, Educrat theme, Elementor with PRO Elements, Yoast, WPForms, WP-Optimize, Flying Scripts, Cloudways, Cloudflare.
- The job: rebuild the site page by page in one design language without losing Google rankings, and turn it into a resource students and parents return to. The site header and footer stay; only page content is rebuilt.

## How he likes to work

- Direct, structured, complete deliverables. Publish-ready first drafts.
- Ask before assuming. He was unhappy when rules (no emoji, no exclamation marks) were set without asking him. Offer an open "what else do you want?" as well as specific questions.
- During technical setup: one instruction and the next step, no explanations.
- He reviews on his phone and sends screenshots. Expect layout feedback from real devices.

## Read these before doing anything

| File (local folder) | Project doc | What it is |
|---|---|---|
| `01 Brand/SJ-ACADEMY-WEB-PLAYBOOK.md` | `claude/sj-academy-brand-guidelines.md` | Design system, v3.2. Colour, type, tokens, page families, elements, components, states, accessibility, consent, facts register, build rules, governance |
| `01 Brand/sj-brand.css` and `sj-brand.min.css` | `claude/sj-brand.css` | Shared stylesheet, v3.1.1. Source and the minified copy that is pasted into WordPress |
| `01 Brand/sj-academy-brand-kit-v3.html` | `claude/sj-academy-brand-kit-v3.html` | Every element and component, live. Copy markup from here |
| `02 Website/Scripts/sj-page-script.js` | `claude/sj-page-script.js` | Standard page script: tabs, phone bottom bar, tap-to-load video, click tracking |
| `01 Brand/SJ-ACADEMY-LANDING-PAGE-COPY-GUIDELINES.md` | `claude/sj-academy-landing-page-copy-guidelines.md` | Landing page copy, v1.2. **Use for every Enrol and Event page** (homepage, level and subject pages, events): section formula, headline patterns, proof ladder, objections, fees and WhatsApp wording, AI prompt block, checklist. Built on the blog voice guide |
| `01 Brand/SJ-ACADEMY-BLOG-VOICE-GUIDELINES.md` | `claude/sj-academy-blog-voice-guidelines.md` | Blog voice, v1.3, built on his own writing. Includes a paste-ready prompt block |
| `01 Brand/sj-academy-voice-tone-guide.html` | `claude/sj-academy-voice-tone-guide.html` | Visual voice and tone guide, linked from the brand kit |
| `01 Brand/sj-academy-landing-copy-guide.html` | `claude/sj-academy-landing-copy-guide.html` | Visual landing page copy guide, linked from the brand kit and the voice guide |
| `02 Website/Planning/SITE-REGISTER.md` and `site-register.csv` | `claude/site-register.md` | Every live page and post, with family, status, build order and overlaps to resolve |
| `02 Website/Pages/` | `claude/*-elementor-widget.html` | The four built pages |
| `01 Brand/Logos/SVG/` | | 13 clean logo SVGs exported from the Illustrator master |

The local folder was reorganised into numbered subfolders on 2 October. Old file names with number prefixes (`31-`, `32-` and so on) no longer exist. The folder's `README.md` and `02 Website/Planning/AI-LANDING-PAGE-DESIGN-GUIDE.md` predate the current system (they say maximum font weight 400) and are superseded by the brand guidelines.

Local folder: `/Users/sunyyanjunaid/Documents/SJ Academy`. SEO folder (not always connected): `/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/SEO`, start with `00_START_HERE/SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md`.

## State of the site

- **The shared stylesheet is live.** `sj-brand.css` is pasted at the end of Appearance > Customize > Additional CSS, after the site's older custom CSS. Confirmed on 2 October: existing pages unchanged, and the brand kit renders correctly in an Elementor draft ("Brand kit test", draft only) in his phone preview: fonts, signature elements, stamps, ticket, pinned cards, tabs and the bottom bar.
- Not yet confirmed by screenshot on that test page: form fields, the stacking table, the FAQ. He reported that everything looked good.
- **Live pages, checked 8 October:** 10 rebuilt pages are live. On the shared stylesheet: A Level, O Level, A Level Maths, A Level Business (v2.1), and the Business, Economics and Maths past papers pages. Still on their own CSS: homepage (`#sjh`), fees (`#sjf`), timetable (`#sjt`). Section 9 of the site register lists each page's keyword targets and live title.
- **A Level Business page is live on v2.1 (8 October),** on the shared stylesheet and the first page written to the landing page copy guidelines. Confirmed live by fetching the page directly. Use it as the template for the other subject pages.
- **Live on 4 October:** stylesheet 3.1.1 is pasted in Additional CSS below the site's older custom CSS, and all four built pages were re-pasted with the new heading weights. He checked them on his phone and reported they look good. The timetable data cache now expires after 10 minutes on the timetable, homepage and A Level Business pages. Not independently verified: the live address `/a-level-business-tuition/` was still returning an older headline ("Secure A* in A Level Business with SJ Academy") when read on 4 October, so confirm which page holds the new Business widget. When replacing the stylesheet, select only from the `/*! sj-brand.css` line downward; the older CSS above it was wiped once by selecting everything.

## Build rules for new pages

- One Elementor HTML widget per page, in a full-width section with zero padding and no entrance animation. Page layout "Elementor Full Width", Hide Title = Yes.
- Wrapper: `<div id="sj" class="sj-p-[page-name]" data-family="[family]">`. The shared stylesheet does the rest.
- Page-only CSS in the widget: under 40 lines, every selector starting `#sj.sj-p-[page-name]`. Never restyle a shared class. If a pattern is needed twice, it goes into the stylesheet with a version bump and a change log entry in the brand guidelines.
- Changing the stylesheet means: edit `01 Brand/sj-brand.css`, rebuild the minified copy, bump the version in the first line, re-paste over the old block in Additional CSS, purge WP-Optimize, Cloudways and Cloudflare.
- Fonts: the three link lines in section 5 of the brand guidelines, once per widget.
- Standard script: copy `02 Website/Scripts/sj-page-script.js` unchanged into the widget.
- Files are plain ASCII: HTML entities in markup, `\XXXX` in CSS, `\uXXXX` in scripts. Check with a non-ASCII grep before delivery.
- Never write the literal `gtag` in inline scripts (Flying Scripts delays by keyword). The standard script already uses `window['gt'+'ag']`.
- Do not use `blockquote` or `footer` tags; the theme styles them.
- The site's older Additional CSS has `.entry-content a` rules (blue, weight 600, underline, pink hover). The stylesheet resets these inside `#sj`.
- Phones: hide `.joinchat` and `#back-to-top` in the page CSS when the bottom bar is used.
- One H1, with the kicker pill inside it when it carries the keyword. FAQ as native `details` and `summary` with matching FAQPage data.
- Subject pages must not link to the teachers page.
- **Addresses never change without a 301 redirect.** See the site register.

## Decisions made on 8 October

- **Landing page copy guidelines adopted** for Enrol and Event pages. The blog voice stays the base; landing pages turn humour down and lead with the reader's situation, specific proof and the first-call questions.
- **Fees:** Enrol pages show the monthly "from" figure, linked to the fee page.
- **Class size:** never a number. Show attention as routine (written answers in class, every answer marked).
- **Parent updates:** teachers tell parents when a child falls behind, and parents can ask any time. No scheduled reports promised.
- **Doubt support outside class:** not promised.
- **Hero actions:** one button, "Book a free demo on WhatsApp", with "Register for a class" as a text link under it (form fills still matter).
- **Sir Sunyyan:** 8+ years of business experience (not teaching). At least one full mock per batch. A Friday past papers class is planned.

## Decisions made on 2 and 3 October

- **Heading weights (3 October):** H1 600, H2 500, tight letter spacing and line height. Paragraph colours stay as they were; he rejected a grey lead paragraph. He found weight 400 headlines too thin and chose this after comparing three options. The old "never above 500" rule is gone; 600 is for H1 only.
- Shared site-wide stylesheet for new pages; existing four pages migrate later.
- Site language: English only. Everyday Pakistani English words (chai, beta, rishta) are allowed in blog humour; no Roman Urdu sentences.
- Consent for student photos, names and results has been verbal. From now on written consent, first name plus initial by default. Wording is in the brand guidelines.
- Logo: horizontal on-light version is the default. Rules and files in section 3 of the brand guidelines.
- Blog voice: verdict first, first-person reasoning, self-mocking, exaggerated, never talking down. Humour is general and relatable. **No named place, organisation or person is ever the target of a joke**, including Cambridge and schools. Gen Z aware, not fluent. Emoji allowed where they add value. Karachi and Pakistan flavour welcome as shared situations, not stereotypes.
- BuzzFeed-style entertainment posts: students only, one for every five guides.

## Fixed links and data

- Registration popup: `#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D`
- WhatsApp: `https://wa.me/923362144454?text=...`. Demo message: "Hi SJ Academy, I would like to book a free demo class for [level] [subject]. My name is "
- Google reviews and map: `https://maps.app.goo.gl/QSrQVThJrZMzJgKF8`
- Timetable sheet (TSV): `https://docs.google.com/spreadsheets/d/e/2PACX-1vRNaIRWzVbWjAz6uXXzEngSykiYmSrY_jeeRCjLgMXf1aF8Zo39EqRCM7s8VuE4RWzf0edXe7UhTCf8/pub?single=true&output=tsv&gid=`
  - May/June 2027: O 674937139, AS 1456859397, A2 1559855613, Lab 1270410396
  - Oct/Nov 2026: O 230541006, AS 526799171, A2 1529699202, Lab 1049078162
  - Shared sessionStorage cache key: `sjh-tt-<gid>`
- Approved facts: 950+ A*s; 4,500+ students taught; rated 5.0 on Google from 226 reviews (never "226+ five-star reviews"); teachers from LUMS, IBA and KGS. These were carried from v2.0 and have not been re-confirmed.
- Never state: a batch size number (say "small batches"), fee figures on marketing pages (link to the fee page), demo classes for lab practicals, unconfirmed frequencies, reviews that are not real word-for-word quotes.
- Fees (fee page only): O Level Rs. 8,500; AS or A2 Rs. 10,500; A Level composite Rs. 20,000 per subject per month; lab practicals Rs. 25,500 one time; admission Rs. 3,500 one time; 10% off for 3 months upfront. Oct/Nov fast-track closed for 2026.

## Testing method

Playwright with `/opt/pw-browsers/chromium` and `NODE_PATH=$(npm root -g)` at 320, 360, 390, 768 and 1,440px. Check sideways overflow, one H1, tap targets and every interaction. Google Sheets, fonts and site images are unreachable from the sandbox, so mock those routes. For widgets that depend on the shared stylesheet, inline `sj-brand.min.css` into the test page. None of this replaces his Elementor preview on a phone.

## What comes next, in order

1. Resolve the overlaps in section 4 of the site register (two Maths pages, two Economics pages, four practicals pages, three ebook pages).
2. Build the first page on the shared stylesheet. Recommended: an Enrol subject tuition template based on the A Level Business page, since 17 subject pages will use it.
3. Decide how the new design reaches blog posts (a blog template, or theme design with the new voice only), then build the blog post template and the entertainment-post template.
4. Author profiles for teacher bylines.
5. Editorial plan at one entertainment post per five guides.
6. Migrate the four existing pages to the shared stylesheet.

## Open items

- **Brand guidelines:** facts register to confirm; past papers decision (host Cambridge files or link out); page details for the four built pages.
- **Blog voice:** sample passages need his sign-off; confirm British spelling, no mild swearing, and the cap of two exclamation marks per post; decide who checks slang.
- **Existing blog:** ten named school reviews and two posts addressed to Cambridge predate the "no named targets" rule and should be reviewed.
- **A Level Business page:** v2.1 is live. Set the Yoast SEO title, meta description and social title (title: "A Level Business tuition in Karachi & online | SJ Academy"). Add the Friday past papers class to the page and the timetable sheet when it starts. Check Search Console for this page around 5 November. Collect a Business review that names a grade or a before and after.
- **Timetable:** confirm "online" means online only and "Batch 2" means a second batch; whether to keep the Oct/Nov 2026 switch.
- **Fee page:** confirm no annual fund or security deposit is charged; share image offered, unanswered.
- **Homepage:** real marked 9609 answer to replace the sample; Law teacher; photos for five teachers; O Level Urdu code.
- **Parked:** duplicate Meta pixel; Core Web Vitals and plugin clean-up; social and share-image templates; self-hosted fonts.
- **Test page:** "Brand kit test" is a draft and should stay unpublished or be deleted.
