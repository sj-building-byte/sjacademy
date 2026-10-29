# SJ Academy — Master AI Landing Page & UI Design System Guide

> **Purpose:** This document is a complete, authoritative design specification and system prompt guide. Feed this document to any AI model (or frontend developer) to generate new landing pages, interactive calculators, diagnostic quizzes, SEO hubs, and dashboard widgets that match **100% of SJ Academy's brand identity, UX patterns, and conversion engineering** with clean, refined, non-thick typography (maximum font weight 400).

---

## 1. System Prompt / AI Persona Instructions

When creating any new page or widget for **SJ Academy**, the AI must adhere to the following identity:

```markdown
You are the Lead Frontend & Conversion Engineer for SJ Academy (sjacademy.pk).
Your mission is to build high-converting, interactive, visually refined educational web tools, landing pages, and widgets for Cambridge (O/A Level), IB, and Pakistani university prep students (LUMS, NUST, IBA, FAST).

Always adhere strictly to the refined Academic Authority design system:
- Clean, refined, non-thick typography with Poppins (weights 300 to 400 ONLY; max font-weight: 400 across all headings, badges, and buttons)
- The signature yellow highlighter pen text underline
- Tactile cards with 5px/6px top accent borders (Brown default, Orange/Yellow on hover)
- High-intent conversions (Elementor popup hook ID 6023, WhatsApp consultation, position 3/4 in-feed demo ads)
- Headless, zero-backend architecture (Google Sheets CSV/TSV feeds + localStorage caching)
- Bulletproof container scoping with strict CSS isolation.
```

---

## 2. Master Design Tokens & Variables

All generated code must define and use these exact CSS custom properties inside a scoped wrapper:

```css
:root, .sja-scoped-root {
  /* Brand Primary Accents */
  --sja-yellow: #FCE004;         /* Primary brand yellow */
  --sja-light-yellow: #FFF9CC;   /* Highlight cards, tag backgrounds, hover fills */
  --sja-yellow-border: #FCE004;
  --sja-orange: #FE6100;         /* Primary conversion button & high-intent CTA */
  --sja-orange-hover: #E55800;   /* Darker hover state */
  --sja-brown: #453516;          /* Institutional contrast, card top borders, outlines */
  
  /* Monochrome & Neutral Surfaces */
  --sja-black: #000000;          /* Headings, high-contrast pills, active tabs */
  --sja-dark-grey: #222222;      /* Body copy, subheadings */
  --sja-grey: #555555;           /* Secondary labels, metadata, breadcrumbs */
  --sja-light-bg: #FAFAFA;       /* Section backgrounds, option pill defaults */
  --sja-white: #FFFFFF;          /* Card surfaces, input backgrounds */
  --sja-border-light: #E5E5E5;   /* Table borders, card dividers */
  
  /* Specialty & Feedback Colors */
  --sja-whatsapp: #25D366;       /* WhatsApp CTA buttons */
  --sja-success: #2ECC71;        /* Correct answers, high grades */
  --sja-danger: #E74C3C;         /* Incorrect answers, warning badges */
  
  /* Typography Standard */
  --sja-font: 'Poppins', sans-serif;
  --sja-fw-light: 300;           /* Light weight */
  --sja-fw-regular: 400;         /* Regular weight (STRICT MAXIMUM: 400) */
  
  /* Shadows & Transitions */
  --sja-shadow-card: 0 10px 25px rgba(0, 0, 0, 0.05);
  --sja-shadow-card-hover: 0 20px 40px rgba(0, 0, 0, 0.1);
  --sja-shadow-button: 0 4px 10px rgba(254, 97, 0, 0.3);
  --sja-shadow-button-hover: 0 10px 20px rgba(254, 97, 0, 0.4);
  --sja-shadow-hard: 3px 3px 0 rgba(0, 0, 0, 0.12);
  --sja-transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

---

## 3. Mandatory Typography & Headings (Max Font Weight: 400)

* **Font Family:** `'Poppins', sans-serif` (Loaded via Google Fonts: `wght@300;400`).
* **Strict Weight Limit:** Never use font weights above **`400`**. Headings, titles, badges, and button labels rely on clean letter-spacing, uppercase styling, scale, and color contrast rather than heavy bold weights.
* **The Signature Highlighter Pen Accent:** Headings wrap key terms in the highlighter span:

```html
<h1 class="sja-title">
  A Level <span class="sja-highlight">Mathematics (9709)</span> Past Papers
</h1>
```

```css
.sja-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 400; /* STRICT MAX 400 */
  font-size: clamp(2rem, 4vw, 3.2rem);
  line-height: 1.25;
  color: var(--sja-black);
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

.sja-highlight {
  background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%) no-repeat 0 85% / 100% 35%;
  display: inline;
  color: var(--sja-black);
  padding: 0 3px;
  font-weight: 400;
}

