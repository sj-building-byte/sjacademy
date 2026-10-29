# 03 - CAIE Past Papers Landing Page

> **Type:** Resource Hub / SEO Landing Page & Cross-Promotional Funnel  
> **Brand / Project:** SJ Academy (`sjacademy.pk/past-papers/`)  
> **Target Audience:** CAIE O Level and A Level students in Pakistan and internationally searching for free downloadable past papers with topical & year-wise filtering.

---

## 1. Overview & Strategic Goals

The **Past Papers Landing Page** serves as an organic search acquisition hub for students looking for free CAIE exam papers.

### Key Goals:
1. **SEO Traffic Ingestion:** Captures high-volume search queries like *"A Level past papers"*, *"O Level physics past papers"*, *"CIE past papers download"*.
2. **Frictionless Navigation:** Dual level-selector cards (A Level and O Level) with instant visual subject pills.
3. **Cross-Promotional Conversion:** Features an interactive **"Master Chemistry with Exam Tools" (Periodic Table)** promo fold with interactive element cards directing traffic deeper into SJ Academy's learning products.

---

## 2. Design System & Tokens

### Typography & Fonts
- **Font Family:** `'Poppins', sans-serif` (Weights: `300`, `400`, `600`, `700`, `800`)

### Color System

| Token | Hex Value | Purpose |
| :--- | :--- | :--- |
| `--primary-yellow` | `#FCE004` | Brand highlights, icon backgrounds, live badges |
| `--brown` | `#453516` | Card top borders, icon borders, secondary CTA button |
| `--orange` | `#FE6100` | Primary action buttons, hover states, accent text |
| `--orange-dark` | `#E55800` | Button hover states and active indicators |
| `--black` | `#000000` | Primary text headings |
| `--dark-grey` | `#222222` | Secondary text |
| `--grey` | `#555555` | Subtitles, meta text, disclaimers |
| `--light-bg` | `#FAFAFA` | Subject pill backgrounds, footer |
| `--light-yellow` | `#FFF9CC` | Promo fold full-width section background |
| `--border-light` | `#E5E5E5` | Card borders and divider lines |

### Interactive States & Shadows
- **Card Shadow:** `0 10px 25px rgba(0,0,0,0.05)`
- **Card Hover:** `transform: translateY(-6px)`, `0 20px 40px rgba(0,0,0,0.1)`, top border and icon switch to `--orange`.
- **Button Shadow:** `0 4px 10px rgba(254,97,0,0.3)`
- **Promo Box Retro Shadow:** `box-shadow: 10px 10px 0 var(--brown)`

---

## 3. Layout & Section Architecture

```
Page Structure
├── Hero Section (H1 + Yellow highlight accent + Subtitle)
│
├── Cards Section (.cards-grid)
│   ├── A Level Card (Icon, Title, Range 2019-2025, Badge, Subject Pills, CTA Button)
│   └── O Level Card (Icon, Title, Range 2019-2025, Badge, Subject Pills, CTA Button)
│
├── Info / Contact Fold (Educational disclaimer + Direct Email & WhatsApp links)
│
├── Promo Fold (.promo-fold with .promo-box)
│   ├── Promo Copy & CTA ("Explore Periodic Table")
│   └── Promo Visual (8-element interactive Periodic Table grid: H, He, Li, O, C, Fe, Au, Ne)
│
└── Footer (Copyright notice)
```

---

## 4. Subject Categorization & Links

### 1. A Level Past Papers (`/a-level-past-papers/`)
- **Years Covered:** 2019 to 2025
- **Featured Subjects:** Business, Maths, Physics, Chemistry, Biology, Economics

### 2. O Level Past Papers (`/o-level-past-papers/`)
- **Years Covered:** 2019 to 2025
- **Featured Subjects:** Pak Studies, Math D, Physics, Chemistry, Economics, Urdu

