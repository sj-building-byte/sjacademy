# SJ Academy style guide: deep review

**Date:** 3 October 2026
**Reviewed:** brand guidelines 3.1, shared stylesheet 3.1.1, brand kit, page script, blog voice guide 1.3, voice and tone page, start-here file, site register, the four built page widgets, and the older documents still in the folder.
**Lens:** a CEO and CMO investing for several years, with the goal that sjacademy.pk becomes the hub for O Level and A Level students in Pakistan.
**Nothing was changed.** This is a list of what to decide, so the guide does not have to be reopened later.

**How to read it**

- **Part A** is structural. Getting these wrong means redoing many pages.
- **Part B** is marketing and strategy. These decide whether the site becomes a hub or stays a set of good pages.
- **Part C** is detail. Cheap to settle now, irritating to discover later.
- **Part D** is what is sound and should not be reopened.
- **Part E** is the list of decisions, with a recommendation for each.

**What was checked and what is judgement**

- Checked directly: file sizes, script and structured data inside each widget, font weights and browser features in the stylesheet, the wording of every guide, the contents of the older documents.
- From knowledge, not tested on this site: how WordPress stores Additional CSS, browser support for specific CSS features, how Yoast outputs structured data.
- From the owner's own concept documents, not checked on the live site: which tools sit behind forms.

---

## Part A. Structural decisions

### A1. The blog is outside the design system

Every rule in the stylesheet starts with `#sj`. Blog posts are WordPress posts shown through the theme's post template, so none of it reaches them. That leaves 74 posts, the blog index, and every future guide and entertainment post looking like the theme, not the brand. The voice guide now describes a blog whose look was never designed.

For a site meant to be a source of knowledge, this is the largest gap. The article is the main product.

**Recommendation:** one blog post template, built once in Elementor's theme builder, that wraps post content in the `#sj` wrapper with the long-form reading styles. Every existing and future post inherits it. Design it before publishing in the new voice, not after. The older link rule in Additional CSS (blue, bold, pink on hover) gets retired at the same time.

### A2. There is no subject architecture

The register shows each subject scattered across unrelated addresses. For A Level Business alone: a tuition page, a past papers page, an older past papers page, a definitions page, a solved papers page, a quiz and at least three blog posts. Nothing in the guide says which page is the centre, or how they link.

This matters more than any visual decision. Search engines and AI assistants reward a clear hub with supporting pages, and students need one place to start.

**Recommendation:** hub and spoke, per subject, with no address changes.

| Page | Job | Reader intent |
|---|---|---|
| Subject hub (the existing `/[level]-past-papers/[subject]/` page) | The centre: papers, definitions, model answers, tools, guides, exam dates | "I need something for this subject" |
| Tuition page | Enrolment | "I need a teacher" |
| Everything else for that subject | Spokes | A specific need |

Rules to add: every spoke links up to its hub in the first screen; the hub links to every spoke; hub and tuition page link to each other once. Decide this before building the subject tuition template or the past papers template, because it changes what goes on both.

### A3. Repeated things are still copied into every page

The shared stylesheet fixed duplicated CSS. The same problem remains for three other things.

| Repeated item | Today | Cost at 100 pages |
|---|---|---|
| Page script | Pasted into every widget. The four built pages carry between 3.5KB and 13.5KB of script each | A bug fix or a new tracking event means editing every page |
| Facts (950+, 4,500+, 226 reviews, the WhatsApp number) | Typed into each page | One changed number means a hunt across the site. The register exists, but nothing enforces it |
| Repeated blocks (bottom bar, final call-to-action band, "for parents" block, author note) | Pasted per page | A wording change means every page |

**Recommendation:** load the standard script once for the whole site, the same way as the stylesheet. Serve the facts through WordPress shortcodes, so a number is changed in one place and stays in the page HTML for search. Keep repeated blocks as Elementor saved templates. The script is the urgent one; it costs almost nothing now and a lot later.

### A4. Two rules contradict each other on live data

The guide says all content that matters for search must be in the HTML, and JavaScript only enriches. But the timetable and the class finder load their content from Google Sheets in the browser. When the sheet fails, the page shows nothing, and search engines may not see the content at all. The same question will come up for 31 past paper pages.

**Recommendation:** a written data policy.

| Content | Where it lives |
|---|---|
| Changes often and is not a ranking target (class times, seats left) | Loaded live, with a readable fallback in the HTML and a "last updated" line |
| What a page ranks for (past paper lists, definitions, fees, thresholds, dates) | In the HTML. Generated from a sheet when the page is built, not in the visitor's browser |

### A5. Navigation, search and the pages around the content are undefined

