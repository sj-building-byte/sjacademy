# Tracking, Forms, And QA

## Conversion Actions To Track

Always check whether these are present or needed:

- WhatsApp click tracking
- Meta Pixel events
- GA4 events
- Form submission tracking
- Thank-you page or confirmation message
- UTM preservation
- Phone click tracking if phone links are present
- Workshop registration events if workshops are promoted
- Admission enquiry events

## Key Events

Suggested event names:

- `whatsapp_click`
- `lead_form_submit`
- `admission_enquiry`
- `course_register_click`
- `popup_open`
- `workshop_registration_click`
- `phone_click`
- `download_resource`

Keep event names consistent across GA4, GTM, and Meta where possible.

## WhatsApp Tracking

For WhatsApp links:

- Use a verified number.
- Use a prefilled message that identifies the offer.
- Track clicks with GA4 and Meta if possible.
- Preserve UTMs from ad traffic where relevant.

Example message:

```text
Hi SJ Academy, I want details about A Level Business classes.
```

## UTM Preservation

If paid campaigns drive to a landing page and then to WhatsApp, UTMs can be lost unless preserved.

Check whether:

- UTM parameters are captured in form hidden fields
- WhatsApp messages include campaign context
- GTM events fire before external navigation
- Landing page stores campaign info in session storage when needed

Simple approach:

- Track WhatsApp click event in GA4 and Meta.
- Include offer-specific prefilled WhatsApp text.
- Add hidden UTM fields to forms when forms are used.

## Form Rules

For landing pages, forms should be short and offer-specific.

Recommended fields:

- Student name
- Phone number
- Class level
- Subject or course
- Preferred mode: physical or online
- Optional note

Avoid:

- Long forms
- Unrelated subjects
- Payment details too early
- Unclear submit button
- Forms without confirmation
- Forms that reload without feedback

## Thank-You And Confirmation

Every form should have one clear post-submit behavior:

- Inline confirmation message
- Redirect to thank-you page
- WhatsApp follow-up prompt
- Email or admin notification

For paid traffic, a thank-you page makes conversion tracking simpler.

## Technical QA Checklist

Before delivery:

- Mobile layout checked
- Desktop layout checked
- No horizontal overflow
- Header and footer preserved
- Elementor section scoped
- CTA links work
- WhatsApp opens correct chat
- Popup opens if popup CTA is used
- Form submits
- Confirmation appears
- No unrelated fields
- No console errors from the new script
- No page-wide CSS conflicts
- Images load
- Fonts load or degrade cleanly
- Sticky CTA works and does not cover content
- FAQ toggles work
- Filters and search work if present

## Conversion QA Checklist

Ask:

- Does the hero explain the offer immediately?
- Is the primary CTA obvious?
- Is the next step low-friction?
- Does the page match visitor intent?
- Is there enough proof before asking for action?
- Are there duplicate CTAs that confuse the user?
- Are parents and students both addressed where needed?
- Does mobile make the same journey easier, not harder?

## Analytics QA Checklist

Check:

- GA4 installed
- Meta Pixel installed
- GTM installed if used
- Events are not firing twice
- WhatsApp clicks are tracked
- Form submissions are tracked
- Thank-you page is marked as a conversion if used
- UTMs are preserved or captured
- Test submissions are excluded or noted

## Risk Notes

Common risks:

- Elementor popup IDs change.
- Optimization plugins delay or combine scripts.
- WhatsApp links lose attribution.
- Forms submit but do not notify admissions.
- Meta Pixel fires on page view but not lead action.
- GA4 receives traffic but not conversion events.
- Sticky bars hide form buttons on mobile.
- CSS from one Elementor widget affects another section.

Document these risks in final delivery when they are not verifiable locally.

