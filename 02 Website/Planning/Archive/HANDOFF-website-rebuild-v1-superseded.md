# SJ Academy website rebuild: handoff (2 October 2026)

Paste this into a new chat, or tell the new chat to read `claude/website-rebuild-handoff.md` in the Website Design project.

## Who and what

- Sunyyan Junaid runs SJ Academy (sjacademy.pk), a CAIE O and A Level tuition centre in DHA Phase 7, Karachi, with live online classes. He teaches A Level Business (9609).
- Stack: WordPress, Educrat theme, Elementor with PRO Elements, Yoast, WPForms, WP-Optimize, Flying Scripts, Cloudways, Cloudflare.
- The job: rebuild the site page by page in one design language without losing Google rankings. The site header and footer stay; only page content is rebuilt.

## How he likes to work

- Direct, structured, complete deliverables. Publish-ready first drafts. No long back-and-forth.
- Copy: no em dashes, active voice, no buzzwords, sentence case.
- Humour: dry and sarcastic, never offensive, and it must add value or be relatable (parents especially). He rejects weak jokes; when in doubt, cut the line. A formal humour section for the brand guideline is parked.
- He reviews on his phone inside Elementor and sends screenshots. Expect layout feedback from real devices.

## Files

Local folder: `/Users/sunyyanjunaid/Documents/Website Pages + Design` (connected). SEO folder: `/Users/sunyyanjunaid/Documents/Website SEO` (read only; start with `00_START_HERE/SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md`).

| Page | Local file | Project doc | Wrapper | Status |
|---|---|---|---|---|
| Homepage | `24-homepage-elementor-widget.html` | `claude/homepage-elementor-widget.html` | `#sjh` | Live |
| Fee structure | `27-fee-structure-elementor-widget.html` (v1.3) | `claude/fee-structure-elementor-widget.html` | `#sjf` | Delivered; live status not confirmed |
| Class timetable | `28-class-timetable-elementor-widget.html` | `claude/class-timetable-elementor-widget.html` | `#sjt` | Delivered; not confirmed live |
| A Level Business tuition | `29-a-level-business-tuition-elementor-widget.html` (v1.3) | `claude/a-level-business-tuition-elementor-widget.html` | `#sjb` | In review; latest fixes not yet confirmed by him |
| Brand guidelines v2.0 | `25-SJ-ACADEMY-BRAND-GUIDELINES.md` | `claude/sj-academy-brand-guidelines.md` | | Approved |
| Brand kit (visual) | `26-sj-academy-brand-kit.html` | | | Approved |
| Homepage audit | `13-homepage-ui-ux-seo-audit.md` | `claude/homepage-ui-ux-seo-audit.md` | | Done |

Read the brand guidelines before building any page. They define page families (Enrol, Tool, Resource, Reading, Proof, Event, Info), the signature elements, accent limits, approved facts and banned claims.

## Build rules (every page)

- One Elementor HTML widget per page, in a full-width section with zero padding and no entrance animation. Page layout "Elementor Full Width", Hide Title = Yes.
- Unique wrapper id and class prefix per page. Every CSS selector starts with the wrapper id. Reset theme styles inside it (headings, links, lists, images, `button{all:unset}`, tables).
- Files are plain ASCII: HTML entities in markup, `\XXXX` in CSS, `\uXXXX` in JS and JSON. Check with a non-ASCII grep before delivery. The Write tool can turn `·` into a literal character, so re-check after writing.
- Fonts: Poppins 400/500 and Caveat 600, loaded with `media="print" onload="this.media='all'"` plus a noscript fallback.
- Never write the literal `gtag` in inline scripts (Flying Scripts delays by keyword). Use `window['gt'+'ag']`. Event `whatsapp_click` with `link_location`.
- Do not use `blockquote`, `footer` or pseudo-elements on them: the theme styles them and breaks layouts. Use `div`.
- Give every grid child `min-width:0`. An image inside a grid column forced text off-screen on his phone.
- Anything interactive must look tappable (raised pill buttons, a visible "tap one" prompt). Instructions buried in a paragraph get missed.
- Phone first fold: one-line keyword label, short intro, one primary button. No floating badges on cards.
- Subject pages must not link to the teachers page.
- One H1, with the keyword label (kicker pill) inside it. FAQ as native `details`/`summary` with matching FAQPage JSON-LD.
- Phones get a bottom bar with the two main actions; hide `.joinchat` on phones and `#back-to-top`.

