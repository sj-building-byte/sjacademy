# 12 - Official Live Fee Structure & Tuition Page

> **Type:** Live Pricing Page / Fee Schedule / Payment Portal  
> **Brand / Project:** SJ Academy (`sjacademy.pk/fee-structure/`)  
> **Target Audience:** Prospective and enrolled O-Level and A-Level students and parents evaluating monthly tuition fees, fast-track crash course rates, lab practical costs, and official payment options.

---

## 1. Overview & Official Pricing Architecture

The **SJ Academy Fee Structure** page delivers 100% transparent pricing for CAIE O-Level and A-Level tuition in Karachi (DHA Phase 7) and Online.

### Official Fee Schedule:
1. **Regular Year-Round Batches (May/June Series):**
   - **O-Level / IGCSE Tuition:** `Rs. 8,500 / month per subject`
   - **A-Level (AS & A2) Tuition:** `Rs. 9,500 / month per subject`
   - **A-Level Science Lab Practicals (Physics, Chem, Bio):** `Rs. 25,500` (One-time payment per subject covering the entire practical exam preparation course and live lab apparatus).
2. **Fast-Track / Crash Course Batches (Oct/Nov Series):**
   - Accelerated, intensive exam-focused sprint with targeted past paper drilling.
3. **Discounts & Registration:**
   - **10% Upfront Discount:** Pay 3 months in advance to receive an instant **10% discount** on tuition.
   - **One-Time Registration Fee:** `Rs. 3,500` (one-time fee for new students; zero hidden charges).
   - **Study Materials:** All topical worksheets, formula sheets, and past papers are included with tuition at zero extra charge.
4. **Official Payment Methods:**
   - **Online Bank Transfer:** Standard Chartered, Faysal Bank (SJ Academy LLP), Meezan Bank.
   - **Physical Payment:** Front-desk office in DHA Phase 7, Karachi (Lane 5, Seher Commercial).
5. **Strict Refined Typography:** All headings, badges, and pricing cards maintain a strict **maximum font-weight of 400** with `Poppins`.

---

## 2. Design Tokens & Styling System

Scoped inside `#sjacademy-fee-portal`.

| Token | Hex / Value | Purpose |
| :--- | :--- | :--- |
| `--sja-yellow` | `#FCE004` | Highlight gradient, active toggle pills, value badges |
| `--sja-light-yellow` | `#FFF9CC` | Recommended tier card surface, highlight callout |
| `--sja-brown` | `#453516` | Card top accent borders, outline buttons, contrast labels |
| `--sja-orange` | `#FE6100` | Primary action CTA button, hover state `#E55800` |
| `--sja-whatsapp` | `#25D366` | Direct WhatsApp advisory button |
| `--sja-black` | `#000000` | Headings, titles, high-contrast borders |
| `--sja-dark-grey` | `#222222` | Body copy, FAQ answer text |
| `--sja-grey` | `#555555` | Metadata, subtitle text |
| `--sja-light-bg` | `#FAFAFA` | Pricing card backgrounds, calculator container |
| `--sja-white` | `#FFFFFF` | Card surfaces, input backgrounds |
| `--sja-border-light` | `#E5E5E5` | Card dividers, table borders |

---

## 3. Component Hierarchy

