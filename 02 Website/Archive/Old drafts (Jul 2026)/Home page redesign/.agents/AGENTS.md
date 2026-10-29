# SJ Academy — Brand & Design System Guide

## 1. Brand Overview

SJ Academy is an educational platform serving students in Pakistan, focused on university admissions guidance, school discovery, and academic tools. The brand is bold, friendly, and trustworthy — designed to feel professional yet approachable for students and parents.

---

## 2. Color Palette

| Name | Hex | Usage |
|---|---|---|
| Primary Yellow | #FCE004 | Highlights, text background marks, badge fills, map buttons, light card backgrounds |
| Brown | #453516 | Card top borders, headings on light backgrounds, outline buttons, tag borders |
| Orange | #FE6100 | Primary buttons, links, hover states, focus rings, active accents |
| Black | #000000 | Main headings, primary text |
| White | #FFFFFF | Page background, card backgrounds, button text on orange |
| Grey | #555555 | Secondary body text, status messages |
| Dark Grey | #222222 | Subtitles, muted body copy |
| Light Background | #FAFAFA | Controls section background, form areas |
| Light Yellow | #FFF9CC | Highlight card backgrounds (Reality Check, special callouts) |
| WhatsApp Green | #25D366 | WhatsApp contact buttons only |

### Color Rules
- One accent at a time. Orange is the action color. Yellow is the highlight/attention color. Never mix them on the same element.
- Buttons: Orange fill for primary actions. White + brown border for secondary/outline actions.
- Highlight text: Yellow underline mark using `background-size: 100% 35%` positioned at `0 85%`.
- Card borders default to brown. On hover, shift to orange.

---

## 3. Typography

### Font Family
Poppins (Google Fonts) at weights: 300, 400, 600, 700, 800

Always load via:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
```

### Type Scale

| Element | Size | Weight | Transform | Notes |
|---|---|---|---|---|
| Page title (desktop) | 3.8rem | 800 | None | Line-height 1.2 |
| Page title (mobile) | 2.2rem | 800 | None | |
| Card heading | 1.5rem | 700 | None | |
| Subtitle | 1.1rem | 400 | None | Color #222 |
| Body text | 15px | 400-500 | None | Color #444, line-height 1.6 |
| Labels | 14px | 700 | uppercase | Letter-spacing 0.5px |
| Meta/footer | 13px | 400 | None | Italic, color #666 |
| Badge text | 12px | 700 | None | |
| Mode pill | 0.85rem | 700 | uppercase | |

---

## 4. Layout & Spacing

### Container
- max-width: 1200px
- margin: 0 auto
- padding: 0 20px

### Section Padding
- Header: 60px 0 40px (desktop), 40px 0 30px (mobile)
- Controls: 50px 0
- Output/Results: 60px 0 (desktop), 40px 0 (mobile)

### Grid System
- Default: 1 column
- Tablet (768px+): 2 columns
- Desktop (992px+): 3 columns
- Gap: 30px

---

## 5. Component Library

### 5.1 Mode Badge (Page Indicator)
A pill inside a bordered container that identifies the tool/section.
```
┌──────────────────────────────┐
│  ┌────────────────────────┐  │  ← border: 2px solid black
│  │  ⚙️ ADMISSION CRITERIA  │  │     border-radius: 50px
│  └────────────────────────┘  │     box-shadow: 4px 4px 0 rgba(0,0,0,0.15)
└──────────────────────────────┘      background: #FCE004
                                      border-radius: 40px
                                      font-weight: 700, uppercase
