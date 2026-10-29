# SJ Academy Homepage Audit: UI, UX, Copy and Ranking Safety

**Page audited:** https://www.sjacademy.pk/
**Audit date:** 2 October 2026
**Perspective:** Design director review before a full homepage redesign and copy rewrite
**Benchmark:** The inside pages in this folder (IBCC calculator, past papers hubs, faculty directory, results wall, fee page, timetable) and `AI-LANDING-PAGE-DESIGN-GUIDE.md`

**How this was audited:** Live HTML crawl (title, meta, headings, schema, links, images), rendered desktop (1440px) and mobile (390px) screenshots, a lab performance run, a link check on all 77 internal links, and a side-by-side read against the inside-page design system.

---

## 1. Executive verdict

The homepage is a themed Educrat template with SJ Academy copy poured into it. The inside pages now look and behave like a product. The homepage still looks like a 2022 tuition-centre site, so the most important page on the domain is the weakest expression of the brand.

Three problems matter more than anything visual:

1. **The page contradicts itself.** The hero promises "1-on-1 attention" and the FAQ says "we do not offer one-on-one tutoring." The meta description says 250+ A*s, the hero stat says 950+ A*s. Faculty is "KGS, IBA & LUMS" in one block and "LUMS, IBA and NED" in the next. A parent who reads carefully stops trusting every number on the page.
2. **The homepage hides SJ Academy's best assets.** No teacher faces, no results wall, no fee signal, no lab practicals section, no free tools (IBCC calculator, past papers, grade strategy tool). Those are exactly the pages you have rebuilt to a high standard, and the homepage barely links to them.
3. **The UX asks for commitment before it earns trust.** Every action leads to the same multi-step registration popup (20 links trigger popup 6023). There is no low-friction WhatsApp-first path in the page body, which conflicts with your own copy rule for cold traffic.

The good news: the page is technically clean enough that a redesign can lift rankings rather than risk them, as long as we protect the elements Google currently relies on (section 8).

---

## 2. Scorecard

These are expert judgments, not user-research measurements.

| Dimension | Score | Summary |
|---|---:|---|
| First impression and clarity | 5/10 | Clear category, generic promise, long hero paragraph |
| Visual design and brand consistency | 4/10 | Template look, heavy type, off-system from inside pages |
| Information architecture | 4/10 | Missing teachers, results, fees, practicals, tools |
| Trust and evidence | 3/10 | Contradictions, unsourced "Top 10" claim, template trust badges |
| Conversion design | 4/10 | One heavy CTA repeated, no WhatsApp in body, vague cards |
| Mobile experience | 4/10 | 13+ screens long, clipped stats, no hero image |
| Accessibility | 3/10 | Zoom disabled, heading order broken, missing alt text |
| Performance | 4/10 | 150 requests, 55 stylesheets, 61 scripts, hero images lazy-loaded |
| On-page SEO foundation | 6/10 | Good title, single H1, canonical, FAQ text, no broken links |
| Structured data and entity signals | 5/10 | Rich but fragmented, incomplete address |

---

## 3. Critical issues (fix in the redesign, no exceptions)