```
#sjacademy-fee-portal
├── .sja-header (Hero Section)
│   ├── .sja-badge ("⭐ TRANSPARENT ACADEMIC PRICING")
│   ├── H1 ("SJ Academy <span class="sja-highlight">Fee Structure</span>")
│   ├── Subtitle ("Excellence shouldn't come with surprises. Simple, transparent pricing...")
│   └── .sja-google-trust-banner ("⭐⭐⭐⭐⭐ Rated 5.0/5.0 by 220+ Students & Parents")
│
├── .sja-tab-nav (Toggle: Regular Batches vs Oct/Nov Fast-Track)
│
├── .sja-pricing-grid (Level Tier Cards)
│   ├── O-Level / IGCSE (Rs. 8,500/mo)
│   ├── A-Level AS/A2 [Featured] (Rs. 9,500/mo)
│   └── A-Level Lab Practicals (Rs. 25,500 one-time course fee)
│
├── .sja-discount-banner ("⭐ 10% Discount when paying for 3 months upfront")
│
├── .sja-calc-section (Interactive Subject & Upfront Discount Calculator)
│   ├── Level Selector (O-Level vs A-Level)
│   ├── Subject Counter (1 to 5 Subjects)
│   ├── Upfront 3-Month Toggle (10% Discount trigger)
│   └── Live Summary Box + Direct Registration CTA
│
├── .sja-faq-section (Official Pricing FAQs & Hidden Cost Transparency)
│
├── .sja-bank-section (Official Bank Transfer & Physical Payment Information)
│
└── .sja-cta-section ("Register For May/June 2027 Batches" + Elementor Popup & WhatsApp CTAs)
```

---