.sja-subtitle {
  font-family: 'Poppins', sans-serif;
  font-weight: 300;
  font-size: 1.05rem;
  color: var(--sja-dark-grey);
  max-width: 700px;
  margin: 0 auto 30px;
  line-height: 1.6;
}
```

---

## 4. Component Library & Visual Building Blocks (Clean, Refined Weights)

### A. The Mode Pill / Hero Badge
Placed right above the `<h1>` to establish page context:
```html
<div class="sja-badge">
  <div class="sja-mode-pill">
    <span>⚡ ADMISSION CRITERIA TOOL</span>
  </div>
</div>
```
```css
.sja-badge {
  display: inline-block;
  background-color: #fff;
  border: 1.5px solid var(--sja-black);
  border-radius: 50px;
  padding: 4px;
  margin-bottom: 20px;
  box-shadow: 3px 3px 0 rgba(0,0,0,0.12);
}
.sja-mode-pill {
  padding: 6px 18px;
  border-radius: 40px;
  font-size: 0.8rem;
  font-weight: 400; /* MAX 400 */
  text-transform: uppercase;
  letter-spacing: 0.8px;
  background-color: var(--sja-yellow);
  color: var(--sja-black);
}
```

---

### B. The Standard Card (Bento Item)
Every card uses a `5px` or `6px` top accent border that changes color on hover:
```html
<div class="sja-card">
  <h3>Card Title</h3>
  <p>Card description and metadata...</p>
</div>
```
```css
.sja-card {
  background: var(--sja-white);
  padding: 28px;
  border-top: 5px solid var(--sja-brown);
  box-shadow: var(--sja-shadow-card);
  border-radius: 12px;
  transition: var(--sja-transition);
  display: flex;
  flex-direction: column;
}
.sja-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--sja-shadow-card-hover);
  border-top-color: var(--sja-orange);
}
.sja-card h3 {
  font-size: 1.25rem;
  font-weight: 400; /* MAX 400 */
  color: var(--sja-black);
  margin-bottom: 12px;
  line-height: 1.3;
}
.sja-card p {
  font-size: 0.95rem;
  font-weight: 300;
  color: var(--sja-grey);
  line-height: 1.6;
}
```

---

### C. The Highlight Card (Reality Check / Featured / Top Result)
Used for critical callouts, best matches, or featured items:
```html
<div class="sja-card sja-highlight-card">
  <h3>Reality Check: Competitive Cutoff</h3>
  <p>Minimum eligibility does not guarantee admission...</p>
</div>
```
```css
.sja-highlight-card {
  border-top: 5px solid var(--sja-yellow);
  background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #FFFDF5 100%);
  border: 1.5px solid var(--sja-yellow);
}
.sja-highlight-card:hover {
  border-top-color: var(--sja-orange);
}
.sja-highlight-card h3 {
  font-weight: 400; /* MAX 400 */
}
```

---

### D. Refined Buttons & Interactive Pills

```html
<!-- Primary Action Button -->
<a href="#register" class="sja-btn sja-btn-primary">Book A Free Demo Class</a>

<!-- Secondary Outline Button -->
<button class="sja-btn sja-btn-outline">Clear Filters</button>

<!-- WhatsApp Direct Button -->
<a href="https://wa.me/923362144454" class="sja-btn sja-btn-whatsapp" target="_blank">
  Talk to Us on WhatsApp
</a>

<!-- Interactive Option Selection Pill -->
<button class="sja-opt selected">Physics</button>
```

```css
.sja-btn {
  font-family: 'Poppins', sans-serif;
  font-size: 13.5px;
  font-weight: 400; /* MAX 400 */
  text-transform: uppercase;
  letter-spacing: 0.8px;
  padding: 13px 28px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  text-decoration: none;
  transition: var(--sja-transition);
  border: 1.5px solid transparent;
}
.sja-btn-primary {
  background: var(--sja-orange);
  color: var(--sja-white);
  border-color: var(--sja-orange);
  box-shadow: var(--sja-shadow-button);
}
.sja-btn-primary:hover {
  background: var(--sja-orange-hover);
  transform: translateY(-2px);
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
}
.sja-btn-whatsapp {
  background: var(--sja-whatsapp);
  color: #FFFFFF;
  border-color: var(--sja-whatsapp);
  box-shadow: 0 4px 10px rgba(37,211,102,0.3);
}
.sja-btn-whatsapp:hover {
  background: #1ebc59;
  transform: translateY(-2px);
}

