# SJ Academy SEO Growth Diagnosis

## Executive conclusion

SJ Academy's organic traffic is not flat. Google Search Console shows 9,598 clicks in the latest 28 days versus 7,907 in the previous 28 days, an increase of 21.4%. Impressions increased from 429,955 to 552,062, or 28.4%. Average position changed only slightly from 6.5 to 6.6, and CTR fell from 1.8% to 1.7%. These first-party results directly contradict the impression created by the Semrush screenshot, which shows estimated desktop traffic in Pakistan falling 7.09% while detected keywords rise 6.94%.[1][2]

The concern is still valid, but the problem is different from "SEO produced zero growth." The new programme has produced early visibility, yet almost none of the site's total traffic or measured business value can be attributed to it. The 30 tracked strategy pages visible in Search Console generated 108 clicks in the latest 28 days, only 1.1% of the site's 9,598 clicks. They added 94 clicks versus the previous period, only 5.6% of the site's total click increase. Most of the site's growth came from existing assets, brand demand, and a highly seasonal O Level grade-threshold page.[1]

The strategy therefore has four central faults:

1. It measures completed actions rather than outcomes.
2. It expanded low-differentiation informational inventory faster than it improved commercial pages.
3. It declared technical work complete while major experience, markup, accuracy, and journey issues remained.
4. It cannot reliably connect rankings or traffic to qualified enquiries and enrolments.

The appropriate response is not to discard SEO. It is to stop treating publication as progress, protect the pages with commercial intent, fix trust and measurement, and test one differentiated subject cluster before scaling further.

## What the data actually says

### First-party traffic is growing, not declining

| Metric | Latest 28 days | Previous 28 days | Change |
| --- | ---: | ---: | ---: |
| Google organic clicks | 9,598 | 7,907 | +1,691, +21.4% |
| Google impressions | 552,062 | 429,955 | +122,107, +28.4% |
| CTR | 1.7% | 1.8% | -0.1 percentage point |
| Average position | 6.6 | 6.5 | -0.1 position |

The screenshot is not an analytics report. Semrush states that Domain Analytics estimates potential traffic by multiplying detected rankings, search volume, and assumed CTR. Semrush also says its own platform is not the best source for measuring a site's actual traffic. It is useful for competitor comparisons and keyword discovery, but Google Search Console and GA4 should decide whether SJ Academy itself gained or lost traffic.[2]

The latest Search Console period also includes a large seasonal effect. In the saved daily export, clicks averaged 288 per day from 16 July to 12 August and 374 per day from 13 August to 2 September. They peaked at 467 per day in the week beginning 17 August, then fell to 325 per day in the week beginning 24 August. The surge coincided with results-related demand, and the new O Level grade-threshold page alone generated 685 clicks in the latest comparison period after having none in the previous period.[1][3]

This explains why two apparently contradictory observations can both be true:

- First-party organic clicks increased strongly over 28 days.
- Traffic fell after a temporary results-season peak, while Semrush's model estimated a 7% monthly decline.

Neither observation proves that the growth strategy worked. Attribution requires page and query cohorts.

### Commercial visibility remains very small

A query cohort covering non-brand tuition, tutor, coaching, and academy searches produced 103 clicks from 7,240 impressions in the latest 28 days, versus 78 clicks from 8,402 impressions previously. A narrower local cohort containing Karachi or "near me" produced 75 clicks from 5,094 impressions, versus 57 clicks from 6,109 impressions.[1]

This is mixed progress:

- Commercial clicks increased 32% in the broad cohort.
- Local commercial clicks increased 32%.
- Commercial impressions fell 14%.
- Local commercial impressions fell 17%.
- The local cohort still contributed only 0.78% of all Search Console clicks.

Several target queries improved, but at very small volumes. "Best O Level coaching in Karachi" moved from average position 8.1 to 3.1 and generated 3 clicks instead of 1. "Best A Level Business teacher in Karachi" moved from 5.9 to 4.6 and generated 3 clicks instead of zero. At the same time, "O Level tutor in Karachi" fell from position 8.0 to 9.4 and "tutor academy in Karachi" slipped from 10.2 to 10.7.[1]