## 4. Complete Standalone Source Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SJ Academy Fee Structure - O & A Level Tuition Fees in Karachi</title>
  <meta name="description" content="Find complete, transparent fee structure for the best O Level and A Level coaching at SJ Academy in Karachi | Admission, Lab fees, registration">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    /* ==========================================================================
       OFFICIAL SJ ACADEMY FEE PORTAL (MAX FONT-WEIGHT: 400)
       ========================================================================== */
    #sjacademy-fee-portal {
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
      --sja-shadow-card: 0 10px 25px rgba(0, 0, 0, 0.05);
      --sja-shadow-card-hover: 0 20px 40px rgba(0, 0, 0, 0.1);
      --sja-shadow-button: 0 4px 10px rgba(254, 97, 0, 0.3);
      --sja-transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);

      font-family: 'Poppins', sans-serif;
      font-weight: 300;
      color: var(--sja-black);
      line-height: 1.6;
      background: var(--sja-white);
      width: 100%;
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
    }

    #sjacademy-fee-portal *, #sjacademy-fee-portal *::before, #sjacademy-fee-portal *::after {
      box-sizing: border-box;
      font-weight: inherit;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* ===== HERO SECTION ===== */
    .sja-header {
      text-align: center;
      padding: 60px 0 35px;
      background: var(--sja-white);
    }

    .sja-badge {
      display: inline-block;
      background: var(--sja-white);
      border: 1.5px solid var(--sja-black);
      border-radius: 50px;
      padding: 4px;
      margin-bottom: 20px;
      box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.12);
    }

    .sja-mode-pill {
      padding: 6px 18px;
      border-radius: 40px;
      font-size: 0.8rem;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      background: var(--sja-yellow);
      color: var(--sja-black);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .sja-title {
      font-size: clamp(2rem, 4.5vw, 3.4rem);
      font-weight: 400;
      margin-bottom: 16px;
      line-height: 1.2;
      color: var(--sja-black);
      letter-spacing: -0.5px;
    }

    .sja-highlight {
      background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%) no-repeat 0 85% / 100% 35%;
      display: inline;
      padding: 0 3px;
      font-weight: 400;
    }

    .sja-subtitle {
      font-size: 1.1rem;
      font-weight: 300;
      color: var(--sja-dark-grey);
      max-width: 760px;
      margin: 0 auto 25px;
      line-height: 1.6;
    }

    .sja-google-trust-banner {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--sja-light-bg);
      border: 1.5px solid var(--sja-border-light);
      border-radius: 30px;
      padding: 8px 20px;
      font-size: 13px;
      color: var(--sja-black);
      box-shadow: 2px 2px 0 rgba(0,0,0,0.06);
    }

    .sja-google-trust-banner .stars {
      color: var(--sja-orange);
      font-size: 13px;
    }

    /* ===== BATCH SWITCHER TABS ===== */
    .sja-batch-switch {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin: 30px auto 10px;
    }

    .sja-tab-btn {
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      padding: 10px 24px;
      border-radius: 40px;
      border: 1.5px solid var(--sja-brown);
      background: var(--sja-white);
      color: var(--sja-black);
      cursor: pointer;
      box-shadow: 2px 2px 0 rgba(0,0,0,0.08);
      transition: all 0.2s ease;
    }

    .sja-tab-btn.active {
      background: var(--sja-yellow);
      border-color: var(--sja-brown);
      box-shadow: 2px 2px 0 rgba(0,0,0,0.15);
    }

    /* ===== PRICING CARDS ===== */
    .sja-pricing-section {
      padding: 30px 0 50px;
      background: var(--sja-white);
    }

    .sja-pricing-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 25px;
      max-width: 1100px;
      margin: 0 auto;
    }

    @media(min-width: 768px) {
      .sja-pricing-grid { grid-template-columns: repeat(3, 1fr); }
    }

    .sja-tier-card {
      background: var(--sja-white);
      border-top: 5px solid var(--sja-brown);
      border-radius: 12px;
      padding: 32px 24px;
      box-shadow: var(--sja-shadow-card);
      transition: var(--sja-transition);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .sja-tier-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--sja-shadow-card-hover);
      border-top-color: var(--sja-orange);
    }

    .sja-tier-card.featured {
      background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #FFFDF5 100%);
      border: 1.5px solid var(--sja-yellow);
      border-top: 5px solid var(--sja-yellow);
    }

    .sja-tier-card.featured:hover {
      border-top-color: var(--sja-orange);
    }

    .sja-featured-badge {
      position: absolute;
      top: -14px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--sja-orange);
      color: #FFFFFF;
      font-size: 10.5px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      padding: 4px 14px;
      border-radius: 20px;
      box-shadow: 0 2px 6px rgba(254, 97, 0, 0.3);
    }

    .sja-tier-title {
      font-size: 1.35rem;
      font-weight: 400;
      color: var(--sja-black);
      margin-bottom: 6px;
    }

    .sja-tier-desc {
      font-size: 12.5px;
      color: var(--sja-grey);
      margin-bottom: 20px;
      min-height: 38px;
    }

    .sja-price-box {
      margin-bottom: 25px;
      padding-bottom: 20px;
      border-bottom: 1px solid #eee;
    }

    .sja-price-currency {
      font-size: 13px;
      color: var(--sja-grey);
      text-transform: uppercase;
    }

    .sja-price-amount {
      font-size: 2.2rem;
      font-weight: 400;
      color: var(--sja-black);
      line-height: 1;
      margin: 4px 0;
    }

    .sja-price-period {
      font-size: 12px;
      color: var(--sja-grey);
    }

    .sja-tier-features {
      list-style: none;
      padding: 0;
      margin: 0 0 30px 0;
      flex-grow: 1;
    }

    .sja-tier-features li {
      font-size: 13px;
      color: var(--sja-dark-grey);
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      line-height: 1.5;
    }

    .sja-tier-features li i {
      color: var(--sja-orange);
      font-size: 12px;
      margin-top: 4px;
      flex-shrink: 0;
    }

    /* 10% Discount Callout */
    .sja-discount-callout {
      text-align: center;
      margin-top: 25px;
      font-size: 13px;
      color: var(--sja-brown);
      background: var(--sja-light-yellow);
      padding: 10px 20px;
      border-radius: 30px;
      border: 1px solid var(--sja-yellow);
      display: inline-block;
    }

    /* ===== INTERACTIVE CALCULATOR SECTION ===== */
    .sja-calc-section {
      padding: 60px 0;
      background: var(--sja-light-bg);
      border-top: 1px solid var(--sja-border-light);
      border-bottom: 1px solid var(--sja-border-light);
    }

    .sja-calc-header {
      text-align: center;
      margin-bottom: 35px;
    }

    .sja-calc-header h2 {
      font-size: 1.8rem;
      font-weight: 400;
      color: var(--sja-black);
      margin-bottom: 8px;
    }

    .sja-calc-box {
      background: var(--sja-white);
      border-top: 5px solid var(--sja-brown);
      border-radius: 12px;
      box-shadow: var(--sja-shadow-card);
      max-width: 900px;
      margin: 0 auto;
      padding: 35px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
    }

    @media(min-width: 768px) {
      .sja-calc-box { grid-template-columns: 1.2fr 0.8fr; }
    }

    .sja-calc-step {
      margin-bottom: 20px;
    }

    .sja-calc-label {
      font-size: 12px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--sja-brown);
      margin-bottom: 10px;
      display: block;
    }

    .sja-calc-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .sja-calc-pill {
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 400;
      padding: 8px 18px;
      border-radius: 40px;
      border: 1.5px solid var(--sja-brown);
      background: var(--sja-white);
      color: var(--sja-black);
      cursor: pointer;
      box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.08);
      transition: all 0.2s ease;
    }

    .sja-calc-pill:hover {
      background: var(--sja-light-yellow);
    }

    .sja-calc-pill.active {
      background: var(--sja-yellow);
      border-color: var(--sja-brown);
      box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.15);
    }

    .sja-toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      background: var(--sja-light-bg);
      border: 1px solid var(--sja-border-light);
      border-radius: 8px;
      margin-top: 10px;
    }

    .sja-checkbox {
      width: 20px;
      height: 20px;
      accent-color: var(--sja-orange);
      cursor: pointer;
    }

    /* Calculator Summary Card */
    .sja-calc-summary {
      background: linear-gradient(135deg, var(--sja-light-yellow) 0%, #FFFDF5 100%);
      border: 1.5px solid var(--sja-yellow);
      border-top: 4px solid var(--sja-orange);
      border-radius: 10px;
      padding: 26px 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-align: center;
    }

    .sja-summary-title {
      font-size: 12px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--sja-brown);
      margin-bottom: 8px;
    }

    .sja-summary-total {
      font-size: 2.3rem;
      font-weight: 400;
      color: var(--sja-black);
      line-height: 1.1;
      margin-bottom: 4px;
    }

    .sja-summary-sub {
      font-size: 12px;
      color: var(--sja-grey);
      margin-bottom: 20px;
    }

    /* ===== FAQS SECTION ===== */
    .sja-faq-section {
      padding: 60px 0;
      background: var(--sja-white);
    }

    .sja-faq-header {
      text-align: center;
      margin-bottom: 40px;
    }

    .sja-faq-header h2 {
      font-size: 1.8rem;
      font-weight: 400;
      color: var(--sja-black);
      margin-bottom: 8px;
    }

    .sja-faq-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 15px;
      max-width: 900px;
      margin: 0 auto;
    }

    @media(min-width: 768px) {
      .sja-faq-grid { grid-template-columns: repeat(2, 1fr); }
    }

    .sja-faq-card {
      background: var(--sja-light-bg);
      border: 1px solid var(--sja-border-light);
      border-left: 4px solid var(--sja-brown);
      border-radius: 8px;
      padding: 20px;
    }

    .sja-faq-card h4 {
      font-size: 14px;
      font-weight: 400;
      color: var(--sja-black);
      margin-bottom: 8px;
    }

    .sja-faq-card p {
      font-size: 13px;
      color: var(--sja-dark-grey);
      line-height: 1.5;
      margin: 0;
    }

    /* ===== BANK DETAILS SECTION ===== */
    .sja-bank-section {
      padding: 50px 0;
      background: var(--sja-light-bg);
      border-top: 1px solid var(--sja-border-light);
    }

    .sja-bank-header {
      text-align: center;
      margin-bottom: 30px;
    }

    .sja-bank-header h3 {
      font-size: 1.5rem;
      font-weight: 400;
      color: var(--sja-black);
    }

    .sja-bank-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 15px;
      max-width: 900px;
      margin: 0 auto;
    }

    @media(min-width: 768px) {
      .sja-bank-grid { grid-template-columns: repeat(3, 1fr); }
    }

    .sja-bank-card {
      background: var(--sja-white);
      border: 1px solid var(--sja-border-light);
      border-radius: 8px;
      padding: 18px;
      font-size: 12.5px;
    }

    .sja-bank-name {
      font-size: 14px;
      font-weight: 400;
      color: var(--sja-black);
      margin-bottom: 4px;
    }

    /* ===== BUTTONS ===== */
    .sja-btn {
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      padding: 13px 26px;
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
      color: #FFFFFF;
      border-color: var(--sja-orange);
      box-shadow: var(--sja-shadow-button);
      width: 100%;
    }

    .sja-btn-primary:hover {
      background: var(--sja-orange-hover);
      transform: translateY(-2px);
    }

    .sja-btn-outline {
      background: var(--sja-white);
      color: var(--sja-brown);
      border-color: var(--sja-brown);
      width: 100%;
    }

    .sja-btn-outline:hover {
      background: var(--sja-brown);
      color: var(--sja-white);
    }

    .sja-btn-whatsapp {
      background: var(--sja-whatsapp);
      color: #FFFFFF;
      border-color: var(--sja-whatsapp);
      box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);
    }

    .sja-btn-whatsapp:hover {
      background: #1ebc59;
      transform: translateY(-2px);
    }

    /* ===== BOTTOM CTA SECTION ===== */
    .sja-cta-section {
      padding: 80px 0;
      background: var(--sja-light-yellow);
      border-top: 5px solid var(--sja-yellow);
      text-align: center;
    }

    .sja-cta-section h2 {
      font-size: clamp(1.8rem, 4vw, 2.6rem);
      font-weight: 400;
      margin-bottom: 12px;
      color: var(--sja-black);
    }

    .sja-cta-section p {
      font-size: 1rem;
      font-weight: 300;
      color: var(--sja-dark-grey);
      max-width: 650px;
      margin: 0 auto 30px;
    }

    .sja-cta-buttons {
      display: flex;
      justify-content: center;
      gap: 15px;
      flex-wrap: wrap;
    }
  </style>
