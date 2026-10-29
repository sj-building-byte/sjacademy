# SJ Academy SEO and AI Search Audit

## 1. Executive assessment

SJ Academy has a valuable search audience and demonstrable visibility in AI-assisted discovery. The business is already attracting substantial education-related traffic, with organic search providing 60.7% of GA4 sessions in the reviewed 28 days. The next phase should concentrate on making this visibility more trustworthy, easier to use, and more productive for admissions. Publishing more pages before repairing the most important weaknesses would spread effort too thinly. [1][2]

The Master SEO Progress Report was directionally right about useful tools, subject hubs, local relevance, and connecting informational visitors to tuition. It was too confident about technical completion, attribution, schema benefits, and some educational claims. Several assets described as future work have since improved, while several supposed completed foundations still need attention. The appropriate decision is to retain the strategy's useful assets and replace its assumptions with a measured, source-checked operating plan. [3]

| Area | Current assessment | Business implication |
| --- | --- | --- |
| Organic visibility | Established, but led by informational articles | Protect successful content and build paths to tuition |
| AI discovery | Real visibility and referrals | Measure relevant citations and qualified enquiries separately |
| Crawl and indexing | Mostly healthy for submitted content | Repair specific exclusions, not every excluded URL |
| Page experience | Material weakness | Fix loading and layout stability before adding visual complexity |
| Education accuracy | Urgent corrections needed | Incorrect advice undermines student trust and citation quality |
| Lead measurement | Active but fragmented | Current event totals cannot establish enrolment ROI |
| Local differentiation | Useful assets, incomplete verification | Strengthen precise business and teacher evidence |

**First priorities:** correct the IBCC calculator and subject-selection guidance; reconcile fees and batch dates; fix remaining broken journeys; improve Core Web Vitals; and establish a consistent enquiry-to-enrolment measurement system. These actions support both Karachi/DHA admissions and live online tuition across Pakistan.

**Scope and evidence.** This assessment is dated September 10, 2026. The public scan fetched all 166 URLs in the two sitemaps captured that morning, then checked 161 additional internal destinations. It includes authenticated GSC and GA4 observations, source-code analysis, a mobile homepage/registration review at 390 x 844, and a rendered Business past-paper hub check. Public HTML snapshots and URL inventories accompany the report. A later Chemistry URL recheck is recorded separately. [1][2][4]

This is a complete scan of that sitemap set, with sampled rendering and deeper review of strategically important pages. It is not a claim that every PDF, external resource, JavaScript interaction, historical URL, or search engine index was exhaustively tested. No website changes were made by this audit.

Footnotes: [1] Authenticated GSC observations. [2] Authenticated GA4 observations. [3] Master SEO Progress Report. [4] September 10 crawl evidence. Full references appear at the end.

---PAGE---

## 2. Search demand and commercial standing

GSC's Web report for June 8 to September 7 shows approximately 24.6K clicks, 1.43M impressions, 1.7% CTR and average position 6.5. The overview gives the more precise click total of 24,594. These figures establish meaningful search visibility, but an average position of 6.5 across mixed queries does not mean SJ Academy ranks sixth for its commercial tuition keywords. [1]

| Leading page | Clicks | Impressions |
| --- | --- | --- |
| Karachi schools and fees | 6,292 | 181,902 |
| Lahore schools | 2,514 | 162,994 |
| Homepage | 2,075 | 29,706 |
| A Level colleges in Karachi | 1,940 | 69,795 |
| Universities in Islamabad | 1,840 | 105,373 |
| Beaconhouse review | 1,599 | 133,902 |
| Best degrees in Pakistan | 920 | 69,559 |
| Karachi Grammar School review | 910 | 34,928 |
| O Level grade thresholds | 684 | 44,593 |
| Alpha College review | 564 | 32,147 |

These are page-level figures from the same GSC period. They should not be added to GA4 sessions or interpreted as distinct students. The Karachi schools article alone accounts for roughly one quarter of the reported site click total, illustrating both the value of the content and concentration risk. [1]

**What is good.** Parents and students already encounter SJ Academy during school selection, fee research, and exam planning. This is a credible entry point into tuition. The brand query also has demand: “sj academy” recorded 1,158 clicks and 2,441 impressions in this period. A relevant education audience is more useful than arbitrary traffic growth. [1]

**What needs to change.** School-fee searches are not automatically high-income or high-intent tuition leads. Some visitors are researching primary schools, unrelated cities, or university choices. Qualify them through helpful, context-specific next steps. Karachi articles should explain campus and online options. Lahore and Islamabad articles should lead to online tuition where relevant, without implying local campuses.

For priority reporting, separate four groups: tuition/programme pages; exam and syllabus resources; school/college decisions; and broad student lifestyle content. Judge each by its purpose. A past-paper visit may be successful without a long session, but it should offer a relevant teaching route when help is needed.