The correct verdict is: early ranking movement exists, but SJ Academy does not yet own enough non-brand commercial demand for it to materially affect total traffic or admissions.

### New assets have started indexing, but they are not yet a traffic engine

| Strategy asset or group | Latest clicks | Previous clicks | Latest impressions | Assessment |
| --- | ---: | ---: | ---: | --- |
| Best tutor academy article | 49 | 12 | 4,294 | CTR improved, but position slipped from 10.0 to 10.7 |
| CAIE retake guide | 24 | 0 | 1,857 | Fast initial visibility; highly seasonal topic |
| IBCC calculator | 18 | 0 | 1,054 | Promising engagement, but published rules require correction |
| Colleges, fees, and coaching guide | 8 | 0 | 685 | Early discovery, minimal traffic |
| O Level past-papers directory | 7 | 2 | 601 | More visibility, lower CTR and worse average position |
| Private-candidate registration page | 1 | 0 | 218 | Not yet competitive |
| 23 child past-paper hubs surfaced in the comparison | 1 total | 0 | 441 total | Indexed or being tested, almost no demand captured |

Across the 30 tracked pages above, the latest period produced 108 clicks and 9,249 impressions. The pages are no longer invisible, but 82% of their clicks came from just three URLs: the academy comparison article, the retake guide, and the IBCC calculator.[1]

The child hubs show the central scaling problem. Many have already reached average positions between 5 and 16 with tiny impression counts, yet almost all have zero clicks. Ranking position at this sample size is unstable and does not mean the pages have established demand. The broad query targets also place SJ Academy against Cambridge, Save My Exams, large past-paper archives, and specialist resource sites that offer deeper coverage and stronger link authority.[4]

## Root-cause analysis

### 1. The operating system tracks output, not SEO or business results

Severity: Critical

The tracker has 34 rows and only six columns: asset, type, target keyword, slug, status, and primary KPI. It has no publication date, baseline, current result, comparison period, owner, next action, lead count, enrolment count, or revenue. Twenty-one rows are marked Published, twelve Generated, and one Planned, even though the live state has moved beyond some of those labels. Twenty-seven of the 34 assets use "Organic Impressions" as their primary KPI.[5]

This makes the programme look busy without answering whether it is working. A URL can be published but not indexed, indexed but not competitive, ranking but not clicked, clicked but not generating an enquiry, or generating an enquiry that never enrols.

Exact fix:

- Replace status reporting with URL-level outcome reporting.
- Record publish date, last material change date, intended search intent, target page, baseline clicks/impressions/position, current results, qualified leads, and next decision.
- Separate brand, commercial, informational, resource, and local cohorts.
- Do not call an item successful until it passes a defined acceptance test.

### 2. The strategy expanded informational breadth before strengthening money pages

Severity: Critical

The programme devoted most of its production capacity to past-paper hubs and broad information assets. That may build an audience eventually, but it does not directly solve SJ Academy's main commercial gap. In the latest comparison, `/a-level-business-tuition/` fell from 21 clicks and 189 impressions to 3 clicks and 32 impressions. `/o-a-level-classes/` fell from 20 clicks and 331 impressions to 2 clicks and 110 impressions. These are more commercially important losses than the appearance of dozens of child hubs with zero clicks.[1]

The new hubs are also very similar. The Business and Physics templates differ mainly in the subject name, code, short syllabus paragraph, and generated file list. They do not contain enough subject-specific teaching expertise, worked answers, examiner insight, original data, or teacher proof to create a defensible reason to rank above established archives.[6]

Google's current guidance explicitly advises against producing many pages for query variations and says that high page quantity does not make a site more relevant or higher quality. It recommends unique, non-commodity content grounded in first-hand expertise.[7]

Exact fix:

- Freeze additional hub creation for four weeks.
- Choose Business 9609 as the pilot because SJ Academy has a named specialist and genuine teaching expertise.
- Turn that cluster into a resource no generic archive can easily copy: topic-level paper index, Sir Sunyyan's answer frameworks, common examiner deductions, one annotated response per question type, Paper 1 to 4 guidance, and a clear AS/A2 enquiry route.
- Link the Business hub, solved-paper assets, definitions, quiz, and tuition page through one intentional journey.
- Scale to another subject only after the pilot produces impressions, clicks, resource-to-tuition clicks, and qualified enquiries.

### 3. Traffic growth is concentrated in informational and seasonal pages

Severity: High

The 90-day account view is led by school-fee lists, school reviews, university lists, degree guides, and grade-threshold content. These pages attract real search demand, but much of it is not tuition intent. A person comparing schools in Lahore or universities in Islamabad is not automatically a candidate for a Karachi academy. The largest existing page, the Karachi schools and fees guide, also lost 754 clicks in the latest comparison, while the new grade-threshold page added 685.[1][8]

This creates a traffic replacement problem. One seasonal information page can temporarily hide a decline in another established page. Total clicks can rise without the site's admissions pipeline improving.

Exact fix:

- Report informational traffic separately from tuition demand.
- Add contextual, low-friction routes from relevant Karachi and CAIE articles to subject pages and WhatsApp.
- Do not force unrelated articles into aggressive tuition pitches.
- For Lahore, Islamabad, and nationwide topics, offer live online tuition only where the connection is natural.
- Measure article-to-subject clicks and article-assisted enquiries rather than assuming audience quality.

### 4. Technical SEO was marked complete when it was not complete

Severity: High

The September 10 crawl found all 166 sitemap URLs returning HTTP 200, which is positive. It also found extra HTML title elements and nested head tags on 52 pages, nested body tags on 53, 37 missing descriptions, conflicting body canonicals on key directories, and seven unresolved content destinations. Google Search Console reported 67 poor mobile URLs, 45 mobile URLs needing improvement, 112 poor desktop URLs, and no good URLs in the Core Web Vitals groups shown.[8]

This does not mean every issue directly caused a ranking loss. It means the claim that the technical foundation is finished is unsupported. The page templates remain very heavy, often around 285 KB to 385 KB of HTML before transferred images, fonts, scripts, and other assets. The stack includes Elementor, a theme, slider code, forms, tracking scripts, Joinchat, optimization code, and custom widgets. Slow LCP and widespread CLS are therefore plausible template-level problems, not isolated page mistakes.[8]

Exact fix:

- Remove complete HTML document wrappers from Elementor widgets. Widgets should contain fragments, scoped styles, and only the required script.
- Keep title, meta description, canonical, and schema ownership in WordPress/Yoast or one controlled source.
- Fix the seven known content links.
- Profile anonymous mobile loads for the homepage, one high-traffic article, one tuition page, and one resource hub.
- Identify the actual LCP element and layout-shift sources before applying more caching or minification changes.

### 5. Accuracy and trust failures undermine the strongest new assets

Severity: Critical

The IBCC calculator is one of the few new assets receiving meaningful impressions and strong engagement. However, it states that A* converts to 90 marks and suggests Cambridge students cannot exceed 90% equivalence. IBCC's current conversion page specifies subject and session-specific A* values above 90 from 2021 onward. The tool's "best eight" and "best three" logic also does not fully account for compulsory subjects and equivalence groups.[8][9]

The audit also found incorrect or overgeneralised subject-selection guidance, conflicting prices, old batch dates, and inconsistent achievement claims. These are not cosmetic issues. They can damage parent trust, produce wrong student decisions, and make the site less reliable for search and AI citations.

Exact fix:

- Pause promotion of the calculator until its rules and examples are independently checked against IBCC.
- Add a visible source date and limitation note.
- Reconcile prices, start dates, review counts, address details, and results claims across copy, forms, schema, and FAQs.
- Give sensitive education pages a named teacher or editor and a last-reviewed date.

### 6. Schema and keyword tactics were expected to do more than they can

Severity: High

The previous strategy claimed that `TutoringService` schema would force Google to categorise the site and help displace a competitor. The audit could not verify `TutoringService` as a supported Schema.org type. Schema can clarify entities and enable specific search features, but it does not force rankings or Maps placement.[8]