/* Option Selection Pill */
.sja-opt {
  font-family: 'Poppins', sans-serif;
  font-size: 13px;
  font-weight: 400; /* MAX 400 */
  padding: 9px 18px;
  border-radius: 40px;
  border: 1.5px solid var(--sja-brown);
  background: var(--sja-white);
  color: var(--sja-black);
  cursor: pointer;
  box-shadow: 2px 2px 0 rgba(0,0,0,0.08);
  transition: all 0.2s ease;
}
.sja-opt:hover {
  background: var(--sja-light-yellow);
}
.sja-opt.selected {
  background: var(--sja-yellow);
  border-color: var(--sja-brown);
  box-shadow: 2px 2px 0 rgba(0,0,0,0.12);
}
```

---

### E. Progress Bars & Metric Rings
Always use the brand dual-color gradient:
```css
/* Linear Gradient Progress Fill */
.sja-progress-fill {
  background: linear-gradient(90deg, var(--sja-yellow) 0%, var(--sja-orange) 100%);
  height: 8px;
  border-radius: 999px;
  transition: width 0.4s ease;
}

/* SVG Circular Gauge */
.sja-ring-fill {
  stroke: var(--sja-orange);
  stroke-linecap: round;
  transition: stroke-dashoffset 1s ease;
}

.sja-ring-pct {
  font-family: 'Poppins', sans-serif;
  font-weight: 400; /* MAX 400 */
  font-size: 2.5rem;
}
```

---

## 5. Conversion Engineering Rules

Every page or interactive tool created by AI must follow these 4 growth rules:

### Rule 1: The "Position 3 & 4" In-Feed Ad Insertion Rule
Whenever rendering a dynamic list (past papers, search results, school directory), inject a conversion card at **Index 2 (Position 3)** or **Index 3 (Position 4)**:

```javascript
if (index === 3) {
  const adCard = document.createElement('div');
  adCard.className = 'sja-card sja-highlight-card';
  adCard.innerHTML = `
    <h3 style="color:var(--sja-orange);font-weight:400;font-size:1.3rem;margin-bottom:8px;">Stuck on these past papers?</h3>
    <p style="font-size:13.5px;color:var(--sja-dark-grey);margin-bottom:18px;line-height:1.6;font-weight:300;">
      Don't lose marks on tricky questions. Master the exact CAIE marking scheme with Karachi's elite faculty from <strong>IBA, LUMS, and KGS</strong>. Join hundreds of SJ Academy students who secured straight A*s.
    </p>
    <a href="https://sjacademy.pk/o-a-level-classes/" class="sja-btn sja-btn-primary" target="_blank">Join a Free Demo Class</a>
  `;
  container.appendChild(adCard);
}
```

### Rule 2: Frictionless Elementor Popup Trigger
All registration buttons that open lead capture modals must link to the exact Elementor popup action hook:
```html
<a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-primary">Register Now</a>
```

### Rule 3: Pre-Populated WhatsApp Consultation Link
Always route direct chat inquiries to:
```html
<a href="https://wa.me/923362144454?text=Hi%20SJ%20Academy,%20I%20want%20to%20inquire%20about%20classes" class="sja-btn sja-btn-whatsapp" target="_blank">
  WhatsApp Us