</head>
<body>

<div id="sjacademy-fee-portal">

  <!-- 1. HERO SECTION -->
  <section class="sja-header">
    <div class="container">
      <div class="sja-badge">
        <div class="sja-mode-pill">
          <i class="fa-solid fa-tag"></i> TRANSPARENT ACADEMIC PRICING
        </div>
      </div>
      <h1 class="sja-title">SJ Academy <span class="sja-highlight">Fee Structure</span></h1>
      <p class="sja-subtitle">
        Excellence shouldn't come with surprises. Simple, transparent pricing that lets you focus entirely on your next A*.
      </p>

      <div class="sja-google-trust-banner">
        <span class="stars">★★★★★</span>
        <span>Rated <strong>5.0 / 5.0</strong> by 220+ Verified Students & Parents on Google</span>
      </div>

      <!-- Regular vs Fast-Track Switcher -->
      <div class="sja-batch-switch">
        <button class="sja-tab-btn active" id="tabRegular">May/June Regular Batches</button>
        <button class="sja-tab-btn" id="tabFastTrack">Oct/Nov Fast-Track Sprint</button>
      </div>
    </div>
  </section>

  <!-- 2. PRICING CARDS SECTION -->
  <section class="sja-pricing-section">
    <div class="container">
      <div class="sja-pricing-grid" id="pricingGrid">

        <!-- O LEVEL / IGCSE -->
        <div class="sja-tier-card">
          <h3 class="sja-tier-title">O Level / IGCSE</h3>
          <p class="sja-tier-desc">Master the syllabus at a steady, confident pace. Consistent guidance all year round.</p>
          <div class="sja-price-box">
            <div class="sja-price-currency">PKR</div>
            <div class="sja-price-amount" id="oLevelPrice">8,500</div>
            <div class="sja-price-period">per subject / month</div>
          </div>
          <ul class="sja-tier-features">
            <li><i class="fa-solid fa-check"></i> Complete syllabus coverage & formula sheets</li>
            <li><i class="fa-solid fa-check"></i> Past paper topical practice after every unit</li>
            <li><i class="fa-solid fa-check"></i> Regular assessments, homework marking & mocks</li>
            <li><i class="fa-solid fa-check"></i> Direct access to subject experts from KGS & IBA</li>
            <li><i class="fa-solid fa-check"></i> Full recording portal access included</li>
          </ul>
          <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-outline">Register Now →</a>
        </div>

        <!-- A LEVEL (FEATURED) -->
        <div class="sja-tier-card featured">
          <div class="sja-featured-badge">Most Popular</div>
          <h3 class="sja-tier-title">A Level (AS & A2)</h3>
          <p class="sja-tier-desc">Comprehensive AS & A2 coaching with in-depth marking scheme mastery.</p>
          <div class="sja-price-box">
            <div class="sja-price-currency">PKR</div>
            <div class="sja-price-amount" id="aLevelPrice">9,500</div>
            <div class="sja-price-period">per subject / month</div>
          </div>
          <ul class="sja-tier-features">
            <li><i class="fa-solid fa-check"></i> AS & A2 comprehensive preparation</li>
            <li><i class="fa-solid fa-check"></i> Intensive past paper topical & yearly sessions</li>
            <li><i class="fa-solid fa-check"></i> CAIE marking scheme & evaluation essay frameworks</li>
            <li><i class="fa-solid fa-check"></i> Full simulated mock exams & diagnostic review</li>
            <li><i class="fa-solid fa-check"></i> Free university admission & IBCC guidance</li>
          </ul>
          <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-primary">Register Now →</a>
        </div>

        <!-- LAB PRACTICALS -->
        <div class="sja-tier-card">
          <h3 class="sja-tier-title">A Level Lab Practicals</h3>
          <p class="sja-tier-desc">Physics, Chemistry, or Biology Paper 3 hands-on laboratory course.</p>
          <div class="sja-price-box">
            <div class="sja-price-currency">PKR</div>
            <div class="sja-price-amount">25,500</div>
            <div class="sja-price-period">one-time full course / subject</div>
          </div>
          <ul class="sja-tier-features">
            <li><i class="fa-solid fa-check"></i> Hands-on lab experience in DHA Phase 7</li>
            <li><i class="fa-solid fa-check"></i> Complete practical preparation (Optics, Titrations, Bio)</li>
            <li><i class="fa-solid fa-check"></i> Paper 3 apparatus handling & uncertainty graphing</li>
            <li><i class="fa-solid fa-check"></i> Mock practical exams under timed conditions</li>
            <li><i class="fa-solid fa-check"></i> Zero recurring monthly fee for practicals</li>
          </ul>
          <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-outline">Register Now →</a>
        </div>

      </div>

      <div style="text-align:center;margin-top:20px;">
        <div class="sja-discount-callout">
          <i class="fa-solid fa-sparkles" style="color:var(--sja-orange);"></i> *Get <strong>10% off</strong> your monthly fees when you pay for 3 months upfront.
        </div>
      </div>
    </div>
  </section>

  <!-- 3. INTERACTIVE TUITION & DISCOUNT ESTIMATOR -->
  <section class="sja-calc-section">
    <div class="container">
      <div class="sja-calc-header">
        <h2>Interactive Fee Calculator</h2>
        <p>Select your subjects and payment preference to calculate your exact investment.</p>
      </div>

      <div class="sja-calc-box">
        <div class="sja-calc-inputs">
          
          <div class="sja-calc-step">
            <span class="sja-calc-label">1. Select Level</span>
            <div class="sja-calc-pills" id="calcLevelPills">
              <button class="sja-calc-pill active" data-rate="8500" data-name="O-Level">O-Level (Rs. 8,500/mo)</button>
              <button class="sja-calc-pill" data-rate="9500" data-name="A-Level">A-Level (Rs. 9,500/mo)</button>
            </div>
          </div>

          <div class="sja-calc-step">
            <span class="sja-calc-label">2. Number of Subjects</span>
            <div class="sja-calc-pills" id="calcSubjectPills">
              <button class="sja-calc-pill" data-count="1">1 Subject</button>
              <button class="sja-calc-pill" data-count="2">2 Subjects</button>
              <button class="sja-calc-pill active" data-count="3">3 Subjects</button>
              <button class="sja-calc-pill" data-count="4">4 Subjects</button>
              <button class="sja-calc-pill" data-count="5">5 Subjects</button>
            </div>
          </div>

          <div class="sja-calc-step">
            <span class="sja-calc-label">3. Upfront Discount</span>
            <div class="sja-toggle-row">
              <div>
                <div style="font-size:13px;font-weight:400;color:#000;">Pay 3 Months Upfront</div>
                <div style="font-size:11.5px;color:#666;">Save 10% on your total quarterly tuition</div>
              </div>
              <input type="checkbox" id="upfrontToggle" class="sja-checkbox">
            </div>
          </div>

        </div>

        <div class="sja-calc-summary">
          <div>
            <div class="sja-summary-title">Estimated Total</div>
            <div class="sja-summary-total" id="calcTotal">PKR 25,500</div>
            <div class="sja-summary-sub" id="calcBreakdown">3 O-Level Subjects × Rs. 8,500 / month</div>
          </div>
          <div>
            <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-primary">Register For Class →</a>
            <div style="font-size:11px;color:#777;margin-top:8px;">Transparent pricing • Zero hidden fees</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 4. OFFICIAL FAQS -->
  <section class="sja-faq-section">
    <div class="container">
      <div class="sja-faq-header">
        <h2>Frequently Asked Questions</h2>
        <p>Everything you need to know about our fees, registration, and lab practicals.</p>
      </div>

      <div class="sja-faq-grid">
        <div class="sja-faq-card">
          <h4>Are there any hidden charges besides the tuition fee?</h4>
          <p>No. SJ Academy believes in transparent pricing. Apart from the Rs. 3,500 one-time registration fee for new students, you only pay the monthly tuition fee for your selected subjects, or the one-time lab fee if applicable.</p>
        </div>

        <div class="sja-faq-card">
          <h4>How does the lab practical fee work?</h4>
          <p>The A Level lab practical fee is a one-time payment of Rs. 25,500 per subject. This covers the entire practical preparation course for the exam session, without any recurring monthly costs for labs.</p>
        </div>

        <div class="sja-faq-card">
          <h4>What is the difference between Regular and Oct/Nov batches?</h4>
          <p>Regular batches run throughout the academic year at standard pacing. The Oct/Nov batches are accelerated, intensive programs designed specifically to prepare students for the Oct/Nov series in a shorter timeframe.</p>
        </div>

        <div class="sja-faq-card">
          <h4>Does the monthly fee include the British Council CAIE exam fee?</h4>
          <p>No, our monthly tuition covers the coaching, assessments, and study resources provided at SJ Academy. The final CAIE exam registration fee is paid separately to the British Council.</p>
        </div>

        <div class="sja-faq-card">
          <h4>Are study materials and past papers included?</h4>
          <p>Yes. We provide all essential topical worksheets, past papers, and proprietary revision notes as part of your regular tuition. There are no surprise costs for basic academy study materials.</p>
        </div>

        <div class="sja-faq-card">
          <h4>Do you offer scholarships or financial aid?</h4>
          <p>Yes. We offer merit-based scholarships and need-based financial aid for deserving students. Please reach out to our administration office to discuss eligibility.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. BANK PAYMENT DETAILS -->
  <section class="sja-bank-section">
    <div class="container">
      <div class="sja-bank-header">
        <h3>Official Payment Methods</h3>
        <p style="font-size:13px;color:#666;">Pay securely via online bank transfer or submit physical payment at our DHA Phase 7 front desk.</p>
      </div>

      <div class="sja-bank-grid">
        <div class="sja-bank-card">
          <div class="sja-bank-name">Standard Chartered Bank</div>
          <div><strong>Account Name:</strong> Salman Junaid</div>
          <div><strong>Account No:</strong> 01730554501</div>
        </div>

        <div class="sja-bank-card">
          <div class="sja-bank-name">Faysal Bank</div>
          <div><strong>Account Name:</strong> SJ Academy LLP</div>
          <div><strong>Account No:</strong> 3190301000002094</div>
        </div>

        <div class="sja-bank-card">
          <div class="sja-bank-name">Meezan Bank</div>
          <div><strong>Account Name:</strong> Salman Junaid</div>
          <div><strong>Account No:</strong> 01960102115003</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. BOTTOM CONVERSION CTA -->
  <section class="sja-cta-section">
    <div class="container">
      <h2>May / June 2027 Batches Open</h2>
      <p>Secure your spot today and join Karachi's premier Cambridge coaching academy. Try before you commit.</p>
      <div class="sja-cta-buttons">
        <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-primary" style="width:auto;min-width:220px;">Register For Class Now →</a>
        <a href="https://wa.me/923362144454?text=Hi%20SJ%20Academy,%20I%20want%20to%20inquire%20about%20Fee%20Structure" class="sja-btn sja-btn-whatsapp" target="_blank" style="width:auto;">
          <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
        </a>
      </div>
    </div>
  </section>

