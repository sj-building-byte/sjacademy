# 04 - Career Pathway & A-Level Subject Combination Finder

> **Type:** Interactive Diagnostic Quiz / Lead Generation & Educational Guidance Tool  
> **Brand / Project:** SJ Academy (`sjacademy.pk/career-finder/`)  
> **Target Audience:** O-Level graduates and prospective A-Level students in Pakistan choosing subject combinations and university career directions.

---

## 1. Overview & Strategic Goals

The **Career Pathway Finder** is an interactive 6-step diagnostic quiz that guides students through selecting the optimal A-Level subject combinations based on:
1. **O-Level Background & Grade Standing** (with category accordions and grade performance boosting)
2. **Subject Interests & Academic Passions**
3. **Personal Cognitive Strengths**
4. **Work Style & Career Preferences**
5. **Subject Constraints / Avoidance Rules** (e.g., avoiding Biology, Math, or heavy-writing subjects)

### Core Outputs Generated:
- **Top 3 Matched Career & Academic Clusters** (with match strength labels: *Excellent match*, *Good match*, *Consider*).
- **Curated A-Level Subject Combinations** (highlighting popular tracks & tailored notes).
- **Target Degree Programs** (e.g., MBBS, Software Engineering, BBA, Architecture, LLB).
- **Matching Pakistani & International Universities** (NUST, LUMS, IBA, GIKI, FAST, AKU, NCA, UET, etc. with direct application links).
- **Shareable Action Plan**: "Copy Plan" clipboard tool and "Send My Plan" email generation to facilitate parent/counselor discussions.
- **Conversion Hook**: Direct WhatsApp advisory link (`+92 336 2144454`).

---

## 2. Design System & Tokens

### Typography & Fonts
- **Font Family:** `'Poppins', sans-serif` (Weights: `300`, `400`, `600`, `700`, `800`)

### Color Palette

| Token | Hex Value | Purpose |
| :--- | :--- | :--- |
| `--sja-yellow` | `#FCE004` | Selected option pills, result badges, hero pill accent |
| `--sja-light-yellow` | `#FFF9CC` | Hover pill backgrounds, result header gradient, strength notes |
| `--sja-brown` | `#453516` | Card top borders, option pill borders, secondary buttons |
| `--sja-orange` | `#FE6100` | Primary action buttons, progress indicators, popular combo badges |
| `--sja-orange-dark` | `#E55800` | Button hover state |
| `--sja-black` | `#000000` | Headings and high-contrast text |
| `--sja-dark-grey` | `#222222` | Subheadings and body copy |
| `--sja-grey` | `#555555` | Labels, notes, metadata |
| `--sja-light-bg` | `#FAFAFA` | Quiz container backdrop, combo card backgrounds |
| `--sja-border-light` | `#E5E5E5` | Form borders and dividers |

### Interactive Tokens & Styling Details
- **Tactile Pill Buttons:** Custom border radius (`40px`), `1.5px solid var(--sja-brown)`, with `3px 3px 0 rgba(0,0,0,0.08)` drop shadow.
- **Dual Progress Indicator:** Centered progress bar on desktop; sticky header progress bar on mobile (`#sj-sticky`).
- **Result Cards:** Card hover elevation (`translateY(-10px)` with `box-shadow: 0 20px 40px rgba(0,0,0,0.1)`), top border shifting from brown to yellow/orange.

---

## 3. Architecture & User Flow

```
Quiz Funnel
├── Header Area
│   ├── Mode Badge ("Career Finder")
│   ├── H1 ("A Level Subject Combinations" with highlight)
│   ├── Subtitle & Progress Bar (Desktop)
│   └── Sticky Progress Bar (Mobile)
│
├── Step 1: O-Level Subject Selection & Grade Standing
│   ├── Accordion Category Groups (Sciences, Math, Languages/Humanities, Business, Creative)
│   └── Performance Selector (Mostly A*/A, Mix of A/B/C, Mostly B/C)
│
├── Step 2: Subject Interests (Multi-select)
├── Step 3: Cognitive & Personal Strengths (Multi-select)
├── Step 4: Work Style (Single-select)
├── Step 5: Preferences & Work Environment (Multi-select)
├── Step 6: Constraints & Avoidance Rules (Multi-select)
│
└── Results Dashboard
    ├── Best Fit Summary Banner ("Most sensible path right now")
    ├── 3-Column Results Grid (Subject Combos + Degree Tags + University Matches)
    ├── Action Bar (Copy Plan to Clipboard + WhatsApp Consultation)
    ├── Email Plan Capture Card
    └── Restart Quiz Trigger
```

---

## 4. Scoring Logic & Career Clusters

### 10 Pre-Configured Career Clusters
1. **Engineering & Technology (`eng_tech`):** Mechanical, Electrical, Civil, Mechatronics (NUST, UET, GIKI, LUMS).
2. **Computer Science & Data (`cs_data`):** CS, Software Eng, Data Science, AI & ML (FAST, LUMS, NUST, GIKI).
3. **Medicine & Health (`medicine`):** MBBS, BDS, Pharmacy, Biomed (AKU, NUMS, Dow, KEMU).
4. **Business, Finance & Economics (`biz_econ`):** Economics, Finance, Accounting, BBA (IBA Karachi, LUMS SDSB, LSE, NBS NUST).
5. **Law & Social Sciences (`law_social`):** LLB, International Relations, Public Policy, Sociology, Psychology (LUMS, IBA, QAU, LSE).
6. **Creative, Media & Communication (`creative_media`):** Design, Media, Journalism, UI/UX, Advertising (BNU, NCA, SZABIST, LUMS).
7. **Architecture & Built Environment (`arch_design`):** Architecture, Urban Planning, Interior Design (NCA, UET, NED, COMSATS).
8. **Pure Sciences & Research (`pure_science`):** Physics, Chemistry, Pure Math, Biotech (LUMS SBASSE, QAU, GIKI, COMSATS).
9. **Education & Human Development (`education_psych`):** Education, Counseling, EdTech (AKU, QAU, BNU, LUMS).
10. **Hospitality, Tourism & Events (`hospitality`):** Hospitality Management, Tourism, Event Management (SZABIST, IBA).

### Constraint & Avoidance Filter Engine
If a student selects avoidance criteria (e.g. `avoid_bio`, `avoid_math`, `avoid_physics`, `avoid_chem`), the algorithm automatically filters out incompatible subject combinations from the recommendations while penalty-weighting relevant clusters.

---

