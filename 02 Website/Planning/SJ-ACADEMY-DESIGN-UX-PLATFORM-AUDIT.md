# SJ Academy Design, UX, Website and Platform Audit

**Audit date:** 10 September 2026  
**Scope:** Every document and implementation in the `Website Pages + Design` folder  
**Perspective:** Product design, conversion, mobile UX, accessibility, content trust, technical maintainability and education platform strategy

## Executive verdict

SJ Academy already has the beginnings of a recognizable product language. The yellow highlighter, orange action color, brown framing, rounded cards, practical calculators and exam-focused language make the work feel more useful and more memorable than a conventional tuition website. The strongest strategic idea is not the visual styling. It is the collection of free tools that help students make difficult academic decisions.

The current collection is not yet a mature design system or a coherent platform. It is a family of individually built widgets that repeatedly use the same visual motifs. The documents define colors and card treatments, but they do not adequately define accessibility, responsive behavior, information architecture, evidence standards, data freshness, error handling, analytics, component states or the relationship between the marketing website and a future learning product.

The biggest opportunity is to evolve SJ Academy from an academy website with tools into a **Cambridge mastery and decision platform for Pakistani students**, with tuition, teachers and live support built into the same journey. That positioning is defensible locally and expandable internationally. It combines three strengths that global platforms rarely combine:

1. Cambridge exam fluency.
2. Pakistani admissions, equivalence and parent decision support.
3. Direct access to teachers through physical and live online classes.

The current visual layer is about 60 percent of the way toward a distinctive brand expression, but the product and trust layers are closer to 30 to 40 percent. The next leap will not come from adding more cards, shadows or animations. It will come from unifying the journeys, proving every claim, correcting critical tool logic, improving mobile interaction and creating a real learning loop.

## What was audited

| Artifact | Role in the system | Audit status |
|---|---|---|
| `README.md` | Catalog and design system index | Reviewed |
| `AI-LANDING-PAGE-DESIGN-GUIDE.md` | Master visual and implementation specification | Reviewed |
| `01-ibcc-equivalence-calculator.md` | Equivalence calculator and lead generator | Reviewed |
| `02-a-level-grade-comeback-calculator.md` | Retake and carry-forward decision tool | Reviewed |
| `03-past-papers-landing-page.md` | Organic acquisition hub | Reviewed |
| `04-career-pathway-finder.md` | Subject and career diagnostic | Reviewed |
| `05-subject-past-papers-hub-math-9709.md` | Programmatic subject resource page | Reviewed |
| `06-a-level-business-quiz-tool.md` | Gated quiz experience | Reviewed |
| `07-live-class-timetable.md` | Live schedule browser | Reviewed |
| `08-university-admission-criteria-tool.md` | Admissions requirements lookup | Reviewed |
| `09-schools-near-me-finder.md` | Karachi school directory | Reviewed |
| `10-teachers-faculty-directory.md` | Faculty discovery and profile experience | Reviewed |
| `11-results-wall-distinctions.md` | Source review content | Reviewed |
| `12-fee-structure-page.md` | Pricing and fee calculator | Reviewed |
| `results-wall.html` | Implemented review wall | Reviewed in source, browser, desktop and mobile |

This is a design and product audit of the supplied material. It is not a live-site audit of all WordPress templates, plugins, network requests, analytics tags or real conversion data. Those should be examined before deployment decisions.

## Directional scorecard

These scores are expert audit judgments, not measured user-research results.

| Dimension | Score | Assessment |
|---|---:|---|
| Brand recognizability | 7/10 | The color system and highlighter treatment are memorable. |
| Visual consistency | 6/10 | Motifs repeat, but tokens, weights, spacing and scoping vary significantly. |
| Immediate clarity | 6/10 | Tool names are clear, but several pages overstate what the tool actually does. |
| Mobile experience | 5/10 | Most pages stack responsively, but stacking is not the same as mobile product design. |
| Accessibility | 2/10 | Keyboard, focus, semantics, contrast, motion and assistive status patterns are incomplete. |
| Trust and evidence | 3/10 | Strong claims are common, but source links, dates and proof objects are rare. |
| Conversion architecture | 5/10 | CTAs are visible, but lead journeys are generic and measurement is almost absent. |
| Performance readiness | 4/10 | Vanilla JavaScript is positive, but repeated fonts, icon libraries, third-party feeds and large inline widgets create risk. |
| Maintainability | 3/10 | Each page carries its own version of the same system, creating drift and regression risk. |
| Learning product depth | 4/10 | Useful tools exist, but they do not yet form a persistent learner experience. |
| Measurement maturity | 1/10 | No coherent GA4, Meta, lead-quality or learning-event specification is present. |

## The current SJ Academy design DNA

### What is working

**1. A recognizable visual signature**

The yellow highlighter is the clearest brand device. Used selectively, it connects academic annotation, revision and teacher feedback to the brand. Brown gives the palette more institutional warmth than a generic black-and-yellow system. Orange creates energy and action.

**2. Tools as marketing**

The calculators, finder, timetable, quiz and past-paper tools are strategically stronger than generic “Why choose us?” content. They let SJ Academy demonstrate expertise before asking for a lead.

**3. Exam-oriented language**

The best copy is specific to the student’s real job: understand thresholds, find the right paper, select subjects, compare university requirements and improve exam technique. This is much stronger than generic tuition language.

**4. Cards and controls are easy to reproduce**

The component vocabulary is simple enough for WordPress and Elementor. Cards, pills, segmented controls, result panels and contextual CTAs can be reused without a large front-end framework.

