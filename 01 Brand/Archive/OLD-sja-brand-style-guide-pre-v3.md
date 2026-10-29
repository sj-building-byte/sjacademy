# SJ Academy (SJA) Brand Style Guide

This document serves as the foundational design system for all interactive tools and web components built for SJ Academy. By adhering to this guide, all future tools will maintain a consistent, premium, and recognizable aesthetic while allowing room for tool-specific creativity.

---

## 1. Brand Colors

The SJA palette is vibrant, high-contrast, and energetic. It relies on a strong interplay between bright yellow/orange and solid black/white to create a modern, slightly bold aesthetic.

### Core Palette
*   **Primary Yellow (`--sja-yellow`)**: `#FCE004` — Used for primary call-to-actions, prominent badges, active states, and thick border accents.
*   **Secondary Orange (`--sja-orange`)**: `#FE6100` — Used for secondary accents, icons (like lock icons, feature checkmarks), and energetic highlights.
*   **Black (`--sja-black`)**: `#000` — Used for primary typography, strong UI borders, and high-contrast structural elements.
*   **White (`--sja-white`)**: `#fff` — The primary background color for interactive cards and the main page.

### Neutrals & Backgrounds
*   **Dark Grey (`--sja-dark-grey`)**: `#222` — Used for secondary headings and strong sub-text.
*   **Medium Grey (`--sja-grey`)**: `#555` — Used for paragraph text, descriptions, and muted labels.
*   **Light Background (`--sja-light-bg`)**: `#fafafa` — Used for alternating section backgrounds and subtle structural grouping.
*   **Light Yellow (`--sja-light-yellow`)**: `#FFF9CC` — Used for subtle hover states on yellow buttons or active selectable items.
*   **Brown (`--sja-brown`)**: `#453516` — Used sparingly for deep, warm contrasts against the primary yellow.

### Semantic Colors
*   **Success Green**: `#2ecc71` (Light background: `#eafaf1`) — Used for correct answers, positive feedback, and success states.
*   **Error Red**: `#e74c3c` (Light background: `#fdedec`) — Used for incorrect answers, error messages, and critical warnings.

---

## 2. Typography

We use **Poppins** exclusively to give the UI a friendly, geometric, and highly readable modern look.

*   **Primary Font Family**: `'Poppins', Arial, sans-serif`
*   **Font Weights**:
    *   `300` (Light) — Sub-text and subtle meta-information.
    *   `400` (Regular) — Standard body copy.
    *   `600` (Semi-Bold) — Interactive labels, buttons, and sub-headings.
    *   `700` (Bold) — Primary headings, key data points, and active states.
    *   `800` (Extra-Bold) — Hero titles and prominent numbers.
*   **Base Styling**: 
    *   Base Font Size: `16px` (scales down slightly on mobile to `15px`).
    *   Line Height: `1.6` for optimal readability.

---

## 3. UI Components & Motifs

### Shapes & Borders
*   **Cards & Panels**: Use a generous `border-radius: 12px` to keep the UI approachable. Often paired with a thick top accent border (e.g., `border-top: 5px solid var(--sja-yellow)`).
*   **Buttons & Inputs**: Use a moderate `border-radius: 6px` to `8px`.
*   **Pills & Badges**: Use fully rounded corners (`border-radius: 40px` to `50px`).
*   **High-Contrast Borders**: Don't shy away from using solid black borders (`2px solid #000`) on light elements (like badges) to give them a modern, slightly "brutalist" or sticker-like pop.

### Shadows (Depth)
Avoid harsh, tight drop shadows. SJA uses two distinct shadow styles:
1.  **Soft & Deep**: For floating panels and main interactive cards, use a large, diffuse shadow to separate them from the background: `box-shadow: 0 30px 60px rgba(0,0,0,0.12);`
2.  **Hard Offset**: For decorative badges or specific CTA buttons, use a solid offset shadow for a playful, tactile feel: `box-shadow: 4px 4px 0 rgba(0,0,0,0.15);`

### Buttons
*   **Primary (Black)**: `#000` background, `#fff` text. Hover state translates up `translateY(-3px)` and adds a soft shadow.
*   **Primary (Yellow)**: `#FCE004` background, `#000` text. Used for "Start" or "Retry" actions.
*   **Secondary (Grey Outline)**: `#fff` background, `#eee` border, `#555` text. Hover changes border to `#000` and text to `#000`.

---

## 4. Layout & Spacing

*   **Container Width**: All tools should be centered with a `max-width: 1200px`.
*   **Padding**:
    *   Desktop: `0 20px` horizontal padding on the main container.
    *   Mobile: `0 14px` horizontal padding.
*   **Vertical Rhythm**: Use generous vertical padding for distinct sections (e.g., `padding: 50px 0` to `80px 0`) to let the content breathe. 
*   **CSS Grid & Flexbox**: Always rely on modern CSS Grid and Flexbox for component layout. Avoid absolute positioning for structural layouts to ensure bulletproof mobile responsiveness.

---

## 5. Creativity & Tool-Specific Adaptations

While this guide defines the core SJA identity, each specific tool should inject its own flavor:

1.  **Micro-Animations**: Every tool should feel alive. Depending on the tool's purpose, introduce custom micro-animations (e.g., a progress bar filling up, a checkmark drawing itself, or a card flipping).
2.  **Data Visualization**: If a tool relies heavily on data (like quiz results), use SVG rings, dynamic charts, or progress bars heavily stylized with the SJA color palette.
3.  **Iconography**: Use clean, stroke-based SVG icons (typically `stroke-width="2"` or `3`, `stroke-linecap="round"`). Feel free to use the secondary Orange color to make icons pop.
4.  **Layout Twists**: The structure of a "Quiz" is different from a "Flashcard App" or a "Calculator". Feel free to invent new UI components (like carousels, split-screens, or sidebars) as long as they adhere to the fundamental tokens (Poppins, 12px radii, SJA colors).