The guide treats the header and footer as the theme's business. For a hub, navigation is the product: the menu, site search, search results, the blog index, category pages, author pages and the "not found" page. None of these are specified, and all of them currently look like the theme. A student who lands on a guide and wants the past papers has no designed path.

**Recommendation:** write the specification now and build it later. At minimum: the menu structure (by level, then subject, plus tools and guides), a site search that covers resources, and designs for the blog index, category, author and "not found" pages.

### A6. The stylesheet lives in a fragile place

WordPress stores Additional CSS per theme. If the theme is ever switched, or a child theme is activated, that box starts empty and every page built on the system loses its styling at once. This is from knowledge of WordPress, not a test on this site.

**Recommendation:** fine for now. Before any theme change, and ideally within a few months, move the stylesheet into a small site plugin or a proper file. Record the risk in the start-here file today.

### A7. The largest page group rests on an open legal question

43 of the 97 pages are resources, mostly past papers. Whether the site hosts Cambridge's files or links out is still undecided, and it shapes the template, the download cards and the data policy.

**Recommendation:** decide before the Resource template is built. This is the owner's call, ideally after a check with someone qualified. The safe design works either way: the page's own value is the organisation, the mark scheme guidance and the model answers, not the files.

### A8. The system cannot yet show what these subjects need

The guide has no pattern for mathematical expressions, chemical formulae, code and pseudocode, diagrams and graphs, or worked solutions in steps. It also bans Urdu script, yet the site has pages for Urdu and Islamiyat, where real content needs it.

**Recommendation:** add a "subject content" section before the first subject hub: how equations are written, a code block style, a figure and caption style, a worked-solution pattern, and a narrow exception allowing Urdu and Arabic script inside subject content, with a named font and right-to-left handling. The site stays English everywhere else.

---

## Part B. Marketing and strategy

### B1. There is no messaging framework

The brand currently carries three lines that are not ranked: "Center of Excellence" in the logo, "Cambridge doesn't mark effort. It marks method." on the homepage, and "a good teacher's notebook" as the design idea. The guide has two sentences of positioning and nothing a writer can reuse.

**Recommendation:** one page. The promise, three or four pillars with the proof behind each, the reasons to believe, and how the message changes for a student and for a parent. State which line is the tagline.

### B2. The site has one conversion and no way to keep a reader

Every call to action is "book a demo", "WhatsApp us" or "register". A student who came for a past paper and is not ready for tuition leaves with no connection to the brand. A hub earns its value from that reader coming back.

The guide also says the registration form is the only form, while the owner's own concept documents describe a quiz behind a form and ebook download pages. So the rule is already contradicted.

**Recommendation:** a written gating policy and one retention channel.

| Content | Policy |
|---|---|
| Past papers, definitions, guides, calculators | Always free, no form |
| Bundled extras (an ebook, a full set of model answers, a revision pack) | May ask for a WhatsApp number or email |
| Retention | One channel, offered after a resource is used: for example a WhatsApp channel for new papers and exam dates |

### B3. WhatsApp leads cannot be traced to a page

The main conversion opens WhatsApp with a pre-filled message. Once the chat starts, nobody can tell which page produced it. The click is tracked, but the enquiry is not tied to it.

**Recommendation:** end every pre-filled message with a short page reference, for example "(Ref: A2-BUS)". The team logs it in the lead tracker. Add a naming rule for campaign links from Instagram.

### B4. Share images are not a "later" item

Students and parents in Pakistan pass links through WhatsApp, and the guide already asks for a share link on every resource. The preview image is the first impression of that link. Today only the homepage has one.

**Recommendation:** move share images up. One template per page family, generated from the title, so every page has one.

### B5. There is no word list

Across 170 pages and several writers, small terms will drift. The guide does not settle them.

**Recommendation:** a one-page list. Examples to settle: "O Level" and "A Level" capitalisation; "AS" and "A2"; "tuition" against "coaching"; "mark scheme"; "past papers"; how teachers are named ("Sir Sunyyan"); currency ("Rs. 8,500"); times; exam series; "enrol". This also closes the spelling question, which is still unconfirmed: the guide uses British spelling, the owner's own writing uses American, and the logo says "Center".

### B6. Trust pages are thin

The register shows one Proof page (teachers) and no About page. A results page was designed but is not in the live sitemap. Parents decide on proof, and search engines weigh who is behind the advice.

**Recommendation:** add About, a verified results page and author profiles to the build order, ahead of campaign pages.

### B7. Page copy has a page; the blog has a book

The blog voice guide is thorough. Everything else (landing pages, buttons, form errors, tool results, WhatsApp messages, the "for parents" block) gets a short list in the brand guide. Enrol pages are where the money is.

**Recommendation:** a short page-copy companion: headline patterns, proof wording, parent wording, and microcopy for tools and forms.