**5. The timetable sets a better interaction baseline**

Of the supplied tools, the timetable has the most deliberate accessibility work. It includes semantic buttons, selected states, an ARIA live status, keyboard handling and busy states. It should be used as the minimum engineering baseline, not treated as the exception.

### What is holding the system back

**1. Consistency is being confused with sameness**

Nearly every page repeats a centered badge, large highlighted heading, subtitle, filters and card grid. That creates recognition, but it also makes unrelated jobs feel identical. A pricing decision, a timed quiz, a faculty evaluation and a school directory should not have the same page rhythm.

The design system needs shared foundations with different experience archetypes:

- Marketing page
- Search and directory
- Calculator and diagnostic
- Learning activity
- Comparison and decision page
- Student dashboard

**2. The maximum font weight of 400 is the wrong rule**

The master guide mandates a maximum font weight of 400, while most page sources load and use weights from 600 to 900. The implemented results wall uses weight 900 for its main heading. The contradiction guarantees drift.

The underlying rule is also not appropriate for this brand. Weight 300 is too fragile for small text on common low-quality mobile displays, and weight 400 alone does not create enough hierarchy in dense tools. Use a restrained scale instead:

- 400 for body copy
- 500 for labels and compact controls
- 600 for buttons and subheadings
- 700 for major headings only
- Avoid 800 and 900 except for a deliberate campaign treatment

This will still feel refined without sacrificing readability or hierarchy.

**3. The brand colors are not being used accessibly**

Calculated contrast ratios show the current combinations are risky:

| Combination | Approximate contrast | Implication |
|---|---:|---|
| White on `#FE6100` | 3.03:1 | Fails 4.5:1 for normal-size text |
| White on `#25D366` | 1.98:1 | Fails normal and large-text contrast |
| White on `#453516` | 11.84:1 | Strong |
| Black on `#FCE004` | 15.80:1 | Strong |

Use black or very dark brown text on the current orange and WhatsApp green, or introduce darker action variants such as `#CC4A00` and `#0F7B3C` when white text is essential. Do not rely on color alone for correct, incorrect, selected or recommended states.

**4. Mobile-first currently means “stack the desktop page”**

The results wall demonstrates the problem. It is visually clean on a 390 px viewport, but the seven filter buttons become a long vertical block. A visitor must traverse the control area before reaching the content. Search placeholder text is truncated, cards become long and the page has no sticky action appropriate to the visitor’s stage.

Mobile layouts need different information priorities:

- Horizontal scrollable filter chips with visible edge affordance
- Bottom sheets for advanced filters
- Sticky contextual actions only when useful
- Collapsed secondary information
- Result summaries before detailed cards
- One primary action per viewport
- Thumb-friendly 44 px target design, even though WCAG 2.2 AA defines a smaller 24 px minimum target with exceptions

**5. Hover animation is overused and incomplete**

Almost every card lifts on hover. This does not communicate meaning, is absent on touch screens and makes static cards appear clickable. Motion should be reserved for controls and meaningful state changes. There is no `prefers-reduced-motion` handling in the supplied sources.

**6. The system does not define trust**

For education, trust is part of UI, not only copy. A user should be able to see:

- Who wrote or reviewed the guidance
- The source of a rule or requirement
- The date it was last verified
- The applicable exam session and syllabus version
- The confidence level of a recommendation
- A direct official source link
- What the tool does not know

This is essential for IBCC equivalence, Cambridge thresholds, university criteria, fees, teacher credentials and review claims.

**7. The design guide hard-codes tactics that should be tested**

The mandatory position 3 or 4 advertisement and mandatory frosted lead gate are not design principles. They are conversion hypotheses. A fixed in-feed interruption can reduce trust or task completion, especially when a student is trying to download a paper. A full gate before value can damage discovery and hide the quality of the learning experience.

Replace mandatory tactics with decision rules and experiments:

- Show contextual help after the user has received useful value.
- Gate saving, personalization or advanced history, not the basic answer.
- Use an inline CTA where the user experiences a relevant problem.
- Measure task completion and lead quality, not just clicks.

**8. The implementation model will not scale**

Each document contains another copy of tokens, font imports, components and logic. Several use global selectors or incompletely scoped generic classes. Fixes must be repeated across many long code blocks.

Build one versioned SJ UI package or WordPress plugin that owns:

- Tokens
- Typography
- Buttons
- Forms
- Cards
- Modals
- Toasts and status messages
- Tracking helpers
- UTM preservation
- Accessibility behavior
- Shared data-fetch and cache handling

Elementor widgets should configure and render shared components, not contain a new mini-application each time.

## Critical issues to fix before broad promotion

