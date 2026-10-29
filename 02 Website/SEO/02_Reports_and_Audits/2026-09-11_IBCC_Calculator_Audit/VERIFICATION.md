# Verification record

11 September 2026

- Read the entire supplied HTML, CSS and JavaScript.
- Original local rendering: measured `innerWidth=375`, document `scrollWidth=397`; horizontal overflow confirmed.
- Original accessibility tree: route/level radios absent; grade controls unnamed; theme checkbox unnamed.
- Patched preview: all 11 grade controls have associated labels; native route/level radio controls and named theme checkbox appear in accessibility tree.
- Selected English A, switched HSSC -> SSC -> HSSC: A remained selected.
- Patched results panel confirmed hidden; warning visible; incorrect numeric option annotations removed.
- Patched layout visually inspected in a fixed 320px iframe. Header and controls fit the narrow column. Broader live-device certification is outstanding.
- Browser viewport override produced inconsistent measurements during a multi-width sweep (550px persisted). Those attempted 320/375/390/768/1280 measurements are NOT treated as passing tests. Used fixed-width iframe for narrow visual inspection instead.
- Official SSC source PDF page 1 rendered using Poppler and visually checked: arithmetic inconsistency exists in source.
- Signed February and July 2026 notices visually read on IBCC website.
- Full calculation regression suite is specified in AUDIT.md; replacement engine has not been implemented or tested.
- No live WordPress, demo form submission, tracking, iOS/Android device or full WCAG conformance tests completed.

Preview is not approved for public use. See AUDIT.md for required engine replacement and source clarification.