### 3. Interactive Periodic Table Tool (`/periodic-table-of-elements/`)
- **Interactive Element Tiles:**
  - $H$ (Hydrogen - #1) - Yellow brand style
  - $He$ (Helium - #2) - Light clean style
  - $Li$ (Lithium - #3) - Orange accent style
  - $O$ (Oxygen - #8) - Brown accent style
  - $C$ (Carbon - #6) - Brown accent style
  - $Fe$ (Iron - #26) - Yellow brand style
  - $Au$ (Gold - #79) - Orange accent style
  - $Ne$ (Neon - #10) - Light clean style

---

## 5. Copy & Marketing Content

### Hero
- **H1:** `Download CAIE Past Papers` (with `CAIE Past Papers` highlighted)
- **Subtitle:** *"Free A Level and O Level past papers for all subjects. Filter by subject, year, session, and download instantly."*

### Cards Copy
- **A Level Card:** *"CIE Cambridge A Level — 2019 to 2025"* | Badge: `Available Now` | CTA: `Browse Papers`
- **O Level Card:** *"CIE Cambridge O Level — 2019 to 2025"* | Badge: `Available Now` | CTA: `Browse Papers`

### Educational Disclaimer & Contact
- *"Past papers for educational purposes only. All content belongs to their respective exam boards. Built with care by SJ Academy."*
- Email: `contact@sjacademy.pk` | WhatsApp: `+92 336 2144454`

### Promo Fold Hook
- **H2:** `Master Chemistry with Exam Tools`
- **Body:** *"Don't just solve papers. Understand the fundamental science. Our Interactive Periodic Table is built specifically to help CAIE students master element properties and trends for their exams."*
- **CTA:** `Explore Periodic Table`

---

## 6. Complete Source Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Past Papers — Download A Level & O Level Papers Free | SJ Academy</title>
  <meta name="description" content="Download free A Level and O Level past papers for Business, Mathematics, Economics, Physics, Chemistry, Biology and more. Filter by subject, year, session, and paper type.">
  <meta name="keywords" content="past papers, A Level past papers, O Level past papers, CIE past papers, Cambridge past papers, A Level Business past papers, A Level Maths past papers, A Level Physics past papers, A Level Chemistry past papers, A Level Biology past papers, A Level Economics past papers, free past papers download">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.sjacademy.pk/past-papers/">
  <meta property="og:title" content="Past Papers — Free Download | SJ Academy">
  <meta property="og:description" content="Download free A Level and O Level past papers for all subjects. Filter by subject, year, session, and paper type.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.sjacademy.pk/past-papers/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-yellow: #FCE004;
      --brown: #453516;
      --orange: #FE6100;
      --orange-dark: #e55800;
      --black: #000000;
      --white: #FFFFFF;
      --grey: #555555;
      --dark-grey: #222222;
      --light-bg: #FAFAFA;
      --light-yellow: #FFF9CC;
      --border-light: #e5e5e5;
      --shadow-card: 0 10px 25px rgba(0,0,0,0.05);
      --shadow-card-hover: 0 20px 40px rgba(0,0,0,0.1);
      --shadow-button: 0 4px 10px rgba(254,97,0,0.3);
      --shadow-button-hover: 0 10px 20px rgba(254,97,0,0.4);
      --transition: cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Poppins', sans-serif;
      background: var(--white);
      color: var(--black);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

    /* ===== HERO ===== */
    .hero {
      padding: 50px 0 24px;
      text-align: center;
    }

    .hero h1 {
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.2;
      color: var(--black);
      margin-bottom: 10px;
      animation: fadeInDown 0.6s ease forwards;
    }

    .hero h1 .highlight {
      background: linear-gradient(120deg, var(--primary-yellow) 0%, var(--primary-yellow) 100%);
      background-repeat: no-repeat;
      background-size: 100% 35%;
      background-position: 0 85%;
      display: inline;
      padding: 0 3px;
    }

    .hero .subtitle {
      font-size: 0.95rem;
      font-weight: 400;
      color: var(--grey);
      max-width: 500px;
      margin: 0 auto;
      animation: fadeInDown 0.6s ease 0.15s forwards;
      opacity: 0;
    }

    @keyframes fadeInDown {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ===== CARDS ===== */
    .cards-section {
      padding: 16px 0 30px;
    }

    .cards-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 1000px;
      margin: 0 auto;
    }

    .level-card {
      background: var(--white);
      border: 1.5px solid var(--border-light);
      border-top: 6px solid var(--brown);
      border-radius: 12px;
      box-shadow: var(--shadow-card);
      padding: 24px;
      transition: all 0.4s var(--transition);
      animation: fadeUp 0.6s ease forwards;
      opacity: 0;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      gap: 16px;
      text-decoration: none;
      color: inherit;
    }

    .level-card:nth-child(1) { animation-delay: 0.1s; }
    .level-card:nth-child(2) { animation-delay: 0.25s; }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(24px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .level-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-card-hover);
      border-top-color: var(--orange);
      border-color: var(--orange);
    }

    .card-top {
      display: flex;
      align-items: flex-start;
      gap: 16px;
    }

    .card-icon {
      width: 48px;
      height: 48px;
      background: var(--primary-yellow);
      border: 2px solid var(--brown);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 3px 3px 0 rgba(0,0,0,0.1);
      flex-shrink: 0;
      transition: all 0.4s var(--transition);
    }

    .level-card:hover .card-icon {
      background: var(--orange);
      border-color: var(--orange);
      transform: rotate(-5deg) scale(1.08);
    }

    .card-icon svg {
      width: 22px;
      height: 22px;
      fill: var(--brown);
      transition: fill 0.4s var(--transition);
    }

    .level-card:hover .card-icon svg {
      fill: var(--white);
    }

    .card-info {
      min-width: 0;
      flex: 1;
    }

    .card-info h2 {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--black);
      margin-bottom: 3px;
    }

    .card-info .card-subtitle {
      font-size: 12px;
      font-weight: 400;
      color: var(--grey);
      margin-bottom: 8px;
    }

    .badge-live {
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 4px 12px;
      border-radius: 40px;
      background: var(--primary-yellow);
      color: var(--black);
      border: 1.5px solid var(--brown);
    }

    .subject-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 10px;
    }

    .subject-pill {
      font-size: 10px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 40px;
      border: 1px solid var(--border-light);
      color: var(--dark-grey);
      background: var(--light-bg);
    }

    .card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border-radius: 5px;
      padding: 12px 24px;
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.3s var(--transition);
      width: 100%;
    }

    .cta-primary {
      background: var(--orange);
      color: var(--white);
      border: 2px solid var(--orange);
      box-shadow: var(--shadow-button);
    }

    .cta-primary:hover {
      background: var(--orange-dark);
      transform: translateY(-3px);
    }

    /* ===== INFO FOLD ===== */
    .info-fold {
      padding: 20px 0 40px;
      text-align: center;
    }

    .info-fold .meta-text {
      font-size: 12px;
      color: var(--grey);
      font-style: italic;
      margin-bottom: 10px;
      line-height: 1.6;
    }

    .info-fold .contact-text {
      font-size: 13px;
      font-weight: 700;
      color: var(--dark-grey);
    }

    .info-fold .contact-text a {
      color: var(--orange);
      text-decoration: none;
    }

    /* ===== ENHANCED PROMO FOLD (Periodic Table) ===== */
    .promo-fold {
      padding: 40px 0 80px;
      background: var(--light-yellow);
      overflow: hidden;
    }

    .promo-box {
      background: var(--white);
      border: 2.5px solid var(--brown);
      border-radius: 24px;
      padding: 30px;
      box-shadow: 10px 10px 0 var(--brown);
      display: flex;
      flex-direction: column;
      gap: 32px;
      align-items: center;
      position: relative;
    }

    .promo-content {
      text-align: center;
      z-index: 2;
    }

    .promo-content h2 {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--black);
      line-height: 1.2;
    }

    .promo-content p {
      font-size: 0.95rem;
      color: var(--grey);
      margin: 12px 0 24px;
      line-height: 1.6;
    }

    /* Decorative Mini Periodic Table */
    .promo-visual {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      padding: 15px;
      background: var(--light-bg);
      border-radius: 16px;
      border: 1.5px solid var(--border-light);
      width: fit-content;
    }

    .element-card {
      width: 50px;
      height: 50px;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border: 1.5px solid var(--brown);
      transition: all 0.3s;
      cursor: help;
    }

    .element-card .symbol { font-weight: 800; font-size: 14px; }
    .element-card .number { font-size: 8px; font-weight: 600; opacity: 0.7; }

    .el-yellow { background: var(--primary-yellow); }
    .el-orange { background: var(--orange); color: white; border-color: var(--orange-dark); }
    .el-brown { background: var(--brown); color: white; }
    .el-light { background: var(--white); }

    .element-card:hover {
      transform: scale(1.1) translateY(-4px);
      box-shadow: 4px 4px 0 rgba(0,0,0,0.1);
      z-index: 10;
    }

    .promo-cta {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--brown);
      color: var(--white) !important;
      padding: 16px 32px;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 800;
      text-transform: uppercase;
      font-size: 14px;
      transition: all 0.3s;
      box-shadow: 4px 4px 0 rgba(0,0,0,0.1);
    }

    .promo-cta:hover {
      background: var(--black);
      transform: translateY(-2px);
      box-shadow: 6px 6px 0 rgba(0,0,0,0.15);
    }

    footer { text-align: center; padding: 30px 20px; border-top: 1px solid var(--border-light); background: var(--light-bg); }
    footer .copyright { font-size: 12px; color: #666; }

    /* ===== DESKTOP ===== */
    @media (min-width: 768px) {
      .hero { padding: 80px 0 40px; }
      .hero h1 { font-size: 3.2rem; }
      .hero .subtitle { font-size: 1.1rem; }
      .cards-section { padding: 20px 0 50px; }

      .cards-grid {
        flex-direction: row;
        gap: 24px;
      }

      .level-card {
        flex: 1;
        padding: 32px;
      }

      .card-top {
        flex-direction: column;
        align-items: center;
        text-align: center;
      }

      .card-info h2 { font-size: 1.4rem; }
      .subject-pills { justify-content: center; }

      .promo-box {
        flex-direction: row;
        text-align: left;
        padding: 50px 60px;
        gap: 60px;
        justify-content: space-between;
      }

      .promo-content { text-align: left; flex: 1; }
      .promo-content h2 { font-size: 2.2rem; }
      .promo-visual { grid-template-columns: repeat(4, 65px); gap: 12px; padding: 20px; }
      .element-card { width: 65px; height: 65px; }
      .element-card .symbol { font-size: 18px; }
      .element-card .number { font-size: 10px; }
    }
  </style>
</head>
<body>

  <section class="hero">
    <div class="container">
      <h1>Download <span class="highlight"> CAIE Past Papers</span></h1>
      <p class="subtitle">Free A Level and O Level past papers for all subjects. Filter by subject, year, session, and download instantly.</p>
    </div>
  </header>

  <section class="cards-section">
    <div class="container">
      <div class="cards-grid">

        <!-- A LEVEL CARD -->
        <a href="https://www.sjacademy.pk/a-level-past-papers/" class="level-card">
          <div class="card-top">
            <div class="card-icon">
              <svg viewBox="0 0 24 24"><path d="M12 3L1 9L12 15L21 10.09V17H23V9M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/></svg>
            </div>
            <div class="card-info">
              <h2>A Level Past Papers</h2>
              <p class="card-subtitle">CIE Cambridge A Level — 2019 to 2025</p>
              <span class="card-badge badge-live">Available Now</span>
              <div class="subject-pills">
                <span class="subject-pill">Business</span>
                <span class="subject-pill">Maths</span>
                <span class="subject-pill">Physics</span>
                <span class="subject-pill">Chemistry</span>
                <span class="subject-pill">Biology</span>
                <span class="subject-pill">Economics</span>
              </div>
            </div>
          </div>
          <div class="card-cta cta-primary">
            <svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z" fill="white"/></svg>
            Browse Papers
          </div>
        </a>

        <!-- O LEVEL CARD -->
        <a href="https://www.sjacademy.pk/o-level-past-papers/" class="level-card">
          <div class="card-top">
            <div class="card-icon">
              <svg viewBox="0 0 24 24"><path d="M12 3L1 9L12 15L23 9M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/></svg>
            </div>
            <div class="card-info">
              <h2>O Level Past Papers</h2>
              <p class="card-subtitle">CIE Cambridge O Level — 2019 to 2025</p>
              <span class="card-badge badge-live">Available Now</span>
              <div class="subject-pills">
                <span class="subject-pill">Pak Studies</span>
                <span class="subject-pill">Math D</span>
                <span class="subject-pill">Physics</span>
                <span class="subject-pill">Chemistry</span>
                <span class="subject-pill">Economics</span>
                <span class="subject-pill">Urdu</span>
              </div>
            </div>
          </div>
          <div class="card-cta cta-primary">
            <svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z" fill="white"/></svg>
            Browse Papers
          </div>
        </a>

      </div>
    </div>
  </section>

  <!-- RELOCATED INFO SECTION -->
  <section class="info-fold">
    <div class="container">
      <p class="meta-text">Past papers for educational purposes only. All content belongs to their respective exam boards. Built with care by SJ Academy.</p>
      <div class="contact-text">
        Email: <a href="mailto:contact@sjacademy.pk">contact@sjacademy.pk</a> | WhatsApp: <a href="https://wa.me/923362144454">+92 336 2144454</a>
      </div>
    </div>
  </section>

  <!-- VISUAL EXAM TOOLS FOLD -->
  <section class="promo-fold">
    <div class="container">
      <div class="promo-box">
        <div class="promo-content">
          <h2>Master Chemistry with <span style="color: var(--orange);">Exam Tools</span></h2>
          <p>Don't just solve papers. Understand the fundamental science. Our Interactive Periodic Table is built specifically to help CAIE students master element properties and trends for their exams.</p>
          <a href="https://www.sjacademy.pk/periodic-table-of-elements/" class="promo-cta">
            Explore Periodic Table
            <svg viewBox="0 0 24 24" width="18" height="18" fill="white"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
          </a>
        </div>

        <!-- Decorative Interactive Element -->
        <div class="promo-visual">
          <div class="element-card el-yellow" title="Hydrogen"><span class="number">1</span><span class="symbol">H</span></div>
          <div class="element-card el-light" title="Helium"><span class="number">2</span><span class="symbol">He</span></div>
          <div class="element-card el-orange" title="Lithium"><span class="number">3</span><span class="symbol">Li</span></div>
          <div class="element-card el-brown" title="Oxygen"><span class="number">8</span><span class="symbol">O</span></div>
          <div class="element-card el-brown" title="Carbon"><span class="number">6</span><span class="symbol">C</span></div>
          <div class="element-card el-yellow" title="Iron"><span class="number">26</span><span class="symbol">Fe</span></div>
          <div class="element-card el-orange" title="Gold"><span class="number">79</span><span class="symbol">Au</span></div>
          <div class="element-card el-light" title="Neon"><span class="number">10</span><span class="symbol">Ne</span></div>
        </div>
      </div>
    </div>
  </section>

</body>
</html>
```