| Priority | Issue | Why it matters | Exact action |
|---|---|---|---|
| P0 | IBCC calculator can display a maximum of 990 marks against a denominator of 1100 | The documented mapping gives at most 90 marks for each of 11 grades, so a perfect input can only show 90%. This is a direct trust and guidance failure. | Remove the tool from promotion until the formula and group rules are verified against current IBCC sources. Add unit tests for official worked examples. |
| P0 | Fee calculator and fast-track pricing disagree | Switching the pricing cards to fast-track values does not update the calculator rates. | Create one pricing data object and render cards and calculator from the same source. Include registration and discount rules explicitly. |
| P0 | Career tool claims an email was sent when it only opens a `mailto:` URL | The success message can mislead users and creates a broken expectation. | Either send through a real consented backend/form workflow or relabel the action “Open Email Draft” and confirm only that the draft was prepared. |
| P0 | Review wall counts and labels conflict | The “All Reviews” chip says 10 while 12 items render. Subject counts also do not cleanly match the keyed records. | Generate every count from the data, add source links or proof references and remove “verified” labels that cannot be independently supported. |
| P0 | Accessibility is not designed across the system | Keyboard and screen-reader users can be blocked by `div` controls, unlabeled inputs, inaccessible modals and invisible focus. | Adopt WCAG 2.2 AA as a release requirement and build accessibility into the shared components. |
| P0 | Analytics and lead attribution are absent | There is no reliable way to know which tools produce qualified leads, demos or enrollments. | Implement a shared event taxonomy, UTM persistence and lead-source transfer into WPForms and WhatsApp links. |
| P1 | Time-sensitive claims and data lack governance | “Latest,” “official,” deadlines, fees and thresholds can silently become stale. | Show last-reviewed dates, source owners, expiry rules and stale-data warnings. |
| P1 | White text on orange and WhatsApp green is low contrast | Key CTAs can be difficult to read. | Use dark text on bright brand colors or accessible darker action variants. |
| P1 | Generic popup CTAs discard user context | A timetable, subject or fee selection should not open an empty generic form. | Pre-fill level, subject, teacher, batch, mode and source in the lead handoff. |

## Artifact-by-artifact findings

### README.md

**What it does well**

- Provides a useful inventory of the design work.
- Makes the tool-led growth strategy visible.
- Summarizes the common palette and typography.

**Issues**

- It describes the master guide as a definitive 100 percent match even though the individual sources contradict the guide on typography, scoping and interaction patterns.
- File links use `file://` URLs, which are not portable across environments.
- It lists page purpose but not maturity, owner, source freshness, deployment status or known risks.

**Exact fix**

Turn the catalog into a product registry with these fields: owner, live URL, source-of-truth data, last verified date, analytics status, accessibility status, release status and known issues.

### AI-LANDING-PAGE-DESIGN-GUIDE.md

**What it does well**

- Codifies color, highlighter, cards, buttons and WordPress scoping.
- Encourages simple vanilla JavaScript and reusable tokens.
- Makes conversion behavior an explicit design concern.

**Issues**

- It is primarily a styling recipe, not a complete product design system.
- The maximum weight 400 rule conflicts with the existing pages and harms hierarchy.
- The “always” rules for in-feed ads, lead gating, Google Sheets and local storage are too rigid.
- It has no complete accessibility, data validation, privacy, consent, event tracking, error-state, empty-state, skeleton-state, localization or content-governance section.
- Its boilerplate scopes some styles but still uses generic `.container`, which can collide outside carefully controlled embedding contexts.

**Exact fix**

Replace it with a versioned design system specification organized around foundations, components, page archetypes, content standards, accessibility, analytics, data governance and release testing. Treat conversion tactics as testable patterns with eligibility conditions.

### 01: IBCC Equivalence Calculator

**Severity: Critical**

**Strengths**

- High-intent utility with clear local relevance.
- Immediate calculation and a clear distinction between SSC and HSSC modes.
- Scoped styles reduce theme collision risk.

**Issues**

- The documented grade values make the HSSC maximum 990 while the UI divides by 1100. A perfect set of inputs therefore displays 90 percent.
- It assumes a single science-group model while equivalence rules can depend on qualification, group, subject requirements and policy changes.
- Subject rows identify only “O Level 1” rather than actual subjects, so mandatory subject rules cannot be checked.
- Users can add rows but cannot remove them.
- The result updates even when the required number of valid grades has not been entered.
- There is no source link, version date or worked-example validation.
- The CTA uses fear about a “bad grade” immediately after a sensitive academic result.

**Recommended structure**

1. Qualification and equivalence goal.
2. Group selection with a short explanation.
3. Named required and elective subjects.
4. Completion validation.
5. Result with calculation breakdown and official-source link.
6. Calm next-step guidance.
7. Contextual WhatsApp option that includes the calculated result only with explicit user choice.

**Design recommendation**

Use a calculation receipt, not one oversized percentage. Show selected subjects, counted grades, excluded grades, formula version and uncertainty. Never call it official. Label it “Estimate based on IBCC guidance reviewed on [date].”

### 02: A-Level Grade Comeback Calculator

**Severity: High**

**Strengths**

- Addresses a stressful, high-value student decision.
- Comparison of carry-forward, retake and composite routes is a strong information design idea.
- The PUM explanation and threshold breakdown can educate, not merely calculate.

**Issues**

- The experience initializes with a 45 PUM and target B, producing forceful recommendations before the student actively enters their situation.
- “Examiner’s Honest Recommendation” implies authority the interface has not established. Use “SJ Academy guidance” and name the academic reviewer.
- Grade and target options are built from non-semantic `div` elements, so keyboard and assistive interaction is weak.
- The modal lacks a declared dialog role, accessible title, focus trap and focus restoration.
- “Latest June 2026 Benchmarks,” “Exam in ~2 Months” and threshold-based calculations can become stale or wrong by session.
- A single deterministic recommendation does not communicate uncertainty, workload, student wellbeing or school advice.
- The page is extremely dense for an anxious mobile user.

**Exact fix**

Create a short input flow followed by a comparison table with “possible,” “high risk” and “needs adviser review.” Require the student to choose an exam session. Show the exact threshold dataset and review date. Make the recommendation explain its assumptions. Offer “Save comparison” and “Discuss this plan” after the value is shown.

### 03: CAIE Past Papers Landing Page

**Severity: Medium**

**Strengths**