Avoid blanket title rewrites aimed at a sitewide CTR target. Review query, position, device, and page together. The school-fees article's calculated CTR is about 3.46%, while the homepage's is about 6.99%; neither should be compared directly with an unrelated generic query. No before/after ranking uplift has been established for the Master Report's keyword changes.

Footnote: [1] GSC Web performance, June 8-September 7, 2026; page and query observations.

---PAGE---

## 3. Crawlability, indexing and technical foundations

The site uses WordPress with the Educrat theme, Elementor/Pro Elements assets, Yoast, WPForms, WPCode-related output, Site Kit, PixelYourSite, Meta-related scripts, Joinchat, Slider Revolution and WP-Optimize caching signals. This is a workable stack, but ownership of metadata and tracking needs clearer boundaries. Presence of a plugin or script does not prove that every feature is configured correctly. [4]

**Verified strengths.** All 166 sitemap URLs returned HTTP 200 in the initial scan and declared indexable robots directives. The robots file permits general crawling while excluding the WPForms uploads directory. The sitemap index contains page and post sitemaps. The homepage's primary canonical uses HTTPS and www. HTTPS non-www redirects to www; HTTP non-www reaches the preferred URL in two redirects. HSTS was present on the final header check, and WP-Optimize reported a cached response. [4][5]

GSC's September 4 indexing data shows 189 indexed and 313 excluded URLs overall. Filtering to submitted pages gives a much more useful picture: **150 indexed, 12 excluded, and zero excluded by noindex**. That is approximately 92.6% indexed within the submitted set reported by GSC. The 162 submitted URLs in that delayed report and the 166 URLs in the September 10 sitemap are different snapshots, not a contradiction. [1]

Of the 12 submitted exclusions, five are crawled but not indexed and seven are discovered but not indexed. Examples include the Quadratics lead page, a study-technique article, the O-Level Accounting hub and a 2027 timeline. Payment and thank-you URLs also appear in the excluded list; they generally need an intentional utility-page policy rather than an effort to force them into search. [1]

| Finding | Severity | Exact response |
| --- | --- | --- |
| Extra HTML titles on 52 pages; nested head tags on 52 and body tags on 53 | Medium; higher on key pages | Strip document wrappers and page-level metadata from Elementor widgets; keep content fragments and scoped styles |
| Conflicting canonical declarations on three pages | High cleanup priority | Keep Yoast's correct primary canonical; remove the erroneous embedded declaration |
| Missing meta descriptions on 37 pages | Medium on search landing pages | Prioritise practicals, teachers and useful articles; do not optimise confirmation pages for traffic |
| Six pages without exactly one H1 | Low to medium | Correct document structure where useful; do not treat H1 count as a ranking penalty |
| Utility pages remain indexable and in sitemap | Medium | Review confirmation, download and registration URLs individually; preserve pages with independent search value |

The A-Level and O-Level directories contain additional canonicals pointing to `sjacademy.com/...-past-papers-faq`; the subject tool contains one pointing to `/career-finder/`. These occur after the original head, inside embedded markup. The proper Yoast canonical is also present. Google may ignore body canonical tags; this is not evidence that ranking signals are actually being transferred to those destinations. Remove them and verify Google's selected canonical through URL Inspection. [4][6]

The old audit overcounted duplicate titles: the extra “WhatsApp” title is inside an SVG icon and is not a second HTML document title. The 52 count above explicitly excludes SVG titles. All extracted JSON-LD blocks parsed as JSON, but this does not establish schema vocabulary validity or rich-result eligibility.

Footnotes: [1] GSC indexing. [4] Crawl and inventory. [5] Robots/sitemaps and header checks. [6] Google canonical guidance.

---PAGE---

## 4. Speed, mobile experience and broken journeys

**Page experience remains a high-priority weakness.** GSC's Chrome UX Report data, updated September 8, shows no good URLs among those reported. Mobile has 67 poor URLs and 45 needing improvement; desktop has 112 poor URLs. On mobile, 67 URLs have LCP above four seconds, 45 have LCP above 2.5 seconds, and 112 have CLS above 0.1. These issue counts overlap and must not be summed. The report shows zero URLs in its listed mobile INP issue row. [1]

These are field-based groups, not a new Lighthouse test of every page. Nevertheless, they contradict the idea that speed is finished. The earlier reductions in page weight and load time were useful progress, but improvement from a very slow baseline is not the same as acceptable performance.

The homepage HTML snapshot is about 385KB before downloading its images, styles, fonts or scripts. The Business tuition page contains 97 script elements, including inline configuration. This is evidence to investigate asset loading, not a claim that 97 separate network requests or 97 unnecessary scripts exist. [4]

