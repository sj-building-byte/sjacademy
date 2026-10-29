# Reusable Prompts

Use these prompts to start future SJ Academy tasks with the right context.

## Landing Page Audit Prompt

```text
Audit this SJ Academy landing page as a senior product engineer, conversion strategist, UX auditor, WordPress/Elementor developer, and direct-response copywriter.

Context:
SJ Academy is an O/A Level tuition academy in DHA Phase 7, Karachi. It offers physical and live online classes. The audience is O Level and A Level students and parents in Pakistan. The tone should be confident, clear, teacher-led, premium but not arrogant. Use SJ Academy colors where relevant: #FCE004, #453516, #fe6100, and #25D366.

Audit first. Do not redesign immediately.

Return:
1. Top conversion issues
2. Severity level
3. Why each issue matters
4. Exact fix
5. Recommended simpler structure
6. Copy improvements
7. Technical implementation plan
8. Risks or things I need to verify

Check mobile layout, CTA journey, Elementor usage, forms, WhatsApp links, scripts, tracking, confusing sections, duplicate content, and visitor intent.
```

## Elementor Section Build Prompt

```text
Create a responsive Elementor HTML widget section for SJ Academy.

Rules:
- Preserve the WordPress header and footer.
- Use scoped CSS only.
- Do not use global body selectors.
- Do not add unnecessary libraries.
- Keep the code editable.
- Use Poppins and SJ Academy colors: #FCE004, #453516, #fe6100, #25D366.
- Make the layout mobile-first.
- Keep copy clear, human, and conversion-focused.
- Do not use em dashes.
- Do not add filler sections.
- If WhatsApp or popup links are not supplied, ask or leave placeholders. Do not invent contact details.

Before implementation, inspect the existing structure and recommend the simplest high-impact page structure.
```

## A Level Business Page Prompt

```text
Create or audit an SJ Academy A Level Business 9609 landing page.

Emphasize:
- Sir Sunyyan Junaid as teacher
- CAIE 9609 exam technique
- Application to case data
- Analysis chains
- Evaluation and recommendation writing
- Paper 1, Paper 2, Paper 3, and Paper 4 support where relevant
- Real-world business understanding plus exam-focused answer writing

Avoid generic tuition copy. Do not promise guaranteed grades. Verify exact paper details from the latest Cambridge syllabus before publishing.
```

## Instagram Carousel Prompt

```text
Create an SJ Academy Instagram carousel script for O/A Level students.

Voice:
Direct, intelligent, practical, student-aware, locally relevant, slightly witty, emotionally aware, confident but not arrogant, tactical, and human.

Rules:
- No em dashes.
- No robotic tone.
- No design notes.
- No cover ideas.
- No visual cues.
- No hallucinated facts.
- Use verified information for Cambridge, university, career, paper, syllabus, or policy claims.

Default structure:
1. Post Strategy
2. Five title options
3. Full carousel script, slide by slide
4. Caption
5. Accuracy notes or verification needed

Strong topics:
- Exam tactics
- CAIE guide posts
- Past-paper mistakes
- Mark scheme strategy
- Calculator hacks
- Subject combinations
- Careers and degrees
- University choices
- Parent-facing education decisions
```

## Scholarship Or Opportunity Page Prompt

```text
Research and build an SJ Academy scholarship or student opportunity page for O Level and A Level students.

Rules:
- Use official sources wherever possible.
- Include Pakistan-based and international options unless narrowed.
- Use honest status labels: open, upcoming, closed, paused, deadline passed, or form live.
- Show deadlines clearly.
- Prefer a high-trust shortlist over a broad low-confidence list.
- Re-check statuses at build time.
- Keep the Elementor section scoped and responsive.
- Do not clone another page structure exactly if the user asks for something slightly different.
```

## Tracking QA Prompt

```text
Check this SJ Academy page for conversion tracking and broken user journeys.

Check:
- WhatsApp click tracking
- Meta Pixel events
- GA4 events
- GTM setup if present
- Form submission tracking
- Thank-you page or confirmation message
- UTM preservation
- Popup tracking
- Broken links
- Mobile CTA visibility
- Duplicate event firing

Return issues by severity with exact fixes and what needs verification inside WordPress, Elementor, GA4, GTM, or Meta Events Manager.
```