- Simple A Level versus O Level choice.
- Search intent and resource utility are clear.
- The periodic table cross-promotion shows an ambition to connect resources.

**Issues**

- The page promises subject, year and session filtering, but this landing page itself only contains two large level cards.
- Global `:root`, `*`, `body` and `footer` rules can interfere with WordPress and Elementor.
- The standalone footer conflicts with the instruction to preserve the existing site footer.
- The periodic-table promotion is visually interesting but weakly connected to many past-paper visitors.
- There is no subject search, recently popular paper list, exam-session shortcut or continuing-study path.
- The page has no contextual tuition conversion beyond contact links.

**Recommended structure**

1. Search by syllabus code or subject.
2. Level shortcuts.
3. Current exam-session shortcuts.
4. Popular and recently accessed subjects.
5. “How to use past papers effectively” learning guidance.
6. Contextual subject support CTA.

The hero should say what can be done on this page, not what becomes possible after another click.

### 04: Career Pathway and Subject Combination Finder

**Severity: High**

**Strengths**

- A valuable bridge between O Level, A Level and university planning.
- Constraints and subject avoidance are more useful than a generic personality quiz.
- Copy and share actions recognize that parents and counselors are involved.

**Issues**

- Weighted heuristic matches are presented as “Excellent match” without explaining the scoring model or its limitations.
- The result can imply university suitability without checking current program requirements.
- The six-step flow requires choices at every step and offers no “not sure” path.
- Accordion category headers are `div` elements rather than accessible disclosure buttons.
- Selected options do not expose pressed or checked state to assistive technology.
- The email flow opens the user’s email client and then claims the plan is ready or sent.
- Answers are lost on refresh and no shareable result identifier exists.
- The university links are embedded static data and can age silently.

**Exact fix**

Reframe the output as “directions to explore,” not a determination. Give each direction a transparent “why this appeared” panel. Separate academic eligibility from interest fit. Offer a parent summary and a student exploration view. Connect every university claim to the admissions criteria tool and a dated official source.

### 05: Subject Past Papers Hub, Mathematics 9709

**Severity: High**

**Strengths**

- Strong search intent and useful syllabus-code framing.
- Filters map to how Cambridge papers are named.
- Subject cross-linking can build a valuable resource graph.

**Issues**

- The script generates a Cartesian product of years, sessions, papers, variants and types without first verifying that each file exists. This can create large numbers of broken download links.
- Question papers and mark schemes are displayed as separate flat results rather than a useful study set.
- Five simultaneous dropdowns create high mobile friction.
- Several generic CSS selectors such as `.controls-section`, `.filters-grid` and `.paper-card` are not prefixed by the widget root.
- The in-feed ad always appears at a fixed position instead of responding to behavior or subject context.
- Links open new tabs without consistently communicating that behavior.
- There is no error feedback when a generated PDF does not exist.

**Exact fix**

Build a verified paper manifest at publish time. Group each question paper with mark scheme, examiner report and insert. Make Year and Session the primary mobile controls, with paper and variant in an “More filters” sheet. Let the student mark a paper as attempted and continue into a review workflow.

### 06: A-Level Business 9609 Quiz Tool

**Severity: High**

**Strengths**

- This is the closest artifact to a real learning product.
- Chapter structure, instant feedback, explanations, review mode and score reporting create a complete practice loop.
- Randomized ten-question sessions support repeat use.

**Issues**

- A full lead gate appears before the user experiences the quality of the questions.
- A permanent local-storage unlock is not a real account or progress system and can disappear with browser data.
- The 45-second-per-question timer is a generic pressure mechanic, not clearly tied to the assessed format or accessibility needs.
- A pulsing danger state has no reduced-motion alternative.
- The timer can disadvantage students who need additional time.
- Screen changes are mostly visual. Focus management and live announcements are missing.
- Inline click handlers and non-native chapter cards add maintenance and accessibility cost.
- The entire remote CSV remains a single point of failure.

**Exact fix**

Let visitors complete a short three-question diagnostic without a gate. Gate saved progress, personalized revision plans or additional chapter history. Add practice and timed modes. Track mastery by syllabus objective, not only percentage correct. Save incorrect-question patterns and recommend the next activity.

### 07: Live Class Timetable

**Severity: Medium**

**Strengths**

- Best accessibility baseline in the collection.
- Clear batch and level separation.
- Live status, caching and sticky table headers show practical engineering.
- Clicking a class cell is a strong high-intent conversion moment.

**Issues**

- A wide matrix still demands horizontal scrolling on mobile.
- A 24-hour cache can conflict with the word “live” when schedule changes are operationally important.
- Every cell opens the same generic popup, losing subject, level, day, time and batch context.
- Hard-coded 2026 and 2027 tabs will require manual yearly changes.
- Online versus physical mode is encoded as unstructured subtext rather than a filter.
- The tab pattern uses both `aria-selected` and `aria-pressed` but does not define complete tab-panel relationships.

**Exact fix**

Use a mobile day agenda as the default and retain the weekly matrix on larger screens. Add filters for mode and subject. Pass the selected class context into the registration form. Show “Updated [time]” and allow a shorter cache with graceful stale fallback.

### 08: University Admission Criteria Tool

**Severity: High**

**Strengths**

- Relational separation between universities, programs and requirements is sensible.
- Last-updated metadata and official admissions links are the correct trust pattern.
- Reality checks can be useful when clearly separated from official minimums.

**Issues**