---

## Part C. Details to settle once

| # | Finding | Why it matters | Recommendation |
|---|---|---|---|
| C1 | After the heading change, large numbers are still weight 400: the proof strip, the circled number, the ticket date | They now look thin beside a 600 headline | Numbers at 500 |
| C2 | Bold text inside long articles is weight 500 against 400 body text | In Poppins that difference is faint. Emphasis nearly disappears, and entertainment posts depend on bold lines | Bold in articles at 600, now that the weight is loaded |
| C3 | Fonts load late from Google, and the stylesheet has no matched fallback | The headline is the first thing drawn. It appears in a system font, then jumps to Poppins. A heavier headline makes the jump more visible | Self-host the two fonts, preload the headline weight, add a size-matched fallback |
| C4 | `overflow-x:clip` has no fallback | Older iPhones ignore it, so tilted elements could cause sideways scroll there | Add a fallback line |
| C5 | One rule uses `:has()` inside a grouped selector | Browsers without it drop the whole rule. Effect is cosmetic | Split the rule |
| C6 | No protection against forced dark mode | Some Android browsers darken pages automatically and can distort the palette | Declare the page as light-only |
| C7 | Icon rules exist but no icon set | Each builder draws its own icons, so they will not match | Approve about 20 icons once |
| C8 | The budget says a page widget stays under 60KB. The homepage widget is 74KB | The reference page breaks its own rule | Raise the budget or trim the page. Decide which |
| C9 | The guide asks pages to carry Course, Article and business data. Yoast already outputs its own. Built pages carry FAQ data only | Two sources can duplicate or contradict | State who owns what: Yoast for site and article data, the widget for FAQ, Course and Event |
| C10 | The build tooling is not in the folder | The minified stylesheet and the brand kit were built by scripts that exist only in a work session | Save the build and test scripts in `07-Code & Scripts` |
| C11 | Older documents contradict the guide | `README.md`, the old design guide, the platform audit and five page concepts describe dark cards, glass effects, weight 300 or a maximum weight of 400. A builder who reads them first gets the old look | Mark them superseded or archive them. Keep the concepts as logic references only |
| C12 | The system assumes one `#sj` wrapper per page | A blog template plus an embedded tool would nest two | Allow the class without the id for embedded blocks |
| C13 | Subjects and levels have no visual coding | A hub with 30 subjects may want it | Deliberately leave it out. Use labels and tabs, not more colours. Confirm |
| C14 | Real photos are required but not available | Five teacher photos are missing, and one image in the assets folder looks AI-generated | A shot list and one photo session |
| C15 | The bottom bar label wraps on narrow phones | Seen in the test | "Free demo" in the bar |

---

## Part D. Sound, and not worth reopening

- The notebook idea and its three tests.
- The palette and the role of each colour.
- Poppins and Caveat, and the heading weights settled on 3 October.
- Page families and the density limits.
- Spacing, radius, shadow and breakpoint tokens.
- The component set and its states.
- The accessibility rules and the checked contrast pairs.
- The blog voice, the humour rules, and the ratio of entertainment posts.
- Consent rules and the facts register as a concept.
- The shared stylesheet approach, now proven on the live site.

---

## Part E. Decisions, with a recommendation for each

| # | Decision | Recommendation | Blocks |
|---|---|---|---|
| 1 | How the design reaches blog posts | One blog template wrapping posts in the system | All blog work |
| 2 | Subject architecture | Hub and spoke; the past papers subject page is the hub; no address changes | Subject and past paper templates |
| 3 | Standard script | Load once, site-wide | Every new page |
| 4 | Facts | Shortcodes, one source | Nothing yet. Soon |
| 5 | Live data policy | Ranking content in HTML; volatile content live with a fallback | Past paper template |
| 6 | Navigation and surrounding pages | Specify now, build later | Hub ambition |
| 7 | Where the stylesheet lives | Stay for now; move before any theme change | Nothing yet |
| 8 | Past papers: host or link | Owner's decision | Resource template |
| 9 | Subject content patterns, including Urdu script | Add before the first subject hub | Subject hubs |
| 10 | Messaging framework and tagline | One page | Page copy |
| 11 | Gating and retention | Resources free; extras may ask for contact; one retention channel | Tool and resource pages |
| 12 | WhatsApp lead reference | Page reference in every message | Every new page |
| 13 | Word list and spelling | One page; British spelling unless overruled | All copy |
| 14 | Share images | One template per family, now | Sharing |
| 15 | Trust pages | About, results, author profiles ahead of campaigns | Parent conversion |
| 16 | Part C items | Apply as one stylesheet and guide update | Nothing |

**The five that would cause real rework if left:** 1, 2, 3, 5 and 9.