**Implementation sequence:** profile anonymous mobile visits to the homepage, a high-traffic article, a tuition page and a resource hub. Identify the actual LCP element and layout-shift sources. Reserve image/video dimensions; avoid late-injected space changes; simplify the first screen; load heavy sliders, forms and resource libraries only where needed; and preserve working tracking during changes. Test caching and deferred scripts against the registration popup and resource filters. Target LCP at or below 2.5 seconds, CLS at or below 0.1 and INP at or below 200ms. [7]

The 390px homepage review showed a long introductory paragraph before the primary CTA. Clicking it opened a narrow, internally scrolling registration popup. The first step requests name, email, student WhatsApp, parent phone and school before subject selection. This is substantial friction for a parent merely exploring classes. The inspection was in a logged-in browser, so the administrator bar and exact vertical spacing are not an anonymous-user speed benchmark. The field burden and CTA destination are still directly observable. [4]

**Seven content destinations were still recorded as 404 after the Chemistry recheck:**

| Destination | Observed referring page | Action |
| --- | --- | --- |
| `/contact` | Contact page | Link directly to the existing contact page or relevant contact action |
| Three subject-specific practical URLs | `/lab-practicals/` | Replace with relevant working destinations or publish substantive pages |
| `/career-finder/` | Subject-combinations tool | Remove stale link/metadata; point to the intended working tool |
| `/a-level-practical-e-book` | Physics practical article | Restore the asset journey or replace the offer |
| Non-www `/register` | Haque Academy review | Use the intended demo/enquiry page |

The O-Level Chemistry hub initially returned 404 and later returned 200 on September 10. It is marked resolved on recheck. Cloudflare's email-protection endpoint also returned 404 to a direct fetch, but its browser-decoded email links worked in the inspected page; it is excluded from the seven content errors. [4]

Footnotes: [1] GSC Core Web Vitals. [4] Crawl, mobile observation and broken-link inventory. [7] Web Vitals guidance.

---PAGE---

## 5. Education accuracy and trust

For an academy, factual reliability is a conversion asset. Guidance about equivalence, eligibility and exam routes can affect a student's choices. These pages deserve stricter verification than generic marketing content. They are also the pages most likely to be reused by AI systems answering precise questions.

**Critical: IBCC calculator guidance.** The published page states that A* converts to 90 marks and that Cambridge students cannot exceed 90% equivalence. IBCC's conversion page instead specifies A* values above 90 from examination session 2021 onward and provides subject/session-specific tables. The page also promises automatic selection of the best eight O-Level and best three A-Level grades, which does not adequately account for required subjects and equivalence groups. [8][9]

Correct the underlying calculation and explanatory copy together. Use exam session, subject, qualification and applicable equivalence group; enforce compulsory subject requirements; distinguish local and overseas routes; and identify unsupported cases rather than producing a precise-looking answer. Publish worked examples checked against IBCC. Until that validation is complete, remove claims that the output is exact or universally maximised. This audit confirms incorrect published rules; it does not certify every calculation branch.

**High: subject-combination article.** The article describes Physics as highly recommended for the pre-medical route, while IBCC's published A-Level pre-medical equivalence requirements specify Physics, Chemistry and Biology. Its FAQ also generalises Physics as a requirement for Computer Science at FAST. FAST's current computing eligibility page lists Mathematics, and should not be conflated with its engineering requirements. Separate equivalence-group requirements from each university/programme's admission rules. [10][11][12]

Replace universal statements about exactly three subjects, automatic rejection, or all universities taking the same best-three approach with dated, institution-specific guidance. A comparison table should link to the relevant programme's requirements and show the review date. Human review should cover the calculator and subject tool as well as the articles.

**High: inconsistent commercial facts.** The fees page lists a Rs.3,500 admission fee and Rs.25,500 practical fee. The practicals page lists Rs.3,000 registration and Rs.25,000 per subject; the general registration form also contains Rs.3,000. The Business page advertises June 15 as its batch start, while its FAQ says June 1. Both are past dates on September 10. Use one maintained source for fees, batch status, available places and schedules. Do not silently choose which price is correct. [4]

**Proof needs definitions.** The homepage shows 950+ A*s and 193+ reviews, while the global schema refers to 250+ A*s and another programme page refers to 220+ reviews. These may reflect different periods, but the periods are not clear. Define cumulative versus recent results and distinguish genuine reviews from selected testimonials. Verify the named testimonials on subject pages before reusing them; this audit does not establish whether they are authentic or fabricated.

The AI-oriented fees article's “80%” tuition claim has no substantiation identified in the inspected copy. Remove it or support it with a relevant study and population. “Cambridge-qualified,” “KGS faculty,” university alumni and former school employment should be stated accurately and individually, without implying institutional endorsement. [4]

Footnotes: [8] SJ IBCC tool. [9] Official conversion rules. [10] SJ subject guide. [11] IBCC British system. [12] FAST eligibility.

---PAGE---

## 6. Architecture and content strategy