- The hero says “Check Your Eligibility,” but the interface collects no grades, test scores or subject combination. It is a program requirements lookup, not a personal eligibility checker.
- Official facts and qualitative “decision engine” advice appear in adjacent cards without a sufficiently strong visual and editorial distinction.
- Four client-side CSV requests can fail independently, producing incomplete or mismatched records.
- A default reality-check paragraph can appear even when specific data is missing.
- Deadlines and fees require aggressive freshness rules, not just a six-hour browser cache.
- There is no country, qualification or intake selector for future international growth.

**Exact fix**

Rename the current version “University Requirements Explorer.” Add a separate eligibility check only after collecting the minimum required inputs. Label content as “Official requirement,” “SJ Academy interpretation” or “Student-reported insight.” Add a source and verification date to every time-sensitive field.

### 09: Karachi Schools Near Me Finder

**Severity: High**

**Strengths**

- Useful local acquisition concept for parents.
- Area, board and sector are understandable filters.
- Map handoff is useful and the in-feed CTA carries UTM parameters.

**Issues**

- It is called “near me,” but it does not use or request location, calculate distance or sort by proximity.
- Updating the title and H1 from query parameters does not create a robust programmatic SEO architecture by itself. Search engines need crawlable, canonical, server-rendered landing pages with unique useful content.
- Board normalization can collapse multi-board schools incorrectly.
- The page depends on a third-party PapaParse script from `unpkg` without an integrity hash or local fallback.
- School records have no last-verified date, data source, admissions link, fee band, level range or comparison capability.
- “Don’t rely solely on school teachers” is an adversarial message on a school discovery page and can damage partnerships and parent trust.
- Dynamic metadata does not update the meta description or provide location-specific page content.

**Exact fix**

Rename it “Karachi School Directory” unless true distance sorting is added. Create real area landing pages for the locations with sufficient inventory and unique guidance. Include data freshness and correction reporting. Replace the attack on school teachers with a complementary message about focused after-school exam support.

### 10: Teachers and Faculty Directory

**Severity: High**

**Strengths**

- Teacher-first storytelling is right for an academy.
- Subject and level filters help evaluation.
- Detailed profiles can carry proof that generic course pages cannot.

**Issues**

- The custom pencil cursor sets `cursor: none` across the widget on desktop. This is a high-risk novelty that reduces usability and can fail unexpectedly.
- The modal lacks `role="dialog"`, an accessible name, focus containment and focus return.
- Social icon-only links lack accessible labels and several new-tab links lack `rel="noopener"`.
- Animated reveal behavior has no reduced-motion alternative.
- Credentials and affiliations appear as claims without direct evidence links or a verification date.
- The bento emphasis on co-founders can make the directory feel promotional rather than helping students choose the right teacher.
- Profiles do not show batch availability, mode, teaching method, sample lesson or a subject-specific action.

**Exact fix**

Remove the custom cursor. Build profile cards around student decision criteria: subject, paper coverage, teaching method, years teaching that syllabus, sample explanation, results evidence, availability and “Book a demo with this teacher.” Use a dedicated profile page or accessible dialog with deep-link support.

### 11: Verified Reviews and Subject Feedback Wall source document

**Severity: Critical for trust**

**Strengths**

- Subject grouping is useful.
- Longer reviews communicate teaching style better than generic star ratings.

**Issues**

- The file is cataloged as a results and distinctions page but contains reviews, not a results wall.
- Some reviews have names and others do not. No review includes a source URL, date, screenshot reference, platform identifier or consent record.
- “100% verified” is not demonstrated in the artifact.
- Results, grade improvements, distinctions and general satisfaction are different proof types and should not be mixed.

**Exact fix**

Create a governed proof library with consent and provenance. Store review source, date, course, teacher, mode, permitted display name, quote and link. Store academic results separately with session, subject, grade, distinction type and evidence status.

### results-wall.html

**Severity: Critical for trust and quality control**

**Strengths**

- The rendered page is visually clean and recognizable.
- The desktop grid is easy to scan.
- The mobile hero and KPI cards fit the viewport without overflow.
- Subject filtering and search are useful concepts.

**Issues found in source and browser**

- The hero section is opened twice, creating invalid nested structure and an unmatched closing pattern.
- The “All Reviews” chip displays 10 while the script renders 12.
- The interface calls every item a Google verified review, although no item links to its original review.
- Every card displays five stars even though the data model stores no rating.
- The search field has no programmatic label.
- “Clear Filters” is an anchor without an `href` and should be a button.
- Filter buttons do not expose selected state through `aria-pressed`.
- Filter result changes are not announced through an ARIA live region.
- The mobile filter list consumes most of a screen before the first review.
- The global `*` reset can affect a WordPress page if pasted as a widget.
- Font weights up to 900 directly contradict the master guide.
- WhatsApp opens in a new tab without `rel="noopener"`.
- No review structured data, canonical URL or proof/source relationship is present.

**Exact fix**

Fix the markup and derive counts and ratings from data. Link each public review to its source when allowed. Replace the KPI “100% real student quotes” with a claim that can be substantiated, or remove it. Convert mobile filters to a horizontal chip rail plus a compact subject filter sheet. Add a featured video or screenshot proof module only when consent and authenticity are documented.

### 12: Fee Structure and Tuition Calculator

**Severity: Critical**

**Strengths**

- Transparent prices reduce a major parent objection.
- The fee calculator makes multi-subject cost understandable.
- FAQ content addresses common concerns.

**Issues**

