# 10 - Expert Faculty & Teachers Bento Grid Directory

> **Type:** Faculty Showcase / Behance-Inspired Bento Grid / Interactive Profile Modal  
> **Brand / Project:** SJ Academy (`sjacademy.pk/faculty/` or embed widget)  
> **Target Audience:** Prospective students and parents evaluating teacher credentials, subject specializations, past distinctions, and prestigious school affiliations (KGS, Beaconhouse, City School, Bay View, etc.).

---

## 1. Overview & Architectural Capabilities

The **Expert Faculty Directory** is a Behance-inspired interactive showcase designed to highlight teacher authority, elite institutional backgrounds, and Cambridge/IB specializations.

### Key Capabilities:
1. **Interactive Custom Pencil Cursor:** Floating animated pencil icon (`#customCursor`) that tracks cursor coordinates, dynamically rotates/scales on hover over `.hover-target` elements, and safely falls back to native cursors on mobile touch devices.
2. **Dynamic Bento Grid with Featured Spans:** Co-founders (e.g., Sir Salman Junaid) span **2 columns** on desktop with golden/brown contrast accents and larger avatars.
3. **Multi-Category Filtering:** Real-time filtering across:
   - `All Teachers`
   - `O-Level`
   - `A-Level`
   - `Business` (Accounts, Economics, Business Studies)
   - `Sciences` (Physics, Chemistry, Biology, Computer Science, Math)
   - `Humanities` (Sociology, Psychology, English, Urdu, Islamiat, Pak Studies)
4. **Glassmorphic Detailed Modal View (`backdrop-filter: blur(15px)`):** Opens full teacher dossiers featuring extensive biographies, direct social profiles, experience years, and school affiliations (KGS, Beaconhouse, LGS, Education Bay, etc.).
5. **Conversion CTA Fold:** Direct registration link targeting Elementor Popup `ID: 6023` and direct WhatsApp consultation (`+92 336 2144454`).

---

## 2. Design Tokens & Styling System

Scoped inside `#sjacademy-teachers-widget`.

| Token | Hex / Value | Purpose |
| :--- | :--- | :--- |
| `--primary-yellow` | `#FCE004` | H1 highlight, mode badge, avatar ring border, modal accent |
| `--light-yellow` | `#FFF9CC` | Bottom CTA section background, highlight pills |
| `--brown` | `#453516` | Filter button outlines, co-founder card border, table labels |
| `--orange` | `#FE6100` | Active filter state, custom cursor, card hover accent, CTA buttons |
| `--black` | `#000000` | Headings, "Full Profile" button, high-contrast borders |
| `--dark-grey` | `#222222` | Subtitles, tag text |
| `--grey` | `#555555` | Bio snippets, secondary text |
| `--light-bg` | `#F9F9F9` | Page background, tag surfaces, social icon background |
| `--white` | `#FFFFFF` | Bento card surfaces, modal container background |
| `--transition` | `all 0.4s cubic-bezier(0.16, 1, 0.3, 1)` | Smooth acceleration curve for hover states & modals |

---

## 3. Component Hierarchy

```
#sjacademy-teachers-widget
├── #customCursor (.custom-cursor font-awesome pencil icon)
│
├── .hero-section
│   ├── .mode-pill ("👨‍🏫 EXPERT FACULTY")
│   ├── .page-title ("Meet the teachers behind SJ Academy")
│   └── .subtitle
│
├── .controls-section (.filter-group)
│   └── Buttons: All | O-Level | A-Level | Business | Sciences | Humanities
│
├── .grid-section
│   └── .bento-grid (#teachersGrid)
│       ├── .teacher-card.featured (2-Column Span: Sir Salman Junaid)
│       └── .teacher-card (1-Column Span: Faculty Cards)
│           ├── .card-top (Avatar + Name + Badges)
│           ├── .teacher-bio-snippet (4-line truncated bio)
│           └── .card-footer (Social icons row + "Full Profile" button)
│
├── .cta-section ("May/June 2027 Batches" + Elementor Popup & WhatsApp CTAs)
│
└── #teacherModal (.modal-overlay with glassmorphism blur)
    └── .modal-container
        ├── #closeModal (Top-right dismiss button)
        └── #modalContent (Modal Header + Full Bio + Key-Value Table)
```

---

## 4. Faculty Dataset Sample