```

### 5.2 Text Highlight
Yellow underline mark on inline text.
```css
background: linear-gradient(120deg, #FCE004 0%, #FCE004 100%);
background-repeat: no-repeat;
background-size: 100% 35%;
background-position: 0 85%;
display: inline;
padding: 0 3px;
```

### 5.3 Select Dropdowns
```css
width: 100%;
padding: 16px 20px;
border: 2px solid #e5e5e5;
border-radius: 5px;          /* sharp, not pill */
font-weight: 500;
appearance: none;
background-image: [custom SVG chevron];
background-position: right 20px center;

/* Focus state */
border-color: #FE6100;
box-shadow: 0 0 0 3px rgba(254,97,0,0.1);
transform: translateY(-2px);
```

### 5.4 Primary Button (Orange)
```css
background: #FE6100;
color: #FFFFFF;
border: 2px solid #FE6100;
border-radius: 5px;
padding: 16px 35px;
font-weight: 700;
text-transform: uppercase;
box-shadow: 0 4px 10px rgba(254,97,0,0.3);

/* Hover */
background: #e55800;
transform: translateY(-3px);
box-shadow: 0 10px 20px rgba(254,97,0,0.4);
```

### 5.5 Outline Button (Secondary)
```css
background: #FFFFFF;
color: #453516;
border: 2px solid #453516;
border-radius: 5px;
padding: 16px 35px;
font-weight: 700;
text-transform: uppercase;

/* Hover */
background: #453516;
color: #FFFFFF;
transform: translateY(-3px);
box-shadow: 0 10px 20px rgba(69,53,22,0.3);
```

### 5.6 Card
```css
background: #FFFFFF;
padding: 30px;
border-top: 6px solid #453516;   /* signature brown top border */
border-radius: 8px;
box-shadow: 0 10px 25px rgba(0,0,0,0.05);
transition: all 0.3s ease;

/* Hover */
transform: translateY(-10px);
box-shadow: 0 20px 40px rgba(0,0,0,0.1);
border-top-color: #FE6100;       /* shifts to orange */
```

### 5.7 Highlight Card (Special Callout)
```css
border-top: 6px solid #FCE004;
background: linear-gradient(135deg, #FFF9CC 0%, #fff6b8 100%);

/* Hover */
border-top-color: #FE6100;
```

### 5.8 Key-Value Pairs
```
┌─────────────────────────────┐
│ LABEL (uppercase, bold)     │  ← font-weight: 700, 14px
│ Value text here             │  ← 15px, color #444
├─────────────────────────────┤  ← border-bottom: 1px solid #eee
│ NEXT LABEL                  │
│ Next value                  │
└─────────────────────────────┘
```
Last row has no bottom border.

### 5.9 Tags / Badges
```css
background: #FCE004;
color: #000000;
font-size: 12px;
font-weight: 700;
padding: 6px 14px;
border-radius: 40px;
border: 1.5px solid #453516;
box-shadow: 3px 3px 0 rgba(0,0,0,0.1);

/* Hover */
background: #ffe66f;
```

### 5.10 Map / Action Button (Yellow)
```css
background: #FCE004;
color: #453516;
border: 2px solid #453516;
border-radius: 5px;
padding: 12px 20px;
font-weight: 700;
text-transform: uppercase;
box-shadow: 0 4px 10px rgba(0,0,0,0.08);

/* Hover */
background: #FE6100;
color: #FFFFFF;
border-color: #FE6100;
transform: translateY(-3px);
box-shadow: 0 10px 20px rgba(254,97,0,0.3);
```

### 5.11 Status Bar
```css
font-size: 14px;
color: #555555;
padding: 12px 24px;
background: rgba(255,255,255,0.9);
border: 1px solid #eee;
border-radius: 5px;
text-align: center;
```

### 5.12 Meta / Footer Note
```css
font-size: 13px;
color: #666;
font-style: italic;
margin-top: 20px;
padding-top: 20px;
border-top: 1px solid #eee;
```
Links inside meta: `color: #FE6100`, hover shifts to `#453516`.

---

## 6. Motion & Interaction

| Trigger | Effect |
|---|---|
| Button hover | `translateY(-3px)` + deeper shadow |
| Card hover | `translateY(-10px)` + shadow grows + border color shifts brown→orange |
| Select focus | `translateY(-2px)` + orange border + orange glow ring |
| Tag hover | Background lightens (#ffe66f) |
| Map button hover | Fills orange, text turns white, lifts up |
| Refresh link hover | Icon rotates 180° |
| Loading state | Horizontal shimmer sweep (1.5s loop) |

### Transition Timing
All transitions use `cubic-bezier(0.25, 0.46, 0.45, 0.94)` for a natural, slightly bouncy feel.

---

## 7. Focus & Accessibility

All interactive elements get:
```css
outline: 3px solid #FE6100;
outline-offset: 2px;
```

- All sections with dynamic content use `aria-live="polite"`
- Color contrast meets WCAG AA on all text/background combinations
- Mobile buttons are full-width for easy tap targets

---

## 8. Responsive Breakpoints

| Breakpoint | Width | Changes |
|---|---|---|
| Mobile | < 768px | 1 column, full-width buttons, smaller title (2.2rem), reduced padding |
| Tablet | 768px+ | 2-column grid, side-by-side controls |
| Desktop | 992px+ | 3-column grid, larger title (3.8rem) |

---

## 9. Brand Voice (Design Implications)

- Bold, not aggressive. Heavy font weights, strong colors, but generous whitespace.
- Structured, not rigid. Clear hierarchy with cards and key-value pairs, but organic hover interactions.
- Helpful, not corporate. Yellow highlights feel warm. Orange buttons feel energetic. Brown grounds everything with credibility.
- Student-first. Mobile-first responsive design. Large tap targets. Clear labels.

---

## 10. What to Avoid

| Never Do | Why |
|---|---|
| Pill/radius-14px selects | SJ Academy uses sharp 5px radius on form controls |
| Inter, Roboto, or system fonts | Always Poppins |
| Purple gradients | Off-brand |
| Centered hero + 3 cards + CTA footer | Generic AI pattern; SJ Academy uses asymmetric grids |
| `border-top` on cards in any color other than brown (default) or orange (hover) | Signature brand element |
| Font weights below 300 | Poppins 300 is the lightest used |
| Mixing orange and yellow on the same element | Orange = action, Yellow = attention. Keep them separate. |