- The fast-track tab changes the displayed card prices but does not update the calculator’s underlying rates.
- The calculator excludes the one-time registration fee unless the user reads other sections.
- Lab fees, discounts, monthly versus quarterly totals and fast-track duration are not represented in one coherent estimate.
- Tab and pill states are visual only and lack semantic selected-state attributes.
- The active pricing selection is not carried into the registration popup.
- Public bank account details sit inside a marketing page without a strong anti-fraud verification pattern.
- Prices have no effective date or next review date.
- “Most Popular,” scholarships and financial-aid statements require operational verification.

**Exact fix**

Create one pricing schema and use it everywhere. The estimate should show tuition, period, registration, discount, optional lab cost and amount due now. Pass the selected package into the lead form. Put payment instructions behind a clearly verified payment page with domain, phone verification warning and receipt process.

## Recommended website architecture

### Main navigation

Keep the first-level navigation small and based on user goals:

1. **Programs**
   - O Level and IGCSE
   - AS Level
   - A2 Level
   - Lab practicals
   - Subject pages
2. **Teachers**
3. **Results and Reviews**
4. **Free Resources**
   - Past papers
   - Quizzes
   - Calculators
   - University guidance
5. **Schedule and Fees**
6. **Get a Study Plan**

On mobile, keep one persistent contextual WhatsApp or demo action, not two competing floating buttons.

### Separate three different visitor intents

**Ready to join**

Traffic from ads and teacher referrals should land on a focused subject or program page. The page should show teacher, syllabus, mode, schedule, teaching method, proof, fee and one next action.

**Trying to solve an immediate problem**

Organic traffic should get the resource or answer quickly. After the useful result, show the next logical learning action. Preserve the subject, level and problem in the CTA.

**Trying to make a decision**

Parents and students comparing teachers, fees, schedules or pathways need structured comparison, evidence and an adviser handoff. They do not need a generic marketing popup.

### Recommended subject page structure

Every high-intent subject page should answer the five-second questions immediately:

1. What course is this?
2. Which level, syllabus and papers are covered?
3. Who teaches it?
4. How does the teaching improve exam performance?
5. What should I do next?

Recommended sequence:

1. Specific hero with subject, syllabus, teacher, mode and CTA.
2. Current batch schedule and seats status.
3. “What students learn to do in exams,” organized by paper.
4. Sample teaching artifact, such as an annotated answer or short explanation.
5. Teacher proof.
6. Results and reviews filtered to that subject.
7. Course process and assessment rhythm.
8. Fees.
9. FAQ.
10. Context-filled demo or WhatsApp action.

For A Level Business, demonstrate case-data application, analysis chains, evaluation and recommendation writing across Papers 1 to 4 where relevant. This should be shown through real teaching artifacts, not only claimed in copy.

## Recommended platform direction

### Product position

Build **SJ Mastery**, a working name for a Cambridge learning and decision layer connected to SJ Academy teaching.

The core loop should be:

```text
Diagnose skill -> Practice by syllabus objective -> Receive examiner-style feedback
-> See mastery change -> Get the next recommended action -> Ask a teacher when stuck
```

The current tools become connected entry points into that loop:

- Past-paper visitor starts a paper set.
- Quiz visitor gets an objective-level diagnosis.
- Grade-comeback visitor receives a revision route.
- Career visitor saves an exploration plan.
- Timetable visitor books the relevant batch.
- Enrolled student sees all activity in one dashboard.

### What the first platform version should include

Do not begin with a large LMS rebuild. The minimum useful platform is:

1. Student account or magic-link identity.
2. Subject and syllabus enrollment.
3. Saved quiz and past-paper progress.
4. Weak-topic and objective tracking.
5. Teacher-recommended next task.
6. Upcoming class schedule in local timezone.
7. Recording and resource links for enrolled students.
8. Parent-friendly monthly progress summary where appropriate and consented.

### What should wait

- Social feeds
- Complex gamification economies
- AI tutor claims without a grounded content and safety layer
- Large community features
- Custom video conferencing
- A native mobile app before the responsive web product proves repeat use

### Recommended technical boundary

**Now:** Keep WordPress and Elementor for marketing pages and editorial SEO. Move shared interactive code into a versioned SJ Academy plugin or front-end package. Use server-controlled data endpoints or WordPress REST endpoints for validated public data.

**Later:** Introduce a separate application at a clear path such as `/learn/` when accounts, progress and permissions justify it. Share the same tokens and content models with WordPress. Avoid turning every Elementor HTML widget into an independent application.

### Content model to build once

Use structured records for:

- Program
- Subject and syllabus version
- Paper and assessment objective
- Teacher
- Batch and class session
- Fee and effective date
- Resource and source rights
- Quiz question and academic reviewer
- Review and consent status
- Result and evidence status
- University requirement and official source
- Tool formula version and verification date

This content model is the foundation for consistent pages, filters, structured data, tracking and future personalization.

## Visual design system, version 2

### Design idea

The right aesthetic is **confident academic clarity**, not generic startup glassmorphism and not childish school graphics.

Use the yellow highlighter as evidence of active learning. Use brown as the authority color. Use orange as a controlled signal for one important action or warning. Use real student work, teacher annotations, class moments and exam artifacts to add humanity.

### Typography

- Keep Poppins for display headings, badges and compact interface labels if it remains part of the identity.
- Use a highly readable sans serif for long body text, or use Poppins at weight 400 with generous size and line height.
- Body minimum: 16 px on mobile.
- Supporting text minimum: 14 px except nonessential legal metadata.
- Headings: weight 600 or 700, not 900.
- Avoid uppercase paragraphs and overly wide letter spacing.
- Use a stable type scale instead of one-off values in every widget.