The subject-hub direction is worth retaining. The rendered A-Level Business resource page displayed downloadable papers and a relevant teaching callout. Its raw HTML initially said “Showing 0,” but the browser populated the list successfully. That is an important distinction: the resource is not proven broken merely because a text-only fetch misses its JavaScript-generated list. [4][13]

The next improvement is resilience. Provide useful subject/year navigation and core resource links in server-rendered HTML where practical, alongside filters. Verify representative files and filters, show an explicit loading/error state, and add concise, original teaching guidance. Avoid turning every hub into a long tuition sales page. A visitor arriving for a mark scheme should find it quickly.

**Recommended simpler architecture:**

- Homepage: establish SJ Academy, Karachi campus and nationwide live online teaching; route to the appropriate level, subject or practical programme.
- O-Level and A-Level tuition hubs: explain delivery, faculty, schedules, fees and subject choices; link to individual teaching pages.
- Subject tuition pages: answer who teaches, which syllabus/papers, what happens in class, when the batch runs, what it costs and how to try it.
- Resource hubs: past papers, syllabus guidance, worked examples and tools; link to the relevant subject tuition page where useful.
- Advice library: school/college decisions, exam routes and revision guidance; each article has an appropriate next step.
- Shared factual pages: fees, teacher profiles, campus/contact details and policies, maintained consistently.

Before creating a new online-tuition hub, map existing page/query overlap and decide whether to strengthen an existing page. If a distinct nationwide-online page is justified, explain recordings, live interaction, marking feedback, timetable/time zone, joining requirements and support. Do not create thin city pages pretending that SJ Academy has campuses across Pakistan.

Several overlapping URLs warrant review, including Maths tuition/teacher pages, older standalone past-paper pages versus the new nested hubs, and the practicals programme/workshop pages. Similar names are not proof of cannibalisation. Use query overlap, indexed canonicals, links and conversions before merging. Keep distinct pages when they serve different offers or exam sessions; redirect only when intent and content genuinely match.

For Business, retain the strong application, analysis and evaluation positioning. Build original, teacher-reviewed examples showing a weak answer, an improved answer, and why the change earns credit. Clearly label these as SJ Academy teaching examples rather than official examiner decisions. This provides a stronger reason to cite SJ than another generic revision list.

The 7115-to-7081 transition should be explicit: Cambridge states that O-Level Business changes code for first assessment in June 2027. Keep legacy past papers labelled as legacy material and explain their relevance and limitations for the new syllabus. Do not indiscriminately replace every 7115 reference with 7081. [14]

Broad student articles can remain if they help the audience, but future editorial effort should favour subjects, exam technique and verified decision support over more distant topics. This is a relevance and resource-allocation judgment, not evidence that Google has applied a topical penalty.

Footnotes: [4] Crawl and rendered review. [13] Business resource hub. [14] Cambridge syllabus transition.

---PAGE---

## 7. Conversion journey and measurement

The current `/o-a-level-classes/` and `/a-level-practicals/` pages already contain meaningful offer explanations, programme details, FAQs and social proof. The Master Report's description of them as simply checkout forms is outdated. Improve their remaining weaknesses instead of commissioning a wholesale redesign based on that old diagnosis. [3][4]

The homepage and subject pages should distinguish **enquiry**, **free demo** and **enrolment**. A cold visitor should be able to ask about a subject or request a demo without completing the full registration/payment workflow. Keep the full form available for students who have decided to join. A free-demo label should lead to a clearly free-demo journey, not an unexplained registration fee.

**Recommended homepage copy direction:** “O & A Level tuition in Karachi and live online across Pakistan.” Follow with: “Learn with subject specialists through structured classes, past-paper practice and feedback on your answers. Visit our DHA Phase 7 campus or join live online.” Use “Ask about classes on WhatsApp” as a primary enquiry action and “Explore subjects” as the secondary route. Add only verified results and teacher credentials.

For Business, keep the existing subject-specific teaching argument, shorten repetition, and state the current joining arrangement. A suitable enquiry label is “Ask about AS or A2 Business.” Replace the conflicting historic start dates with a confirmed batch status and catch-up policy. For school-fee articles, a relevant CTA is “Looking for O or A Level support alongside school? Explore our subjects and meet the teachers.” Avoid using anxiety about a named school as an unsupported sales claim.

**Tracking exists, but the definitions need repair.** GA4 for August 13-September 9 shows 18,217 sessions, 46 key events and a 0.25% session key-event rate. The events report includes the following: [2]

| Event | Event count | Reported users |
| --- | --- | --- |
| `submit_lead_form` | 429 | 366 |
| `whatsapp_click` | 215 | 191 |
| `generate_lead` | 82 | 71 |
| `form_submit` | 7 | 5 |
| `file_download` | 807 | 199 |

The key-event selector contained `purchase` and `generate_lead`; the selected lead key-event report showed 46, rather than the 82 total occurrences in Events. Timing of key-event designation, trigger scope and counting rules require inspection. These differences do not prove broken tracking, nor can the totals be added together as unique leads. [2]

