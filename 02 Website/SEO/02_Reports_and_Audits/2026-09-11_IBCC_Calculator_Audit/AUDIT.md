# SJ Academy IBCC calculator: accuracy, policy and mobile audit

Reviewed 11 September 2026. Decision: **do not publish the supplied calculator.**

The supplied HTML was reviewed in full. Its calculation engine is materially inaccurate and its inputs cannot establish the applicable equivalence rules. An estimate disclaimer does not repair systematic overstatement. This is an independent technical and education-policy audit, not IBCC certification or a claim to possess personal professional credentials.

## Scope and deliverables

- `original.html`: unchanged copy of the supplied attachment, used for reproduction.
- `ui-review-preview.html`: limited mobile/accessibility/copy fixes, with results deliberately hidden and a prominent review-only notice. Not a usable public calculator.
- `mobile-accessibility-patch.css`: extracted preview styles, including the result suppression; do not apply blindly to production.
- `patch_ui.py`: reproducible transformation of the supplied HTML.
- This report: diagnosis, source evidence, simpler structure, copy, implementation plan and release checks.

No WordPress or production files were changed. The attachment is a standalone HTML document with embedded CSS/JS, an external Google Font and a demo-registration link. There are no shortcodes, submission handlers, GA4 calls, Meta Pixel calls or WhatsApp links in it. Whether the host page supplies those is unverified. The WordPress theme, Elementor configuration, live header/footer, consent manager and registration submission journey cannot be established from this attachment. Runtime testing used a local copy; this is not a live-site certification.

## 1. Critical accuracy findings

| Severity | Finding and impact | Exact fix |
|---|---|---|
| Critical | `gradeValues` awards A/B/C/D/E five excess marks each. Every completed all-A case is shown as 90% instead of 85%. | Replace the letter conversion table with A=85, B=75, C=65, D=55, E=45. Keep grade conversion distinct from subject eligibility. [S1] |
| Critical | A* is hard-coded to 100 for every subject and year. The form cannot choose the correct annual value. | Store subject, qualification level and examination year per result. Resolve A* against the appropriate published table; no universal fallback. [S2] |
| Critical | HSSC always adds eight local O Levels and three A Levels. This misses the new science-group cohort rule. | Add group and O Level completion cohort routing. Count five compulsory O Level subjects plus relevant A Level sciences for the notification's applicable cases; retain O Level elective eligibility checks. Do not apply this automatically to Humanities or every A Level award in 2027. [S3] |
| High | Local SSC /800, overseas SSC /500 and overseas HSSC /800 are presented as equivalence certificate marks. Raw subject totals and certificate scales are conflated. | Show raw converted subtotal explicitly. Normalize certificate marks only using a verified route/cohort scale. Overseas HSSC official example scales /800 to /1100. SSC sources conflict and need clarification. [S4,S5,S6] |
| Critical | Blank and U grades count as zero but still produce a finished-looking result. A missing compulsory pass can therefore look like a valid equivalence. | Separate incomplete, failed, unsupported, needs-review and calculated states. Never issue a completed result with missing mandatory information or an unaccepted required grade. |
| High | Electives and A Levels have no subject identities. Three arbitrary entries appear sufficient for every group; duplicates cannot be detected. | Use unique recognized subject identities, group-specific requirements and qualification checks. State AS-only results are unsupported for this full-A-Level route. [S7] |
| High | “Overseas / Expat” conflates nationality, residence and examination location. | Ask O and A examination locations separately; ask only necessary nationality/exemption category. Mixed-location cases and unconfirmed exemptions must receive review guidance, not an automatic five-subject route. [S8] |
| High | No support boundary for 9–1 grades, double awards, alternative qualifications, retakes, exemptions or mixed years. | Support a verified explicit subset; give an honest unsupported-case message for all other cases. Add numeric grades only with qualification-specific conversion and acceptance validation. |

### Verified 2026 A* / grade 9 table

The signed 27 July 2026 notification, published 28 July, gives these examination-year values. The column labels are SSC and HSSC. These are **2026 values**, not 2027 forecasts. [S2]

| Subject | SSC | HSSC |
|---|---:|---:|
| Physics | 94 | 95 |
| Chemistry | 94 | 94 |
| Biology | 94 | 94 |
| Computer Science | 94 | 93 |
| Mathematics | 94 | 94 |
| English | 93 | Not listed |
| Urdu | 93 | Not listed |
| Pakistan Studies | 94 | Not listed |
| Islamiyat | 94 | Not listed |
| Other elective subjects | 94 | 94 |