### Color roles

| Role | Recommended use |
|---|---|
| Yellow `#FCE004` | Highlight, selected state, active learning, progress accent |
| Brown `#453516` | Authority, high-contrast buttons, important framing |
| Orange `#FE6100` | Accent, urgency or selected marker with dark text |
| Dark orange `#CC4A00` | White-text primary action where required |
| WhatsApp green `#25D366` | Brand recognition with black text |
| Ink `#151515` | Main text |
| Muted ink `#5F5F5F` | Secondary text that still passes contrast |
| Canvas `#F7F5EF` | Warm section background |
| White `#FFFFFF` | Primary surface |

### Component rules

- Radius: 10 to 14 px for cards, 8 to 10 px for controls.
- Border: use a complete light border plus one accent edge only when it communicates status or grouping.
- Shadow: one subtle elevation level and one overlay level. Remove routine hover lifting from static cards.
- Buttons: primary, secondary and text action only. Do not place orange, green and outline actions at equal visual weight.
- Focus: visible two-color or high-contrast outline on every interactive element.
- Forms: persistent labels, helper text, error text, success state and input purpose.
- Modals: proper dialog semantics, focus trap, Escape close, return focus and mobile bottom-sheet behavior where appropriate.
- Loading: skeleton for content collections, progress for multi-step actions and plain-language recoverable errors.
- Empty states: explain why there is no result and offer one useful correction.
- Motion: 150 to 250 ms for controls, no decorative motion required to understand content, and full reduced-motion support.

## Trust and evidence design

SJ Academy can outperform larger platforms by being more transparent.

### Every decision tool should show

- “Reviewed by” with a named qualified person
- “Last verified” date
- Applicable session or intake
- Source links
- Assumptions
- Confidence or limitation
- Correction/report link

### Every proof item should show

- Source type: Google review, written testimonial, result card or student interview
- Date
- Subject and teacher
- Online or physical mode if relevant
- Consent status in the internal system
- Link or evidence reference when publishable

Do not label an item verified merely because the interface places a Google icon beside it.

### Cambridge language

Avoid wording that could imply endorsement, privileged examiner access or official status. Cambridge itself distinguishes endorsed resources from other materials and warns against claims that a resource is official, essential or contains privileged information. Describe SJ Academy accurately as exam-focused and syllabus-aligned, then prove the method with examples.

## Conversion system

### Replace generic CTA repetition with contextual handoffs

| Context | Better CTA | Data carried forward |
|---|---|---|
| Past paper | “Get help with Mathematics 9709” | Subject, paper, year, source page |
| Quiz result | “Build my Business revision plan” | Chapter, score, weak objectives |
| Timetable cell | “Ask about this class” | Batch, level, subject, day, time, mode |
| Fee calculator | “Check availability for this plan” | Level, subject count, period, estimate |
| Teacher profile | “Try a class with Sir/Sir/Miss [Name]” | Teacher, subject, mode |
| Career result | “Review these choices with an adviser” | Result ID, preferred path, student level |

### Value-before-gate rule

Give the basic utility first. Ask for contact details when the user wants to:

- Save progress
- Receive a detailed plan
- Get a teacher review
- Book a class
- Access extended history

This creates a fair exchange and usually improves lead intent.

### WhatsApp design

- Preserve UTM source in the generated message or backend lead record.
- Include the relevant tool context.
- Never include sensitive grades or personal results without explicit user action.
- Set expectations such as response hours.
- Use one WhatsApp action at a time.

## Measurement plan

The website cannot become excellent without a learning and conversion evidence loop.

### Core journey events

- `tool_start`
- `tool_complete`
- `tool_error`
- `quiz_answer`
- `quiz_complete`
- `paper_search`
- `paper_download`
- `schedule_view`
- `class_select`
- `fee_estimate`
- `teacher_view`
- `review_filter`
- `whatsapp_click`
- `lead_form_start`
- `generate_lead`
- `demo_booked`
- `demo_attended`
- `enrollment_complete`

Use GA4 recommended events where they fit. Google identifies `generate_lead` as the recommended event for a generated lead, while `search`, `share` and `sign_up` are also standard recommended events. Custom events should carry consistent parameters such as level, subject, syllabus, tool, teacher, batch, mode and traffic source.

### Funnel reporting

Report by page, traffic source and subject:

```text
Landing view -> useful action started -> useful action completed
-> CTA clicked -> lead generated -> demo booked -> demo attended -> enrolled
```

Do not optimize only for WhatsApp clicks. A page that generates fewer but better-qualified demo attendances can be more valuable.

### Learning metrics

- First activity completed
- Questions attempted per active learner
- Accuracy by syllabus objective
- Repeat practice within 7 days
- Incorrect answer reviewed
- Past paper and mark scheme paired use
- Mastery improvement
- Teacher intervention requested

## Accessibility and performance release standard

Use WCAG 2.2 AA as the product baseline. The supplied system currently lacks widespread focus-visible states, reduced-motion handling and semantic selected states. WCAG 2.2 also includes minimum target-size and focus-not-obscured requirements that are particularly relevant to sticky mobile interfaces.

Required release checks:

- Complete all tasks with keyboard only.
- Screen-reader names and states for every control.
- Visible focus on every interactive element.
- Text contrast of at least 4.5:1 for normal text.
- UI component contrast of at least 3:1 where required.
- 200 percent zoom without lost content.
- Reflow at 320 CSS px without two-dimensional scrolling except true data tables.
- Reduced motion support.
- Error messages connected to the relevant fields.
- No time limit in practice mode, with accessible extension or disable options where timing is used.