## Fixed links and data

- Registration popup: `#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D`
- WhatsApp: `https://wa.me/923362144454?text=...`. Demo message: "Hi SJ Academy, I would like to book a free demo class for [level] [subject]. My name is "
- Google reviews and map: `https://maps.app.goo.gl/QSrQVThJrZMzJgKF8`
- Timetable sheet (TSV): `https://docs.google.com/spreadsheets/d/e/2PACX-1vRNaIRWzVbWjAz6uXXzEngSykiYmSrY_jeeRCjLgMXf1aF8Zo39EqRCM7s8VuE4RWzf0edXe7UhTCf8/pub?single=true&output=tsv&gid=`
  - May/June 2027: O 674937139, AS 1456859397, A2 1559855613, Lab 1270410396
  - Oct/Nov 2026: O 230541006, AS 526799171, A2 1529699202, Lab 1049078162
  - Shared sessionStorage cache key: `sjh-tt-<gid>`
- Approved facts: 950+ A*s; 4,500+ students taught; rated 5.0 on Google from 226 reviews (never "226+ five-star reviews"); teachers from LUMS, IBA and KGS.
- Never state: a batch size number (say "small batches"), fee figures on marketing pages (link to the fee page), demo classes for lab practicals, unconfirmed frequencies, reviews that are not real word-for-word quotes.
- Fees (fee page only): O Level Rs. 8,500; AS or A2 Rs. 10,500; A Level composite Rs. 20,000 per subject per month; lab practicals Rs. 25,500 one time; admission Rs. 3,500 one time; 10% off for 3 months upfront. Oct/Nov fast-track closed for 2026.

## Testing method

Playwright with `/opt/pw-browsers/chromium` and `NODE_PATH=$(npm root -g)`, inside a "hostile theme" test page that mimics the theme's global styles, at 320, 346, 360, 390, 768 and 1,440px. Check sideways overflow, one H1, tap targets and every interaction. Google Sheets, fonts and site images are unreachable from the sandbox, so mock those routes. None of this replaces his Elementor preview.

## A Level Business page: where it stands

Sections: hero with AS/A2 class card (timings from the sheet), proof strip, three marked answer lines, mark picker on a brown band, teacher section with two photos (classroom shot large, portrait small), Paper 1 to 4 tabs, batch inclusions plus "For parents", three reviews, four resource tiles, nine FAQs, final call to action, phone bottom bar.

Photos used:
- `https://www.sjacademy.pk/wp-content/uploads/2026/05/IMG_7174-1-768x473.jpg` (also `-1024x631`)
- `https://www.sjacademy.pk/wp-content/uploads/2025/07/296167730_10159330125240939_9121453372746153911_n-min-768x521.jpg`

Waiting on him:
- Confirm v1.3 looks right in Elementor (first fold, mark picker, reviews, tick list no longer cut off on the right).
- Check the mark splits (20-mark split 3/2/8/7 and the paper durations, marks and weightings came from the assistant's knowledge, not a verified source).
- Check the three sample answer lines, "over 8 years", and the batch claims (syllabus by February, multiple mocks, lesson recordings).
- Hassan Raza review was left out as it reads like placeholder text. Add back only if real.

Suggested Yoast settings:
- Title: `A Level Business Tuition in Karachi & Online (9609) | SJ Academy`
- Description: `A Level Business (9609) tuition with Sir Sunyyan Junaid. AS and A2 classes at DHA Phase 7, Karachi, and live online. Answer checking, mocks and a free demo.`
- Search data: 291 impressions at position 6.9; top query "best a level business teacher in karachi".

## Open items on other pages

- Timetable: confirm "online" means online only, "Batch 2" means a second batch, and whether to keep the Oct/Nov 2026 switch. Suggested title `SJ Academy Class Timetable - O & A Level Class Schedule in Karachi`.
- Fee page: share image offered (1200x630), unanswered. Confirm no annual fund or security deposit is charged.
- Homepage: real marked 9609 answer to replace the sample; Law teacher; photos for five teachers; O Level Urdu code.
- Parked by him: humour section in the brand guideline; duplicate Meta pixel (PixelYourSite plus a plain pixel block); Core Web Vitals and plugin clean-up.

## Likely next steps

Other subject tuition pages and level pages, using the Business page as the pattern for the Enrol family. Per the guidelines, each new page changes its lead accent, handwriting and circled number so pages look related, not copied.