## 5. Complete Source Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Discover Your A Level Subjects combinations| SJ Academy</title>
  <meta name="description" content="Answer a few quick questions and discover the best A Level subject combinations, degree directions, and career clusters for you. Free tool by SJ Academy.">
  <meta name="keywords" content="career pathway finder, A Level subject combination, which A Levels should I take, career quiz Pakistan, university subject guide, SJ Academy">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.sjacademy.pk/career-finder/">
  <meta property="og:title" content="Career Pathway Finder | SJ Academy">
  <meta property="og:description" content="Discover the best A Level subject combinations and career clusters for you. Free tool by SJ Academy.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.sjacademy.pk/career-finder/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --sja-yellow: #FCE004;
      --sja-brown: #453516;
      --sja-black: #000000;
      --sja-orange: #FE6100;
      --sja-orange-dark: #e55800;
      --sja-white: #FFFFFF;
      --sja-grey: #555555;
      --sja-dark-grey: #222222;
      --sja-light-bg: #FAFAFA;
      --sja-light-yellow: #FFF9CC;
      --sja-border-light: #e5e5e5;
      --sja-shadow-card: 0 10px 25px rgba(0,0,0,0.05);
      --sja-shadow-card-hover: 0 20px 40px rgba(0,0,0,0.1);
      --sja-shadow-button: 0 4px 10px rgba(254,97,0,0.3);
      --sja-shadow-button-hover: 0 10px 20px rgba(254,97,0,0.4);
      --sja-transition: cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Poppins', sans-serif;
      background: var(--sja-white);
      color: var(--sja-black);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }

    html { scroll-behavior: smooth; }
    #sj-career-finder, #sj-career-finder * { user-select: text; }
    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

    /* ===== HEADER ===== */
    .sja-header {
      background: var(--sja-white);
      padding: 60px 0 40px;
      text-align: center;
    }

    .sja-badge {
      display: inline-block;
      background-color: var(--sja-white);
      border: 2px solid var(--sja-black);
      border-radius: 50px;
      padding: 5px;
      margin-bottom: 25px;
      box-shadow: 4px 4px 0px rgba(0,0,0,0.15);
    }

    .sja-mode-pill {
      padding: 8px 20px;
      border-radius: 40px;
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      line-height: 1;
    }

    .sja-mode-pill--career {
      background-color: var(--sja-yellow);
      color: var(--sja-black);
    }

    .sja-title {
      font-size: 2.8rem;
      font-weight: 800;
      color: var(--sja-black);
      margin: 0 0 20px 0;
      line-height: 1.2;
    }

    .sja-subtitle {
      font-size: 1.1rem;
      color: var(--sja-dark-grey);
      margin: 0 auto 30px;
      max-width: 650px;
      font-weight: 400;
    }

    .sja-highlight {
      background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%);
      background-repeat: no-repeat;
      background-size: 100% 35%;
      background-position: 0 85%;
      display: inline;
      color: var(--sja-black);
      padding: 0 3px;
    }

    /* ===== PROGRESS ===== */
    .sja-progress-wrap {
      max-width: 400px;
      margin: 0 auto;
    }

    .sja-progress {
      height: 10px;
      background: var(--sja-light-bg);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid #e5e5e5;
    }

    .sja-progress > div {
      height: 100%;
      background: var(--sja-orange);
      border-radius: 999px;
      width: 0%;
      transition: width 0.4s var(--sja-transition);
    }

    .sja-progress-label {
      font-size: 12px;
      color: var(--sja-grey);
      text-align: center;
      margin-top: 8px;
      font-weight: 600;
    }

    /* ===== STICKY PROGRESS (Mobile) ===== */
    .sja-sticky-progress {
      display: none;
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--sja-white);
      padding: 10px 20px;
      border-bottom: 1px solid #eee;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .sja-sticky-progress .sja-sticky-inner {
      max-width: 800px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .sja-sticky-progress .sja-sticky-label {
      font-size: 12px;
      font-weight: 700;
      color: var(--sja-dark-grey);
      white-space: nowrap;
      min-width: 80px;
    }

    .sja-sticky-progress .sja-progress {
      flex: 1;
      height: 8px;
    }

    .sja-sticky-progress .sja-sticky-pct {
      font-size: 12px;
      font-weight: 700;
      color: var(--sja-orange);
      min-width: 36px;
      text-align: right;
    }

    @media (max-width: 767px) {
      .sja-sticky-progress { display: block; }
    }

    /* ===== QUIZ SECTION ===== */
    .sja-quiz-section {
      padding: 40px 0 60px;
      background: var(--sja-light-bg);
      border-top: 1px solid #eee;
      border-bottom: 1px solid #eee;
    }

    .sja-quiz-inner {
      max-width: 800px;
      margin: 0 auto;
    }

    /* ===== QUESTION CARD ===== */
    .qcard {
      background: var(--sja-white);
      padding: 30px;
      border-top: 6px solid var(--sja-brown);
      border-radius: 8px;
      box-shadow: var(--sja-shadow-card);
      margin-bottom: 20px;
    }

    .qtitle {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--sja-black);
      margin-bottom: 20px;
      line-height: 1.3;
    }

    .qstep-label {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--sja-orange);
      margin-bottom: 10px;
    }

    /* ===== OPTION PILLS ===== */
    .optgrid {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .opt {
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 18px;
      border-radius: 40px;
      border: 1.5px solid var(--sja-brown);
      background: var(--sja-white);
      color: var(--sja-black);
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 3px 3px 0 rgba(0,0,0,0.08);
      min-height: 42px;
      display: inline-flex;
      align-items: center;
    }

    .opt:hover {
      background: var(--sja-light-yellow);
      border-color: var(--sja-brown);
    }

    .opt.selected {
      background: var(--sja-yellow);
      border-color: var(--sja-brown);
      color: var(--sja-black);
      box-shadow: 3px 3px 0 rgba(0,0,0,0.12);
    }

    .opt:focus {
      outline: 3px solid var(--sja-orange);
      outline-offset: 2px;
    }

    /* ===== O LEVEL CATEGORY GROUPS ===== */
    .olevel-categories {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .olevel-category {
      background: var(--sja-light-bg);
      border: 1px solid #eee;
      border-radius: 8px;
      overflow: hidden;
    }

    .olevel-cat-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      cursor: pointer;
      font-weight: 700;
      font-size: 13px;
      color: var(--sja-brown);
      user-select: none;
      transition: background 0.2s ease;
    }

    .olevel-cat-header:hover {
      background: rgba(252,224,4,0.1);
    }

    .olevel-cat-header .arrow {
      transition: transform 0.3s ease;
      font-size: 11px;
    }

    .olevel-cat-header.open .arrow {
      transform: rotate(180deg);
    }

    .olevel-cat-body {
      padding: 0 16px 14px;
      display: none;
    }

    .olevel-cat-body.open {
      display: block;
    }

    .olevel-cat-count {
      font-size: 11px;
      color: var(--sja-grey);
      font-weight: 500;
    }

    /* ===== PERFORMANCE SELECT ===== */
    .perf-select {
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid #eee;
    }

    .perf-select label {
      display: block;
      font-weight: 700;
      font-size: 14px;
      color: var(--sja-black);
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* ===== NAVIGATION ===== */
    .sja-nav-row {
      display: flex;
      gap: 12px;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }

    @media (max-width: 767px) {
      .sja-nav-row { flex-direction: column; }
    }

    /* ===== BUTTONS ===== */
    .sja-btn {
      font-family: 'Poppins', sans-serif;
      transition: all 0.3s var(--sja-transition);
      text-decoration: none;
      border-radius: 5px;
      text-transform: uppercase;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      cursor: pointer;
      border: 2px solid transparent;
      padding: 14px 30px;
      font-size: 14px;
      letter-spacing: 0.3px;
      min-width: 140px;
    }

    .sja-btn:focus {
      outline: 3px solid var(--sja-orange);
      outline-offset: 2px;
    }

    .sja-btn-primary {
      background: var(--sja-orange);
      color: var(--sja-white);
      border-color: var(--sja-orange);
      box-shadow: var(--sja-shadow-button);
    }

    .sja-btn-primary:hover {
      background: var(--sja-orange-dark);
      border-color: var(--sja-orange-dark);
      transform: translateY(-3px);
      box-shadow: var(--sja-shadow-button-hover);
    }

    .sja-btn-outline {
      background: var(--sja-white);
      color: var(--sja-brown);
      border-color: var(--sja-brown);
    }

    .sja-btn-outline:hover {
      background: var(--sja-brown);
      color: var(--sja-white);
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(69,53,22,0.3);
    }

    .sja-btn-whatsapp {
      background: #25D366;
      color: var(--sja-white);
      border-color: #25D366;
      box-shadow: 0 4px 10px rgba(37,211,102,0.3);
    }

    .sja-btn-whatsapp:hover {
      background: #1ebe57;
      border-color: #1ebe57;
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(37,211,102,0.4);
    }

    .sja-btn[disabled] {
      background: #ccc;
      color: #666;
      border-color: #ccc;
      cursor: not-allowed;
      opacity: 0.6;
      transform: none !important;
      box-shadow: none !important;
    }

    .sja-btn[disabled]:hover {
      background: #ccc;
      border-color: #ccc;
      transform: none;
      box-shadow: none;
    }

    .sja-btn svg { width: 16px; height: 16px; fill: currentColor; }

    @media (max-width: 767px) {
      .sja-btn { width: 100%; }
    }

    /* ===== RESET LINK ===== */
    .sja-reset-link {
      display: block;
      text-align: center;
      margin-top: 16px;
    }

    .sja-reset-link a {
      color: var(--sja-grey);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: color 0.2s ease;
    }

    .sja-reset-link a:hover {
      color: var(--sja-orange);
      text-decoration: underline;
    }

    /* ===== VALIDATION ===== */
    .sja-validation {
      font-size: 13px;
      color: #b00020;
      margin-top: 10px;
      font-weight: 500;
    }

    /* ===== RESULTS SECTION ===== */
    .sja-results-section {
      padding: 60px 0;
      background: var(--sja-white);
    }

    /* ===== RESULTS HEADER ===== */
    .sja-results-header {
      padding: 30px;
      border-top: 6px solid var(--sja-yellow);
      border-radius: 8px;
      box-shadow: var(--sja-shadow-card);
      margin-bottom: 30px;
      text-align: center;
      background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #fff6b8 100%);
    }

    .sja-results-header h2 {
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--sja-black);
      margin-bottom: 8px;
    }

    .sja-results-header .sja-results-sub {
      font-size: 14px;
      color: var(--sja-grey);
    }

    .sja-best-path {
      margin-top: 16px;
      background: var(--sja-white);
      border: 1px solid #e5e5e5;
      border-radius: 8px;
      padding: 16px 20px;
      text-align: left;
    }

    .sja-best-path .k {
      font-weight: 700;
      font-size: 14px;
      color: var(--sja-black);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .sja-best-path .v {
      font-size: 14px;
      color: #444;
      line-height: 1.6;
    }

    /* ===== RESULTS GRID ===== */
    .sja-results-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
    }

    @media (min-width: 768px) {
      .sja-results-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (min-width: 992px) {
      .sja-results-grid { grid-template-columns: repeat(3, 1fr); }
    }

    /* ===== RESULT CARD ===== */
    .sja-result-card {
      background: var(--sja-white);
      padding: 30px;
      border-top: 6px solid var(--sja-brown);
      border-radius: 8px;
      box-shadow: var(--sja-shadow-card);
      transition: transform 0.3s var(--sja-transition), box-shadow 0.3s var(--sja-transition), border-color 0.3s var(--sja-transition);
      height: 100%;
      display: flex;
      flex-direction: column;
    }

    .sja-result-card:hover {
      transform: translateY(-10px);
      box-shadow: var(--sja-shadow-card-hover);
      border-top-color: var(--sja-orange);
    }

    .sja-result-card.sja-best {
      border-top-color: var(--sja-yellow);
      background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #fffef5 100%);
    }

    .sja-result-card.sja-best:hover {
      border-top-color: var(--sja-orange);
    }

    .sja-result-card h3 {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--sja-black);
      margin: 0 0 6px 0;
      line-height: 1.2;
    }

    .sja-result-card .sja-cluster-blurb {
      font-size: 14px;
      color: var(--sja-grey);
      margin-bottom: 16px;
    }

    /* ===== MATCH BADGE ===== */
    .sja-match-badge {
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 4px 12px;
      border-radius: 40px;
      margin-bottom: 14px;
    }

    .sja-match-excellent {
      background: var(--sja-yellow);
      color: var(--sja-black);
      border: 1.5px solid var(--sja-brown);
      box-shadow: 2px 2px 0 rgba(0,0,0,0.08);
    }

    .sja-match-good {
      background: var(--sja-light-bg);
      color: var(--sja-dark-grey);
      border: 1.5px solid var(--sja-border-light);
      box-shadow: 2px 2px 0 rgba(0,0,0,0.04);
    }

    .sja-match-consider {
      background: var(--sja-white);
      color: var(--sja-grey);
      border: 1.5px solid var(--sja-border-light);
    }

    /* ===== KEY-VALUE ===== */
    .sja-kv { flex-grow: 1; }

    .sja-kv .row {
      margin-bottom: 20px;
      padding-bottom: 20px;
      border-bottom: 1px solid #eee;
    }

    .sja-kv .row:last-child {
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }

    .sja-kv .k {
      font-weight: 700;
      font-size: 14px;
      color: var(--sja-black);
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .sja-kv .v {
      font-size: 14px;
      color: #444;
      line-height: 1.6;
    }

    /* ===== COMBO CARDS ===== */
    .sja-combo {
      background: var(--sja-light-bg);
      border: 1px solid #eee;
      border-radius: 8px;
      padding: 14px 16px;
      margin-bottom: 10px;
      transition: border-color 0.2s ease;
    }

    .sja-combo:last-child { margin-bottom: 0; }
    .sja-combo:hover { border-color: var(--sja-yellow); }

    .sja-combo-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .sja-combo-title {
      font-weight: 700;
      font-size: 14px;
      color: var(--sja-black);
    }

    .sja-popular-badge {
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 2px 8px;
      border-radius: 40px;
      background: var(--sja-orange);
      color: var(--sja-white);
      white-space: nowrap;
    }

    .sja-combo-notes {
      font-size: 12px;
      color: var(--sja-grey);
      font-style: italic;
      margin-top: 6px;
    }

    /* ===== SUBJECT TAGS ===== */
    .sja-subject-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }

    .sja-subject-tag {
      display: inline-block;
      background: var(--sja-yellow);
      color: var(--sja-black);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 40px;
      border: 1px solid var(--sja-brown);
      box-shadow: 2px 2px 0 rgba(0,0,0,0.06);
    }

    .sja-subject-tag.strong {
      background: var(--sja-yellow);
      border-color: var(--sja-brown);
    }

    .sja-subject-tag.weak {
      background: var(--sja-light-bg);
      border-color: var(--sja-border-light);
      color: var(--sja-grey);
    }

    /* ===== DEGREE TAGS ===== */
    .sja-degree-list {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .sja-degree-tag {
      display: inline-block;
      background: var(--sja-light-bg);
      color: var(--sja-dark-grey);
      font-size: 12px;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 40px;
      border: 1px solid var(--sja-border-light);
    }

    /* ===== UNIVERSITY MATCHES ===== */
    .sja-uni-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .sja-uni-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
      background: var(--sja-light-bg);
      border: 1px solid #eee;
      border-radius: 8px;
      transition: border-color 0.2s ease;
    }

    .sja-uni-item:hover { border-color: var(--sja-yellow); }

    .sja-uni-name {
      font-weight: 700;
      font-size: 13px;
      color: var(--sja-black);
    }

    .sja-uni-program {
      font-size: 12px;
      color: var(--sja-grey);
    }

    .sja-uni-link {
      font-size: 12px;
      font-weight: 700;
      color: var(--sja-orange);
      text-decoration: none;
      white-space: nowrap;
      transition: color 0.2s ease;
    }

    .sja-uni-link:hover { color: var(--sja-brown); }

    /* ===== STRENGTH NOTE ===== */
    .sja-strength-note {
      font-size: 12px;
      color: var(--sja-grey);
      padding: 8px 12px;
      background: var(--sja-light-yellow);
      border-radius: 6px;
      margin-top: 6px;
      border-left: 3px solid var(--sja-yellow);
    }

    .sja-strength-note.weak {
      background: #fff5f5;
      border-left-color: #e57373;
      color: #b00020;
    }

    /* ===== FILTERED MSG ===== */
    .sja-filtered-msg {
      font-size: 13px;
      color: var(--sja-grey);
      font-style: italic;
      padding: 10px 0;
    }

    /* ===== META ===== */
    .sja-meta {
      font-size: 13px;
      color: #666;
      font-style: italic;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid #eee;
    }

    .sja-meta a {
      color: var(--sja-orange);
      text-decoration: none;
      font-weight: 600;
      transition: color 0.2s ease;
    }

    .sja-meta a:hover {
      color: var(--sja-brown);
      text-decoration: underline;
    }

    /* ===== EMAIL CAPTURE ===== */
    .sja-email-section {
      background: var(--sja-white);
      padding: 30px;
      border-top: 6px solid var(--sja-brown);
      border-radius: 8px;
      box-shadow: var(--sja-shadow-card);
      margin-top: 30px;
      text-align: center;
    }

    .sja-email-section h3 {
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 6px;
    }

    .sja-email-section .sja-email-sub {
      font-size: 14px;
      color: var(--sja-grey);
      margin-bottom: 20px;
    }

    .sja-email-form {
      display: flex;
      gap: 10px;
      max-width: 450px;
      margin: 0 auto;
    }

    .sja-email-form input {
      flex: 1;
      padding: 14px 18px;
      border: 2px solid var(--sja-border-light);
      border-radius: 5px;
      font-family: 'Poppins', sans-serif;
      font-size: 15px;
      font-weight: 500;
      outline: none;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .sja-email-form input:focus {
      border-color: var(--sja-orange);
      box-shadow: 0 0 0 3px rgba(254,97,0,0.1);
    }

    @media (max-width: 767px) {
      .sja-email-form { flex-direction: column; }
    }

    .sja-email-success {
      display: none;
      padding: 16px;
      background: var(--sja-light-yellow);
      border: 1px solid var(--sja-yellow);
      border-radius: 8px;
      margin-top: 16px;
      font-size: 14px;
      color: var(--sja-dark-grey);
      font-weight: 500;
    }

    /* ===== RESULTS ACTIONS ===== */
    .sja-results-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
      margin-top: 30px;
    }

    .sja-results-restart {
      text-align: center;
      margin-top: 16px;
    }

    .sja-results-restart a {
      color: var(--sja-grey);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: color 0.2s ease;
    }

    .sja-results-restart a:hover {
      color: var(--sja-orange);
      text-decoration: underline;
    }

    /* ===== FOOTER ===== */
    footer {
      text-align: center;
      padding: 30px 20px;
      border-top: 1px solid #eee;
      background: var(--sja-light-bg);
    }

    footer .meta {
      font-size: 12px;
      color: #666;
      font-style: italic;
    }

    footer .meta a {
      color: var(--sja-orange);
      text-decoration: none;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    footer .meta a:hover { color: var(--sja-brown); }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 767px) {
      .sja-header { padding: 40px 0 30px; }
      .sja-title { font-size: 2.2rem; }
      .sja-quiz-section { padding: 30px 0 40px; }
      .sja-results-section { padding: 40px 0; }
      .qcard { padding: 20px; }
      .sja-result-card { padding: 25px; }
      .sja-results-header { padding: 25px; }
      .sja-email-section { padding: 25px; }
      .qtitle { font-size: 1.15rem; }
      .opt { font-size: 12px; padding: 9px 14px; }
    }

    @media (min-width: 992px) {
      .sja-title { font-size: 3.8rem; }
    }
  </style>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Career Pathway Finder",
    "description": "Answer a few quick questions and discover the best A Level subject combinations, degree directions, and career clusters for you.",
    "url": "https://www.sjacademy.pk/career-finder/",
    "publisher": {
      "@type": "Organization",
      "name": "SJ Academy",
      "url": "https://www.sjacademy.pk"
    }
  }
  </script>