| # | Issue | Evidence | Why it matters |
|---|---|---|---|
| C1 | 1-on-1 contradiction | Hero: "requires focused, 1-on-1 attention". FAQ: "we do not offer one-on-one tutoring service" | Direct credibility break, and Google reads both |
| C2 | A* count contradiction | Meta description and schema: "250+ A*s". Hero stat: "950+ A*s" | Numbers are your strongest proof; inconsistent numbers become your weakest |
| C3 | Faculty claim drift | "KGS, IBA & LUMS" (meta, A Level intro), "LUMS, IBA and NED" (reasons block), "ex-KGS" (about block) | Pick one verified, nameable claim and prove it with faces |
| C4 | Syllabus code error | Footer: O Level Physics **5056** (correct code 5054). Correction, 2 Oct: the nav's O Level Business **7081** is not an error. 7115 becomes 7081 from June 2027, so 7081 is right for new batches and 7115 for historical past papers | Cambridge codes are a credibility signal for this audience; errors look careless |
| C5 | Template trust badges | Hero floating cards "Congrats! Your Admission Completed" and a static image "5.0 Students / Parents Reviews" | These are theme demo artefacts; parents recognise them as decoration, not proof |
| C6 | Zoom disabled | `maximum-scale=1, user-scalable=0` in the viewport tag | WCAG 1.4.4 failure; parents on phones cannot pinch to read |
| C7 | Unsourced ranking claim | H2 "Why is SJ Academy Ranked as a Top 10 Coaching Center in Karachi?" | Ranked by whom? Either cite the source or drop the claim |
| C8 | Above-the-fold images lazy-loaded | All 6 hero collage images (Slider Revolution layer images) carry `loading="lazy"`, `width="0" height="0"` and no alt text | Delays LCP and causes layout shift, the two biggest Core Web Vitals levers for this page |

---

## 4. Section-by-section review

### 4.1 Announcement bar
**What it does:** "LIMITED SEATS. May/June 2027 Admissions: Enrollments are open and filling up fast! SIGN UP NOW"

- The urgency is generic. "Filling up fast" without a date or seat count reads as marketing noise.
- It competes with the header CTA and the hero CTA: three yellow buttons in the first 900px.
- **Recommendation:** Keep the bar, make it specific and useful. Example: "May/June 2027 batches start [date]. Free demo classes this week for Maths, Physics, Chemistry and Business." Link to the timetable, not a form. Make it dismissible.

### 4.2 Header and navigation
- Mega menus are long and mix audiences: students, parents, teachers looking for jobs ("Teacher Registration"), and resource hunters all share one menu.
- "Fees Structure" should read "Fee structure". "Contact" has a dropdown, which is unexpected.
- No "Teachers" or "Results" at the top level, although these are your two strongest decision pages.
- Inside the HTML, H3 tags wrap "Call Us" and the phone number, so the first headings Google sees on the page are H3s before the H1.
- **Recommendation (aligned with your platform audit):** Programs, Teachers, Results, Free Tools, Schedule & Fees, then one primary action. Move teacher jobs to the footer. Turn header contact items into plain text, not headings.

### 4.3 Hero
**Desktop:** Strong yellow underline accents and a large H1, but the layout feels like a theme demo. Decorative circle, plus, star and grey blob shapes add noise. The image collage shows real students (good) but at small sizes with template cards layered on top.

**Mobile:** No image at all. The 75-word paragraph fills the screen. The stats row overflows and clips ("950+ A" is cut off at 390px). The WhatsApp float sits over the stats.

**Copy:** "Helping O & A Level Students Achieve Their A* Dreams!" is category-generic; any academy in Karachi could say it. The paragraph mixes three ideas (1-on-1, small batches, online drills) and keyword phrases ("A Level tutor in Karachi") that read as SEO insertions.

**CTAs:** "Register For Class" (high commitment) and "Contact Us" (vague). No WhatsApp, no demo, no "see schedule".

**Recommendation:**
- One sharp promise, one supporting line under 25 words, a mode pill above the H1 (matching inside pages), the highlighter treatment on the key term.
- Primary CTA: "Book a free demo class". Secondary: "Chat on WhatsApp". Tertiary text link: "See this week's timetable".
- Proof strip directly under CTAs with verified, consistent numbers, each linked to its proof (Google reviews, results wall).
- One real, well-cropped class photo or a teacher-at-board photo, loaded eagerly with `fetchpriority="high"`.