```javascript
[
  {
    id: 100,
    name: "Sir Salman Junaid",
    isCoFounder: true,
    subjects: ["Math", "Physics"],
    level: ["O-Level", "A-Level"],
    category: ["sciences", "o-level", "a-level"],
    affiliations: ["SJ Academy (Co-founder)", "Ex-KGS Faculty", "NED University"],
    experience: "12+ Years"
  },
  {
    id: 1,
    name: "Sir Sunyyan Junaid",
    subjects: ["Business"],
    level: ["A-Level"],
    category: ["business", "a-level"],
    experience: "8+ Years"
  },
  {
    id: 2,
    name: "Sir Khawar Shuaib",
    subjects: ["Economics"],
    level: ["A-Level", "IB"],
    category: ["business", "a-level"],
    experience: "Since 2014"
  }
  // + Abdullah Zaman (Chem), Umair (Bio), Riza Walji (CS), Shaibaz Ali (Accounts),
  // Asmat Zafar (Urdu), Kashaan Ali (Isl/P.St), Saifullah (Accounts), Alyaan (Biz/Econ),
  // Muzna Zaidi (Psych), Tayyaba Yaseen (Soc/Eng), Basharat (Chem/Phy)
]
```

---

## 5. Complete Source Code

```html
<!-- SJ Academy Teachers Page - Elementor HTML Widget Code -->

<!-- Fonts & Icons -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
/* SJ Academy - Modern & Bold Behance Inspired Design */
#sjacademy-teachers-widget {
    --primary-yellow: #FCE004;
    --brown: #453516;
    --orange: #FE6100;
    --black: #000000;
    --white: #FFFFFF;
    --grey: #555555;
    --dark-grey: #222222;
    --light-bg: #F9F9F9;
    --light-yellow: #FFF9CC;
    
    --font-main: 'Poppins', sans-serif;
    --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

#sjacademy-teachers-widget * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    cursor: none !important;
}

#sjacademy-teachers-widget {
    font-family: var(--font-main) !important;
    background-color: var(--light-bg) !important;
    color: var(--black) !important;
    line-height: 1.6 !important;
    overflow-x: hidden !important;
}

#sjacademy-teachers-widget img {
    max-width: 100% !important;
    height: auto;
    display: block;
}

/* Custom Cursor */
#sjacademy-teachers-widget .custom-cursor {
    position: fixed !important;
    top: 0;
    left: 0;
    pointer-events: none !important;
    z-index: 100000 !important;
    font-size: 24px !important;
    color: var(--orange) !important;
    transform: translate(0, -100%) !important;
    transition: font-size 0.2s, color 0.2s !important;
}

#sjacademy-teachers-widget .hover-target:hover ~ .custom-cursor,
#sjacademy-teachers-widget a:hover ~ .custom-cursor,
#sjacademy-teachers-widget button:hover ~ .custom-cursor,
#sjacademy-teachers-widget .filter-btn:hover ~ .custom-cursor {
    font-size: 32px !important;
    color: var(--primary-yellow) !important;
    transform: translate(0, -100%) rotate(-15deg) !important;
}

/* Typography */
#sjacademy-teachers-widget .page-title {
    font-size: clamp(2.5rem, 6vw, 4.5rem) !important;
    font-weight: 900 !important;
    line-height: 1.1 !important;
    margin-bottom: 20px !important;
    letter-spacing: -2px !important;
    color: var(--black) !important;
}

#sjacademy-teachers-widget .text-outline {
    color: transparent !important;
    -webkit-text-stroke: 2px var(--black) !important;
}

#sjacademy-teachers-widget .highlight-text {
    background: linear-gradient(120deg, var(--primary-yellow) 0%, var(--primary-yellow) 100%) !important;
    background-repeat: no-repeat !important;
    background-size: 100% 35% !important;
    background-position: 0 85% !important;
    display: inline !important;
    padding: 0 5px !important;
}

#sjacademy-teachers-widget .subtitle {
    font-size: clamp(1rem, 2vw, 1.3rem) !important;
    font-weight: 400 !important;
    color: var(--dark-grey) !important;
    max-width: 700px !important;
    margin: 0 auto !important;
}

/* Layout */
#sjacademy-teachers-widget .container {
    max-width: 1300px !important;
    margin: 0 auto !important;
    padding: 0 20px !important;
}

/* Hero Section */
#sjacademy-teachers-widget .hero-section {
    padding: 60px 0 40px !important;
    text-align: center !important;
}

#sjacademy-teachers-widget .mode-pill-wrapper {
    margin-bottom: 40px !important;
}

#sjacademy-teachers-widget .mode-pill {
    border: 2px solid var(--black) !important;
    border-radius: 50px !important;
    box-shadow: 4px 4px 0 rgba(0, 0, 0, 0.15) !important;
    background: var(--primary-yellow) !important;
    color: var(--black) !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    font-size: 0.85rem !important;
    padding: 10px 28px !important;
    display: inline-block !important;
}

/* Filters */
#sjacademy-teachers-widget .controls-section {
    padding: 20px 0 50px !important;
}

#sjacademy-teachers-widget .filter-group {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
    gap: 15px !important;
}

#sjacademy-teachers-widget .filter-btn {
    background: transparent !important;
    border: 2px solid var(--brown) !important;
    border-radius: 50px !important;
    padding: 10px 24px !important;
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    color: var(--brown) !important;
    text-transform: uppercase !important;
    transition: var(--transition) !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .filter-btn:hover {
    background: var(--brown) !important;
    color: var(--white) !important;
    transform: translateY(-2px) !important;
}

#sjacademy-teachers-widget .filter-btn.active {
    background: var(--orange) !important;
    border-color: var(--orange) !important;
    color: var(--white) !important;
    box-shadow: 0 4px 10px rgba(254, 97, 0, 0.3) !important;
}

/* Bento Grid */
#sjacademy-teachers-widget .grid-section {
    padding: 0 0 80px !important;
}

#sjacademy-teachers-widget .bento-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)) !important;
    grid-auto-rows: minmax(350px, auto) !important;
    gap: 25px !important;
}

/* Teacher Card (Bento Item) */
#sjacademy-teachers-widget .teacher-card {
    background: var(--white) !important;
    border-radius: 16px !important;
    border: 2px solid rgba(0,0,0,0.05) !important;
    padding: 30px !important;
    display: flex !important;
    flex-direction: column !important;
    position: relative !important;
    overflow: hidden !important;
    transition: var(--transition) !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.02) !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .teacher-card.featured {
    grid-column: span 2 !important;
    background: var(--white) !important;
    border: 2px solid var(--brown) !important;
}

#sjacademy-teachers-widget .teacher-card:hover {
    transform: translateY(-10px) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08) !important;
    border-color: var(--orange) !important;
}

#sjacademy-teachers-widget .card-top {
    display: flex !important;
    align-items: center !important;
    gap: 20px !important;
    margin-bottom: 20px !important;
}

#sjacademy-teachers-widget .teacher-card.featured .card-top {
    flex-direction: row !important;
}

#sjacademy-teachers-widget .teacher-img-wrap {
    width: 100px !important;
    height: 100px !important;
    border-radius: 50% !important;
    padding: 4px !important;
    border: 2px solid var(--primary-yellow) !important;
    transition: var(--transition) !important;
    flex-shrink: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .teacher-card.featured .teacher-img-wrap {
    width: 140px !important;
    height: 140px !important;
}

#sjacademy-teachers-widget .teacher-card:hover .teacher-img-wrap {
    transform: scale(1.05) rotate(5deg) !important;
    border-color: var(--orange) !important;
}

#sjacademy-teachers-widget .teacher-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    border-radius: 50% !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
    border: none !important;
}

#sjacademy-teachers-widget .card-header-info {
    flex-grow: 1 !important;
}

#sjacademy-teachers-widget .teacher-name {
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    color: var(--black) !important;
    margin-bottom: 8px !important;
    line-height: 1.2 !important;
}

#sjacademy-teachers-widget .teacher-card.featured .teacher-name {
    font-size: 2rem !important;
}

#sjacademy-teachers-widget .teacher-tags {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    margin: 0 !important;
    padding: 0 !important;
}

#sjacademy-teachers-widget .tag {
    background: var(--light-bg) !important;
    color: var(--dark-grey) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    padding: 5px 12px !important;
    border-radius: 4px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    border: 1px solid #ddd !important;
    transition: var(--transition) !important;
    margin: 0 !important;
    display: inline-block !important;
    line-height: 1.5 !important;
}

#sjacademy-teachers-widget .teacher-card.featured .tag.highlight-tag {
    background: var(--primary-yellow) !important;
    border-color: var(--brown) !important;
    color: var(--black) !important;
}

#sjacademy-teachers-widget .teacher-card:hover .tag {
    border-color: var(--orange) !important;
}

#sjacademy-teachers-widget .teacher-bio-snippet {
    font-size: 15px !important;
    color: var(--grey) !important;
    line-height: 1.6 !important;
    margin-bottom: 25px !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 4 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    flex-grow: 1 !important;
}

#sjacademy-teachers-widget .teacher-card.featured .teacher-bio-snippet {
    -webkit-line-clamp: 3 !important;
    font-size: 16px !important;
}

#sjacademy-teachers-widget .card-footer {
    margin-top: auto !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    border-top: 1px solid #f0f0f0 !important;
    padding-top: 15px !important;
    background: transparent !important;
}

#sjacademy-teachers-widget .social-links {
    display: flex !important;
    gap: 10px !important;
    background: transparent !important;
    align-items: center !important;
}

#sjacademy-teachers-widget .social-icon {
    width: 35px !important;
    height: 35px !important;
    min-width: 35px !important;
    min-height: 35px !important;
    border-radius: 50% !important;
    background: var(--light-bg) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: var(--brown) !important;
    text-decoration: none !important;
    transition: var(--transition) !important;
    border: 1px solid #eee !important;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 1 !important;
}

#sjacademy-teachers-widget .social-icon i {
    font-size: 16px !important;
    line-height: 1 !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
}

#sjacademy-teachers-widget .social-icon:hover {
    background: var(--orange) !important;
    color: var(--white) !important;
    border-color: var(--orange) !important;
    transform: translateY(-3px) !important;
}

#sjacademy-teachers-widget .read-more-btn {
    background: var(--black) !important;
    color: var(--white) !important;
    border: none !important;
    padding: 10px 24px !important;
    border-radius: 50px !important;
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
    font-size: 12px !important;
    text-transform: uppercase !important;
    line-height: 1.5 !important;
    transition: var(--transition) !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    height: auto !important;
    min-height: 38px !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .read-more-btn:hover {
    background: var(--orange) !important;
    color: var(--white) !important;
    transform: translateX(5px) !important;
}

/* Modal Overlay (Glassmorphism) */
#sjacademy-teachers-widget .modal-overlay {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: rgba(0, 0, 0, 0.4) !important;
    backdrop-filter: blur(15px) !important;
    z-index: 10000 !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    opacity: 0 !important;
    visibility: hidden !important;
    transition: var(--transition) !important;
    padding: 20px !important;
}

#sjacademy-teachers-widget .modal-overlay.active {
    opacity: 1 !important;
    visibility: visible !important;
}

#sjacademy-teachers-widget .modal-container {
    background: var(--white) !important;
    width: 100% !important;
    max-width: 800px !important;
    max-height: 90vh !important;
    border-top: 6px solid var(--orange) !important;
    border-radius: 16px !important;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2) !important;
    position: relative !important;
    transform: translateY(40px) scale(0.95) !important;
    transition: var(--transition) !important;
    overflow-y: auto !important;
    margin: 0 !important;
    padding: 0 !important;
}

#sjacademy-teachers-widget .modal-overlay.active .modal-container {
    transform: translateY(0) scale(1) !important;
}

#sjacademy-teachers-widget .close-modal {
    position: absolute !important;
    top: 20px !important;
    right: 20px !important;
    background: var(--light-bg) !important;
    border: 2px solid var(--black) !important;
    width: 40px !important;
    height: 40px !important;
    border-radius: 50% !important;
    font-size: 18px !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    transition: var(--transition) !important;
    z-index: 10 !important;
    color: var(--black) !important;
    padding: 0 !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .close-modal:hover {
    background: var(--orange) !important;
    color: var(--white) !important;
    border-color: var(--orange) !important;
    transform: rotate(90deg) !important;
}

#sjacademy-teachers-widget .modal-content {
    padding: 50px !important;
}

#sjacademy-teachers-widget .modal-header {
    display: flex !important;
    gap: 30px !important;
    align-items: center !important;
    margin-bottom: 30px !important;
}

#sjacademy-teachers-widget .modal-img {
    width: 160px !important;
    height: 160px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    border: 4px solid var(--primary-yellow) !important;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1) !important;
    margin: 0 !important;
    padding: 0 !important;
}

#sjacademy-teachers-widget .modal-header-info h2 {
    font-size: 2.5rem !important;
    font-weight: 800 !important;
    margin-bottom: 10px !important;
    line-height: 1.1 !important;
    color: var(--black) !important;
}

#sjacademy-teachers-widget .modal-socials {
    display: flex !important;
    gap: 15px !important;
    margin-top: 15px !important;
}

#sjacademy-teachers-widget .modal-social-btn {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    padding: 8px 16px !important;
    background: var(--light-bg) !important;
    border: 1px solid #ddd !important;
    border-radius: 50px !important;
    color: var(--brown) !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    transition: var(--transition) !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .modal-social-btn:hover {
    background: var(--black) !important;
    color: var(--primary-yellow) !important;
    border-color: var(--black) !important;
}

#sjacademy-teachers-widget .modal-bio {
    font-size: 17px !important;
    color: #333 !important;
    line-height: 1.8 !important;
    margin-bottom: 40px !important;
    padding: 30px 0 !important;
    border-top: 1px solid #eee !important;
    border-bottom: 1px solid #eee !important;
}

/* KEY VALUE TABLE */
#sjacademy-teachers-widget table,
#sjacademy-teachers-widget table tbody,
#sjacademy-teachers-widget table tr,
#sjacademy-teachers-widget table th,
#sjacademy-teachers-widget table td {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
    margin: 0 !important;
    padding: 0 !important;
}

#sjacademy-teachers-widget .kv-table {
    width: 100% !important;
    border-collapse: collapse !important;
    table-layout: auto !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .kv-table tr.kv-row {
    border-bottom: 1px solid #eee !important;
    background: transparent !important;
}

#sjacademy-teachers-widget .kv-table tr.kv-row:last-child {
    border-bottom: none !important;
}

#sjacademy-teachers-widget .kv-table td.kv-label {
    padding: 15px 0 !important;
    font-weight: 800 !important;
    font-size: 13px !important;
    text-transform: uppercase !important;
    color: var(--brown) !important;
    width: 30% !important;
    vertical-align: top !important;
    letter-spacing: 1px !important;
    text-align: left !important;
    border: none !important;
}

#sjacademy-teachers-widget .kv-table td.kv-value {
    padding: 15px 0 !important;
    font-size: 15px !important;
    color: #444 !important;
    font-weight: 500 !important;
    vertical-align: top !important;
    text-align: left !important;
    border: none !important;
}

/* CTA & Footer */
#sjacademy-teachers-widget .cta-section {
    padding: 100px 0 !important;
    background: var(--light-yellow) !important;
    border-top: 6px solid var(--primary-yellow) !important;
    text-align: center !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .cta-container h2 {
    font-size: clamp(2rem, 5vw, 3rem) !important;
    font-weight: 900 !important;
    margin-bottom: 20px !important;
    color: var(--black) !important;
}

#sjacademy-teachers-widget .cta-container p {
    color: var(--black) !important;
    font-size: 16px !important;
    margin-bottom: 0 !important;
}

#sjacademy-teachers-widget .btn-primary {
    background: var(--orange) !important;
    color: var(--white) !important;
    border: 2px solid var(--orange) !important;
    border-radius: 50px !important;
    padding: 16px 40px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 10px rgba(254, 97, 0, 0.3) !important;
    text-decoration: none !important;
    display: inline-block !important;
    line-height: 1.5 !important;
    transition: var(--transition) !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .btn-primary:hover {
    background: var(--black) !important;
    border-color: var(--black) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2) !important;
}

#sjacademy-teachers-widget .btn-whatsapp {
    background: #25D366 !important;
    color: var(--white) !important;
    border: 2px solid #25D366 !important;
    border-radius: 50px !important;
    padding: 16px 35px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3) !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
    line-height: 1.5 !important;
    transition: var(--transition) !important;
    font-family: var(--font-main) !important;
    margin: 0 !important;
}

#sjacademy-teachers-widget .btn-whatsapp:hover {
    background: #1ebc59 !important;
    border-color: #1ebc59 !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 20px rgba(37, 211, 102, 0.4) !important;
}

#sjacademy-teachers-widget .cta-buttons {
    display: flex !important;
    justify-content: center !important;
    gap: 20px !important;
    margin-top: 30px !important;
}

/* Animation utilities */
#sjacademy-teachers-widget .reveal-up {
    opacity: 0;
    transform: translateY(40px);
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeInUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive */
@media (max-width: 992px) {
    #sjacademy-teachers-widget .bento-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    #sjacademy-teachers-widget .teacher-card.featured {
        grid-column: span 2 !important;
    }
}

@media (max-width: 768px) {
    #sjacademy-teachers-widget * { cursor: auto !important; }
    #sjacademy-teachers-widget .custom-cursor { display: none !important; }
    
    #sjacademy-teachers-widget .bento-grid {
        grid-template-columns: 1fr !important;
    }
    #sjacademy-teachers-widget .teacher-card.featured {
        grid-column: span 1 !important;
    }
    #sjacademy-teachers-widget .teacher-card.featured .card-top, 
    #sjacademy-teachers-widget .modal-header {
        flex-direction: column !important;
        text-align: center !important;
    }
    #sjacademy-teachers-widget .modal-socials {
        justify-content: center !important;
    }
    #sjacademy-teachers-widget .cta-buttons {
        flex-direction: column !important;
    }
    #sjacademy-teachers-widget .kv-label, 
    #sjacademy-teachers-widget .kv-value {
        display: block !important;
        width: 100% !important;
        padding: 10px 0 !important;
    }
    #sjacademy-teachers-widget .kv-label {
        padding-bottom: 0 !important;
    }
    
    #sjacademy-teachers-widget .modal-content {
        padding: 30px !important;
    }
}
</style>

<div id="sjacademy-teachers-widget" class="sjacademy-teachers">
    <!-- Custom Cursor -->
    <div class="custom-cursor" id="customCursor"><i class="fa-solid fa-pencil"></i></div>

    <!-- Modern Typography Hero Section -->
    <section class="hero-section">
        <div class="container hero-container">
            <div class="mode-pill-wrapper reveal-up">
                <div class="mode-pill">👨‍🏫 EXPERT FACULTY</div>
            </div>
            <h1 class="page-title reveal-up" style="animation-delay: 0.1s;">
                Meet the <span class="highlight-text">teachers</span><br>
                behind SJ Academy
            </h1>
            <p class="subtitle reveal-up" style="animation-delay: 0.2s;">
                Our world-class educators bring decades of experience, having produced hundreds of regional and world distinctions. Join a community that transforms potential into excellence.
            </p>
        </div>
    </section>

    <!-- Filters Section -->
    <section class="controls-section" id="faculty">
        <div class="container">
            <div class="filter-group">
                <button class="filter-btn active hover-target" data-filter="all">All Teachers</button>
                <button class="filter-btn hover-target" data-filter="o-level">O-Level</button>
                <button class="filter-btn hover-target" data-filter="a-level">A-Level</button>
                <button class="filter-btn hover-target" data-filter="business">Business</button>
                <button class="filter-btn hover-target" data-filter="sciences">Sciences</button>
                <button class="filter-btn hover-target" data-filter="humanities">Humanities</button>
            </div>
        </div>
    </section>

    <!-- Bento Grid Section -->
    <section class="grid-section">
        <div class="container">
            <div class="bento-grid" id="teachersGrid"></div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container cta-container">
            <h2 class="reveal-up">May/June 2027 Batches</h2>
            <p class="reveal-up" style="animation-delay: 0.1s;">Registrations are now open. Secure your spot today and start your journey with SJ Academy.</p>
            <div class="cta-buttons reveal-up" style="animation-delay: 0.2s;">
                <a href="https://www.sjacademy.pk/#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="btn-primary hover-target">Register Now</a>
                <a href="https://wa.me/923362144454" class="btn-whatsapp hover-target" target="_blank"><i class="fa-brands fa-whatsapp"></i> WhatsApp Us</a>
            </div>
        </div>
    </section>

    <!-- Teacher Detail Modal -->
    <div class="modal-overlay" id="teacherModal">
        <div class="modal-container">
            <button class="close-modal hover-target" id="closeModal"><i class="fa-solid fa-xmark"></i></button>
            <div class="modal-content" id="modalContent"></div>
        </div>
    </div>
</div>

<script>
const teachers = [
    {
        id: 100,
        name: "Sir Salman Junaid",
        isCoFounder: true,
        subjects: ["Math", "Physics"],
        level: ["O-Level", "A-Level"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Learn A Level Math with Sir Salman Junaid, an NED University engineer and former Karachi Grammar School (KGS) faculty member who makes abstract concepts visual, exam techniques precise, and past paper patterns easier to master. He is also the Co-founder of SJ Academy, bringing 12+ years of teaching excellence to the platform.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/06/salman-1-modified.png",
        experience: "12+ Years",
        affiliations: ["SJ Academy (Co-founder)", "Ex-KGS Faculty", "NED University"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://www.youtube.com/@sjacademypk",
            instagram: "https://instagram.com/#"
        }
    },
    {
        id: 1,
        name: "Sir Sunyyan Junaid",
        isCoFounder: false,
        subjects: ["Business"],
        level: ["A-Level"],
        category: ["business", "a-level"],
        bio: "Sunyyan Junaid is a passionate educator with over 8 years of experience in business, marketing, and leadership. He brings real-world insights into the classroom. His teaching approach focuses on simplifying complex concepts, developing critical thinking, and helping students apply business theory to real-life scenarios.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/07/296167730_10159330125240939_9121453372746153911_n-min.jpg",
        experience: "8+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://www.linkedin.com/in/sunyyan-junaid/",
            twitter: "https://twitter.com/#",
            youtube: "https://www.youtube.com/@sjacademypk"
        }
    },
    {
        id: 2,
        name: "Sir Khawar Shuaib",
        subjects: ["Economics"],
        level: ["A-Level", "IB"],
        category: ["business", "a-level"],
        bio: "KHAWAR SHUAIB is an experienced economics educator and entrepreneur with a strong background in teaching A-Level and IB Economics. He started his teaching career in 2014 and has since worked with students across Pakistan, the UAE, and the UK. His approach combines conceptual clarity with practical application.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2026/06/Khawar-2.jpeg",
        experience: "Since 2014",
        affiliations: ["Pakistan", "UAE", "UK"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 4,
        name: "Sir Abdullah Zaman",
        subjects: ["Chemistry"],
        level: ["O-Level", "A-Level"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Sir Abdullah Zaman is a dedicated and accomplished Chemistry educator with over five years of professional teaching experience in O Level and A Level. His teaching philosophy emphasizes conceptual understanding, analytical thinking, and real-world application of chemical principles.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/12/Zaman-chemistry.jpeg",
        experience: "5+ Years",
        affiliations: ["Lions Schooling System", "Iqra University", "Progressive Public School", "SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#"
        }
    },
    {
        id: 5,
        name: "Sir Umair",
        subjects: ["Biology"],
        level: ["O-Level", "A-Level", "IB"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Muhammad Umair is a dedicated teacher for Biology with extensive experience in teaching multiple curricula. He began teaching at Beaconhouse as an IB Biology teacher and has taught IB and Cambridge A levels for the past 8 years. He also designed the new federal Biology curriculum for inter and matric.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Umair-Pic-1.jpg",
        experience: "8+ Years",
        affiliations: ["Beaconhouse", "SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 6,
        name: "Sir Riza Walji",
        subjects: ["Computer Science"],
        level: ["O-Level", "A-Level", "IGCSE"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Mohammed Riza Walji is a seasoned Computer Science educator with over nine years of teaching experience. He has developed a strong reputation for his subject expertise and engaging teaching style with a commitment to academic excellence and student success.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Sir-Riza.webp",
        experience: "9+ Years",
        affiliations: ["Jaffar Public School", "Beaconhouse", "Links School", "Bay View Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#"
        }
    },
    {
        id: 7,
        name: "Sir Shaibaz Ali",
        subjects: ["Accounts"],
        level: ["O-Level", "A-Level"],
        category: ["business", "o-level", "a-level"],
        bio: "Shahbaz Ali (CAT - ACCA) is an expert Accounting teacher who has been teaching since 2011. He brings extensive experience from various prestigious schools, ensuring top-tier accounting education for his students.",
        image: "",
        experience: "Since 2011",
        affiliations: ["BSS (PECHS)", "LGS (DHA Campus)", "The Froebel's School", "Karachi High School"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 8,
        name: "Miss Asmat Zafar",
        subjects: ["Urdu"],
        level: ["O-Level", "A-Level"],
        category: ["humanities", "o-level", "a-level"],
        bio: "Miss Asmat Zafar is an experienced O/A Level Urdu teacher. She has served as Head of Urdu Department at Education Bay and worked as a Senior Author with the University of Cambridge. She is known for her clear teaching style and strong command of Urdu literature.",
        image: "https://ui-avatars.com/api/?name=Asmat+Zafar&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Experienced",
        affiliations: ["Education Bay", "University of Cambridge", "St. Michael’s Convent"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 9,
        name: "Sir Kashaan Ali",
        subjects: ["Islamiat", "Pak Studies"],
        level: ["O-Level", "IGCSE"],
        category: ["humanities", "o-level"],
        bio: "Kashan Ali is an enthusiastic individual who has taught generations through his teaching career of 22 years. He began his career in 2003 and is associated with prestigious institutes.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/07/Kashan-Ali.jpeg",
        experience: "22 Years",
        affiliations: ["Bahria Foundation", "Beaconhouse DHA", "The City School", "LINKS", "The Indus Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 10,
        name: "Sir Saifullah",
        subjects: ["Accounts"],
        level: ["O-Level", "A-Level"],
        category: ["business", "o-level", "a-level"],
        bio: "Saifullah is an experienced Accounting educator specializing in O Level and A Level Accounting. He is a CAIE-certified Accounting teacher whose teaching approach emphasizes conceptual clarity, real-world application, and exam-focused preparation.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2026/07/Saifullah-Accounts.jpeg",
        experience: "5+ Years",
        affiliations: ["The City School", "The Next School", "The Academy", "Falconhouse"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 11,
        name: "Sir Aaliyan",
        subjects: ["Business", "Economics"],
        level: ["O-Level"],
        category: ["business", "o-level"],
        bio: "Syed Alyan Ali is a spirited instructor having over 7 years of experience in coaching O and A Level students. His lectures instill problem-solving techniques that help students apply theoretical concepts to practical situations.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2026/06/Alyaan.jpeg",
        experience: "7+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 12,
        name: "Miss Muzna Zaidi",
        subjects: ["Psychology"],
        level: ["A-Level"],
        category: ["humanities", "a-level"],
        bio: "Miss Muzna Zaidi is an enthusiastic and insightful A-Level Psychology educator who specializes in simplifying complex psychological concepts. With a strong command of the Cambridge Psychology syllabus, she focuses on building critical thinking and analytical writing skills.",
        image: "https://ui-avatars.com/api/?name=Muzna+Zaidi&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Currently pursuing degree",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            instagram: "https://instagram.com/#"
        }
    },
    {
        id: 13,
        name: "Miss Tayyaba Yaseen",
        subjects: ["Sociology", "English"],
        level: ["O-Level", "A-Level", "IGCSE"],
        category: ["humanities", "o-level", "a-level"],
        bio: "Tayyaba Yaseen is a passionate and student-focused teacher with over 3 years of teaching experience. With a background in psychology, she designs lessons that are engaging, practical, and easy to grasp, encouraging curiosity and critical thinking.",
        image: "https://ui-avatars.com/api/?name=Tayyaba+Yaseen&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "3+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 3,
        name: "Sir Basharat",
        subjects: ["Chemistry", "Physics"],
        level: ["O-Level"],
        category: ["sciences", "o-level"],
        bio: "Not Available detail. An experienced educator in Chemistry and Physics, dedicated to building strong foundational knowledge for O-Level students.",
        image: "https://ui-avatars.com/api/?name=Sir+Basharat&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Experienced",
        affiliations: ["SJ Academy"],
        socials: {}
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const customCursor = document.getElementById('customCursor');
    
    if (customCursor) {
        window.addEventListener('mousemove', (e) => {
            const posX = e.clientX;
            const posY = e.clientY;
            
            customCursor.style.left = `${posX}px`;
            customCursor.style.top = `${posY}px`;
        });
    }

    const grid = document.getElementById('teachersGrid');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const modalOverlay = document.getElementById('teacherModal');
    const modalContent = document.getElementById('modalContent');
    const closeModal = document.getElementById('closeModal');

    function renderTeachers(filter = 'all') {
        grid.innerHTML = '';
        
        const filtered = teachers.filter(t => filter === 'all' || t.category.includes(filter));
        
        filtered.forEach((teacher, index) => {
            const delay = index * 0.1;
            const allTags = [...teacher.subjects, ...teacher.level];
            const tagClass = teacher.isCoFounder ? 'tag highlight-tag' : 'tag';
            const tagsHTML = allTags.map(tag => `<span class="${tagClass}">${tag}</span>`).join('');
            
            let socialsHTML = '';
            if(teacher.socials) {
                if(teacher.socials.linkedin) socialsHTML += `<a href="${teacher.socials.linkedin}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>`;
                if(teacher.socials.twitter) socialsHTML += `<a href="${teacher.socials.twitter}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-twitter"></i></a>`;
                if(teacher.socials.instagram) socialsHTML += `<a href="${teacher.socials.instagram}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-instagram"></i></a>`;
                if(teacher.socials.youtube) socialsHTML += `<a href="${teacher.socials.youtube}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-youtube"></i></a>`;
            }

            const card = document.createElement('div');
            card.className = `teacher-card reveal-up ${teacher.isCoFounder ? 'featured' : ''}`;
            card.style.animationDelay = `${delay}s`;
            
            card.innerHTML = `
                <div class="card-top">
                    <div class="teacher-img-wrap">
                        <img src="${teacher.image}" alt="${teacher.name}" class="teacher-img">
                    </div>
                    <div class="card-header-info">
                        <h3 class="teacher-name">${teacher.name}</h3>
                        <div class="teacher-tags">
                            ${teacher.isCoFounder ? `<span class="tag highlight-tag" style="background:var(--orange) !important;color:#fff !important;border:none !important;">Co-founder</span>` : ''}
                            ${tagsHTML}
                        </div>
                    </div>
                </div>
                <p class="teacher-bio-snippet">${teacher.bio}</p>
                <div class="card-footer">
                    <div class="social-links">
                        ${socialsHTML}
                    </div>
                    <button class="read-more-btn hover-target" data-id="${teacher.id}">
                        Full Profile
                    </button>
                </div>
            `;
            
            grid.appendChild(card);
        });

        document.querySelectorAll('.read-more-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.currentTarget.getAttribute('data-id'));
                openModal(id);
            });
        });
    }

    function openModal(id) {
        const teacher = teachers.find(t => t.id === id);
        if (!teacher) return;
        
        const allTags = [...teacher.subjects, ...teacher.level];
        const tagsHTML = allTags.map(tag => `<span class="tag" style="background:#eee !important;border-color:#ccc !important;">${tag}</span>`).join('');
        
        let socialsHTML = '';
        if(teacher.socials) {
            if(teacher.socials.linkedin) socialsHTML += `<a href="${teacher.socials.linkedin}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>`;
            if(teacher.socials.twitter) socialsHTML += `<a href="${teacher.socials.twitter}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-twitter"></i> Twitter</a>`;
            if(teacher.socials.instagram) socialsHTML += `<a href="${teacher.socials.instagram}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-instagram"></i> Instagram</a>`;
            if(teacher.socials.youtube) socialsHTML += `<a href="${teacher.socials.youtube}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-youtube"></i> YouTube</a>`;
        }
        
        modalContent.innerHTML = `
            <div class="modal-header">
                <img src="${teacher.image}" alt="${teacher.name}" class="modal-img">
                <div class="modal-header-info">
                    <h2>${teacher.name}</h2>
                    <div class="teacher-tags" style="margin-bottom: 10px !important;">
                        ${teacher.isCoFounder ? `<span class="tag highlight-tag" style="background:var(--orange) !important;color:#fff !important;border:none !important;">Co-founder</span>` : ''}
                        ${tagsHTML}
                    </div>
                    <div class="modal-socials">
                        ${socialsHTML}
                    </div>
                </div>
            </div>
            <div class="modal-bio">${teacher.bio}</div>
            
            <table class="kv-table">
                <tr class="kv-row">
                    <td class="kv-label">EXPERIENCE</td>
                    <td class="kv-value">${teacher.experience}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">SUBJECTS</td>
                    <td class="kv-value">${teacher.subjects.join(', ')}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">LEVELS</td>
                    <td class="kv-value">${teacher.level.join(', ')}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">AFFILIATIONS</td>
                    <td class="kv-value">${teacher.affiliations.join(', ')}</td>
                </tr>
            </table>
        `;
        
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function close() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    closeModal.addEventListener('click', close);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) close();
    });
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
            close();
        }
    });

    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => b.classList.remove('active'));
            e.currentTarget.classList.add('active');
            const filter = e.currentTarget.getAttribute('data-filter');
            renderTeachers(filter);
        });
    });

    renderTeachers();
});
</script>
```