“Other elective” is not permission to accept every qualification or duplicate subject. Dash entries must not be converted to zero. Annual documents for 2021–2025 are linked from IBCC's conversion page but have not all been transcribed or verified in this audit. The replacement must load and test each supported year's table before offering that year. [S1]

### What the February 2026 notification actually changes

The notice is dated 17 February, published on 18 February. It concerns Pakistan-obtained HSSC science equivalence, explicitly naming Pre-Medical, Pre-Engineering and Computer Science. It excludes O Level electives from the HSSC marks calculation and retains the five compulsory subjects plus the relevant A Level sciences. Its cohort wording refers to students completing O Level/equivalent qualifications in session 2026 and A Level/equivalent qualifications thereafter. It preserves the previously approved national-subject exemptions for foreign/dual nationals. [S3]

Do not infer a universal “A Levels 2027” switch. A student finishing O Levels in 2025 and A Levels in 2027 is not explicitly placed in that cohort by this wording. Mixed-session completion, retakes and exempt cases need a verified interpretation. The notice specifies which subjects count, but does not supply a worked normalization/rounding example. Confirm that detail before claiming exact certificate marks. This also must not be used to tell students they can skip the O Level electives required for the qualification/group.

No 2027 annual A* table was found in the official sources checked on the review date. Label 2027 unavailable until published. If offering planning scenarios, clearly distinguish assumed grades from verified annual conversion data; never reuse 2026 silently.

### Source conflict: SSC scale and arithmetic

IBCC's currently linked SSC example prints `(750/800)*1100 = 844/1100`. I downloaded and rendered page 1 and visually verified that this is in the PDF, not just search extraction. The left side equals 1031.25, not 844. Its subject marks sum to 750. [S4]

Cambridge's currently linked Destination Pakistan brochure instead illustrates SSC normalization to 900. [S6] These conflicting public examples cannot establish one universally reliable current SSC certificate scale. The safe implementation is a clearly labelled converted-subject percentage plus raw subtotal, with certificate marks withheld until the applicable scale and rounding are confirmed. Do not copy the erroneous worked result or quietly choose 900, 1100 or 1200.

The official overseas HSSC example gives a 750/800 subtotal normalized to 1100 and displays 1031. That establishes normalization in that example, but one rounded example does not prove the universal rounding convention. [S5]

### Reproducible numerical failures

These comparisons use ordinary letter grades, avoiding annual A* ambiguity:

| Input | Existing code | Correct converted-grade percentage |
|---|---:|---:|
| Eight local O Level As | 720/800, 90% | 680/800, 85% raw subtotal |
| Eight local O Level Bs | 640/800, 80% | 600/800, 75% raw subtotal |
| Legacy local HSSC: eleven As | 990/1100, 90% | 935/1100, 85% |
| Overseas HSSC: eight As | 720/800, 90% | 680/800, 85%; 935/1100 if that verified route applies |
| One A with other fields blank | Finished-looking nonzero percentage | Incomplete; no completed equivalence |
| Required subject U | Zero silently included | Required pass unmet; no completed equivalence |

A hypothetical applicable new science cohort with five compulsory O Level As and three A Level Bs has raw subtotal 650/800 = 81.25%. If the O Level electives were all As, the old eleven-subject selection would instead yield 905/1100 = 82.27% even after fixing grade conversions. This demonstrates the separate subject-selection error. The new raw percentage is arithmetic under the specified counted subjects, not a verified certificate-scale/rounding claim.

## 2. Mobile, accessibility and interaction audit

| Severity | Evidence / consequence | Fix |
|---|---|---|
| High | At a 375 CSS-pixel viewport, original document width is 397px. Widget width plus padding uses content-box sizing. | Apply scoped border-box sizing, flexible header and narrow-screen rows. |
| High | Route/level radios use `display:none`; they disappear from the accessibility tree and keyboard path. | Keep native radios visually hidden but focusable; show focus on their labels. Add group legends in the rebuilt form. |
| High | Generated subject labels have no `for`; selects have no IDs or accessible names. | Connect each label to a unique select ID. Verified in preview accessibility tree. |
| Medium | Theme checkbox has no accessible name, tiny 36×20 visual control and no explicit focus style. | Add accessible label, larger target, visible focus; retain system-native interaction. |
| High | White CTA text on #FE6100 is approximately 3.03:1, below 4.5:1 for its small text. Orange compulsory labels also need correction. | Use black CTA text and theme-specific darker/lighter label colors. [S9] |
| Medium | Labels/helpers/disclaimer are 10–11px. Grade controls are 13–14px. | Increase helper/label size and set input text to 16px; use at least 44px control height as a usability target. This size is not the universal AA minimum. |
| High | Switching level or route deletes all entered grades. | Preserve selections by stable subject identity. Preview preserves current fixed rows by label; production should use canonical IDs. |
| Medium | Dynamic result has no announced status or error summary. | Add polite status output and inline errors; avoid announcing the entire form on every change. |
| Medium | No reset, no calculation breakdown and no clear unsupported-state explanation. | Add a reset action and result breakdown with counted and excluded subjects. |
| Medium | Light focus border is yellow on white; custom select border is very pale. | High-contrast focus outline and control boundaries, tested in both themes. |
| Low | Animation ignores reduced-motion preference; dark dropdown background is transparent. | Respect reduced motion and use opaque theme colors for native menus. |