Performance targets should be measured at the 75th percentile on mobile and desktop:

- LCP at or below 2.5 seconds.
- INP at or below 200 milliseconds.
- CLS at or below 0.1.

To reach these targets:

- Load one optimized font family and only necessary weights.
- Replace full Font Awesome loads with local SVG icons.
- Avoid repeated third-party font and icon imports inside widgets.
- Reserve image dimensions.
- Lazy-load noncritical media.
- Move large inline scripts into cached versioned assets.
- Validate and cache remote data server-side where possible.
- Measure real-user Web Vitals rather than relying only on lab tests.

## SEO and global expansion

### Pakistan first

Own the intersection of Cambridge education and Pakistani decisions:

- IBCC equivalence
- Subject selection
- University requirements
- Past-paper workflows
- Teacher-led exam technique
- Physical DHA and live online modes

### International expansion

Do not internationalize by changing “Karachi” to “worldwide.” Build explicit layers:

- Country-aware admissions guidance
- Local timezone schedules
- Currency and payment options
- Clear online-class experience
- International parent proof
- English-first copy with future Urdu support where useful
- Low-bandwidth and offline-friendly resources
- Accessibility as a global quality signal

The internationally scalable part is Cambridge mastery. The Pakistan-specific decision tools remain a strong local acquisition moat.

### SEO implementation

- Create crawlable subject, syllabus, area and program pages with unique useful content.
- Do not depend on client-side title changes as the programmatic SEO strategy.
- Use canonical URLs consistently.
- Add accurate structured data only when it matches visible content.
- Use `Course` and `ItemList` structures for real course collections that meet Google’s requirements.
- Keep review markup factual and complete. Google’s structured-data policies explicitly prohibit misleading or fake review content.
- Add source, author, reviewer and update dates to guidance content.

## Recommended 90-day sequence

### Days 1 to 14: trust and correctness

1. Pause promotion of the IBCC calculator until verified and tested.
2. Fix fee pricing state and career email behavior.
3. Correct the review wall markup, counts and verification claims.
4. Inventory every time-sensitive fact, source and owner.
5. Define the analytics event schema and UTM handoff.
6. Establish WCAG 2.2 AA and Core Web Vitals as acceptance criteria.

### Days 15 to 35: design system foundation

1. Build SJ UI version 2 tokens and shared components.
2. Implement accessible button, chip, tabs, accordion, modal, form, toast, table and card patterns.
3. Create the six page archetypes.
4. Add content and evidence schemas.
5. Move common assets out of individual Elementor widgets.

### Days 36 to 60: rebuild the highest-value journeys

1. Build one flagship subject page, preferably A Level Business 9609.
2. Rebuild fees and timetable as a connected decision flow.
3. Rebuild reviews and results as a verified proof library.
4. Turn the past-paper hub into verified paper sets.
5. Add contextual form prefill and WhatsApp handoff.

### Days 61 to 90: learning platform MVP

1. Release value-first Business diagnostic quiz.
2. Add magic-link account and saved progress.
3. Track mastery by syllabus objective.
4. Add teacher-recommended next tasks.
5. Test parent and student dashboard summaries.
6. Run moderated mobile tests with at least five students and five parents across different devices and connection quality.

## The three flagship experiences to design first

### 1. A Level Business 9609 subject experience

This should become the reference for the whole brand. It can connect teacher authority, exam technique, sample work, timetable, fees, reviews, quiz diagnosis and WhatsApp guidance in one coherent journey.

### 2. Past-paper mastery workflow

Do not stop at downloads. Let students choose a paper, set a timer, mark it, identify weak objectives and receive the next recommended practice. This is the clearest bridge from SEO traffic to repeat learning.

### 3. Parent decision center

Combine teacher, schedule, fee, mode, batch and proof into a calm comparison and inquiry flow. Parents should be able to understand the offer and next step without exploring five separate pages.

## Final design principles

1. **Useful before persuasive.** Give students a real win before asking for contact details.
2. **Prove before claiming.** Attach evidence, source and date to academic and marketing claims.
3. **One page, one dominant job.** A tool should solve its task before cross-promoting another tool.
4. **Mobile is a distinct experience.** Reprioritize and simplify, not merely stack.
5. **The state is part of the design.** Loading, empty, error, stale, selected, disabled, success and focus states all need explicit treatment.
6. **Context must survive the handoff.** Forms and WhatsApp must know what the visitor selected.
7. **Accessibility is brand quality.** It cannot be added after visual design.
8. **A platform remembers progress.** Local storage is a cache, not a learner relationship.
9. **Learning outcomes are the moat.** Cards and gradients are replaceable. Objective-level diagnosis, teacher feedback and demonstrated improvement are not.
10. **SJ Academy should feel teacher-led and technologically excellent.** The product should make the expertise visible, not hide it behind generic app patterns.

## Standards and external references used

- [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/)
- [What is new in WCAG 2.2, W3C](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
- [Core Web Vitals, web.dev](https://web.dev/articles/vitals)
- [JavaScript SEO basics, Google Search Central](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Course list structured data, Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/course)
- [General structured data guidelines, Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [GA4 recommended events, Google Analytics](https://developers.google.com/analytics/devguides/collection/ga4/reference/events)
- [Cambridge learning and revision guidance](https://www.cambridgeinternational.org/support-and-training-for-schools/support-for-teachers/learning-revision/)
- [Cambridge endorsed resources guidance](https://www.cambridgeinternational.org/support-and-training-for-schools/endorsed-resources/)

