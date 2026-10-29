# SJ Academy Landing Page Creative System

Version: 1.0  
Use this document with Codex, Antigravity, Elementor, or any AI builder when creating SJ Academy landing pages.

## 1. Purpose

This is not only a brand guide. It is a creative and conversion system for building modern, interactive, high-converting SJ Academy landing pages.

The goal is to stop generic pages that all look the same. Every page should feel:

- clear within 5 seconds
- premium but not arrogant
- exam-focused
- teacher-led
- mobile-first
- interactive where it helps decision-making
- practical for students and parents in Pakistan

The page should look like a modern education product, not a generic tuition brochure.

## 2. Core Brand Direction

SJ Academy is an O/A Level tuition academy in Karachi. The brand should feel structured, confident, useful, and student-first.

### Brand Personality

- Bold, not loud
- Premium, not flashy
- Helpful, not corporate
- Structured, not rigid
- Exam-focused, not generic
- Human, not robotic

### Visual Feel

Use a modern editorial and product-style design language:

- strong asymmetric layouts
- large confident headings
- sharp section contrast
- clean interactive blocks
- useful sticky elements
- purposeful motion
- high-quality visual hierarchy
- fewer but stronger sections

Avoid generic AI website patterns:

- centered hero with three cards underneath
- repeated 3-card grids
- oversized generic icons
- purple or blue gradients
- floating blob backgrounds
- vague marketing copy
- decorative motion with no purpose
- testimonial carousels that auto-slide
- long forms before the student understands the offer

## 3. Brand Tokens

### Colors

| Token | Hex | Use |
|---|---:|---|
| Primary Yellow | `#FCE004` | Highlights, attention marks, small badges, special callouts |
| Brown | `#453516` | Headings on light backgrounds, card top borders, outline buttons |
| Orange | `#FE6100` | Primary CTAs, active states, links, focus rings |
| WhatsApp Green | `#25D366` | WhatsApp buttons only |
| Black | `#000000` | Main text and headings |
| Dark Grey | `#222222` | Subtitles and strong body copy |
| Grey | `#555555` | Secondary copy |
| Light Background | `#FAFAFA` | Form areas, controls, quiet sections |
| Light Yellow | `#FFF9CC` | Special callouts |
| White | `#FFFFFF` | Main page background and card backgrounds |

### Color Rules

- Orange is the action color.
- Yellow is the attention color.
- Brown is the structure and credibility color.
- Do not mix orange and yellow on the same element.
- WhatsApp green is only for WhatsApp-specific actions.
- Avoid one-note pages dominated by only yellow, brown, or orange.
- Use white space and black text generously so the brand colors feel intentional.

### Typography

Use Poppins only.

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

Recommended type scale:

| Element | Desktop | Mobile | Weight |
|---|---:|---:|---:|
| Hero title | 3.4rem to 4.2rem | 2.1rem to 2.5rem | 800 |
| Section title | 2.2rem to 3rem | 1.7rem to 2rem | 800 |
| Card heading | 1.25rem to 1.6rem | 1.1rem to 1.3rem | 700 |
| Subtitle | 1.05rem to 1.2rem | 1rem | 400 to 500 |
| Body | 15px to 16px | 15px | 400 to 500 |
| Label | 12px to 14px | 12px | 700 |

Rules:

- Do not use negative letter spacing.
- Do not scale font size directly with viewport width.
- Keep body copy short and scannable.
- Use bold headings for structure, not hype.

## 4. Design Quality Bar

A page is not ready unless it passes all of these:

- A parent or student understands the offer within 5 seconds.
- The main CTA is obvious above the fold.
- Mobile layout is stronger than desktop, not an afterthought.
- The page has at least one meaningful interactive element.
- The CTA journey is consistent.
- The page does not force a long registration form too early.
- The design does not repeat the same grid pattern across sections.
- The page feels custom to the offer, not like a template.
- Every section earns its place.

## 5. Page Creation Workflow

Do not let an AI builder jump straight into code.

### Step 1: Audit First

Before designing or editing a page, inspect:

- page goal
- traffic source
- visitor intent
- offer details
- existing WordPress or Elementor structure
- forms and shortcodes
- WhatsApp CTAs
- scripts and tracking
- mobile layout
- duplicate sections
- confusing user journeys