</head>
<body>

  <div id="sj-career-finder">

    <!-- Header -->
    <section class="sja-header">
      <div class="container">
        <div class="sja-badge">
          <div class="sja-mode-pill sja-mode-pill--career">
            <span>Career Finder</span>
          </div>
        </div>
        <h1 class="sja-title">A Level <span class="sja-highlight">Subject Combinations</span></h1>
        <p class="sja-subtitle">Answer a few quick questions. We will suggest degree and career clusters plus A Level subject combinations that suit you.</p>
        <div class="sja-progress-wrap">
          <div class="sja-progress"><div id="sj-progress"></div></div>
          <div class="sja-progress-label" id="sj-progress-label">Question 1 of 6</div>
        </div>
      </div>
    </section>

    <!-- Sticky Progress (Mobile) -->
    <div class="sja-sticky-progress" id="sj-sticky">
      <div class="sja-sticky-inner">
        <div class="sja-sticky-label" id="sj-sticky-label">Q1 of 6</div>
        <div class="sja-progress"><div id="sj-sticky-bar"></div></div>
        <div class="sja-sticky-pct" id="sj-sticky-pct">17%</div>
      </div>
    </div>

    <!-- Quiz -->
    <section class="sja-quiz-section">
      <div class="container">
        <div class="sja-quiz-inner">
          <div id="sj-quiz"></div>
        </div>
      </div>
    </section>

    <!-- Results -->
    <section id="sj-results" class="sja-results-section" style="display:none;">
      <div class="container">
        <div id="sj-results-inner"></div>
      </div>
    </section>

    <footer>
      <div class="container">
        <p class="meta">Guidance only. Always check university subject requirements before finalizing choices. Built with care by <a href="https://www.sjacademy.pk">SJ Academy</a>.</p>
      </div>
    </footer>

  </div>