Create a documented event map: WhatsApp/call clicks are contact intent; a successful enquiry is `generate_lead` with `form_id`, subject, level and delivery mode; demo booked, demo attended and enrolment confirmed are separate downstream states. Preserve first and latest acquisition source where feasible, and associate enquiries with an internal lead identifier. Never send names, phone numbers or emails as GA4 event parameters.

Audit browser/server Meta events for deduplication and GA4 scripts for overlapping ownership. Preserve UTMs through the actual form journey and confirm thank-you behaviour. Test successful submission, validation errors, mobile WhatsApp opening and a return visit. No test enquiry was submitted during this audit, so end-to-end delivery and attribution are not certified.

Footnotes: [2] GA4 acquisition and Events reports. [3] Master report. [4] Public pages and mobile form inspection.

---PAGE---

## 8. AI search visibility and citation strategy

There is direct evidence that SJ Academy appears in AI-assisted discovery. Google's GSC Generative AI features beta report shows **429K impressions** for June 8-September 7. GA4 reports **307 AI Assistant sessions** in August 13-September 9, including 296 sessions attributed to `chatgpt.com / ai-assistant` in the snapshot. These are different products, periods and metrics, and should not be combined. [1][2]

| Google AI-feature page | Reported impressions |
| --- | --- |
| Karachi schools and fees | 60,119 |
| Lahore schools | 54,246 |
| Beaconhouse review | 46,584 |
| Islamabad universities | 44,078 |
| Best degrees in Pakistan | 29,556 |
| A Level colleges in Karachi | 26,007 |

The inspected Google AI report exposed impressions, not an AI click or enrolment total. AI Assistant traffic in GA4 had 60.59% engagement, 46 seconds average engagement per session, four lead key events and a 0.98% session key-event rate. Organic Search had 52.47% engagement and a 0.23% key-event rate. The AI sample is too small, and its lead definitions too uncertain, to declare it four times better for admissions. [1][2]

**The right strategic change is from citation-seeking to citation-worthy evidence.** Correct the calculator and eligibility content first. Then publish original teacher explanations, dated fee information, documented resource methods and specific institutional facts. Each important assertion should be traceable to an official source, a clearly described SJ dataset, or a named teacher's expertise. An estimated fee should say what is estimated, when it was checked and what it includes.

Google's current guidance emphasises helpful original content and established SEO foundations. It does not require special AI schema or an `llms.txt` file. Tables and clear headings help readers, but do not establish a mechanical citation advantage. The same guidance rejects inauthentic mention tactics. The Master Report's “citation-bait” framing should be replaced with reliable reference material. [15]

Keep crawler access deliberate. The public robots file currently permits general access, but that alone does not prove Cloudflare allows every verified crawler IP. OpenAI distinguishes OAI-SearchBot, used for search discovery, from GPTBot, used for model-training collection. Training permission is not a prerequisite for choosing to permit search crawling. Validate actual access through server/Cloudflare logs, rather than treating a spoofed user-agent request as proof. [5][16]

**Measurement plan:** maintain a fixed list of realistic parent/student questions covering Karachi tuition, online classes, Business 9609, practicals and IBCC. Record engine, date, locale, wording, answer, cited URL and accuracy. Repeat consistently; distinguish brand mention, citation, referral click and qualified lead. Pair this with the available GSC AI report and GA4 channel data. This audit did not run a reproducible multi-engine prompt panel, so it cannot claim a ChatGPT/Perplexity citation share.

Footnotes: [1][2] Live account reports. [5] Robots. [15] Google AI optimisation guidance. [16] OpenAI crawler documentation.

---PAGE---

## 9. Local authority, competitors and structured data

SJ Academy has useful local signals: a stated DHA Phase 7 address, telephone, campus offer, teacher content, testimonials and consistent broad Karachi positioning. The opportunity is to make these facts precise, current and independently corroborated. Google describes local ranking through relevance, distance and prominence; a website schema change cannot guarantee a Maps position. [4][17]

The backlink evidence is concentrated. GSC reports 151 external links in its sample, with Reddit accounting for 113. Other visible sources include cloudwaysapps.com, pakbestlist.com and etech.pk. The homepage, practicals page, school-fees article, petition and Business quiz are among the linked destinations. These are link counts, not unique referring-domain counts, and GSC is not an exhaustive backlink database. [1]

Retain useful Reddit participation, but diversify earned coverage through accurate resources, school counsellors, teacher collaborations and relevant education organisations. Check the cloudwaysapps references to determine whether they come from a staging copy or another legitimate source. Do not infer a spam problem from a domain name or submit a blanket disavow file from this limited evidence.