### Step 2: Recommend the Simplest Strategy

State:

- top conversion problem
- primary visitor intent
- recommended page archetype
- main CTA
- sections to keep
- sections to remove
- sections to add
- tracking needed
- risks to verify

### Step 3: Propose 3 Visual Directions

Before implementation, propose three different visual directions:

1. Premium editorial
2. Interactive product-style
3. Exam-focused conversion page

For each direction, describe:

- hero layout
- core interaction
- section rhythm
- visual assets needed
- CTA journey
- mobile behavior

Wait for approval before major implementation.

### Step 4: Build

Implementation rules:

- preserve the existing WordPress header and footer
- use scoped CSS for Elementor HTML widgets
- avoid unnecessary libraries
- keep code readable and editable
- include responsive states
- include accessibility states
- avoid heavy animations on mobile

### Step 5: QA

Check:

- mobile first
- desktop second
- CTA links
- WhatsApp tracking
- form behavior
- Meta Pixel or GA4 events
- loading speed
- visual consistency
- no overlapping text
- no repeated generic layout sections

## 6. Page Archetypes

Use the archetype before choosing sections. This prevents every page from looking the same.

### 6.1 Cold Paid Traffic Subject Page

Use for:

- subject-specific ads
- WhatsApp lead campaigns
- urgent batch enrollment

Visitor mindset:

- interested but not fully convinced
- wants quick answers
- does not want a long form

Primary CTA:

- WhatsApp inquiry

Page length:

- short to medium
- 6 to 8 sections

Required sections:

- direct hero
- problem diagnosis
- teacher or method credibility
- what students will train
- class details
- FAQ
- final CTA

Avoid:

- long registration forms above the fold
- broad multi-subject forms
- payment steps before inquiry
- too many unrelated offers

Best interactions:

- sticky mobile WhatsApp CTA
- paper or topic tabs
- fee and batch detail accordion
- WhatsApp intent buttons

### 6.2 SEO Subject Page

Use for:

- organic search pages
- evergreen tuition pages
- city or subject landing pages

Visitor mindset:

- researching options
- comparing teachers or academies
- may need more explanation

Primary CTA:

- WhatsApp inquiry

Secondary CTA:

- short form or class details request

Page length:

- medium to long

Required sections:

- SEO-friendly hero
- subject explanation
- exam-board relevance
- common student problems
- teaching method
- class details
- FAQs
- internal links

Best interactions:

- sticky table of contents
- FAQ accordion
- topic tabs
- course breakdown matrix

Avoid:

- thin pages with only sales copy
- generic claims without subject detail
- hiding location, mode, or teacher information

### 6.3 Teacher-Led Page

Use for:

- Sir Sunyyan Junaid pages
- subject pages where teacher trust matters
- premium batch enrollment

Visitor mindset:

- wants to know who is teaching
- needs confidence before contacting

Primary CTA:

- ask about classes on WhatsApp

Page length:

- medium

Required sections:

- teacher-led hero
- teaching philosophy
- exam method
- student problem diagnosis
- class details
- proof or credibility
- FAQ

Best interactions:

- expandable teacher profile
- teaching method timeline
- before and after answer snippets
- sticky enrollment panel

Avoid:

- making the page only about personality
- vague “experienced teacher” claims
- stock photos replacing real teacher visuals

### 6.4 Course Registration Page

Use for:

- warmer traffic
- students already convinced
- enrollment after WhatsApp or retargeting

Visitor mindset:

- ready to register
- needs clarity and confidence

Primary CTA:

- registration form

Secondary CTA:

- WhatsApp help

Page length:

- short

Required sections:

- course summary
- date, fee, mode, and location
- what happens after registration
- form
- support CTA

Best interactions:

- step indicator
- conditional fields
- form progress
- FAQ accordion

Avoid:

- mixing many offers in one form
- unnecessary payment fields before the student is ready
- unclear confirmation message

### 6.5 Interactive Tool Page

Use for:

- admission tools
- school discovery tools
- quizzes
- calculators
- checkers

Visitor mindset:

- wants immediate value
- will leave if the tool is buried

Primary CTA:

- use the tool

Secondary CTA:

- WhatsApp or lead capture after value is shown

Page length:

- tool first, content second

Required sections:

- compact tool-first hero
- interactive tool
- result area
- next-step CTA
- explanation or FAQ

Best interactions:

- dynamic filters
- live results
- progress steps
- email or WhatsApp capture after result

Avoid:

- long intro before the tool
- asking for contact details before showing value
- fake complexity

### 6.6 Retargeting Page

Use for:

- warm visitors
- people who clicked ads before
- people who watched content

Visitor mindset:

- already aware
- needs final reason to contact

Primary CTA:

- WhatsApp

Page length:

- short

Required sections:

- direct reminder hero
- specific pain or objection
- class details
- proof
- FAQ
- CTA

Best interactions:

- objection accordion
- WhatsApp intent buttons
- batch detail card

Avoid:

- repeating cold awareness content
- long explanations
- making the visitor search for basic details

## 7. Hero Patterns

Choose the hero based on the page archetype.

### 7.1 Direct Offer Hero

Best for:

- cold paid traffic
- subject enrollment

Structure:

- left: clear offer, subject, exam board, who it is for, CTA
- right: batch details, teacher photo, or sticky class summary

Must answer:

- what is this
- who is it for
- why does it matter
- what should I do next

CTA:

- primary WhatsApp button
- optional secondary details button

Avoid:

- vague brand headlines
- abstract hero graphics
- hiding fee, mode, or start date if known

### 7.2 Problem-First Hero

Best for:

- exam technique pages
- students losing marks despite studying

Structure:

- bold problem statement
- short explanation
- CTA
- small proof or method strip

Example direction:

> Most A Level Business students do not lose marks because they know nothing. They lose marks because their answers stay descriptive.

### 7.3 Teacher-Led Hero

Best for:

- pages where Sir Sunyyan is the trust driver

Structure:

- teacher photo or strong teacher block
- subject and class promise
- short credibility line
- WhatsApp CTA

Avoid:

- stock student images
- long biography above the fold

### 7.4 Outcome-First Hero

Best for:

- exam preparation pages

Structure:

- headline about the exam skill outcome
- small list of trained skills
- CTA
- visual answer-writing cue

Good for:

- analysis chains
- evaluation writing
- case data application
- paper-specific preparation

### 7.5 Tool-First Hero

Best for:

- quizzes
- school finders
- admission checkers

Structure:

- compact headline
- tool interface visible above the fold
- minimal explanatory copy

Avoid:

- long hero copy before the tool

### 7.6 Comparison Hero

Best for:

- competitive decision pages
- “why SJ Academy” pages

Structure:

- left: common mistake or old way
- right: SJ Academy method
- CTA beneath comparison

### 7.7 Batch Urgency Hero

Best for:

- upcoming batch launches

Structure:

- batch name
- start date
- mode
- teacher
- limited seats or deadline only if true
- WhatsApp CTA

Avoid:

- fake urgency
- countdown timers without a real deadline

## 8. Section System

Every section must have a job. Do not add filler sections.

### 8.1 Problem Diagnosis

Purpose:

- make the visitor recognize the real problem

Use when:

- students may not understand why marks are low
- you need urgency before the CTA

Layout:

- two-column layout
- one side has short problem list
- other side has a highlighted reality check

Interaction options:

- expandable “what this looks like in an answer”
- tabs by paper or skill
- before and after answer example

Avoid:

- three generic problem cards
- vague lines like “students face many challenges”

### 8.2 What You Will Train

Purpose:

- show the practical skills taught in class

Layout:

- skill matrix
- paper tabs
- timeline
- checklist

For A Level Business, include:

- application to case data
- analysis chains
- evaluation
- recommendation writing
- Paper 1 and Paper 2 for AS
- Paper 3 and Paper 4 for A2

### 8.3 Paper-by-Paper Breakdown

Purpose:

- show detailed subject expertise

Layout:

- tabs for Paper 1, Paper 2, Paper 3, Paper 4
- each tab has: challenge, what students practice, class outcome

Interaction:

- tab switch
- mobile accordion fallback

### 8.4 Teacher Credibility

Purpose:

- build confidence through the teacher, not generic claims

Layout options:

- teacher photo plus teaching method
- quote-style principle
- credentials strip
- “how Sir Sunyyan teaches this” block