WCAG 2.2 AA is the recommended engineering target, not a claim that this audit certifies legal accessibility compliance. The full page, keyboard operation, zoom/reflow and assistive technology must be tested after integration. [S9]

## 3. Conversion and trust

The highest-impact conversion improvement is a result students can trust. The original badge implies rules have been applied even on an empty form, and the tiny disclaimer cannot undo the impression of precision.

Remove the unsupported claim about hundreds of students securing straight A*s last year. No evidence was supplied for it. Replace fear-based wording about a bad grade ruining merit. An equivalence tool visitor primarily wants an answer and an explanation, then an optional relevant next step.

Preserve the existing demo URL in the preview. Do not invent a WhatsApp number. A verified WhatsApp advisory CTA can be added after the result if the academy provides that service; demo booking is suitable for tuition interest. Confirm that “free” is still accurate and test the entire destination form before release. No grade data should be placed into URLs or analytics by default.

### Recommended simple structure and copy

1. Heading: **IBCC Equivalence Calculator**.
2. Intro: **Estimate your O Level or A Level equivalence using the published rules for your examination year. Final equivalence is issued by IBCC.**
3. Choose SSC or HSSC, then examination location and necessary group/cohort details.
4. Enter named subjects, grades and examination years. Show extra fields only when needed.
5. Result state: percentage, converted subtotal, applicable rule and readable breakdown. Only show certificate marks when the scale is verified.
6. Short sources/method section with last-reviewed date and supported-case boundaries.
7. Optional CTA: **Planning your next exam attempt?** / **Get exam-focused O and A Level support at SJ Academy, with physical classes in DHA Phase 7, Karachi, and live online classes.** / **Book a free demo** (subject to offer verification).

Empty-state copy: **Select your subjects, grades and exam years to calculate an estimate.**

Missing-rule copy: **We have not verified the conversion data for this examination year. Please check with IBCC before using a marks estimate.**

Unsupported-case copy: **Your qualification or exemption needs an individual IBCC assessment. This calculator cannot confirm an accurate result for this case.**

Avoid a large sticky promotional banner during grade entry. If a sticky control is useful, make it a compact “View result” action that does not obscure fields or focus.

## 4. Technical implementation plan requiring approval

The correct repair is a contained replacement of the calculator's form and engine, while keeping the brand and WordPress header/footer.

1. Separate a pure conversion engine from DOM rendering. Represent each result with subject ID, qualification, grade scale, exam year and grade. Keep completion year separate from per-subject exam year.
2. Create a versioned rules registry with source URLs, publication/effective scope, verified date and review status. Encode the 2026 table exactly. Load earlier verified years before exposing them.
3. Implement route/group eligibility before arithmetic: required subjects, duplicate rejection, full A Levels, accepted pass grades and verified exemption handling. Do not infer nationality from residence. Avoid collecting documents or personal identifiers.
4. Select counted subjects using cohort/group policy. Retain a separate list of subjects required for eligibility but excluded from marks.
5. Return structured result states. Unknown lookup, invalid pass, unverified route and missing field must never fall back to zero. Do not use `value || 0` for data validation.
6. Show transparent raw subtotal and percentage. Certificate-scale output remains behind a verified rule. Preserve full precision internally and format only at the end.
7. Keep CSS scoped and JS in an isolated initializer. Use unique instance IDs, no global `gradeValues` or inline handlers. Verify Elementor reinitialization and avoid duplicate event listeners. Provide widget markup without nested document/head/body tags; load fonts once at the host level.
8. Add progressive form semantics, focusable radios, labelled selects, error summaries, result announcements and reset. Retain entries when changing views.
9. Add consent-aware analytics through the site's existing setup: `tool_start`, successful `tool_complete`, and `demo_click`/`whatsapp_click` only on their actual actions. Do not fire `generate_lead` on a click; use successful submission/confirmation. Prevent duplicate Meta/GA events and send no grades, marks or nationality category. Preserve only approved attribution parameters for the booking journey.
10. Stage in the real Elementor page, test alongside existing header/footer, cache/minification, deferred scripts and consent tooling, then publish only after review.

