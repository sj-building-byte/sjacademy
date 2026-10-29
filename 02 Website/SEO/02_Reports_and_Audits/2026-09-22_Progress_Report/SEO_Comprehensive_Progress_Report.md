# SJ Academy SEO: Complete Comprehensive Progress, History, & AI Handoff Report

**Prepared:** September 22, 2026  
**Project:** SJ Academy SEO Program (`www.sjacademy.pk`)  
**Workspace Path:** `/Users/sunyyanjunaid/Documents/WEbsite SEO`  
**Purpose:** A master context document. This file contains the complete granular record of all SEO audits, growth diagnoses, identified technical faults, the 90-day execution roadmap, and **all necessary technical and brand context for any AI agent or developer joining the project**.

---

## 1. Business Context & Strategic Baseline

Before analyzing data, we verified the core business goals and boundaries for SJ Academy. We are operating a **dual-pronged strategy**:
1. **Tuition Leads & Brand Authority:** Equal focus on physical tuition in DHA Phase 7 (Karachi) and nationwide live online tuition across Pakistan. Positioned as exam-focused, structured, teacher-led (Sir Sunyyan Junaid), and premium (specifically A-Level Business 9609).
2. **Mass Audience & Affiliate Revenue:** Capturing massive top-of-funnel traffic through high-volume, student-lifestyle topics (e.g., Top 10 Laptops for O/A Level students, best study apps, top websites). This traffic serves to build broader brand awareness and generate secondary income via affiliates.

**Competitor Clarification (Teachwink):** Teachwink uses the exact same DHA Phase 7 address as SJ Academy but is a separate, independent competitor. **Rule for agents:** Do not claim Teachwink copied the address without evidence. Reconcile the local SEO address discrepancy with concrete proof.

---

## 2. Phase 1: Comprehensive SEO & Technical Audit (September 10)

We analyzed the site using authenticated Google Search Console (GSC), GA4 data, and a 166-URL public crawl.

### A. Real Search Performance & AI Visibility
* **Traffic (June 8 - Sept 7):** 24.6K clicks, 1.43M impressions, 1.7% CTR.
* **Top Traffic Drivers:** Heavily skewed to informational content. "Karachi schools and fees" drove ~25% of all clicks (6,292 clicks). 
* **AI Search Discovery:** SJ Academy has real visibility in generative AI features (429K AI impressions). GA4 tracked 307 sessions from AI Assistants (like ChatGPT), but no verified revenue/enrolments were tied to these yet.

### B. Technical Crawl & Indexing Health
* **Indexing is Healthy:** 150 of 162 submitted pages are indexed (~92.6%).
* **Core Web Vitals are Failing:** Zero "Good" URLs. 67 "Poor" URLs on mobile (LCP > 4s). Desktop showed 112 "Poor" URLs.
* **Elementor Bloat:** 52 pages had nested `<head>` tags, and 53 had nested `<body>` tags—caused by pasting full HTML documents into Elementor widgets, severely hurting page speed.
* **Missing Metadata:** 37 pages lacked meta descriptions.
* **Embedded Canonical Conflicts:** Yoast SEO provided correct canonicals in the `<head>`, but Elementor body content incorrectly embedded conflicting canonicals on 3 key pages:
  1. A-Level past papers directed to `https://sjacademy.com/a-level-past-papers-faq`
  2. O-Level past papers directed to `https://sjacademy.com/o-level-past-papers-faq`
  3. A-Level subject tool directed to `https://www.sjacademy.pk/career-finder/`
* **Broken Content Journeys (7 Live 404s):**
  1. `/contact-us/` linking to `https://www.sjacademy.pk/contact`
  2. `/lab-practicals/` linking to `/a-level-physics-practicals/`
  3. `/lab-practicals/` linking to `/a-level-chemistry-practicals/`
  4. `/lab-practicals/` linking to `/a-level-biology-practicals/`
  5. `/a-level-subject-combinations-tool/` linking to `/career-finder/`
  6. `/blog/a-level-physics-practical-your-ultimate-guide/` linking to `/a-level-practical-e-book`
  7. `/blog/haque-academy-review/` linking to `https://sjacademy.pk/register`
* **Schema Validation Failure:** All 166 pages used `TutoringService` schema. This is an invalid/unsupported Schema.org type (returns 404).

### C. Conversion & Measurement Faults
* **Broken GA4 Event Logic:** The tracking is highly fragmented. We observed 429 `submit_lead_form` events, 797 `form_start` events, 215 `whatsapp_click` events, but only 46 `generate_lead` events and exactly 7 `form_submit` events. 
* **Conclusion:** We cannot currently separate which channels generate enrolled tuition students versus which channels generate affiliate clicks.
* **Mobile Journey Friction:** The homepage registration popup is too narrow, internally scrollable, and demands too much upfront commitment.

---

## 3. Phase 2: Growth Diagnosis & Strategy Deep Dive (September 11)

We investigated claims that SEO traffic was dropping based on third-party Semrush screenshots, and audited the "Master SEO Progress Report".

### A. Refuting Traffic Declines
* **The Reality:** GSC data showed organic clicks **increased by 21.4%** (9,598 vs 7,907) and impressions grew by 28.4% over the latest 28 days. Semrush's estimated 7% drop was inaccurate.
* **Strategic Adjustment:** The traffic growth came largely from broad informational assets. Previously, this was seen as a failure of commercial SEO. **The corrected strategy:** We must embrace this mass audience by actively monetizing it through affiliate links (laptops, apps, resources) while *simultaneously* building out high-intent commercial hubs (like Business 9609) for tuition leads.