### 4.4 O Level and A Level class cards
- Only 3 of 9 O Level and 3 of 7 A Level subjects appear. **A Level Business (9609), your flagship pilot, is missing.**
- Each card spends its biggest text on "In-Class & Online", which is the same on all six cards. That line is also marked up as an H4, six times.
- "Timing: See Schedule" gives no information; it pushes the work back onto the parent.
- Button labels drift: "Register for Free Demo Class" vs "Join Free Demo Class".
- Six identical yellow buttons in a row reduce the value of each one.
- Cards lack the inside-page treatment (top accent border, hover state, refined weights).
- **Recommendation:** Replace with a compact subject grid: all subjects, grouped O Level / AS / A2 / Practicals, each tile showing code, teacher name and photo, days, and linking to its subject page. One shared CTA for the block. This also strengthens internal linking to subject pages, which supports their rankings.

### 4.5 "Why is SJ Academy ranked as a Top 10 coaching center"
- Large classroom photo with a text block. Good use of a real photo, but it reads as filler because nothing in the copy refers to it.
- Copy is abstract ("we prepare them for life", "values-based learning culture"). No specifics, no names, no numbers.
- Bold keyword phrases ("best tutor academy in Karachi", "A Level in Pakistan") look like keyword stuffing to readers.
- **Recommendation:** Replace with a "How we teach" section showing method as artefacts: an annotated past-paper answer, a marking-scheme breakdown, a practical lab photo. Show, do not claim.

### 4.6 "Reasons why parents and students choose SJ Academy"
- Three generic benefit columns with line icons. Every academy site has this block.
- Small batch size is your real differentiator; the page never states the number.
- **Recommendation:** Merge with 4.5. State concrete facts: maximum batch size, weekly test rhythm, parent update frequency, practical lab equipment.

### 4.7 Testimonials
- Good content, real names, real voice. Weak presentation.
- Carousel with 10 dots: most visitors see one or two reviews only.
- Every reviewer labelled "Student". No subject, grade achieved, year, or school. No parent reviews, although parents are the paying decision maker.
- Two different Google Maps short links for "193+ Reviews" and "See all reviews on Google".
- **Recommendation:** Static grid of 6 curated reviews with subject, series and grade outcome; one parent review highlighted; link to the full results wall. Use one canonical Google Business Profile link everywhere.

### 4.8 Blog
- Shows the latest 3 posts automatically. Today that includes an Apple iPhone post next to exam-day guidance, which dilutes the homepage message for a parent.
- **Recommendation:** Replace with a curated "Free tools and guides" block: IBCC calculator, past papers hub, A Level grade strategy tool, subject combination finder, CAIE date sheet. These are your highest-value SEO assets and the homepage is the strongest internal link source on the site. Keep a smaller "Latest from the blog" row below if needed.

### 4.9 FAQ
- 8 questions, accordion, with matching FAQPage schema. This is valuable content for search and AI answers; keep it.
- Answers are generic ("modern tech", "affordable") and some contradict the hero (C1).
- "Frequently Asked Questions." has a stray full stop.
- Questions written for keywords ("tutor academy near me") instead of the questions parents actually ask: batch size, fee per subject, demo class, online vs in-class, timetable, results, practicals registration as private candidate.
- **Recommendation:** Rewrite to 8 to 10 real parent questions with specific answers (numbers, links). Keep the visible text identical to the schema text.

### 4.10 Footer
- The footer brand paragraph ("The difference between a good grade and an A* is never luck. It is method.") is the best copy on the page. It deserves the hero, not the footer.
- "Website Made by Usama" credit weakens a premium positioning.
- Address in the footer is shortened to "Phase 7, DHA, Karachi" while the header shows the full address. Keep one consistent full address everywhere (NAP consistency for local SEO).
- Footer headings "QUICK LINKS" and "CLASSES" are H2s in the markup.

### 4.11 Hidden popups in the HTML
- The registration popup ships inside the homepage HTML with every price tier (PKR 8,500, 10,500, 15,500, 20,000, 25,500, 30,000 per subject). Google can read this text and may surface it, out of context, in snippets.
- **Recommendation:** Load the popup form on demand, or move registration to a dedicated page and link to it.

---

## 5. Visual system gap: homepage vs inside pages