Avoid:

- long biographies
- unsupported superiority claims

### 8.5 Class Details

Purpose:

- answer the practical enrollment questions

Required fields:

- subject
- exam board
- teacher
- level
- mode
- location
- batch date
- fee if confirmed
- next step

Layout:

- sticky side panel on desktop
- compact accordion or summary card on mobile

### 8.6 Who This Is For

Purpose:

- help students self-identify

Layout:

- checklist
- segmented by student situation

Examples:

- you know the content but cannot write strong evaluation
- your answers stay descriptive
- you struggle to use case data
- you are starting A2 and need structure

Avoid:

- “for all students”

### 8.7 Method Timeline

Purpose:

- show how class works

Layout:

- 3 to 5 steps
- horizontal timeline on desktop
- vertical timeline on mobile

Example:

1. Understand the concept
2. Read the case data
3. Build the analysis chain
4. Evaluate options
5. Write the final recommendation

### 8.8 Before and After Answer Block

Purpose:

- make exam technique visible

Layout:

- split comparison
- left: weak answer habit
- right: improved answer structure

Interaction:

- toggle between weak and strong
- highlighted annotations

Avoid:

- using real student work without permission

### 8.9 Proof Section

Purpose:

- reduce risk

Use proof only when real.

Proof types:

- testimonials
- result screenshots
- parent feedback
- student messages
- teacher track record
- number of batches if accurate

Avoid:

- fake counters
- generic “trusted by hundreds” without evidence

### 8.10 Objection Section

Purpose:

- handle friction before CTA

Good objections:

- Is this for AS or A2?
- Can I join online?
- What if I am weak in concepts?
- Do you cover past papers?
- Can I ask about the fee first?

Layout:

- accordion
- short direct answers

### 8.11 FAQ

Purpose:

- answer final decision questions

Layout:

- accordion
- no more than 8 questions unless it is an SEO page

Rules:

- answer directly
- avoid long paragraphs
- include CTA after the FAQ

### 8.12 Final CTA

Purpose:

- close the page with one clear next step

Layout:

- strong text
- one primary CTA
- one support line

Good CTA examples:

- Ask About A Level Business Classes
- Message on WhatsApp
- Check Batch Timings
- Ask About Physical and Online Classes

Avoid:

- multiple competing CTAs
- generic “Submit”
- “Get Started” without context

## 9. Interaction System

Interactions must help the visitor understand, compare, decide, or contact. Do not add interaction only to look modern.

### Required Modern Interaction

Every landing page should include at least one of:

- tabs
- toggles
- accordions
- sticky CTA
- sticky details panel
- interactive quiz
- dynamic filter
- before and after comparison
- scroll anchor navigation

### Recommended Interactions

#### Paper Tabs

Use for:

- AS and A2
- Paper 1, Paper 2, Paper 3, Paper 4
- topic breakdowns

Mobile:

- convert to accordion if tabs become cramped

#### Physical / Online Toggle

Use when:

- both class modes are available

Show:

- location for physical
- platform or live class details for online
- same teacher if true
- timing differences if any

#### WhatsApp Intent Buttons

Use instead of one generic WhatsApp button when the visitor may have different questions.

Examples:

- Ask About Fee
- Check Batch Timing
- Ask If This Is Right For Me
- Join Trial Class

Each button can prefill a different WhatsApp message.

#### Sticky Enrollment Panel

Desktop:

- place on right side of long subject pages
- include fee, start date, mode, teacher, CTA

Mobile:

- collapse into sticky bottom CTA or compact class summary

#### FAQ Accordion

Use for:

- practical objections
- fee
- timing
- online class questions

Rules:

- first item may be open by default
- no auto animation that causes layout jump

#### Before and After Toggle

Use for:

- exam answer writing
- weak vs strong response
- descriptive vs analytical answer

Purpose:

- make the teaching method visible

#### Scroll Anchor Navigation

Use for:

- SEO pages
- long course pages

Rules:

- desktop sticky nav is allowed
- mobile should be compact or horizontal scroll
- do not cover content

### Interaction Rules

- All buttons need visible hover, focus, and active states.
- All interactive elements must be keyboard accessible.
- Use `aria-expanded` for accordions.
- Use `aria-live="polite"` for dynamic result areas.
- Avoid scroll hijacking.
- Avoid heavy animation on mobile.
- Avoid auto-playing carousels.

