# 01 - IBCC Equivalence Calculator

> **Type:** Interactive Tool / Lead Generation Landing Widget  
> **Brand / Project:** SJ Academy (`sjacademy.pk`)  
> **Target Audience:** O-Level and A-Level students in Pakistan applying for Pakistani university admissions / IBCC Equivalence certificate.

---

## 1. Overview & Purpose

The **IBCC Equivalence Calculator** is an interactive widget and landing page tool designed to help Pakistani O/A Level students calculate their official Inter Board Committee of Chairmen (IBCC) equivalence score.

It provides immediate utility to students while serving as a high-conversion lead generation tool with an embedded pattern-interrupt CTA directing users to book a free demo class at SJ Academy.

---

## 2. Design System & Tokens

### Typography
- **Primary Font Family:** `'Poppins', sans-serif` (Weights: `300`, `400`, `500`, `600`, `700`, `800`)

### Color Palette

| Token | Light Theme | Dark Theme | Purpose / Usage |
| :--- | :--- | :--- | :--- |
| `--primary-yellow` | `#FCE004` | `#FCE004` | Brand primary, highlights, active toggles, badge background |
| `--orange` | `#FE6100` | `#FE6100` | Accent color, score highlights, primary CTA button |
| `--orange-dark` | `#E55800` | `#E55800` | Hover state for CTA buttons |
| `--bg-body` | `transparent` | `#0A0F16` | Widget backdrop / container background |
| `--bg-card` | `#FFFFFF` | `#111822` | Calculator main card background |
| `--bg-results` | `#FFF9CC` | `rgba(252, 224, 4, 0.05)` | Results score card background |
| `--text-main` | `#000000` | `#FFFFFF` | Primary headings, values, and strong text |
| `--text-sec` | `#222222` | `#F8FAFC` | Secondary copy, labels, percentages |
| `--text-muted` | `#555555` | `#94A3B8` | Subtitles, helper text, disclaimers |
| `--border-color` | `#E5E5E5` | `rgba(255, 255, 255, 0.15)` | Form input borders, dashed add buttons |
| `--border-heavy` | `#453516` | `#FCE004` | Card top accent border, active state outlines |

### Features & Controls
- **Dual Theme Support:** Light mode and Dark mode toggle with an iOS-style toggle switch.
- **WordPress-Resistant Styling:** Uses explicit scoped selector `#sj-ibcc-widget` with `!important` declarations to avoid WordPress theme conflicts.
- **Responsive Breakpoint:** Mobile-first layout switching to a 2-column grid on desktop (`min-width: 768px`).

---

## 3. Component Hierarchy & Layout Structure

```
#sj-ibcc-widget [data-theme="light" | "dark"]
├── header
│   ├── .header-controls (Grid: Spacer | Badge | Dark Mode Switch)
│   ├── h1 ("IBCC Equivalence" with highlighted accent)
│   └── p.subtitle
│
└── .calc-wrapper (Card with top accent border)
    ├── .type-toggle (Radio buttons: HSSC / A-Level vs SSC / O-Level)
    └── .calc-grid
        ├── .grade-section #olevel-section (O Level inputs + Add Subject button)
        ├── .grade-section #alevel-section (A Level inputs + Add Subject button)
        ├── .results-panel #results-panel (Algorithm badge, total marks, percentage, disclaimer)
        └── .seo-cta (Pattern interrupt dark box with demo booking CTA)
```

---

## 4. Calculation Logic & Formula

### IBCC Grade Conversion Table

| Grade | Marks Allocated |
| :--- | :--- |
| **A\*** | `90` |
| **A** | `85` |
| **B** | `75` |
| **C** | `65` |
| **D** | `55` |
| **E** | `45` |
| **U** | `0` |
| **None** | Excluded (`-1`) |

### Modes & Selection Rules