| Element | Homepage today | Inside-page standard |
|---|---|---|
| Heading font | GT Walsheim Pro at heavy weight, mixed with Poppins | Poppins only, weights 300 to 400 |
| Highlighter | Thin yellow underline | Signature highlighter pen band behind the key term |
| Hero context | Orange "In-Class & Online" text | Mode pill above the H1 |
| Cards | Thin grey border, no accent | 5 to 6px brown top border, orange on hover, 12px radius |
| Primary CTA | Yellow button, black text | Orange conversion button (dark orange for white text contrast) |
| Secondary CTA | Grey pill | Outline or text action |
| WhatsApp | Floating button only | WhatsApp consultation as a designed CTA |
| Decorative shapes | Circles, plus signs, stars, blob, wave | None; real student work and artefacts carry the visual interest |
| Lead capture | Generic popup for everything | Contextual demo card at position 3 or 4, prefilled by subject |

**Decision needed before design:** your design guide caps font weight at 400, while the September platform audit recommends 600 to 700 for headings. The homepage should follow whatever the inside pages actually ship. Confirm which one is current.

---

## 6. Mobile UX

- Page height on a 390px phone: about 11,400px, roughly 13.5 screens. Most of that is stacked cards and long paragraphs.
- Hero image disappears on mobile, so the first screen is text only.
- Stats row clips horizontally.
- 83 tappable elements under 32px tall (mostly menu items and links), below the 44px comfort target.
- Testimonial subheading line height is cramped and lines overlap visually.
- WhatsApp float overlaps content and CTAs in the hero.
- **Recommendation:** Design mobile first. Target 6 to 8 screens. Use a sticky bottom bar on mobile with two actions (Demo, WhatsApp) and remove the floating button to avoid duplicates. Use horizontal scroll rails for subjects and reviews instead of full stacks.

---

## 7. Performance and technical

Lab run from a cloud browser; treat as directional and confirm with PageSpeed Insights field data (CrUX) before and after launch.

| Metric | Desktop | Mobile |
|---|---:|---:|
| Requests | 151 | 136 |
| Stylesheets / scripts | 55 / 61 | 53 / 61 |
| Font files | 10 | 10 |
| LCP (lab) | about 6.5s | about 5.1s |
| CLS (lab, includes scroll) | 0.47 | 0.09 |

Main causes:
- Two font families plus Themify and Font Awesome icon fonts.
- Elementor, Slider Revolution, WPForms, PixelYourSite and theme assets load on the homepage whether used or not.
- Hero images lazy-loaded with no dimensions reserved.
- PNG images where WebP would do (`home2-5-EDITED1.png`, `home2-8.png`, a 158KB blog banner PNG).

Positives worth keeping: single canonical, single H1, `index, follow`, clean robots.txt with sitemap, all 77 internal links return 200, HTTPS with www redirect.

---

## 8. Ranking safety plan: redesign without losing positions

The homepage currently ranks on: a clear title ("The Best O & A Level Coaching Center in Karachi | SJ Academy"), about 1,650 words of main-content text, an FAQ block, strong internal links to every subject page, and a rich schema graph. The redesign must keep these signals and add more.

### 8.1 Before we touch anything (baseline)
1. Export Google Search Console data for the homepage URL: top queries, clicks, impressions, average position (last 16 months and last 3 months).
2. Record current positions for the 15 to 20 queries that drive homepage clicks.
3. Save the current HTML and a full-page screenshot (done in this audit; files can be archived).
4. List external backlinks pointing at the homepage.
5. Check PageSpeed Insights field data for the homepage.

### 8.2 Non-negotiables in the new page
- **Same URL**, no redirects, same canonical.
- **Title tag** stays on the same topic. Refine wording only after reviewing query data.
- **One H1** that still names O & A Level and Karachi (or places Karachi in the first supporting line).
- **Equal or more indexable text** in the main content (target 1,600 to 2,000 words), written for parents, not keyword density.
- **Keep the FAQ** as visible HTML (not loaded by JavaScript), rewritten with specifics, with schema text matching exactly.
- **Keep or increase internal links** to every subject page, practicals, fee page, teachers, results and free tools, using descriptive anchor text.
- **Do not let the homepage compete with** `/o-level-tuition-center-karachi/` and `/a-level-tuition-center-karachi/`. The homepage owns the brand and the broad "O and A Level academy in Karachi" intent; the level pages own the level-specific queries. The homepage links down to them with matching anchors.