## 10. Layout System

### Composition Rules

- Do not center every section.
- Do not use repeated 3-card grids.
- Every page must include at least one asymmetric section.
- Every long page should include either sticky navigation or a sticky CTA.
- Use cards only when comparing separate items.
- Use full-width bands for major transitions.
- Use sticky side panels for enrollment details on desktop.
- Use compact stacked layouts on mobile.
- Keep hero and first CTA visible without awkward scrolling on mobile.

### Layout Families

#### Editorial Split

Best for:

- premium subject pages
- teacher-led pages

Structure:

- large left-aligned heading
- right-side proof, image, or details module
- strong whitespace

#### Product Interface

Best for:

- tools
- school discovery
- admission checkers

Structure:

- tool or controls visible early
- result panel
- status bar
- dynamic content area

#### Sticky Detail Layout

Best for:

- longer subject pages
- enrollment pages

Structure:

- main content on left
- sticky class summary on right

#### Comparison Layout

Best for:

- exam technique
- before and after
- SJ Academy method vs common mistake

Structure:

- two columns
- strong labels
- direct contrast

#### Timeline Layout

Best for:

- teaching process
- batch journey
- exam prep plan

Structure:

- 3 to 5 steps
- visible progress

#### Immersive Hero Layout

Best for:

- major campaigns
- high-importance pages

Structure:

- strong first-viewport visual
- real photo or answer-writing visual
- text overlays only if readable

Avoid:

- decorative SVG scenes when real educational visuals would be better

## 11. Component Rules

### Buttons

Primary:

- orange fill
- white text
- 5px radius
- strong hover lift

Secondary:

- white background
- brown border
- brown text
- hover fills brown

WhatsApp:

- WhatsApp green
- use only for WhatsApp actions

Rules:

- mobile buttons should be full-width when stacked
- CTA labels must describe the action
- avoid generic “Learn More” as the main CTA

### Cards

Default card:

- white background
- 8px radius
- `border-top: 6px solid #453516`
- hover shifts top border to orange

Rules:

- do not use cards for everything
- avoid cards inside cards
- avoid more than one full 3-card grid per page
- use cards when comparing distinct items

### Highlight Text

Use yellow underline marks for short emphasis only.

Rules:

- do not highlight full sentences
- do not combine yellow highlight with orange text

### Tags

Use for:

- exam board
- level
- mode
- paper
- batch status

Avoid:

- too many tags in the hero

### Tables and Matrices

Use for:

- paper breakdown
- fee comparison
- class mode comparison
- course outcomes

Rules:

- make mobile tables stack or scroll cleanly
- do not squeeze text into tiny columns

## 12. Motion Guidelines

Motion should feel responsive and premium, not distracting.

Allowed:

- button lift on hover
- card lift on hover
- subtle reveal on scroll
- tab panel fade
- accordion height animation
- progress indicator
- hover image zoom if subtle

Avoid:

- scroll hijacking
- auto-sliding carousels
- random floating objects
- excessive parallax
- heavy animation on mobile
- animations that delay content visibility

Timing:

- use `cubic-bezier(0.25, 0.46, 0.45, 0.94)`
- keep most transitions between 180ms and 350ms

## 13. Visual Asset Rules

Modern pages need real visual substance. If no visual asset is used, the page must compensate with strong typography, data visuals, answer snippets, or interactive blocks.

Preferred visuals:

- Sir Sunyyan Junaid photo
- real classroom photo
- whiteboard photo
- exam paper or answer-writing visual
- student result proof if permission exists
- WhatsApp chat-style inquiry preview
- timetable or batch card
- location map preview

Avoid:

- generic stock students
- abstract education illustrations
- fake 3D objects
- decorative icons with no meaning
- blurred dark background images

Image rules:

- crop faces carefully
- keep text readable
- avoid large images that slow mobile
- use `loading="lazy"` below the fold
- set explicit width, height, or aspect ratio

## 14. Copy System

### Voice

Write like a confident teacher explaining the offer clearly.

Use:

- clear direct lines
- specific exam language
- short paragraphs
- practical student problems
- proof when available

Avoid:

- “unlock your potential”
- “world-class education”
- “transform your future”
- “best tuition in Karachi” without evidence
- robotic hype
- long abstract paragraphs
- em dashes

### Hero Copy Formula

Use:

> Subject + exam board + student pain + clear outcome + next step

Example:

> A Level Business 9609 classes for students who need stronger case application, analysis chains, and evaluation writing.

### Problem Copy Formula

Use:

> Students are not just losing marks because they forgot content. They are losing marks because their answers do not match the way Cambridge rewards application, analysis, and evaluation.

### CTA Copy Rules

CTA labels should be specific:

- Ask About A Level Business Classes
- Message on WhatsApp
- Check Batch Timings
- Ask About Online Classes
- See Paper Breakdown
- Get Class Details

Avoid:

- Submit
- Learn More
- Get Started
- Click Here

### FAQ Copy Rules

- answer in 2 to 4 lines
- use simple language
- do not hide important details
- say “to be confirmed” if a detail is not final

## 15. Conversion Rules

Every page needs one main conversion goal.

### CTA Hierarchy

Cold traffic:

1. WhatsApp
2. short details request
3. registration only after inquiry or strong intent

Warm traffic:

1. registration
2. WhatsApp support

SEO traffic:

1. WhatsApp
2. short form
3. internal link to related pages

Interactive tools:

1. use the tool
2. show result
3. capture lead or WhatsApp after value

### Form Rules

Only ask for what is needed at that moment.

Cold traffic form should usually ask:

- student name
- parent or student phone
- subject
- level
- preferred mode

Avoid early:

- payment method
- receipt upload
- bank details
- unrelated subjects
- too many fee options
- long multi-step registration before the student has asked questions

### WhatsApp Rules

WhatsApp CTAs should use prefilled messages.

Example:

```text
Hi SJ Academy, I want to ask about A Level Business 9609 classes. Please share batch timings, fee, and whether physical or online classes are available.
```

Intent-specific messages:

- fee inquiry
- timing inquiry
- online class inquiry
- trial class inquiry
- suitability inquiry

## 16. Tracking Rules

Always check whether the page needs:

- WhatsApp click tracking
- Meta Pixel events
- GA4 events
- Google Tag Manager events
- form submission tracking
- thank-you page or confirmation message
- UTM preservation

Recommended event names:

- `whatsapp_click`
- `form_start`
- `form_submit`
- `view_class_details`
- `paper_tab_click`
- `faq_open`
- `batch_mode_toggle`

Recommended event parameters:

- page name
- subject
- level
- CTA label
- CTA location
- traffic source if available

## 17. Accessibility Rules

Required:

- visible focus states
- keyboard accessible tabs and accordions
- readable contrast
- large mobile tap targets
- `aria-expanded` on accordions
- `aria-live="polite"` for dynamic results
- alt text for meaningful images

Avoid:

- tiny text in cards
- hover-only information
- sticky buttons that cover content
- animations that make content hard to read

## 18. Elementor Implementation Rules

When building inside Elementor HTML widgets:

- scope all CSS under a unique wrapper class
- avoid styling global tags without a wrapper
- avoid external libraries unless clearly needed
- preserve header and footer
- keep HTML readable for future editing
- use semantic sections where possible
- keep JavaScript small and isolated
- avoid duplicate IDs if the snippet may be reused

Recommended wrapper pattern:

```html
<section class="sja-lp sja-business-9609">
  ...
</section>
```

Recommended CSS pattern:

```css
.sja-business-9609 {
  font-family: 'Poppins', sans-serif;
  color: #000;
}

.sja-business-9609 .sja-button {
  ...
}
```

## 19. Mobile Rules

Design mobile first.

Mobile requirements:

- hero answer visible quickly
- CTA visible without hunting
- no cramped tabs
- no tiny multi-column grids
- sticky CTA must not cover important content
- forms must be easy to complete
- large tap targets
- images should not push the offer too far down

Mobile layout conversions:

- tabs can become accordions
- side panel becomes sticky CTA or summary block
- comparison tables become stacked cards
- horizontal timelines become vertical timelines
- two-column sections become stacked sections

## 20. Page Review Checklist

Use this before publishing.

### Strategy