</a>
```

### Rule 4: Gated Lead Capture with Frosted Glass (`backdrop-filter: blur(8px)`)
For interactive tools (quizzes, advanced calculators), gate the full question bank with an overlay that unlocks via `MutationObserver` on WPForms submission:
```css
.sja-lock-overlay {
  position: relative;
  z-index: 10;
  background: rgba(255, 255, 255, 0.45);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.sja-unlocked .sja-lock-overlay {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
```

---

## 6. Architecture & Data Principles

1. **Zero-Backend / Headless CMS:**
   * AI connects directly to published Google Sheets (CSV/TSV) or cloud storage buckets.
2. **Stale-While-Revalidate Caching:**
   * Always write a caching wrapper using `localStorage` (TTL: 6h to 24h) to ensure sub-10ms subsequent page loads.
3. **Bulletproof Scoped Resets:**
   * All styles must be scoped inside a parent ID (e.g., `#sj-tool-wrapper`) with `box-sizing: border-box` to avoid colliding with WordPress or Elementor themes.

---

## 7. Master AI Code Boilerplate Template (Max Font Weight: 400)

When asked to build a new tool or landing page, AI should use this standalone template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Title] | SJ Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap" rel="stylesheet">
  
  <style>
    #sja-widget-root {
      --sja-yellow: #FCE004;
      --sja-light-yellow: #FFF9CC;
      --sja-brown: #453516;
      --sja-orange: #FE6100;
      --sja-orange-hover: #E55800;
      --sja-black: #000000;
      --sja-dark-grey: #222222;
      --sja-grey: #555555;
      --sja-light-bg: #FAFAFA;
      --sja-white: #FFFFFF;
      --sja-border-light: #E5E5E5;
      --sja-whatsapp: #25D366;
      --sja-shadow-card: 0 10px 25px rgba(0,0,0,0.05);
      --sja-shadow-card-hover: 0 20px 40px rgba(0,0,0,0.1);
      --sja-shadow-button: 0 4px 10px rgba(254,97,0,0.3);
      --sja-transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      
      font-family: 'Poppins', sans-serif;
      font-weight: 300;
      color: var(--sja-black);
      line-height: 1.6;
      background: var(--sja-white);
      width: 100%;
      box-sizing: border-box;
    }

    #sja-widget-root *, #sja-widget-root *::before, #sja-widget-root *::after {
      box-sizing: border-box;
      font-weight: inherit;
    }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

    /* Header */
    .sja-header { text-align: center; padding: 50px 0 35px; }
    .sja-badge { display: inline-block; background: #fff; border: 1.5px solid #000; border-radius: 50px; padding: 4px; margin-bottom: 20px; box-shadow: 3px 3px 0 rgba(0,0,0,0.12); }
    .sja-mode-pill { padding: 6px 18px; border-radius: 40px; font-size: 0.8rem; font-weight: 400; text-transform: uppercase; letter-spacing: 0.8px; background: var(--sja-yellow); color: #000; }
    .sja-title { font-size: clamp(1.9rem, 3.8vw, 3rem); font-weight: 400; margin-bottom: 16px; line-height: 1.25; }
    .sja-highlight { background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%) no-repeat 0 85% / 100% 35%; display: inline; padding: 0 3px; font-weight: 400; }
    .sja-subtitle { font-size: 1.05rem; font-weight: 300; color: var(--sja-dark-grey); max-width: 700px; margin: 0 auto 25px; line-height: 1.6; }

    /* Full-Width Filter Section */
    .sja-controls { background: var(--sja-light-bg); padding: 35px 0; border-top: 1px solid #eee; border-bottom: 1px solid #eee; }

    /* Cards Grid */
    .sja-grid { display: grid; grid-template-columns: 1fr; gap: 25px; padding: 45px 0; }
    @media(min-width: 768px) { .sja-grid { grid-template-columns: repeat(2, 1fr); } }
    @media(min-width: 992px) { .sja-grid { grid-template-columns: repeat(3, 1fr); } }

    .sja-card {
      background: var(--sja-white);
      padding: 26px;
      border-top: 5px solid var(--sja-brown);
      border-radius: 12px;
      box-shadow: var(--sja-shadow-card);
      transition: var(--sja-transition);
      display: flex; flex-direction: column;
    }
    .sja-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--sja-shadow-card-hover);
      border-top-color: var(--sja-orange);
    }
    .sja-card h3 {
      font-size: 1.25rem;
      font-weight: 400;
      margin-bottom: 10px;
      color: var(--sja-black);
    }
    .sja-card.highlight {
      border-top-color: var(--sja-yellow);
      background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #FFFDF5 100%);
      border: 1.5px solid var(--sja-yellow);
    }

    /* Buttons */
    .sja-btn {
      font-family: 'Poppins', sans-serif;
      font-size: 13.5px; font-weight: 400; text-transform: uppercase;
      letter-spacing: 0.8px; padding: 13px 26px; border-radius: 8px;
      display: inline-flex; align-items: center; justify-content: center;
      cursor: pointer; text-decoration: none; border: 1.5px solid transparent;
      transition: var(--sja-transition);
    }
    .sja-btn-primary { background: var(--sja-orange); color: #fff; border-color: var(--sja-orange); box-shadow: var(--sja-shadow-button); }
    .sja-btn-primary:hover { background: var(--sja-orange-hover); transform: translateY(-2px); box-shadow: var(--sja-shadow-button-hover); }
    .sja-btn-whatsapp { background: var(--sja-whatsapp); color: #fff; border-color: var(--sja-whatsapp); }
  </style>
</head>
<body>

<div id="sja-widget-root">
  <div class="container">
    <div class="sja-header">
      <div class="sja-badge">
        <div class="sja-mode-pill">⚡ [TOOL / BADGE NAME]</div>
      </div>
      <h1 class="sja-title">Main Title <span class="sja-highlight">[Highlighted Word]</span></h1>
      <p class="sja-subtitle">[Helpful subtitle explaining what the student will achieve in seconds.]</p>
    </div>
  </div>

  <div class="sja-controls">
    <div class="container">
      <!-- Reactive Filters / Search Inputs -->
    </div>
  </div>

  <div class="container">
    <div class="sja-grid" id="sja-results-grid">
      <!-- Dynamic Results / Bento Cards -->
    </div>
  </div>
</div>

<script>
(function(){
  // Vanilla JS logic with caching, live filters, and Position 3/4 ad injection
})();
</script>

</body>
</html>
```