1. **A-Level Equivalence (HSSC / 1100 Marks):**
   - **O-Level component:** Automatically sorts all entered O-Level grades and picks the **Top 8 highest marks** (Max: 8 * 90 = 720).
   - **A-Level component:** Automatically sorts all entered A-Level grades and picks the **Top 3 highest marks** (Max: 3 * 90 = 270 or up to total scale of 1100).
   - **Total Maximum Marks:** `1100`
   - **Formula:** Equivalence % = ((Sum of Best 8 O-Levels + Sum of Best 3 A-Levels) / 1100) * 100

2. **O-Level Only Equivalence (SSC / 800 Marks):**
   - Automatically picks the **Top 8 highest O-Level marks**.
   - **Total Maximum Marks:** `800`
   - **Formula:** Equivalence % = (Sum of Best 8 O-Levels / 800) * 100

---

## 5. Copy & Marketing Content

### Header
- **Tool Badge:** `Calculator Tool`
- **Headline:** `IBCC Equivalence` (with `Equivalence` highlighted)
- **Subtitle:** *"Enter all your subjects. Our algorithm automatically picks your highest grades to maximize your equivalence score!"*

### Results & Algorithm Notice
- **Algorithm Badge (HSSC):** *"Algorithm applied: Best 8 O-Levels & Best 3 A-Levels"*
- **Algorithm Badge (SSC):** *"Algorithm applied: Best 8 O-Levels Only"*
- **Disclaimer:** *"Calculated using the standard Science Group formula. Official equivalence certificates are issued strictly by IBCC."*

### SEO Lead-Gen CTA (Pattern Interrupt)
- **Heading:** *"Worried about a low equivalence?"*
- **Body Copy:** *"Don't let a bad grade ruin your university merit formula. Master the exact CAIE marking scheme with Karachi's elite faculty. Join hundreds of SJ Academy students who secured straight A*s last year."*
- **Button CTA:** `Book a Free Demo` (`https://www.sjacademy.pk/demo-class-registration/`)
- **Subtext:** `In-class (DHA) & Online`

---