Teachwink's current website offers a clear free-demo route, explains live/recorded classes, and describes ongoing academic support. Those are useful competitive benchmarks. It also lists the same Plot 29C, Lane 5 address found on SJ Academy's site. SJ Academy's owner confirmed the businesses are independent competitors. That establishes a discrepancy to investigate, not its cause. Verify SJ's exact floor/unit, signage, map pin and business profile; preserve evidence before requesting a factual correction. [18]

Do not assume competitors' self-published rankings, ratings, experience or results are independently verified. This audit inspected Teachwink's public offer but did not establish a reproducible Karachi Maps rank grid, current market share, or a full competitor backlink comparison. No claim that SJ currently outranks or trails every competitor is warranted.

**Schema requires correction, not more volume.** All 166 pages contain a custom `TutoringService` declaration. Its Schema.org type URL returned 404 during verification and no matching type was found in the focused Schema.org search. Treat the type as unverified/unsupported and replace it with documented vocabulary after validation. `EducationalOrganization` is a documented type; relevant `Service`, `Course` and `Offer` entities can describe actual offerings. Connect them to one consistent organisation identifier. [4][19]

Use the complete verified address, accurate entity name and supported properties. Remove promotional keyword expansions from `alternateName` unless they are real names. Reconcile the schema's 250+ A*s with the homepage's 950+ claim. GSC's valid breadcrumbs and review-snippet detections are useful technical signals, but they do not prove eligibility for every rich result or justify self-serving review markup. [1][4][20]

The Master Report's FAQ rich-result win is outdated: Google's documentation update says FAQ rich results ceased appearing from May 7, 2026. Keep helpful FAQs for users; do not count FAQ markup as an earned Google visibility result. [21]

Footnotes: [1] GSC Links. [17] Google local ranking. [18] Teachwink and owner clarification. [19] Schema.org. [20] Review guidance. [21] Google documentation updates.

---PAGE---

## 10. Assessment of the Master SEO Progress Report

The central strategy deserves continuation, but the report should be rewritten as a verified progress ledger. Separate implementation, technical validation, search outcomes and business outcomes. An asset can be published without being indexed; indexed without ranking; visited without generating enquiries; and cited without producing admissions. [3]

| Master Report position | Audit verdict | Required change |
| --- | --- | --- |
| Interactive tools are valuable assets | Right direction, incomplete quality control | Correct IBCC rules; validate tools before promotion |
| Technical SEO is completed | Not supported | Reopen performance, embedded markup, metadata and broken journeys |
| Schema forces accurate classification | Overstated; type needs validation | Use documented vocabulary and consistent facts; remove ranking guarantees |
| Hard links improve hub discovery | Sensible | Preserve accessible links; verify rendering, downloads and indexed status |
| Twenty-five subject hubs need building | Status partly outdated | Most generated assets are live; improve value and reconcile URL mapping |
| FAQ schema secured rich snippets | Outdated expectation | Remove this success claim; retain useful FAQ content |
| Exact-match homepage changes push page-one rankings | Unproven causality | Compare matched queries over comparable periods before claiming uplift |
| AI strategy is working | Visibility supported; attribution incomplete | Report actual AI impressions/referrals, not assumed enrolment impact |
| Paid traffic has a 2.7-second bounce rate | Incorrect metric label | Use engagement time; diagnose current campaigns before judging spend |
| Competitor-fee visitors are highly qualified | Hypothesis | Segment actual enquiries and enrolled students |
| Main programme pages are checkout forms | No longer accurate | Refine current pages rather than restart from an outdated brief |
| eBook users need a 50%-off demo tripwire | Not justified by evidence | Use a coherent free-demo or diagnostic offer and test it |
| Review keyword seeding improves local standing | Wrong operational emphasis | Request honest experience-based reviews without scripting claims |

The original competitor plan also promises that a specific landing page will “mathematically” outrank a competitor. No such guarantee follows from title choice, specificity or schema. Different query intent, location, link authority, brand demand, content quality and page experience all matter.

**What to retain:** teacher-led subject pages; the resource-to-tuition relationship; useful school/college guidance; honest local information; source-backed tools; mobile improvements; and first-party analytics. **What to stop:** marking work complete solely because code was added, treating traffic as leads, publishing unsupported numeric claims, or using generic SEO promises to decide priorities.

The right commercial objective is more qualified enquiries and enrolments from both Karachi and nationwide online traffic. Search clicks and AI impressions are leading indicators. They should inform, rather than replace, that objective.

Footnote: [3] Master report and original competitor plan, assessed against the live findings and official sources in this audit.

---PAGE---

## 11. Prioritised implementation plan

Effort estimates below are planning judgments for a competent WordPress developer and teacher/editor. They are not quotations or guaranteed schedules. Preserve the WordPress header/footer and existing valuable URLs. Major layout or URL changes should first be approved as a concrete staging preview.