## 5. Release checks and remaining questions

### Required calculation tests

- Every supported letter and numeric conversion; each supported A* subject/year/level lookup.
- Mixed-year results and retakes without silently replacing historical values.
- Eight/five-subject SSC route requirements; legacy HSSC; applicable new science cohort; Humanities kept distinct.
- O Levels completed before 2026 with A Levels in 2027; O Levels in 2026 with subsequent A Levels; mixed-session completion routed safely.
- Required U/F/G/missing grades, duplicate subjects, AS-only and unsupported double awards cannot produce completed results.
- Unknown year including 2027, unknown subject and unverified exemption cannot fall back to a guessed value.
- Official worked arithmetic fixtures independently recomputed; erroneous published arithmetic is flagged rather than made into an expected test result.
- Precise totals and rounding near boundaries, percentage consistency with displayed marks, no stale result after changing inputs.

### Integration checks

Test 320, 375, 390, 768 and 1280px; landscape; 200% text resize; keyboard-only and VoiceOver; light/dark native menus; slow/offline font loading; reset; repeated widget initialization; no horizontal overflow or focus obstruction. Validate actual iOS Safari and Android Chrome before calling it mobile-ready. Measure performance in the live page rather than claiming scores from this standalone snippet.

Check CTA landing, form success message/thank-you, required-field relevance, analytics delivery, consent and UTM continuity. This attachment contains no form or submission to validate.

### Exact points for IBCC clarification

- Current SSC certificate total and rounding for Pakistan/exempt/overseas cases, given the conflicting examples.
- Normalization and rounding for the new five-compulsory-plus-three-science calculation.
- Cohort handling for subjects spread across sessions, improvements and O Level completion before 2026.
- How preserved exemptions interact with counted subjects in the new calculation.
- Overseas Computer Science grouping: the British-system page lists Physics/Computer/Mathematics locally but Physics/Chemistry/Mathematics in its overseas text. Do not silently repair a possible source error. [S7]
- Approved non-Muslim compulsory-subject substitutions and special qualifications before adding them to supported scope.

The main form/engine replacement is a major change and is awaiting approval under the supplied AGENTS.md instruction. The local UI preview does not resolve the accuracy blockers and must not be deployed.

## Sources checked

S1. [IBCC conversion tables and annual document links](https://ibcc.edu.pk/conversion-for-equivalence/). Page inspected live in browser; search corroboration.

S2. [IBCC 2026 grading notice](https://ibcc.edu.pk/equivalence-grading-2026/) and [signed table image](https://ibcc.edu.pk/wp-content/uploads/2026/07/Grading-2026.png). Image visually read in browser.

S3. [IBCC science-group calculation notification](https://ibcc.edu.pk/notification-for-calculation-of-a-level-equivalent-qualification-based-on-compulsory-subjects-of-o-level/) and [linked signed document](https://ibcc.edu.pk/wp-content/uploads/2026/05/Notification-for-calculation-of-A-level-Equivalent-Qual-based-on-compulsory-subjects-of-O-Lvl.pdf). Embedded notice visually read; publication and document dates distinguished.

S4. [IBCC SSC worked example](https://ibcc.edu.pk/wp-content/uploads/2026/04/Example-for-Calculating-O-Level-Marks-1.pdf). Page 1 downloaded/rendered; arithmetic inconsistency visually confirmed.

S5. [IBCC HSSC worked example](https://ibcc.edu.pk/equivalence/Example-for-Calculating-A-Levels-Marks-1.pdf). Indexed official document text, including overseas example.

S6. [Cambridge Destination Pakistan brochure](https://www.cambridgeinternational.org/Images/505904-destination-pakistan-brochure.pdf), printed pages 6–9. Useful corroboration, not authority to override a newer IBCC notice.

S7. [IBCC British-system requirements](https://ibcc.edu.pk/equivalence-intro/british-system/). Official indexed requirements; overseas Computer Science wording requires clarification.

S8. [IBCC equivalence FAQs](https://ibcc.edu.pk/faqs/equivalence-faqs/) and [Cambridge recognition page](https://www.cambridgeinternational.org/programmes-and-qualifications/recognition-and-acceptance/country/pakistan/). Examination-location rules and qualification requirements.

S9. [W3C WCAG 2.2](https://www.w3.org/TR/wcag/). Accessibility engineering criteria.

Several IBCC pages returned 403 to the search reader; browser access allowed the two signed notices and conversion tables to be inspected. Evidence strength is stated above. No claim is made to know unpublished future updates.