- What is the visitor intent?
- What is the one primary conversion goal?
- Is WhatsApp or form the correct first step?
- Does the page match the traffic source?
- Are there any unrelated offers or fields?

### Clarity

- Does the hero explain the offer in 5 seconds?
- Is the subject clear?
- Is the exam board clear?
- Is the teacher clear?
- Is the mode clear?
- Is the next step clear?

### Design

- Does the page avoid repeated 3-card grids?
- Is there at least one asymmetric section?
- Is there at least one meaningful interaction?
- Are visual assets real or useful?
- Does the page feel premium and specific?

### Mobile

- Does the page work well on a phone?
- Are CTAs easy to tap?
- Does text fit cleanly?
- Do sticky elements avoid covering content?
- Are accordions and tabs usable?

### Technical

- Are styles scoped?
- Are scripts isolated?
- Are CTA links correct?
- Are WhatsApp messages correct?
- Are tracking events present?
- Are forms tested?
- Are images optimized?

## 21. AI Builder Prompt

Use this prompt with Codex or Antigravity before asking it to build.

```md
You are building an SJ Academy landing page. Do not jump straight into code.

First, audit the page goal, traffic source, visitor intent, CTA journey, mobile experience, form friction, and tracking needs.

Then propose 3 different visual directions:
1. Premium editorial
2. Interactive product-style
3. Exam-focused conversion page

For each direction, describe:
- hero layout
- main interaction
- section rhythm
- visual assets needed
- CTA journey
- mobile behavior
- trade-offs

Use the SJ Academy Landing Page Creative System:
- Poppins only
- yellow #FCE004 for attention
- orange #FE6100 for primary action
- brown #453516 for structure
- WhatsApp green #25D366 only for WhatsApp
- no purple gradients
- no generic centered hero plus 3 cards
- no repeated 3-card grids
- no robotic copy
- no em dashes
- mobile-first
- at least one meaningful interactive section
- CTA journey must match the visitor intent

Do not implement until I approve one visual direction.
```

## 22. AI Implementation Prompt

Use this after approving a direction.

```md
Build the approved SJ Academy landing page direction.

Implementation requirements:
- preserve the existing WordPress header and footer
- make the page work inside Elementor HTML widgets
- use scoped CSS under a unique wrapper class
- use Poppins
- no unnecessary libraries
- include responsive desktop, tablet, and mobile layouts
- include at least one useful interaction
- include visible focus states
- include sticky mobile WhatsApp CTA if appropriate
- include WhatsApp prefilled messages
- include GA4 or GTM-friendly event hooks where relevant
- keep copy clear, direct, human, and specific
- avoid em dashes
- avoid repeated 3-card grids
- avoid generic AI layout patterns

After building:
- test desktop and mobile layouts
- check for overlapping text
- check all CTA links
- check form or WhatsApp behavior
- summarize what changed
- list anything I need to verify before publishing
```

## 23. Example Page Direction: A Level Business 9609

### Recommended Archetype

Cold paid traffic subject page or teacher-led page.

### Primary CTA

WhatsApp inquiry.

### Hero Direction

Use a direct or problem-first hero:

> A Level Business 9609 classes for students who need stronger case application, analysis chains, and evaluation writing.

Support copy:

> Taught by Sir Sunyyan Junaid at SJ Academy, with physical classes in DHA Phase 7 Karachi and live online support where available.

Primary CTA:

> Ask About A Level Business Classes

### Recommended Structure

1. Hero with class summary and WhatsApp CTA
2. Why students lose marks in Business
3. Paper-by-paper training tabs
4. How Sir Sunyyan teaches answer writing
5. Class details with mode, fee, timing, and location
6. FAQ accordion
7. Final WhatsApp CTA

### Best Interactions

- Paper 1, Paper 2, Paper 3, Paper 4 tabs
- before and after answer-writing comparison
- sticky class detail panel
- sticky mobile WhatsApp CTA
- FAQ accordion

### Avoid

- long generic registration form at the top
- payment fields before inquiry
- unrelated subjects
- vague tuition claims
- repeated cards with no exam detail

## 24. Final Rule

Modern design is not decoration. For SJ Academy, modern design means the page helps a student or parent understand faster, trust faster, compare faster, and contact faster.

If an interaction, section, image, or animation does not help that, remove it.