| Priority | Work package | Owner and effort | Acceptance test |
| --- | --- | --- | --- |
| P0 | Correct calculator and eligibility guidance | Teacher/editor + developer; 1-3 days after rule review | Official-source checks and worked examples pass; unsupported routes clearly identified |
| P1 | Reconcile fees, dates, reviews and result claims | Academy admin + editor; half to one day | Same current facts across pages, forms, schema and FAQs |
| P1 | Repair seven broken content destinations | Developer/editor; half day | Intended links return correct content, not merely HTTP 200 |
| P1 | Remove conflicting metadata and nested wrappers | Developer; 1-2 days | One CMS-owned title/canonical; key pages render correctly |
| P1 | Diagnose and fix LCP/CLS | Developer; 2-5 days initially | Repeatable mobile lab gains; field report improves as data refreshes |
| P1 | Reconcile lead events and offline outcomes | Analytics + admissions; 1-3 days | Known test journey produces one intended lead; source retained; no duplicate counting |
| P2 | Shorten enquiry/demo path | UX/editor + developer; 1-2 days | Mobile user can enquire without completing enrolment details |
| P2 | Improve subject hubs and relevant internal links | Teacher/editor; ongoing | Resources work; guidance is original; relevant tuition path exists |
| P2 | Strengthen entity/teacher evidence and local profile | Owner + editor; 1-2 days | Verified address, teacher facts and proof agree across surfaces |

**Days 1-7:** close the accuracy and commercial-fact risks; fix broken links; remove erroneous embedded canonicals; document the event map; and establish page-template performance baselines. Keep successful articles online while correcting them. Review whether utility pages belong in the sitemap; do not apply sitewide noindex rules.

**Days 8-30:** improve the four main templates: homepage, tuition page, article and resource hub. Start with the mobile first screen and the enquiry path. Add contextual links from the highest-value existing articles. Update Business and Maths teaching pages using real teacher evidence and current offers. Recheck Search Console exclusions selectively.

**Days 31-90:** publish a small number of distinctive teacher-reviewed resources; maintain a verified equivalence/admissions source register; build relevant external mentions; and repeat the AI prompt panel. Compare changes against pre-change baselines using the same query/page groups. Account for the June, August-results and October/November exam cycles rather than attributing seasonal movement to SEO alone.

**Operating dashboard:** qualified organic enquiries by level/subject/mode; demo bookings and attendance; enrolments and revenue linked to source where feasible; commercial-page non-brand clicks; resource-to-tuition click-through; indexed intended landing pages; Core Web Vitals by template; AI impressions/referrals/citations; and the age of last factual review for sensitive pages.

Use one change log with URL, purpose, date, owner, supporting source, test result and follow-up metric. Audit UTM preservation and Meta/GA4 event behaviour whenever a form, popup or caching rule changes. Do not launch a broad redirect, schema or cache change without rollback and representative journey tests.

---PAGE---

## 12. Evidence boundaries and final decision

**Established by this audit:** a successful 166-URL sitemap fetch; active organic and AI discovery; largely healthy submitted-page indexing; poor field page experience; genuine metadata/template problems; seven remaining content-link errors in the recorded scan; inaccurate published IBCC and eligibility statements; conflicting prices/dates; and multiple recorded lead-event names.

**Not established:** enrolment ROI by source; a complete before/after SEO uplift; exact cause of each Core Web Vitals problem; correctness of every calculator branch; authenticity of every testimonial; all current business-profile fields; complete backlink quality; every external resource's availability; every engine's crawler access; or a reproducible AI citation share. These are explicit follow-up verification tasks, not reasons to ignore the confirmed issues.

The full crawl and link checks were performed before the final recheck. The Chemistry hub changed from 404 to 200 during the session and has been removed from the active issue count. Other recommendations describe the saved September 10 snapshots unless a later recheck is noted. Google account reports have their own date windows and reporting delays. No production content or configuration was altered by this audit.

**Decision:** continue the resource, subject-expertise and local-plus-online strategy. Make accuracy, experience and measurement the next investment. SJ Academy is already visible enough that repairing the trust and conversion gaps should take precedence over indiscriminately expanding the content library. There is no evidence-based reason to discard the whole SEO programme, and no basis for describing its foundations as fully complete.

## Sources