## 6. Complete Source Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IBCC Equivalence Calculator</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        #sj-ibcc-widget {
            /* Brand Colors (Static across themes) */
            --primary-yellow: #FCE004;
            --orange: #FE6100;
            --orange-dark: #e55800;
            
            /* Light Theme Variables */
            --bg-body: transparent;
            --bg-card: #FFFFFF;
            --bg-results: #FFF9CC;
            --text-main: #000000;
            --text-sec: #222222;
            --text-muted: #555555;
            --border-color: #e5e5e5;
            --border-heavy: #453516; /* Brown */
            --shadow: 0 10px 25px rgba(0,0,0,0.05);
            --select-bg: #FFFFFF;
            --badge-text: #000000;
            
            font-family: 'Poppins', sans-serif;
            color: var(--text-main);
            background-color: var(--bg-body) !important;
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 15px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        #sj-ibcc-widget[data-theme="dark"] {
            /* Dark Theme Variables */
            --bg-body: #0A0F16;
            --bg-card: #111822;
            --bg-results: rgba(252, 224, 4, 0.05);
            --text-main: #FFFFFF;
            --text-sec: #F8FAFC;
            --text-muted: #94A3B8;
            --border-color: rgba(255,255,255,0.15);
            --border-heavy: #FCE004;
            --shadow: 0 10px 30px rgba(0,0,0,0.5);
            --select-bg: rgba(0,0,0,0.4);
            --badge-text: #000000;
        }

        /* Header Grid - Perfect centering for badge, right-aligned toggle */
        #sj-ibcc-widget .header-controls {
            display: grid !important;
            grid-template-columns: 1fr auto 1fr !important;
            align-items: center !important;
            width: 100% !important;
            margin-bottom: 25px !important;
        }

        #sj-ibcc-widget .header-spacer {
            display: block !important;
        }

        /* Sleek iOS-style Toggle Switch */
        #sj-ibcc-widget .theme-switch-wrapper {
            justify-self: end !important;
            display: flex !important;
            align-items: center !important;
            gap: 8px !important;
        }

        #sj-ibcc-widget .theme-switch-label {
            font-size: 10px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            color: var(--text-muted) !important;
            letter-spacing: 0.5px !important;
            font-style: normal !important;
        }

        #sj-ibcc-widget .theme-switch {
            position: relative !important;
            display: inline-block !important;
            width: 36px !important;
            height: 20px !important;
            margin: 0 !important;
        }

        #sj-ibcc-widget .theme-switch input { 
            opacity: 0 !important;
            width: 0 !important;
            height: 0 !important;
            position: absolute !important;
        }

        #sj-ibcc-widget .slider {
            position: absolute !important;
            cursor: pointer !important;
            top: 0 !important; 
            left: 0 !important; 
            right: 0 !important; 
            bottom: 0 !important;
            background-color: #e5e5e5 !important;
            transition: .3s !important;
            border-radius: 34px !important;
        }

        #sj-ibcc-widget[data-theme="dark"] .slider {
            background-color: var(--border-color) !important;
        }

        #sj-ibcc-widget .slider:before {
            position: absolute !important;
            content: "" !important;
            height: 14px !important;
            width: 14px !important;
            left: 3px !important;
            bottom: 3px !important;
            background-color: white !important;
            transition: .3s !important;
            border-radius: 50% !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        }

        #sj-ibcc-widget .theme-switch input:checked + .slider {
            background-color: var(--primary-yellow) !important;
        }

        #sj-ibcc-widget .theme-switch input:checked + .slider:before {
            transform: translateX(16px) !important;
            background-color: #000000 !important;
        }

        /* Top Header Area */
        #sj-ibcc-widget header { 
            text-align: center; 
            margin-bottom: 30px; 
            padding-top: 20px;
        }

        #sj-ibcc-widget .mode-badge-wrap {
            display: inline-block;
            border: 2px solid var(--text-main) !important;
            border-radius: 50px !important;
            padding: 4px 6px !important;
            box-shadow: 3px 3px 0 rgba(0,0,0,0.15) !important;
            margin-bottom: 16px !important;
        }

        #sj-ibcc-widget[data-theme="dark"] .mode-badge-wrap {
            border-color: var(--primary-yellow) !important;
        }

        #sj-ibcc-widget .mode-badge {
            background: var(--primary-yellow) !important;
            color: var(--badge-text) !important;
            font-size: 0.75rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            padding: 6px 14px !important;
            border-radius: 40px !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
            margin: 0 !important;
        }

        #sj-ibcc-widget h1 {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            line-height: 1.2 !important;
            color: var(--text-main) !important;
            margin-bottom: 12px !important;
            margin-top: 0 !important;
            border: none !important;
            padding: 0 !important;
        }

        #sj-ibcc-widget h1 .highlight {
            background: linear-gradient(120deg, var(--primary-yellow) 0%, var(--primary-yellow) 100%) !important;
            background-repeat: no-repeat !important;
            background-size: 100% 35% !important;
            background-position: 0 85% !important;
            display: inline !important;
            padding: 0 3px !important;
            transition: all 0.3s ease !important;
        }

        #sj-ibcc-widget[data-theme="dark"] h1 .highlight {
            color: #000000 !important;
            background-size: 100% 100% !important;
            background-position: 0 0 !important;
            padding: 0 10px !important;
            border-radius: 6px !important;
        }

        #sj-ibcc-widget .subtitle {
            font-size: 0.95rem !important;
            font-weight: 500 !important;
            color: var(--text-sec) !important;
            margin: 0 auto !important;
            line-height: 1.5 !important;
            max-width: 600px !important;
        }

        /* Calculator Wrapper */
        #sj-ibcc-widget .calc-wrapper {
            background: var(--bg-card) !important;
            border-top: 6px solid var(--border-heavy) !important;
            border-radius: 12px !important;
            box-shadow: var(--shadow) !important;
            padding: 20px !important;
            transition: all 0.3s ease !important;
        }

        #sj-ibcc-widget .type-toggle {
            display: flex !important;
            flex-direction: column !important;
            gap: 12px !important;
            margin-bottom: 25px !important;
            padding-bottom: 25px !important;
            border-bottom: 2px solid var(--border-color) !important;
        }

        #sj-ibcc-widget .type-toggle div {
            display: block !important;
        }

        #sj-ibcc-widget .type-toggle label {
            cursor: pointer !important;
            font-weight: 700 !important;
            font-size: 13px !important;
            padding: 12px 16px !important;
            border-radius: 8px !important;
            border: 2px solid var(--border-color) !important;
            color: var(--text-muted) !important;
            transition: all 0.2s ease !important;
            text-align: center !important;
            display: block !important;
            margin: 0 !important;
            background: transparent !important;
        }

        #sj-ibcc-widget .type-toggle input { display: none !important; }

        #sj-ibcc-widget .type-toggle input:checked + label {
            background: var(--primary-yellow) !important;
            border-color: var(--border-heavy) !important;
            color: var(--badge-text) !important;
        }

        /* Grid */
        #sj-ibcc-widget .calc-grid {
            display: grid !important;
            grid-template-columns: 1fr !important;
            gap: 30px !important;
        }

        #sj-ibcc-widget .grade-section h3 {
            font-size: 1.1rem !important;
            font-weight: 800 !important;
            color: var(--text-main) !important;
            margin-bottom: 5px !important;
            margin-top: 0 !important;
            display: flex !important;
            align-items: center !important;
            gap: 8px !important;
            border: none !important;
        }

        #sj-ibcc-widget .grade-section p.helper {
            font-size: 11px !important;
            color: var(--text-muted) !important;
            margin-bottom: 15px !important;
            font-weight: 500 !important;
            margin-top: 0 !important;
        }

        #sj-ibcc-widget .subject-row {
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            margin-bottom: 10px !important;
            animation: fadeUp 0.3s ease forwards;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        #sj-ibcc-widget .subject-row label {
            font-size: 11px !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            color: var(--text-sec) !important;
            margin: 0 !important;
        }

        /* Select Dropdowns */
        #sj-ibcc-widget select {
            width: 120px !important;
            padding: 10px 12px !important;
            border: 2px solid var(--border-color) !important;
            border-radius: 8px !important;
            font-family: 'Poppins', sans-serif !important;
            font-size: 13px !important;
            font-weight: 700 !important;
            color: var(--text-main) !important;
            background-color: var(--select-bg) !important;
            -webkit-appearance: none !important;
            -moz-appearance: none !important;
            appearance: none !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
            background-image: linear-gradient(45deg, transparent 50%, currentColor 50%), linear-gradient(135deg, currentColor 50%, transparent 50%) !important;
            background-position: calc(100% - 15px) calc(1em + 2px), calc(100% - 10px) calc(1em + 2px) !important;
            background-size: 5px 5px, 5px 5px !important;
            background-repeat: no-repeat !important;
            margin: 0 !important;
            height: auto !important;
            box-shadow: none !important;
        }

        #sj-ibcc-widget select:focus {
            outline: none !important;
            border-color: var(--primary-yellow) !important;
        }

        #sj-ibcc-widget .add-subject-btn {
            background: none !important;
            border: 2px dashed var(--border-color) !important;
            color: var(--text-muted) !important;
            font-weight: 700 !important;
            font-size: 12px !important;
            text-transform: uppercase !important;
            padding: 14px !important;
            width: 100% !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
            margin-top: 10px !important;
            display: block !important;
        }

        #sj-ibcc-widget .add-subject-btn:hover {
            border-color: var(--orange) !important;
            color: var(--orange) !important;
            background: rgba(254, 97, 0, 0.05) !important;
        }

        /* Results Panel */
        #sj-ibcc-widget .results-panel {
            grid-column: 1 / -1 !important;
            margin-top: 10px !important;
            background: var(--bg-results) !important;
            border: 2px solid var(--primary-yellow) !important;
            border-radius: 12px !important;
            padding: 25px 15px !important;
            text-align: center !important;
            transition: all 0.3s ease !important;
        }

        #sj-ibcc-widget .results-panel p.label {
            font-size: 11px !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            color: var(--text-muted) !important;
            margin-bottom: 5px !important;
            margin-top: 0 !important;
        }

        #sj-ibcc-widget .total-score {
            font-size: 3rem !important;
            font-weight: 800 !important;
            color: var(--text-main) !important;
            line-height: 1.1 !important;
            margin: 5px 0 !important;
        }
        
        #sj-ibcc-widget .total-score span {
            color: var(--orange) !important;
        }

        #sj-ibcc-widget .total-percentage {
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            color: var(--text-sec) !important;
            margin-top: 5px !important;
            margin-bottom: 15px !important;
        }

        #sj-ibcc-widget .algorithm-note {
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
            background: var(--primary-yellow) !important;
            padding: 6px 10px !important;
            border-radius: 6px !important;
            font-size: 10px !important;
            font-weight: 700 !important;
            color: var(--badge-text) !important;
            margin-bottom: 15px !important;
            margin-top: 0 !important;
        }

        #sj-ibcc-widget .disclaimer {
            font-size: 10px !important;
            color: var(--text-muted) !important;
            font-style: italic !important;
            line-height: 1.5 !important;
            max-width: 600px !important;
            margin: 0 auto !important;
        }

        /* SEO CTA (High Contrast Pattern Interrupt) */
        #sj-ibcc-widget .seo-cta {
            grid-column: 1 / -1 !important;
            margin-top: 20px !important;
            background: #111822 !important; 
            border-top: 6px solid var(--orange) !important;
            border-radius: 12px !important;
            padding: 30px 20px !important;
            text-align: center !important;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2) !important;
            border-bottom: none !important;
            border-left: none !important;
            border-right: none !important;
        }

        #sj-ibcc-widget .seo-cta h4 {
            color: var(--primary-yellow) !important; 
            font-weight: 800 !important;
            font-size: 1.3rem !important;
            margin-bottom: 10px !important;
            margin-top: 0 !important;
            border: none !important;
        }
        
        #sj-ibcc-widget .seo-cta p {
            font-size: 13px !important;
            font-weight: 400 !important;
            color: #F8FAFC !important; 
            margin-bottom: 20px !important;
            max-width: 700px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            line-height: 1.6 !important;
            margin-top: 0 !important;
        }

        #sj-ibcc-widget .btn-cta {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            background: var(--orange) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 20px !important;
            font-family: 'Poppins', sans-serif !important;
            font-size: 13px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            text-decoration: none !important;
            box-shadow: var(--shadow-button) !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
        }

        #sj-ibcc-widget .btn-cta:hover {
            background: var(--orange-dark) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 15px rgba(254,97,0,0.4) !important;
        }
        
        #sj-ibcc-widget .btn-subtext {
            display: block !important;
            font-size: 10px !important;
            font-weight: 800 !important;
            color: var(--primary-yellow) !important;
            margin-top: 12px !important;
            text-transform: uppercase !important;
        }

        /* Desktop Breakpoint */
        @media (min-width: 768px) {
            #sj-ibcc-widget { padding: 40px 20px; }
            #sj-ibcc-widget .theme-toggle-wrapper { top: 30px; right: 40px; }
            #sj-ibcc-widget h1 { font-size: 2.8rem !important; }
            #sj-ibcc-widget header { padding-top: 0; }
            #sj-ibcc-widget .calc-wrapper { padding: 40px !important; }
            #sj-ibcc-widget .type-toggle { 
                flex-direction: row !important; 
                justify-content: center !important;
                gap: 15px !important;
            }
            #sj-ibcc-widget .type-toggle label {
                padding: 12px 24px !important;
                border-radius: 40px !important;
                font-size: 14px !important;
            }
            #sj-ibcc-widget .calc-grid {
                grid-template-columns: 1fr 1fr !important;
                gap: 40px !important;
            }
            #sj-ibcc-widget select { width: 140px !important; font-size: 14px !important; }
            #sj-ibcc-widget .results-panel { padding: 30px !important; }
            #sj-ibcc-widget .total-score { font-size: 3.5rem !important; }
            #sj-ibcc-widget .seo-cta { padding: 40px !important; }
            #sj-ibcc-widget .seo-cta h4 { font-size: 1.5rem !important; }
            #sj-ibcc-widget .btn-cta { width: auto !important; padding: 14px 30px !important; font-size: 14px !important; }
        }
    </style>