</div>

<script>
(function(){
  let currentRate = 8500;
  let currentLevelName = 'O-Level';
  let currentSubjectCount = 3;
  let isUpfront = false;

  const totalEl = document.getElementById('calcTotal');
  const breakdownEl = document.getElementById('calcBreakdown');
  const upfrontToggle = document.getElementById('upfrontToggle');

  function calculate(){
    let monthlyBase = currentRate * currentSubjectCount;
    if(isUpfront){
      let quarterlyGross = monthlyBase * 3;
      let discountedQuarterly = quarterlyGross * 0.90; // 10% discount
      totalEl.textContent = 'PKR ' + Math.round(discountedQuarterly).toLocaleString();
      breakdownEl.textContent = `3 Months (${currentSubjectCount} ${currentLevelName} Subjects) with 10% Upfront Discount applied`;
    } else {
      totalEl.textContent = 'PKR ' + monthlyBase.toLocaleString();
      breakdownEl.textContent = `${currentSubjectCount} ${currentLevelName} Subjects × Rs. ${currentRate.toLocaleString()} / month`;
    }
  }

  // Level selector
  document.querySelectorAll('#calcLevelPills .sja-calc-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#calcLevelPills .sja-calc-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentRate = parseInt(btn.getAttribute('data-rate'));
      currentLevelName = btn.getAttribute('data-name');
      calculate();
    });
  });

  // Subject count selector
  document.querySelectorAll('#calcSubjectPills .sja-calc-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#calcSubjectPills .sja-calc-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentSubjectCount = parseInt(btn.getAttribute('data-count'));
      calculate();
    });
  });

  // Upfront toggle
  upfrontToggle.addEventListener('change', (e) => {
    isUpfront = e.target.checked;
    calculate();
  });

  // Tab switcher
  const tabRegular = document.getElementById('tabRegular');
  const tabFastTrack = document.getElementById('tabFastTrack');
  const oPrice = document.getElementById('oLevelPrice');
  const aPrice = document.getElementById('aLevelPrice');

  tabRegular.addEventListener('click', () => {
    tabRegular.classList.add('active');
    tabFastTrack.classList.remove('active');
    oPrice.textContent = '8,500';
    aPrice.textContent = '9,500';
  });

  tabFastTrack.addEventListener('click', () => {
    tabFastTrack.classList.add('active');
    tabRegular.classList.remove('active');
    oPrice.textContent = '10,500';
    aPrice.textContent = '12,000';
  });

  calculate();
})();
</script>

</body>
</html>
```