[1] Google Search Console, authenticated property `https://www.sjacademy.pk/`, accessed September 10, 2026. Web and AI performance: June 8-September 7; indexing updated September 4; Core Web Vitals updated September 8; Links report observed September 10. [Open property](https://search.google.com/search-console?resource_id=https%3A%2F%2Fwww.sjacademy.pk%2F). Account observations are preserved in `evidence/account_observations.md`.

[2] Google Analytics 4, SJ ACADEMY / www.sjacademy.pk, property 482748209. Reports snapshot, Traffic acquisition and Events; August 13-September 9, 2026. [Open GA4](https://analytics.google.com/analytics/web/#/a349763169p482748209/reports/reportinghub). Authenticated observations, not a raw export.

[3] SJ Academy internal documents: `SEO_Docs/SJ_Academy_Master_SEO_Progress_Report.md`, September 2026; `SEO_Docs/seo_domination_plan.md`; archived SEO audit summary and verification documents. Local sources supplied in the workspace.

[4] SJ Academy public HTML crawl, September 10, 2026: 166 sitemap URLs and 161 additional internal destinations. Saved HTML, `crawl.json`, `link_checks.json`, `summary.json`, and Chemistry recheck in `evidence/`; human-readable metadata in `page_inventory.csv` and link findings in `broken_links.csv`. Representative pages: [Homepage](https://www.sjacademy.pk/), [Business tuition](https://www.sjacademy.pk/a-level-business-tuition/), [Programmes](https://www.sjacademy.pk/o-a-level-classes/), [Practicals](https://www.sjacademy.pk/a-level-practicals/), [Fees](https://www.sjacademy.pk/fee-structure/), [AI-oriented guide](https://www.sjacademy.pk/blog/o-a-level-colleges-fees-coaching-karachi/).

[5] SJ Academy [robots.txt](https://www.sjacademy.pk/robots.txt) and [sitemap index](https://www.sjacademy.pk/sitemap_index.xml), fetched September 10, 2026. HTTP/HTTPS and www redirect/header checks completed the same day.

[6] Google Search Central, [How to specify a canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), accessed September 10, 2026.

[7] Google web.dev, [Web Vitals](https://web.dev/articles/vitals), current performance thresholds; accessed for this report.

[8] SJ Academy, [IBCC Equivalence Calculator](https://www.sjacademy.pk/ibcc-equivalence-calculator/), September 10 HTML snapshot.

[9] IBCC, [Conversion for Equivalence](https://ibcc.edu.pk/conversion-for-equivalence/), subject/session-specific A* conversion guidance, accessed September 10, 2026.

---PAGE---

## Sources continued

[10] SJ Academy, [Best A-Level Subjects in Pakistan for University](https://www.sjacademy.pk/blog/best-a-level-subjects-combinations/), September 10 snapshot. The page displays an August 26, 2025 publication date with a 2026-2027 guide title.

[11] IBCC, [British System: O & A Levels](https://ibcc.edu.pk/equivalence-intro/british-system/), accessed September 10, 2026. Used to distinguish compulsory subjects and equivalence groups.

[12] FAST-NUCES, [Eligibility Criteria](https://www.nu.edu.pk/Admissions/EligibilityCriteria), page updated August 10, 2026; accessed September 10. Computing and engineering criteria are separate.

[13] SJ Academy, [A Level Business 9609 past papers](https://www.sjacademy.pk/a-level-past-papers/business-9609/), raw and rendered review on September 10, 2026.

[14] Cambridge International, [O Level Business Studies 7115](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-business-studies-7115/), notice of change to Business 7081 for first assessment June 2027; accessed September 10, 2026.

[15] Google Search Central, [Optimising your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), accessed September 10, 2026.

[16] OpenAI, [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), accessed September 10, 2026. Used for the distinction between OAI-SearchBot and GPTBot.

[17] Google Business Profile Help, [Tips to improve your local ranking](https://support.google.com/business/answer/7091), accessed September 10, 2026.

[18] Teachwink, [Homepage](https://teachwink.com/), accessed September 10, 2026. Public claims used for limited offer/address comparison, not independently verified. SJ Academy's owner confirmed in this audit conversation that the businesses are independent competitors.

[19] Schema.org, [EducationalOrganization](https://schema.org/EducationalOrganization), accessed September 10, 2026. Direct fetch of `https://schema.org/TutoringService` returned 404; its response is preserved in `evidence/schema_tutoringservice.html`.

[20] Google Search Central, [Review snippet structured data](https://developers.google.com/search/docs/appearance/structured-data/review-snippet), accessed September 10, 2026. Valid parsing does not guarantee display; business self-serving review eligibility needs care.

[21] Google Search Central, [Documentation updates](https://developers.google.com/search/updates), May 8 and June 15, 2026 entries, accessed September 10. Records FAQ rich-result retirement from May 7, 2026 and subsequent documentation removal.

## Accompanying files

`page_inventory.csv` contains a row for each of the 166 scanned sitemap URLs, including response, primary title, non-SVG HTML title count, H1s, descriptions, canonical declarations, HTML bytes and flags. It is a technical worklist, not an independent ranking score.

`broken_links.csv` contains the eight original content-link failures, with the Chemistry hub marked as resolved on recheck. Cloudflare's email-protection fetch is excluded from the content-error count.

The evidence directory preserves the underlying public crawl and account observation notes. Script-element counts include inline scripts; HTML sizes exclude dependent resources; and source HTML findings do not substitute for rendered-browser or Google-selected-canonical tests.