</head>
<body>

<div id="sj-ibcc-widget" data-theme="light">

    <header>
        <div class="header-controls">
            <div class="header-spacer"></div>
            <div class="mode-badge-wrap" style="justify-self: center;">
                <div class="mode-badge">
                    <svg width="14" height="14" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 9h-2V7h-2v5H6v2h2v5h2v-5h2v-2z" fill="currentColor"/></svg>
                    Calculator Tool
                </div>
            </div>
            <div class="theme-switch-wrapper">
                <em class="theme-switch-label">Dark Mode</em>
                <label class="theme-switch" for="theme-checkbox">
                    <input type="checkbox" id="theme-checkbox" onchange="toggleTheme()">
                    <div class="slider"></div>
                </label>
            </div>
        </div>
        
        <h1>IBCC <span class="highlight">Equivalence</span></h1>
        <p class="subtitle">Enter all your subjects. Our algorithm automatically picks your highest grades to maximize your equivalence score!</p>
    </header>

    <div class="calc-wrapper">
        
        <div class="type-toggle">
            <div>
                <input type="radio" id="type-hssc" name="calc-type" value="hssc" checked onchange="toggleCalculationType()">
                <label for="type-hssc">A-Level Equivalence (HSSC / 1100)</label>
            </div>
            <div>
                <input type="radio" id="type-ssc" name="calc-type" value="ssc" onchange="toggleCalculationType()">
                <label for="type-ssc">O-Level Only (SSC / 800)</label>
            </div>
        </div>

        <div class="calc-grid">
            
            <!-- O Level Section -->
            <div class="grade-section" id="olevel-section">
                <h3>📘 O Level</h3>
                <p class="helper">IBCC requires exactly 8 subjects.</p>
                <div id="olevel-inputs"></div>
                <button class="add-subject-btn" onclick="addSubjectRow('olevel-inputs', 'O Level')">+ Add O Level Subject</button>
            </div>

            <!-- A Level Section -->
            <div class="grade-section" id="alevel-section">
                <h3>📙 A Level</h3>
                <p class="helper">IBCC requires exactly 3 subjects.</p>
                <div id="alevel-inputs"></div>
                <button class="add-subject-btn" onclick="addSubjectRow('alevel-inputs', 'A Level')">+ Add A Level Subject</button>
            </div>

            <!-- Results Section -->
            <div class="results-panel" id="results-panel">
                <div class="algorithm-note" id="algo-note">
                    <svg width="12" height="12" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="currentColor"/></svg>
                    Algorithm applied: Best 8 O-Levels & Best 3 A-Levels
                </div>
                <p class="label">Estimated Equivalence Marks</p>
                <div class="total-score"><span id="total-marks">0</span> / <span id="max-marks" style="color: inherit;">1100</span></div>
                <div class="total-percentage" id="total-percentage">0.00%</div>
                <p class="disclaimer">*Calculated using the standard Science Group formula. Official equivalence certificates are issued strictly by IBCC.</p>
            </div>

            <!-- SEO CTA Section (Pattern Interrupt) -->
            <div class="seo-cta">
                <h4>Worried about a low equivalence?</h4>
                <p>Don't let a bad grade ruin your university merit formula. Master the exact CAIE marking scheme with Karachi's elite faculty. Join hundreds of SJ Academy students who secured straight A*s last year.</p>
                <a href="https://www.sjacademy.pk/demo-class-registration/" class="btn-cta">Book a Free Demo</a>
                <span class="btn-subtext">In-class (DHA) & Online</span>
            </div>

        </div>
    </div>

    <script>
        function toggleTheme() {
            const widget = document.getElementById('sj-ibcc-widget');
            const checkbox = document.getElementById('theme-checkbox');
            
            if (checkbox.checked) {
                widget.setAttribute('data-theme', 'dark');
            } else {
                widget.setAttribute('data-theme', 'light');
            }
        }

        const gradeValues = {
            "A*": 90, "A": 85, "B": 75, "C": 65,
            "D": 55, "E": 45, "U": 0, "None": -1
        };

        let oLevelCount = 0;
        let aLevelCount = 0;

        function createDropdown() {
            let options = '<option value="None">None</option>';
            for (const [grade, value] of Object.entries(gradeValues)) {
                if(grade !== "None") {
                    options += `<option value="${grade}">${grade} (${value})</option>`;
                }
            }
            return `<select class="grade-select" onchange="calculateEquivalence()">${options}</select>`;
        }

        function addSubjectRow(containerId, typeLabel) {
            const container = document.getElementById(containerId);
            const isOLevel = containerId === 'olevel-inputs';
            const count = isOLevel ? ++oLevelCount : ++aLevelCount;
            
            const div = document.createElement('div');
            div.className = 'subject-row';
            div.innerHTML = `
                <label>${typeLabel} ${count}</label>
                ${createDropdown()}
            `;
            container.appendChild(div);
            calculateEquivalence();
        }

        // Initialize default rows
        for (let i = 0; i < 8; i++) addSubjectRow('olevel-inputs', 'O Level');
        for (let i = 0; i < 3; i++) addSubjectRow('alevel-inputs', 'A Level');

        function toggleCalculationType() {
            const isHSSC = document.getElementById('type-hssc').checked;
            const aLevelSection = document.getElementById('alevel-section');
            const algoNote = document.getElementById('algo-note');
            
            if (isHSSC) {
                aLevelSection.style.display = 'block';
                algoNote.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="currentColor"/></svg> Algorithm applied: Best 8 O-Levels & Best 3 A-Levels';
            } else {
                aLevelSection.style.display = 'none';
                algoNote.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="currentColor"/></svg> Algorithm applied: Best 8 O-Levels Only';
            }
            calculateEquivalence();
        }

        function calculateEquivalence() {
            const isHSSC = document.getElementById('type-hssc').checked;
            let totalMarks = 0;
            const maxMarks = isHSSC ? 1100 : 800;
            
            const oSelects = document.querySelectorAll('#olevel-inputs select');
            let oScores = [];
            oSelects.forEach(sel => {
                const val = gradeValues[sel.value];
                if (val > -1) oScores.push(val);
            });
            oScores.sort((a,b) => b - a);
            const best8OLevels = oScores.slice(0, 8);
            totalMarks += best8OLevels.reduce((a, b) => a + b, 0);

            if (isHSSC) {
                const aSelects = document.querySelectorAll('#alevel-inputs select');
                let aScores = [];
                aSelects.forEach(sel => {
                    const val = gradeValues[sel.value];
                    if (val > -1) aScores.push(val);
                });
                aScores.sort((a,b) => b - a);
                const best3ALevels = aScores.slice(0, 3);
                totalMarks += best3ALevels.reduce((a, b) => a + b, 0);
            }

            document.getElementById('total-marks').innerText = totalMarks;
            document.getElementById('max-marks').innerText = maxMarks;
            
            const percentage = ((totalMarks / maxMarks) * 100).toFixed(2);
            document.getElementById('total-percentage').innerText = `${percentage}%`;
        }

        toggleCalculationType();
    </script>
</div>
</body>
</html>
```