The homepage keyword injection produced some promising movement, but the clearest homepage gain is consistent with increased branded demand. The homepage gained 378 clicks, while visible brand-query variants such as "sj academy," "sjacademy," and "sj academy karachi" increased strongly. This is an inference, not proof that the title change caused the gain.[1]

Exact fix:

- Replace unsupported types with documented `EducationalOrganization`, `Service`, `Course`, and `Offer` entities where accurate.
- Use one consistent organisation identifier and verified business facts.
- Evaluate title and copy changes against a fixed generic-query cohort, not total homepage clicks.
- Stop promising that exact-match wording, schema, or FAQ markup will produce a specific rank.

### 7. Authority building is too narrow for the chosen keywords

Severity: High

The GSC links sample shows 151 external links, 113 from Reddit. The remainder is concentrated across a small number of sources. The record does not prove a penalty or toxic-link problem, but it does show limited diversity for a strategy competing with national and international resource domains.[8]

Quora answers, directory submissions, and general social mentions are unlikely to create enough authority by themselves. The stronger path is earned relevance: teacher collaborations, school counsellor resources, accurate admissions tools, original exam analysis, and pages that specialist communities cite because they solve a real problem.

Exact fix:

- Build links to one validated, exceptional asset rather than spreading outreach across 25 template pages.
- Seek relevant education organisations, school counsellors, teacher communities, and Pakistan admissions resources.
- Audit the cloudwaysapps.com links to rule out an old staging copy.
- Do not buy links or submit a blanket disavow file based on this limited sample.

### 8. Conversion measurement cannot tell whether SEO produces admissions

Severity: Critical

GA4 recorded multiple overlapping lead signals: 429 `submit_lead_form` events, 82 `generate_lead` events, 215 WhatsApp clicks, and only 7 `form_submit` events in the inspected report. The key-event view showed 46 `generate_lead` key events, not 82. The available landing-page export shows zero key events for the major commercial and new strategy URLs, including the Business page, classes page, practicals page, academy article, past-paper hubs, IBCC calculator, and private-candidate page.[8][10]

These figures do not prove that no leads occurred. They prove that event definitions, reporting windows, and attribution are not reliable enough for strategy decisions. GA4 also records zero revenue, and no offline enrolment outcome is connected to acquisition source.[8]

Exact fix:

- Define WhatsApp click as contact intent, not a lead.
- Fire one `generate_lead` event only after a successful enquiry, with non-sensitive fields such as form ID, level, subject, and delivery mode.
- Track demo booked, demo attended, and enrolment confirmed as separate downstream stages.
- Preserve first and latest source plus UTMs through the enquiry journey.
- Test one complete mobile journey and verify that it produces exactly one intended event.
- Reconcile weekly qualified leads with admissions records.

### 9. The CTA journey adds friction before trust is established

Severity: High

The mobile audit found that the primary homepage CTA opened a narrow, internally scrolling registration popup asking for name, email, student WhatsApp, parent phone, and school before subject selection. That is too much commitment for a cold visitor who only wants to ask about classes or a demo. The site also uses inconsistent paths for enquiry, demo, registration, payment, and WhatsApp.[8]

Exact fix:

- Make "Ask about classes on WhatsApp" the primary cold-traffic action.
- Offer a short demo enquiry with name, WhatsApp, level, subject, and physical or online mode.
- Keep full registration and payment for visitors who have decided to join.
- Use the same destination and event definitions across homepage, tuition pages, articles, and hubs.

### 10. The programme is too young to judge as a mature SEO campaign

Severity: Medium, but important

Most local assets were created or substantially revised between 18 August and 2 September. The latest Search Console period ends 8 September, so some pages had only days or two weeks to be crawled, indexed, tested, and ranked. Google states that some improvements can affect search within days, while broader quality reassessment can take several months.[11]

The launch also overlapped Google's August 2026 spam update, which ran from 18 to 20 August.[12] There is no evidence that SJ Academy was penalised. The overlap simply makes short before-and-after attribution weaker.

Exact fix:

- Do not declare failure or success from a single monthly chart.
- Use 28-day comparisons for operational monitoring and year-over-year comparisons for seasonal topics.
- Allow eight to twelve weeks for the pilot cluster, while still correcting obvious defects immediately.

## What is working and should be retained

1. The site already has strong organic reach. Search is not starting from zero.
2. The homepage and brand demand grew materially in the latest period.
3. The retake guide and IBCC calculator gained visibility quickly.
4. The best-academy article improved CTR from 0.2% to 1.1%, even though its average position slipped.
5. Several target local queries moved into stronger positions.
6. The sitemap set is crawlable and submitted-page indexing is mostly healthy.
7. The Business tuition page has a differentiated exam-technique proposition worth protecting.
8. AI-assisted search visibility and referral traffic are real, although attribution to enrolments is not established.[8]

## What should stop now

- Stop creating more near-identical hub pages until one pilot proves the model.
- Stop using Semrush estimated traffic as the scoreboard for SJ Academy's own performance.
- Stop reporting schema insertion, publication, or indexing as ranking success.
- Stop treating all school, university, or fee traffic as qualified tuition demand.
- Stop promoting the IBCC calculator until its logic is corrected.
- Stop making ranking guarantees based on exact-match titles, FAQs, or schema.
- Stop counting WhatsApp clicks, form starts, form submissions, and leads as interchangeable outcomes.

## Recommended simpler strategy

### Strategic structure

| Layer | Purpose | Primary KPI |
| --- | --- | --- |
| Money pages | Convert subject and local demand | Qualified leads and enrolments |
| Teacher-led subject cluster | Prove expertise and support money pages | Non-brand clicks plus resource-to-enquiry rate |
| High-traffic information pages | Reach and assisted discovery | Relevant assisted enquiries |
| Local entity and GBP | Capture Karachi and DHA demand | Calls, directions, qualified local leads |
| Technical and measurement foundation | Protect every layer | Good journeys, clean events, Core Web Vitals trend |

### First pilot: A Level Business 9609

Use one authoritative cluster rather than a large generic library:

1. `/a-level-business-tuition/` as the commercial destination.
2. `/a-level-past-papers/business-9609/` as the exam-resource hub.
3. Solved answers organised by Paper 1, 2, 3, and 4.
4. A focused guide to application, analysis chains, evaluation, and recommendation writing.
5. Definitions and quizzes linked by syllabus topic.
6. Clear teacher authorship and evidence for Sir Sunyyan Junaid.
7. One consistent CTA: "Ask about AS or A2 Business."

Each page should have a distinct intent. Avoid multiple URLs competing for "A Level Business past papers" or "A Level Business tuition Karachi" unless the search and conversion data supports separate pages.

## 30-day recovery plan

### Days 1 to 7: restore trust and measurement

| Action | Owner | Acceptance test |
| --- | --- | --- |
| Correct or pause IBCC calculator | Teacher/editor + developer | Official examples pass; limitations and source date visible |
| Fix seven known broken content links | Developer | Every intended destination returns the correct content |
| Reconcile fees, dates, address, and result claims | Academy admin + editor | Same verified facts across pages, forms, schema, and FAQs |
| Create GA4 event map | Analytics + admissions | One test enquiry fires one lead event with UTMs retained |
| Create the new SEO scorecard | SEO owner | Brand, commercial, resource, and information cohorts visible |

### Days 8 to 14: protect the money pages

- Diagnose the loss on Business tuition and O/A Level classes by query, device, and landing page.
- Confirm canonical ownership and remove embedded document metadata.
- Simplify the mobile first screen and enquiry path.
- Add WhatsApp and short-demo CTAs with consistent tracking.
- Link only contextually relevant high-traffic pages to these commercial destinations.

### Days 15 to 30: build and test the Business pilot

- Upgrade the Business hub with original teacher material.
- Add current paper coverage and verify every resource link.
- Publish at least one genuinely solved, annotated response for each major paper type.
- Add contextual links between the hub, teaching page, definitions, quizzes, and solved answers.
- Start selective outreach to relevant teacher and education communities.
- Review the cohort weekly, but make the scale or stop decision after enough data accumulates.