### 8.3 Upgrades that should lift rankings
- **Core Web Vitals:** eager hero image with `fetchpriority="high"`, reserved image dimensions, one font family, no unused plugin assets on the homepage, popup form loaded on demand. Target LCP under 2.5s on mobile field data.
- **Heading hierarchy:** H1 once, H2 per section, H3 for items inside sections. No headings in the header or footer.
- **Alt text** on every meaningful image, describing the scene (e.g. "A Level Physics students doing a practical at SJ Academy, DHA Phase 7").
- **Accessibility:** allow zoom, visible focus states, 44px tap targets, sufficient contrast for white text on orange.
- **Entity and schema clean-up:** merge the three organisation entities (Yoast Organization, TutoringService, EducationalOrganization) into one connected graph with `@id` references; add the full street address (Plot 29C, Lane No. 5, Seher Commercial Area, DHA Phase 7, Karachi 75500), geo coordinates, opening hours, and `sameAs` links only to external profiles (remove the self-link). Match Google Business Profile exactly.
- **E-E-A-T:** named teachers with photos, qualifications and subjects; dated, verifiable results; a "how we teach" section built from real artefacts. These also make the page more citable by AI search.
- **Fix all contradictions** (C1 to C4) so Google and AI assistants extract one consistent set of facts.
- **Social meta:** set `og:title`, `og:description` and `twitter:title` (currently "Home") to match the new positioning, with a designed 1200 x 630 share image.

### 8.4 Launch process
1. Build on staging with `noindex`.
2. QA checklist: headings, schema validation (Rich Results Test), links, mobile, Lighthouse.
3. Publish, clear all caches (WP-Optimize, Cloudflare), request indexing in Search Console.
4. Monitor homepage queries weekly for 6 weeks. Small fluctuations in weeks 1 to 2 are normal.
5. Keep the old Elementor template saved as a rollback.

---

## 9. Proposed homepage structure for the redesign

1. **Announcement bar:** specific batch date and demo offer.
2. **Hero:** mode pill, H1 with highlighter, one-line method promise, Demo + WhatsApp CTAs, verified proof strip, real photo.
3. **Proof band:** Google rating (live link), A* count with series and year, students taught, linked to the results wall.
4. **Choose your level:** O Level, AS, A2, Lab practicals as four entry cards, each linking to its hub.
5. **Subjects grid:** every subject with code, teacher, days, link to subject page.
6. **Meet the teachers:** 4 to 6 faces, qualifications, subjects, link to faculty directory.
7. **How we teach:** method shown through real artefacts (annotated answers, practicals, weekly tests), with the "never luck, it is method" line.
8. **Results:** distinctions highlights by subject and series, link to the full wall.
9. **Reviews:** static grid of student and parent reviews with subject and outcome.
10. **Free tools and guides:** IBCC calculator, past papers, grade strategy tool, subject combinations, date sheet.
11. **Schedule and fees snapshot:** "from PKR X per subject per month" with a link to the fee page and timetable.
12. **Visit us:** full address, map, timings, phone, WhatsApp.
13. **FAQ:** 8 to 10 real parent questions with specific answers.
14. **Final CTA:** demo class with subject preselect, WhatsApp alternative.

---

## 10. What I need from you before design starts

1. The verified numbers: total A*s (and since which year), students taught, Google rating and review count, maximum batch size.
2. The one faculty claim you can stand behind publicly (and which teachers it covers).
3. Search Console access or an export of homepage queries for the baseline.
4. Confirmation of the type-weight rule (400 max vs 600 to 700 headings).
5. Whether the homepage stays in Elementor or becomes a scoped custom HTML build like the inside pages.