<script>
(function(){
  const OLEVEL_CATEGORIES = [
    { name: "Sciences", subjects: [["physics","Physics"],["chemistry","Chemistry"],["biology","Biology"],["cs","Computer Science"]] },
    { name: "Mathematics", subjects: [["math","Mathematics"],["addmath","Additional Mathematics"]] },
    { name: "Languages & Humanities", subjects: [["english","English Language"],["urdu","Urdu"],["isl","Islamiat"],["pkstd","Pakistan Studies"],["history","History"]] },
    { name: "Business & Social Sciences", subjects: [["econ","Economics"],["business","Business Studies"],["accounting","Accounting"],["sociology","Sociology"]] },
    { name: "Creative & Other", subjects: [["art","Art & Design"],["geo","Geography"],["envmgmt","Environmental Management"]] }
  ];

  const CLUSTERS = [
    { id: "eng_tech", name: "Engineering & Technology", blurb: "Build systems, products, and infrastructure.", subjectCombos: [
      {title:"Core Engineering", subjects:["Math","Physics","Chemistry"], notes:"Most engineering programs expect Math and Physics.", popular:true},
      {title:"CS-leaning Engineering", subjects:["Math","Physics","Computer Science"], notes:"Good for Electrical, Computer, Mechatronics.", popular:true},
      {title:"Design + Build", subjects:["Math","Physics","Art & Design"], notes:"Useful for product and industrial design."}
    ], degrees:["Mechanical","Electrical","Civil","Mechatronics","Industrial Engineering"],
    uniMatches:[
      {uni:"NUST",program:"Engineering (all)",url:"https://www.nust.edu.pk"},
      {uni:"UET Lahore",program:"Engineering (all)",url:"https://www.uet.edu.pk"},
      {uni:"GIKI",program:"Engineering",url:"https://giki.edu.pk"},
      {uni:"LUMS",program:"SBASSE Engineering",url:"https://admissions.lums.edu.pk"}
    ]},
    { id: "cs_data", name: "Computer Science & Data", blurb: "Create software and work with data.", subjectCombos:[
      {title:"Pure CS", subjects:["Math","Computer Science","Physics"], notes:"Classic combo for CS, AI, Software.", popular:true},
      {title:"Data & Stats", subjects:["Math","Computer Science","Further Math"], notes:"Strong for Data Science and ML."},
      {title:"CS + Business", subjects:["Math","Computer Science","Economics"], notes:"Great for product and analytics.", popular:true}
    ], degrees:["Computer Science","Software Engineering","Data Science","AI & ML","Information Systems"],
    uniMatches:[
      {uni:"FAST",program:"Computer Science",url:"https://www.nu.edu.pk"},
      {uni:"LUMS",program:"CS (SBASSE)",url:"https://admissions.lums.edu.pk"},
      {uni:"NUST",program:"SEECS (CS & SE)",url:"https://www.nust.edu.pk"},
      {uni:"GIKI",program:"CS & Data Science",url:"https://giki.edu.pk"}
    ]},
    { id: "medicine", name: "Medicine & Health", blurb: "Help people through science and care.", subjectCombos:[
      {title:"Pre-Med Core", subjects:["Biology","Chemistry","Physics"], notes:"Safest for Medicine and Dentistry.", popular:true},
      {title:"Bio Focus", subjects:["Biology","Chemistry","Math"], notes:"Good for Biomed, Pharmacy, Nutrition.", popular:true}
    ], degrees:["MBBS","Dentistry","Pharmacy","Biomedical Science","Nursing"],
    uniMatches:[
      {uni:"Aga Khan University",program:"MBBS",url:"https://www.aku.edu"},
      {uni:"NUMS",program:"MBBS (Army Medical College)",url:"https://www.numspak.edu.pk"},
      {uni:"Dow University",program:"MBBS",url:"https://www.duhs.edu.pk"},
      {uni:"King Edward (KEMU)",program:"MBBS",url:"https://www.kemu.edu.pk"}
    ]},
    { id: "biz_econ", name: "Business, Finance & Economics", blurb: "Understand markets and manage money.", subjectCombos:[
      {title:"Quant Business", subjects:["Math","Economics","Accounting"], notes:"For Finance and Economics.", popular:true},
      {title:"Management & Marketing", subjects:["Business","Economics","Math"], notes:"Balanced for management and marketing."},
      {title:"Commerce Track", subjects:["Accounting","Business","Economics"], notes:"Solid for ACCA or CA and management.", popular:true}
    ], degrees:["Economics","Finance","Accounting","Business Administration","Marketing","Supply Chain"],
    uniMatches:[
      {uni:"IBA Karachi",program:"BBA / Economics",url:"https://www.iba.edu.pk"},
      {uni:"LUMS",program:"SDSB (BBA / Econ)",url:"https://admissions.lums.edu.pk"},
      {uni:"LSE (Lahore)",program:"Economics / Business",url:"https://www.lse.edu.pk"},
      {uni:"NBS (NUST)",program:"BBA",url:"https://www.nust.edu.pk"}
    ]},
    { id: "law_social", name: "Law & Social Sciences", blurb: "Shape policy and justice.", subjectCombos:[
      {title:"Law Ready", subjects:["English Language","Law","History"], notes:"Strong reading and writing subjects help."},
      {title:"Policy & IR", subjects:["Economics","Politics","Sociology"], notes:"For IR, Public Policy, Development."},
      {title:"Psych & Society", subjects:["Psychology","Sociology","Biology"], notes:"Useful for Psychology and Human Sciences."}
    ], degrees:["LLB","International Relations","Public Policy","Sociology","Psychology"],
    uniMatches:[
      {uni:"LUMS",program:"Humanities (Law & Policy)",url:"https://admissions.lums.edu.pk"},
      {uni:"IBA",program:"Social Sciences",url:"https://www.iba.edu.pk"},
      {uni:"QAU",program:"Law / IR",url:"https://www.qau.edu.pk"},
      {uni:"LSE",program:"Political Science",url:"https://www.lse.edu.pk"}
    ]},
    { id: "creative_media", name: "Creative, Media & Communication", blurb: "Tell stories and design experiences.", subjectCombos:[
      {title:"Design & Visuals", subjects:["Art & Design","Media Studies","IT/Computer Science"], notes:"Graphic Design, UI or UX, Animation."},
      {title:"Content & Comms", subjects:["English Language","Media Studies","Sociology"], notes:"Journalism, PR, Advertising."},
      {title:"Music & Performing Arts", subjects:["Music","Drama","English Literature"], notes:"Performance and production."}
    ], degrees:["Design","Media & Comms","Journalism","Film & TV","Advertising","UI or UX"],
    uniMatches:[
      {uni:"BNU (Beaconhouse)",program:"Design / Media",url:"https://www.bnu.edu.pk"},
      {uni:"NCA",program:"Fine Art / Design",url:"https://www.nca.edu.pk"},
      {uni:"SZABIST",program:"Media Studies",url:"https://www.szabist.edu.pk"},
      {uni:"LUMS",program:"Humanities (Media)",url:"https://admissions.lums.edu.pk"}
    ]},
    { id: "arch_design", name: "Architecture & Built Environment", blurb: "Shape cities and spaces.", subjectCombos:[
      {title:"Architecture Core", subjects:["Math","Physics","Art & Design"], notes:"Math is essential. Portfolio matters.", popular:true},
      {title:"Urban & Planning", subjects:["Geography","Math","Economics"], notes:"Urban Planning, Real Estate, Environmental Design."}
    ], degrees:["Architecture","Urban Planning","Interior Design","Construction Management"],
    uniMatches:[
      {uni:"NCA",program:"Architecture",url:"https://www.nca.edu.pk"},
      {uni:"UET Lahore",program:"Architecture",url:"https://www.uet.edu.pk"},
      {uni:"NED University",program:"Architecture & Planning",url:"https://www.neduet.edu.pk"},
      {uni:"COMSATS",program:"Architecture",url:"https://www.comsats.edu.pk"}
    ]},
    { id: "pure_science", name: "Pure Sciences & Research", blurb: "Explore how the universe works.", subjectCombos:[
      {title:"Physical Sciences", subjects:["Math","Physics","Chemistry"], notes:"For Physics, Chemistry, Earth Sciences.", popular:true},
      {title:"Biological Sciences", subjects:["Biology","Chemistry","Math"], notes:"Microbiology, Biotech, Environmental."},
      {title:"Math Heavy", subjects:["Math","Further Math","Physics"], notes:"Mathematics, Theoretical Physics, Statistics."}
    ], degrees:["Physics","Chemistry","Mathematics","Biology","Biotech","Earth Sciences"],
    uniMatches:[
      {uni:"LUMS",program:"SBASSE (Sciences)",url:"https://admissions.lums.edu.pk"},
      {uni:"QAU",program:"Natural Sciences",url:"https://www.qau.edu.pk"},
      {uni:"GIKI",program:"Engineering & Sciences",url:"https://giki.edu.pk"},
      {uni:"COMSATS",program:"Sciences",url:"https://www.comsats.edu.pk"}
    ]},
    { id: "education_psych", name: "Education, Teaching & Human Development", blurb: "Guide learners and study how people grow.", subjectCombos:[
      {title:"Teaching Track", subjects:["English Language","Psychology","Sociology"], notes:"Education, Counseling, EdTech."},
      {title:"STEM Teaching", subjects:["Math","Physics","Computer Science"], notes:"If you plan to teach STEM or build EdTech."}
    ], degrees:["Education","Counseling","EdTech","Special Education","Human Development"],
    uniMatches:[
      {uni:"Aga Khan University",program:"Education",url:"https://www.aku.edu"},
      {uni:"QAU",program:"Education",url:"https://www.qau.edu.pk"},
      {uni:"BNU",program:"Education",url:"https://www.bnu.edu.pk"},
      {uni:"LUMS",program:"Humanities (Education)",url:"https://admissions.lums.edu.pk"}
    ]},
    { id: "hospitality", name: "Hospitality, Tourism & Events", blurb: "Design memorable experiences.", subjectCombos:[
      {title:"Events & Service", subjects:["Business","Economics","English Language"], notes:"Events, Hospitality, Tourism."},
      {title:"Brand & Experience", subjects:["Media Studies","Business","Art & Design"], notes:"Experiential and brand hospitality."}
    ], degrees:["Hospitality Management","Tourism","Event Management"],
    uniMatches:[
      {uni:"SZABIST",program:"Hospitality Management",url:"https://www.szabist.edu.pk"},
      {uni:"IBA",program:"Business (Hospitality track)",url:"https://www.iba.edu.pk"}
    ]}
  ];

  const QUESTIONS = [
    { id:"olevel", title:"Which O Level subjects did you take?", type:"olevel", options:[] },
    { id:"interests", title:"What do you enjoy studying most?", type:"multi", options:[
      ["math","Math"],["physics","Physics"],["chemistry","Chemistry"],["biology","Biology"],["cs","Computer Science"],["econ","Economics"],["business","Business"],["accounting","Accounting"],["english","English"],["urdu","Urdu"],["history","History"],["politics","Politics"],["sociology","Sociology"],["psychology","Psychology"],["art","Art & Design"],["media","Media Studies"],["geography","Geography"],["music","Music"],["drama","Drama"] ]},
    { id:"strengths", title:"Which strengths describe you?", type:"multi", options:[
      ["problem_solving","Problem solving"],["creativity","Creativity"],["communication","Communication"],["analysis","Data analysis"],["empathy","Empathy"],["leadership","Leadership"],["precision","Precision and detail"],["experiments","Enjoy experiments"],["visual","Visual thinking"] ]},
    { id:"workstyle", title:"What type of work sounds fun?", type:"single", options:[
      ["build","Building or coding things"],["research","Researching and investigating"],["people","Working with people"],["business_ops","Running or growing a business"],["story","Telling stories or designing visuals"] ]},
    { id:"preferences", title:"Pick the statements that fit you", type:"multi", options:[
      ["lab","I like labs and experiments"],["numbers","I like numbers and logic"],["care","I want to help people directly"],["policy","I care about laws, policy, or society"],["design","I love design and aesthetics"],["outdoors","I enjoy geography and the outdoors"] ]},
    { id:"constraints", title:"Any constraints to consider?", type:"multi", options:[
      ["avoid_bio","Prefer to avoid Biology"],["avoid_physics","Prefer to avoid Physics"],["avoid_chem","Prefer to avoid Chemistry"],["avoid_math","Prefer to avoid Math"],["no_heavy_writing","Prefer less heavy writing"] ]}
  ];

  const WEIGHTS = {
    interests:{
      math:{eng_tech:1, cs_data:1.2, biz_econ:0.8, pure_science:1.1, arch_design:0.6},
      physics:{eng_tech:1.2, cs_data:0.6, pure_science:1, arch_design:0.8},
      chemistry:{eng_tech:0.7, pure_science:1.1, medicine:0.8},
      biology:{medicine:1.2, pure_science:0.8, education_psych:0.4},
      cs:{cs_data:1.3, eng_tech:0.6, biz_econ:0.5, creative_media:0.4},
      econ:{biz_econ:1.2, law_social:0.6, hospitality:0.5},
      business:{biz_econ:1.1, hospitality:0.6, law_social:0.4},
      accounting:{biz_econ:1.1}, english:{law_social:0.8, creative_media:0.7, education_psych:0.6}, urdu:{law_social:0.7, creative_media:0.6, education_psych:0.5},
      history:{law_social:1}, politics:{law_social:1}, sociology:{law_social:0.8, education_psych:0.8},
      psychology:{education_psych:1, law_social:0.5}, art:{creative_media:1.2, arch_design:0.9}, media:{creative_media:1.2},
      geography:{arch_design:0.5, hospitality:0.6, pure_science:0.4}, music:{creative_media:0.8}, drama:{creative_media:0.8}
    },
    strengths:{
      problem_solving:{eng_tech:0.8, cs_data:1, biz_econ:0.6},
      creativity:{creative_media:1, arch_design:0.7, biz_econ:0.4},
      communication:{law_social:0.8, creative_media:0.6, education_psych:0.6, hospitality:0.6},
      analysis:{cs_data:1, biz_econ:0.8, pure_science:0.7},
      empathy:{medicine:0.8, education_psych:0.9, hospitality:0.5},
      leadership:{biz_econ:0.8, law_social:0.5},
      precision:{medicine:0.6, eng_tech:0.7, pure_science:0.7},
      experiments:{pure_science:0.8, medicine:0.6, eng_tech:0.5},
      visual:{creative_media:1, arch_design:0.8}
    },
    workstyle:{
      build:{eng_tech:0.8, cs_data:0.9, arch_design:0.5},
      research:{pure_science:0.9, cs_data:0.6, law_social:0.5},
      people:{education_psych:0.8, medicine:0.6, hospitality:0.6},
      business_ops:{biz_econ:0.9, hospitality:0.4},
      story:{creative_media:1, law_social:0.4}
    },
    preferences:{
      lab:{pure_science:0.8, medicine:0.6, eng_tech:0.5},
      numbers:{cs_data:0.8, biz_econ:0.7, eng_tech:0.6},
      care:{medicine:0.9, education_psych:0.7},
      policy:{law_social:0.9},
      design:{creative_media:0.9, arch_design:0.7},
      outdoors:{arch_design:0.5, hospitality:0.4, pure_science:0.4}
    },
    constraints:{
      avoid_bio:{medicine:-1.2, pure_science:-0.3},
      avoid_physics:{eng_tech:-1, arch_design:-0.6, pure_science:-0.3},
      avoid_chem:{medicine:-0.7, pure_science:-0.4},
      avoid_math:{cs_data:-1.1, eng_tech:-0.9, biz_econ:-0.7, pure_science:-0.7, arch_design:-0.5},
      no_heavy_writing:{law_social:-0.8, creative_media:-0.4}
    }
  };

  const OLEVEL_TO_ALEVEL = {
    physics:"physics", chemistry:"chemistry", biology:"biology", cs:"cs",
    math:"math", addmath:"math", econ:"econ", business:"business",
    accounting:"accounting", english:"english", art:"art", geo:"geography",
    sociology:"sociology", history:"history"
  };

  const state = {
    step: 0,
    answers: {},
    results: null,
    openCats: new Set(),
    emailSent: false
  };

  const $quiz = document.getElementById('sj-quiz');
  const $results = document.getElementById('sj-results');
  const $resultsInner = document.getElementById('sj-results-inner');
  const $progress = document.getElementById('sj-progress');
  const $progressLabel = document.getElementById('sj-progress-label');
  const $stickyBar = document.getElementById('sj-sticky-bar');
  const $stickyLabel = document.getElementById('sj-sticky-label');
  const $stickyPct = document.getElementById('sj-sticky-pct');

  function esc(s){ return String(s||'').replace(/[&<>"']/g,function(m){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]; }); }

  function pct(){
    var total = QUESTIONS.length;
    return Math.min(100, Math.round(((state.step+1)/(total+1))*100));
  }

  function setProgress(){
    var p = pct();
    $progress.style.width = p + "%";
    $stickyBar.style.width = p + "%";
    $stickyPct.textContent = p + "%";
    if(state.step < QUESTIONS.length){
      $progressLabel.textContent = "Question " + (state.step+1) + " of " + QUESTIONS.length;
      $stickyLabel.textContent = "Q" + (state.step+1) + " of " + QUESTIONS.length;
    } else {
      $progressLabel.textContent = "Results ready";
      $stickyLabel.textContent = "Done";
    }
  }

  function toggleMulti(id, opt){
    var current = new Set(state.answers[id] || []);
    if(current.has(opt)) current.delete(opt); else current.add(opt);
    state.answers[id] = Array.from(current);
    render();
  }

  function setSingle(id, opt){ state.answers[id] = opt; render(); }

  function isStepValid(){
    var q = QUESTIONS[state.step];
    if(!q) return false;
    if(q.type === 'olevel'){
      var subs = state.answers.olevel_subjects || [];
      var perf = state.answers.olevel_performance;
      return subs.length > 0 && !!perf;
    }
    var a = state.answers[q.id];
    if(q.type === 'multi') return Array.isArray(a) && a.length > 0;
    if(q.type === 'single') return typeof a === 'string' && a.length > 0;
    return false;
  }

  function optHtml(id, type, opt){
    var a = state.answers[id];
    var selected = Array.isArray(a) ? a.indexOf(opt[0]) !== -1 : a === opt[0];
    return '<button class="opt '+(selected?'selected':'')+'" data-qid="'+id+'" data-type="'+type+'" data-opt="'+opt[0]+'">'+esc(opt[1])+'</button>';
  }

  function renderOLevel(){
    var subs = state.answers.olevel_subjects || [];
    var perf = state.answers.olevel_performance || '';
    var valid = isStepValid();

    var catsHtml = OLEVEL_CATEGORIES.map(function(cat){
      var isOpen = state.openCats.has(cat.name);
      var selectedInCat = cat.subjects.filter(function(s){ return subs.indexOf(s[0]) !== -1; }).length;
      var pills = cat.subjects.map(function(s){
        return optHtml('olevel_subjects', 'multi', s);
      }).join('');

      return '<div class="olevel-category">'
        + '<div class="olevel-cat-header '+(isOpen?'open':'')+'" data-cat="'+esc(cat.name)+'">'
          + '<span>'+esc(cat.name)+(selectedInCat ? ' <span class="olevel-cat-count">('+selectedInCat+')</span>' : '')+'</span>'
          + '<span class="arrow">'+(isOpen?'▲':'▼')+'</span>'
        + '</div>'
        + '<div class="olevel-cat-body '+(isOpen?'open':'')+'">'
          + '<div class="optgrid">'+pills+'</div>'
        + '</div>'
      + '</div>';
    }).join('');

    var perfOptions = [
      ["strong","Mostly A* and A grades"],
      ["mixed","Mix of A, B, and C grades"],
      ["weaker","Mostly B and C grades"]
    ];

    var perfHtml = perfOptions.map(function(p){
      return optHtml('olevel_performance', 'single', p);
    }).join('');

    $quiz.innerHTML =
      '<div class="qcard">'
        + '<div class="qstep-label">Step 1 of '+QUESTIONS.length+'</div>'
        + '<div class="qtitle">Which O Level subjects did you take?</div>'
        + '<div class="olevel-categories">'+catsHtml+'</div>'
        + '<div class="perf-select">'
          + '<label>How were your grades?</label>'
          + '<div class="optgrid">'+perfHtml+'</div>'
        + '</div>'
        + (valid ? '' : '<div class="sja-validation">Select your subjects and grade level to continue.</div>')
      + '</div>'
      + '<div class="sja-nav-row">'
        + '<button class="sja-btn sja-btn-primary" data-nav="next" '+(valid?'':'disabled')+'>Continue</button>'
      + '</div>'
      + '<div class="sja-reset-link"><a href="#" id="sj-reset">Reset quiz</a></div>';
  }

  function renderQuestion(){
    var q = QUESTIONS[state.step];
    if(!q){ $quiz.innerHTML = ""; return; }
    var opts = q.options.map(function(o){ return optHtml(q.id, q.type, o); }).join("");
    var valid = isStepValid();

    var navBtns = '';
    if(state.step > 0){
      navBtns += '<button class="sja-btn sja-btn-outline" data-nav="back">Back</button>';
    }
    if(state.step < QUESTIONS.length-1){
      navBtns += '<button class="sja-btn sja-btn-primary" data-nav="next" '+(valid?'':'disabled')+'>Continue</button>';
    } else {
      navBtns += '<button class="sja-btn sja-btn-primary" data-nav="submit" '+(valid?'':'disabled')+'>See My Pathways</button>';
    }

    $quiz.innerHTML =
      '<div class="qcard">'
        + '<div class="qstep-label">Step '+(state.step+1)+' of '+QUESTIONS.length+'</div>'
        + '<div class="qtitle">'+esc(q.title)+'</div>'
        + '<div class="optgrid">'+opts+'</div>'
        + (valid ? '' : '<div class="sja-validation">Pick at least one option to continue.</div>')
      + '</div>'
      + '<div class="sja-nav-row">'+navBtns+'</div>'
      + '<div class="sja-reset-link"><a href="#" id="sj-reset">Reset quiz</a></div>';
  }

  function score(){
    var scores = {};

    function add(map, key, mult){
      if(!map||!key) return;
      var wm = map[key]||{};
      Object.entries(wm).forEach(function(e){
        scores[e[0]] = (scores[e[0]]||0) + e[1]*(mult||1);
      });
    }

    ["interests","strengths","preferences","constraints"].forEach(function(k){
      var sel = state.answers[k] || [];
      if(Array.isArray(sel)) sel.forEach(function(opt){ add(WEIGHTS[k], opt, 1); });
    });

    if(state.answers.workstyle) add(WEIGHTS.workstyle, state.answers.workstyle, 1);

    var olevelSubs = state.answers.olevel_subjects || [];
    var perf = state.answers.olevel_performance;
    var perfMult = perf === 'strong' ? 0.35 : perf === 'mixed' ? 0.15 : 0;

    olevelSubs.forEach(function(olSub){
      var alKey = OLEVEL_TO_ALEVEL[olSub];
      if(alKey && WEIGHTS.interests[alKey]){
        add({temp: WEIGHTS.interests[alKey]}, 'temp', perfMult);
      }
    });

    var entries = Object.entries(scores).sort(function(a,b){ return b[1]-a[1]; });
    var top = entries.slice(0,3).map(function(e){
      var c = CLUSTERS.find(function(x){ return x.id===e[0]; });
      if(!c) return null;
      return Object.assign({}, c, {score: Number(e[1].toFixed(2))});
    }).filter(Boolean);

    var avoid = new Set(state.answers.constraints||[]);
    var filtered = top.map(function(p){
      return Object.assign({}, p, {
        subjectCombos: p.subjectCombos.filter(function(combo){
          var s = combo.subjects.map(function(x){ return x.toLowerCase(); });
          if(avoid.has("avoid_bio") && s.indexOf("biology") !== -1) return false;
          if(avoid.has("avoid_physics") && s.indexOf("physics") !== -1) return false;
          if(avoid.has("avoid_chem") && s.indexOf("chemistry") !== -1) return false;
          if(avoid.has("avoid_math") && s.indexOf("math") !== -1) return false;
          return true;
        })
      });
    });

    return { picks: filtered, raw: entries };
  }

  function labelForIndex(i){ return i===0? 'Excellent match' : i===1? 'Good match' : 'Consider'; }
  function badgeClassForIndex(i){ return i===0? 'sja-match-excellent' : i===1? 'sja-match-good' : 'sja-match-consider'; }

  function getStrengthNote(combo){
    var olevelSubs = state.answers.olevel_subjects || [];
    var perf = state.answers.olevel_performance;
    if(!olevelSubs.length) return null;

    var strong = [];
    var weak = [];
    combo.subjects.forEach(function(sub){
      var subLower = sub.toLowerCase();
      var foundOLevel = false;
      olevelSubs.forEach(function(ol){
        var mapped = OLEVEL_TO_ALEVEL[ol];
        if(mapped && (subLower.indexOf(mapped) !== -1 || mapped.indexOf(subLower) !== -1)){
          foundOLevel = true;
        }
      });
      if(foundOLevel){
        if(perf === 'strong') strong.push(sub);
        else if(perf === 'weaker') weak.push(sub);
        else { strong.push(sub); }
      }
    });

    if(strong.length >= 2 && perf === 'strong'){
      return { text: "Strong O Level foundation in " + strong.join(", ") + ". You are well prepared.", type: "strong" };
    }
    if(weak.length >= 2 && perf === 'weaker'){
      return { text: "You studied " + weak.join(", ") + " at O Level but grades were mixed. Consider extra preparation.", type: "weak" };
    }
    if(strong.length >= 1){
      return { text: "You have O Level background in " + strong.join(", ") + ".", type: "strong" };
    }
    return null;
  }

  function getUniMatches(clusterId){
    var cluster = CLUSTERS.find(function(c){ return c.id === clusterId; });
    if(!cluster || !cluster.uniMatches) return [];
    return cluster.uniMatches;
  }

  function renderResults(){
    var r = state.results;
    if(!r){ $results.style.display='none'; return; }

    var best = r.picks[0];
    var reasons = [];
    var A = state.answers;
    if(A.interests && A.interests.length) reasons.push('Interests: '+A.interests.slice(0,3).join(', '));
    if(A.strengths && A.strengths.length) reasons.push('Strengths: '+A.strengths.slice(0,3).join(', '));
    if(A.workstyle){ var wmap={build:'building things',research:'research',people:'working with people',business_ops:'business ops',story:'story or design'}; reasons.push('Work style: '+(wmap[A.workstyle]||A.workstyle)); }
    if(A.olevel_subjects && A.olevel_subjects.length) reasons.push('O Level subjects: '+A.olevel_subjects.join(', '));

    var cards = r.picks.map(function(p,i){
      var comboHtml = '';
      if(p.subjectCombos.length === 0){
        comboHtml = '<div class="sja-filtered-msg">We filtered out combos based on your avoid list. Edit constraints for more options.</div>';
      } else {
        comboHtml = p.subjectCombos.map(function(c){
          var tags = c.subjects.map(function(s){ return '<span class="sja-subject-tag">'+esc(s)+'</span>'; }).join('');
          var popularBadge = c.popular ? '<span class="sja-popular-badge">Popular</span>' : '';
          var strengthNote = getStrengthNote(c);
          var noteHtml = strengthNote ? '<div class="sja-strength-note '+(strengthNote.type==='weak'?'weak':'')+'">'+esc(strengthNote.text)+'</div>' : '';

          return '<div class="sja-combo">'
            + '<div class="sja-combo-header">'
              + '<div class="sja-combo-title">'+esc(c.title)+'</div>'
              + popularBadge
            + '</div>'
            + '<div class="sja-subject-tags">'+tags+'</div>'
            + '<div class="sja-combo-notes">'+esc(c.notes)+'</div>'
            + noteHtml
          + '</div>';
        }).join("");
      }

      var degreeTags = p.degrees.map(function(d){ return '<span class="sja-degree-tag">'+esc(d)+'</span>'; }).join('');

      var unis = getUniMatches(p.id);
      var uniHtml = '';
      if(unis.length){
        var uniItems = unis.map(function(u){
          return '<div class="sja-uni-item">'
            + '<div>'
              + '<div class="sja-uni-name">'+esc(u.uni)+'</div>'
              + '<div class="sja-uni-program">'+esc(u.program)+'</div>'
            + '</div>'
            + '<a class="sja-uni-link" href="'+esc(u.url)+'" target="_blank" rel="noopener">Visit →</a>'
          + '</div>';
        }).join("");
        uniHtml = '<div class="row"><div class="k">Matching Universities</div><div class="sja-uni-list">'+uniItems+'</div></div>';
      }

      return '<div class="sja-result-card '+(i===0?'sja-best':'')+'">'
        + '<h3>'+(i===0?'Best fit: ':'')+esc(p.name)+'</h3>'
        + '<span class="sja-match-badge '+badgeClassForIndex(i)+'">'+labelForIndex(i)+'</span>'
        + '<div class="sja-cluster-blurb">'+esc(p.blurb)+'</div>'
        + '<div class="sja-kv">'
          + '<div class="row">'
            + '<div class="k">Suggested A Level Combinations</div>'
            + comboHtml
          + '</div>'
          + '<div class="row">'
            + '<div class="k">Degree Directions</div>'
            + '<div class="sja-degree-list">'+degreeTags+'</div>'
          + '</div>'
          + uniHtml
        + '</div>'
      + '</div>';
    }).join("");

    var bestPathHtml = '';
    if(best){
      bestPathHtml = '<div class="sja-best-path">'
        + '<div class="k">Most sensible path right now: '+esc(best.name)+'</div>'
        + '<div class="v">Why: '+(esc(reasons.join(' \u2022 ')) || 'Strong alignment with your choices.')+'</div>'
      + '</div>';
    }

    $resultsInner.innerHTML =
      '<div class="sja-results-header">'
        + '<h2>Your Results</h2>'
        + '<div class="sja-results-sub">Top matches based on your answers.</div>'
        + bestPathHtml
      + '</div>'
      + '<div class="sja-results-grid">'+cards+'</div>'
      + '<div class="sja-results-actions">'
        + '<button class="sja-btn sja-btn-primary" id="btn-copy">'
          + '<svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>'
          + 'Copy Plan'
        + '</button>'
        + '<a href="https://wa.me/923362144454" target="_blank" rel="noopener" class="sja-btn sja-btn-whatsapp">'
          + '<svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.2 2.4 3.2 4.4 5.6 5.6l1.9-1.9c.2-.2.5-.3.8-.2 1 .3 2 .5 3.1.5.4 0 .7.3.7.7v3c0 .4-.3.7-.7.7-8.4 0-15.3-6.9-15.3-15.3 0-.4.3-.7.7-.7h3c.4 0 .7.3.7.7 0 1.1.2 2.1.5 3.1.1.3 0 .6-.2.8l-1.9 1.9z"/></svg>'
          + 'Talk to Us'
        + '</a>'
      + '</div>'
      + '<div class="sja-email-section" id="sja-email-section">'
        + '<h3>Save Your Results</h3>'
        + '<div class="sja-email-sub">Enter your email and we will send your personalized pathway plan so you can share it with your parents or counselor.</div>'
        + '<div class="sja-email-form" id="sja-email-form">'
          + '<input type="email" id="sja-email-input" placeholder="your@email.com" aria-label="Email address">'
          + '<button class="sja-btn sja-btn-primary" id="sja-email-btn" style="min-width:auto;">Send My Plan</button>'
        + '</div>'
        + '<div class="sja-email-success" id="sja-email-success">Your plan details are ready. Check your email or share the link above with your parents and counselor.</div>'
      + '</div>'
      + '<div class="sja-results-restart"><a href="#" data-nav="restart">Restart quiz</a></div>';

    $results.style.display = '';
    $results.scrollIntoView({behavior:'smooth', block:'start'});
  }

  function generatePlanText(){
    var r = state.results;
    if(!r) return '';
    var top = r.picks;
    var best = top[0];
    var lines = [];
    lines.push('=== SJ Academy Career Pathway Plan ===');
    lines.push('');
    if(best){
      lines.push('Best fit: ' + best.name);
      lines.push('Why: ' + best.blurb);
      lines.push('');
    }
    top.forEach(function(p,i){
      lines.push((i+1) + '. ' + p.name + ' (' + labelForIndex(i) + ')');
      if(p.subjectCombos.length){
        p.subjectCombos.forEach(function(c){
          lines.push('   - ' + c.title + ': ' + c.subjects.join(', '));
          lines.push('     ' + c.notes);
        });
      }
      lines.push('   Degrees: ' + p.degrees.join(', '));
      var unis = getUniMatches(p.id);
      if(unis.length){
        lines.push('   Universities: ' + unis.map(function(u){ return u.uni + ' (' + u.program + ')'; }).join(', '));
      }
      lines.push('');
    });
    lines.push('Built by SJ Academy — www.sjacademy.pk');
    return lines.join('\n');
  }

  function handleActions(e){
    var t = e.target;

    while(t && t !== document.body && !t.classList.contains('opt') && !t.dataset.nav && !t.dataset.cat && t.id !== 'sj-reset' && t.id !== 'btn-copy' && t.id !== 'sja-email-btn' && !t.classList.contains('olevel-cat-header')){
      t = t.parentElement;
    }
    if(!t || t === document.body) return;

    if(t.dataset.cat){
      var catName = t.dataset.cat;
      if(state.openCats.has(catName)) state.openCats.delete(catName); else state.openCats.add(catName);
      render();
      return;
    }

    if(t.classList.contains('opt')){
      var id = t.getAttribute('data-qid');
      var type = t.getAttribute('data-type');
      var opt = t.getAttribute('data-opt');
      type === 'multi' ? toggleMulti(id,opt) : setSingle(id,opt);
      return;
    }

    if(t.dataset.nav === 'back'){ state.step = Math.max(0, state.step-1); render(); return; }
    if(t.dataset.nav === 'next'){ if(!isStepValid()) return; state.step = Math.min(QUESTIONS.length-1, state.step+1); render(); return; }
    if(t.dataset.nav === 'submit'){
      if(!isStepValid()) return;
      state.results = score();
      state.step = QUESTIONS.length;
      setProgress();
      render();
      return;
    }

    if(t.id === 'sj-reset'){ e.preventDefault(); resetAll(); return; }

    if(t.id === 'btn-copy'){
      var text = generatePlanText();
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(text).then(function(){
          t.textContent = 'Copied!';
          setTimeout(function(){ t.innerHTML = '<svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg> Copy Plan'; }, 1500);
        });
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        t.textContent = 'Copied!';
        setTimeout(function(){ t.innerHTML = '<svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg> Copy Plan'; }, 1500);
      }
      return;
    }

    if(t.id === 'sja-email-btn'){
      var emailInput = document.getElementById('sja-email-input');
      var email = emailInput ? emailInput.value.trim() : '';
      if(!email || !email.indexOf('@') || email.indexOf('@') < 1){
        if(emailInput) emailInput.style.borderColor = '#b00020';
        return;
      }

      var planText = generatePlanText();
      var best = state.results && state.results.picks ? state.results.picks[0] : null;
      var subject = encodeURIComponent('SJ Academy — My Career Pathway Plan' + (best ? ' (' + best.name + ')' : ''));
      var body = encodeURIComponent('Hi,\n\nHere is my career pathway plan from SJ Academy:\n\n' + planText);

      var mailto = 'mailto:' + encodeURIComponent(email) + '?subject=' + subject + '&body=' + body;
      window.location.href = mailto;

      var emailForm = document.getElementById('sja-email-form');
      var emailSuccess = document.getElementById('sja-email-success');
      if(emailForm) emailForm.style.display = 'none';
      if(emailSuccess) emailSuccess.style.display = 'block';

      return;
    }

    if(t.dataset.nav === 'restart'){ if(e.preventDefault) e.preventDefault(); resetAll(); return; }
  }

  function resetAll(){
    state.step = 0;
    state.answers = {};
    state.results = null;
    state.openCats = new Set();
    state.emailSent = false;
    render();
  }

  function render(){
    setProgress();
    if(state.step < QUESTIONS.length){
      var q = QUESTIONS[state.step];
      if(q.type === 'olevel'){
        renderOLevel();
      } else {
        renderQuestion();
      }
      $results.style.display = 'none';
    } else {
      $quiz.innerHTML = '';
      renderResults();
    }
  }

  document.getElementById('sj-career-finder').addEventListener('click', handleActions);
  render();
})();
</script>

</body>
</html>
```
