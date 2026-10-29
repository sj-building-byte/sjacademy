# Elementor Implementation Standards

## Default Assumption

Most SJ Academy page work happens inside WordPress and Elementor, often through custom HTML, CSS, and JS sections.

Preserve the existing WordPress header and footer unless explicitly asked to replace them.

## Elementor HTML Widget Rules

When delivering a section for an Elementor HTML widget:

- Keep CSS scoped to a unique wrapper ID or class.
- Avoid global selectors.
- Avoid modifying `body`, `html`, or unrelated Elementor wrappers.
- Do not add full document wrappers unless requested.
- For section-only snippets, do not include `<html>`, `<head>`, or `<body>`.
- Avoid unnecessary libraries.
- Keep code readable and editable.
- Use semantic HTML where practical.
- Make all sections responsive.

## Scoping Pattern

Use a unique wrapper:

```html
<section id="sja-example-page">
  <style>
    #sja-example-page,
    #sja-example-page * {
      box-sizing: border-box;
    }

    #sja-example-page {
      --yellow: #FCE004;
      --brown: #453516;
      --orange: #fe6100;
      --whatsapp: #25D366;
      font-family: 'Poppins', Arial, sans-serif;
    }
  </style>

  <!-- Content here -->
</section>
```

## Risky Patterns To Avoid

Do not use:

```js
document.querySelectorAll("body *")
```

unless there is a very strong, documented reason. DOM-wide cleanup scripts are risky inside Elementor because they can damage unrelated WordPress content, headers, footers, forms, popups, and tracking.

Avoid:

- `body *` selectors
- Global resets
- Unscoped button styles
- Unscoped `h1`, `h2`, `p`, `a`, or `img` rules
- JS that rewrites outside the section
- CSS that changes Elementor containers globally
- Hardcoded assumptions about header height unless verified

## Styling Standards

Use:

- Poppins when matching existing SJ Academy custom sections
- Brand colors from `01-brand-positioning.md`
- Clear section spacing
- Mobile-first layouts
- `max-width` wrappers
- Responsive grid fallbacks
- Readable text sizes
- 6px to 12px border radii depending on existing page style

Avoid:

- One-off visual systems that do not match SJ Academy
- Excessive shadows
- Overly decorative gradients
- Generic stock-feeling UI
- Tiny mobile text
- Huge desktop-only hero layouts

## Images

Prefer real SJ Academy images for:

- Lab pages
- Classroom pages
- Teacher pages
- Student proof

Use background images only when the crop can be controlled. Add clear `role="img"` and `aria-label` where the image is CSS-based and meaningful.

## CTA Implementation

For WhatsApp links:

```html
<a href="https://wa.me/VERIFIED_NUMBER?text=Hi%20SJ%20Academy%2C%20I%20want%20details%20about%20A%20Level%20classes." target="_blank" rel="noopener">
  WhatsApp for Details
</a>
```

Only use a number that was supplied or already verified in the current project. Existing workspace pages include a WhatsApp number in some opportunity CTAs, but verify the current number before reusing it on a new public page.

For Elementor popups:

- Preserve the existing popup action URL if the page already uses one.
- Do not replace popup flows with WhatsApp unless that is the approved change.
- If popup ID is unclear, ask or inspect the existing page.

## JavaScript Rules

Use vanilla JS unless a library is already present and necessary.

Keep JS:

- Scoped
- Small
- Defensive
- Easy to remove

Good JS use cases:

- Filters
- Search within cards
- FAQ expand behavior
- Review read-more toggles
- Sticky CTA visibility
- Tracking event hooks

Avoid JS for:

- Layout that CSS can handle
- Content that should be editable in HTML
- Rewriting large DOM blocks unless data-driven cards are clearly easier to maintain

## Responsive QA Checklist

Check at least:

- 390px mobile width
- 768px tablet width if layout is complex
- 1280px desktop width

Verify:

- No horizontal overflow
- Hero reads cleanly
- CTA is visible and tappable
- Sticky CTA does not hide important content
- Cards stack correctly
- Images crop acceptably
- Text does not overlap
- Buttons do not overflow
- Filter controls wrap correctly
- FAQ and interactive elements work

## Local Preview

For standalone HTML previews:

- Use local browser or simple static server when needed.
- Verify DOM, layout, and interactions before delivery.
- For Elementor snippets, remember that final behavior can differ inside WordPress because of theme CSS, Elementor containers, optimization plugins, and scripts.

## Final Delivery Notes

When delivering Elementor code, mention:

- Whether it is section-only or full-page preview HTML
- Where to paste it
- Which CTA links, popup IDs, or numbers need verification
- What responsive checks were performed
- Any tracking that still needs setup in WordPress, GA4, GTM, or Meta Pixel