### B. Overruling the Prior Master SEO Progress Report
* The previous report incorrectly claimed "Technical SEO is completed" (disproved by canonicals and Core Web Vitals).
* It incorrectly tracked "Organic Impressions" as a success KPI for commercial tuition pages.
* **The Pivot:** We will measure success on two separate tracks. 
  1. *Affiliate/Audience Track:* Measured by sheer traffic volume and affiliate link clicks.
  2. *Tuition Track:* Measured exclusively by qualified leads and demo bookings (starting with the Business 9609 pilot).

---

## 4. Phase 3: IBCC Calculator Strict Policy Audit (September 11)

The drafted IBCC Calculator tool was rigorously audited for mathematical accuracy, official policy compliance, and UI/UX. **We blocked its publication.**

### A. Critical Grading & Math Errors
* **A* Hardcoded to 100:** Based on IBCC's July 2026 notification, A* varies by subject and year (e.g., Physics = 94).
* **Letter Grade Inflation:** Incorrectly awarded A/B/C/D/E grades an excess of 5 marks.
* **Blank/Fail Grades Ignored:** Blank or 'U' grades were silently counted as zero but allowed the calculator to output a "finished" percentage.

### B. Cohort & Policy Errors
* Failed to apply the February 2026 IBCC notice for Science students.
* Conflated local SSC (/800), overseas SSC (/500), and overseas HSSC scales.

### C. UI & Accessibility Failures
* **Contrast:** White CTA text on Orange (`#FE6100`) failed WCAG contrast ratios (3.03:1).
* **Data Loss:** Switching between routes deleted all previously entered grades.

---

## 5. Developer & AI Agent Context (Crucial for Handoffs)

If you are an AI agent or developer continuing this project, **you must adhere to the following environment rules, brand guidelines, and workspace structure.**

### A. Tech Stack & Environment
Assume the following stack is in use on `www.sjacademy.pk`:
* **CMS:** WordPress
* **Theme:** Educrat
* **Page Builder:** Elementor & Pro Elements
* **Active Plugins/Scripts:** Yoast SEO, WPForms, WP-Optimize, Site Kit, PixelYourSite, Joinchat, Slider Revolution.

### B. Brand & Design Guidelines
* **Brand Colors:** Yellow (`#FCE004`), Brown (`#453516`), Orange (`#fe6100`), WhatsApp Green (`#25D366`).
* **Copywriting Rules:** No em dashes. Keep copy natural. WhatsApp-first CTAs for cold traffic. Don't force full enrolment forms early.

### C. Development & AI Working Rules
* **Audit First:** Recheck live URLs before making edits.
* **Do Not Break WordPress:** Preserve the WordPress header and footer.
* **CSS Scoping:** Use scoped, responsive CSS if editing Elementor widgets. Do not inject full `<html>` or `<body>` wrappers inside widgets.

### D. Workspace Structure Reference (`/Users/sunyyanjunaid/Documents/WEbsite SEO/`)
* `/SEO_Audit_2026_09_10/`: Original full audit PDF, exact crawl data, python scripts.
* `/SEO_Deep_Dive_2026_09_11/`: Growth Diagnosis refuting Semrush data.
* `/IBCC_Audit_2026_09_11/`: Calculator audit, flawed HTML, `patch_ui.py` script.
* `/HTML_Tools_and_Drafts/`: Raw HTML tools and landing page drafts.

---

## 6. The Comprehensive 90-Day Implementation Roadmap

### Priority 0: Accuracy and Trust
* **IBCC Calculator:** Rebuild the logic engine accurately (no 'U' grade calculation, correct 2026 A* values).
* **Subject Combinations:** Correct the A-Level guide with official university criteria.
* **Factual Reconciliation:** Align all fees, batch dates, and result claims across the site.

### Priority 1: Technical Cleanup & Measurement
* **Technical Fixes:** Repair 7 broken links, delete 3 embedded Elementor canonicals, fix 37 missing meta descriptions.
* **Core Web Vitals:** Strip full HTML document wrappers out of Elementor widgets.
* **GA4 Tracking (Two Tracks):** Separate tracking for `generate_lead` (Tuition) vs. `affiliate_click` (Monetized Content).

### Priority 2: Commercial Conversion & Mass Audience Scaling
* **Business 9609 Pilot (Tuition Track):** Overhaul this hub using teacher evidence. Include topic-level paper indexes, answer frameworks, and clear paths to tuition. 
* **High-Volume Listicles (Affiliate Track):** Produce highly optimized, AI-citation-ready content targeting mass student audiences (e.g., "Top 10 Laptops for O/A Level Students", "Best Apps for Studying"). 
* **Homepage Journey:** Simplify the hero section and replace the registration popup with a low-friction CTA.

### Priority 3: Authority & AI Strategy
* **Local SEO:** Resolve the Teachwink address discrepancy. Secure honest Google Business Profile reviews.
* **AI Citations:** Optimize both the tuition pilot and the mass-audience listicles for LLM discovery (ChatGPT, Perplexity).
* **Reporting Dashboard:** Unified dashboard tracking: *Qualified organic enquiries*, *Affiliate Clicks*, and *AI Impressions*.