## Decision rules for the next 8 to 12 weeks

Continue or scale the Business cluster only if most of these signals improve:

- Non-brand impressions for the target query set rise.
- Median position improves across the set, not just one low-volume query.
- CTR improves at comparable positions.
- The resource hub earns clicks, not only impressions.
- Users move from resources to the tuition page or WhatsApp.
- Qualified Business enquiries are recorded with source.
- Mobile journey completion improves.

If impressions rise but clicks remain near zero, improve the result proposition and content depth. If clicks rise but enquiries do not, fix the offer and CTA journey. If neither impressions nor rankings improve after the pilot is technically clean and genuinely differentiated, reassess query difficulty, intent, and authority before creating more pages.

## Risks and verification gaps

- Search Console comparison data is current through 8 September 2026, while GA4 exports in the workspace use different windows. They should not be combined as if they covered identical dates.
- Page publication dates are inferred from workspace timestamps and strategy records. WordPress revision history should be used for the authoritative change log.
- The current analysis does not prove the cause of every ranking change. Search seasonality, the August spam update, competitor changes, snippets, device mix, and page changes can all contribute.
- Google Business Profile fields, map-grid rankings, server logs, and Cloudflare crawler logs were not rechecked in this analysis.
- No test enquiry was submitted, so lead delivery and deduplication remain unverified.
- Backlink counts are GSC samples, not a full referring-domain inventory.

## Final verdict

The strategy is not failing because Google ignored all the work. It is underperforming because the work was aimed too heavily at volume and visibility, while the measurement system, commercial pages, technical quality, trust, and conversion journey remained weak.

There are early positive signals: total Google clicks are up, several new pages are indexed, and some local rankings improved. However, the new tracked assets account for only 1.1% of clicks, local commercial queries account for less than 1%, and the main tuition pages lost visibility. The next move should be concentration, not more production.

Fix measurement and accuracy first. Recover the money pages second. Prove one teacher-led Business cluster third. Scale only what generates qualified enquiries.

## Sources

1. Google Search Console, authenticated SJ Academy property, live comparison of last 28 days versus previous 28 days, accessed 11 September 2026. Supporting earlier account notes: `SEO_Audit_2026_09_10/evidence/account_observations.md`.
2. Semrush, [Traffic Analytics vs Domain Analytics](https://www.semrush.com/kb/858-traffic-numbers-in-semrush), accessed 11 September 2026.
3. SJ Academy Search Console export, `Data_Vault/Search console/Chart.csv`, 3 March to 2 September 2026.
4. Cambridge International, [AS & A Level Business 9609 past papers](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-business-9609/past-papers/); Save My Exams, [CIE A Level Business past papers](https://www.savemyexams.com/a-level/business/cie/past-papers/), accessed 11 September 2026.
5. SJ Academy internal tracker, `Data_Vault/SJ_Academy_SEO_Tracker.csv`, workspace version dated 25 August 2026.
6. SJ Academy hub templates, `A_Level_Hubs/hub_a_level_business_9609.html` and `A_Level_Hubs/hub_a_level_physics_9702.html`, workspace versions dated 24 August 2026.
7. Google Search Central, [Guide to optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), accessed 11 September 2026.
8. SJ Academy, `SEO_Audit_2026_09_10/SJ_Academy_SEO_Director_Report.md`; crawl evidence, page inventory, and link checks captured 10 September 2026.
9. Inter Boards Coordination Commission, [Conversion for Equivalence](https://ibcc.edu.pk/conversion-for-equivalence/), accessed 11 September 2026.
10. SJ Academy GA4 exports, `Data_Vault/Search console/GA4 Metrics.csv`, `Landing_page_Landing_page.csv`, and authenticated account observations.
11. Google Search Central, [Google Search core updates and your website](https://developers.google.com/search/docs/appearance/core-updates), accessed 11 September 2026.
12. Google Search Status Dashboard, [Ranking history](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history), August 2026 spam update, accessed 11 September 2026.
