# 9 market diagrams (A Level Economics reel)

Fourth reel in the draw-reel series. Copied from `../circle-theorems/` on 11 November 2026; engine extended for graphs (axes instead of a circle, shaded areas, a second shift on beat 5).

## Five-line brief
1. **Who and when:** A Level Economics (9708) students, AS and A2, scrolling in the evening before a test or mock.
2. **The one thing:** the nine market diagrams that come up most in sections 2, 3 and 7, each with the rule in one line.
3. **The idea:** the pen draws each diagram on the beat, the shift lands on beat 3, the labels stamp on 4 and 5, and all nine sit on one screen to screenshot.
4. **The proof:** the 9708 syllabus topics.
5. **Format and level:** teacher reel, 9:16, 46.0 s, 128 BPM, ink ground, original music composed in code.

## Syllabus basis
Cambridge International AS & A Level Economics 9708, syllabus for 2026, 2027 and 2028, version 2 (downloaded 11 November 2026 from cambridgeinternational.org, 697423-2026-2028-syllabus.pdf). The title says "9", not "Every": the list leaves out consumer and producer surplus, buffer stocks and elasticity diagrams.

| # | Diagram | Section | Box text |
|---|---|---|---|
| 1 | Demand rises | 2.1.5, 2.4.2 | When demand rises, price and quantity rise |
| 2 | Supply rises | 2.1.6, 2.4.2 | When supply rises, price falls and quantity rises |
| 3 | Move or shift | 2.1.7 | A change in its own price moves along the curve. Other causes shift it |
| 4 | Maximum price | 3.2.4 | A maximum price below equilibrium causes a shortage |
| 5 | Minimum price | 3.2.4 | A minimum price above equilibrium causes a surplus |
| 6 | Indirect tax | 3.2.1 | An indirect tax shifts supply up and buyers and sellers share it |
| 7 | Subsidy | 3.2.2 | A subsidy shifts supply down so buyers pay less, sellers get more |
| 8 | Negative production externality | 7.4.1, 7.4.5 | Social cost is above private cost so the market over-produces |
| 9 | Positive consumption externality | 7.4.2, 7.4.5 | Social benefit is above private benefit so the market under-produces |

Box wording is SJ's own (the syllabus lists topics, not statements). Sunyyan approved the list and wording on 11 November 2026.

## Accuracy check (00 Start Here/ACCURACY.md), 11 November 2026
- **Solved twice.** First solve: `build.py` builds each diagram from straight-line equations. Second solve: `verify_markets.py` re-finds every equilibrium by intersecting the drawn segments and checks every dot, dashed line, axis label and shaded area against them, then re-tests all nine rules by algebra on 2,000 random straight-line markets. Result: ALL PASS, no counter-example.
- **Conditions stated.** Max price "below equilibrium", min price "above equilibrium". Tax and subsidy notes say "The split depends on elasticity", so "share it" is not read as a universal rule (with perfectly inelastic demand, buyers pay it all). Item 3's note gives a cause that shifts demand the same way for every good ("more buyers"), not income, which reverses for inferior goods.
- **Every letter defined on its own slide.** P1/Q1/P2/Q2, A/B, E, Qd/Qs, Pc/Pp/P1, PC/SC, PB/SB, Qm/Qo are named in each note. D and S are standard.
- **Diagram honest.** Shifts are parallel; the tax and subsidy gap Pc to Pp equals the vertical shift exactly; the deadweight triangles run from Qo to Qm between the social and private curves.
- **Frames reviewed as a student:** all nine scenes, the recap, the phone and the end card (snapshots 11 November 2026). Fixed: labels Q1/Q2 touching, "Surplus" under "Min price", "subsidy" over S2, cramped recap labels.

## Music: SJ's own synth track
`music/compose.py`: 128 BPM, D minor, Dm, Bb, F, C over a D drone, new hook in four phrases. Half-time opening, four-on-the-floor from beat 40 (the tax item). Measured with `draw-reel-kit/tools/music_check.py`:
- Loudness -14.0 LUFS, peak -5.7 dBFS
- Lead harmonics -17.8 and -27.2 dB (target about -18 and -26)
- Similarity to 4 bars earlier 0.48 (target 0.5 or less)
- Accent medians: beat 0 +3.4 dB, beat 4 +2.5 dB, beat 5 +7.9 dB (all rise). Three individual beat-4 hits do not rise clearly. Fixed at 128 BPM by shortening the lead notes before the hits, quietening the offbeat bass and open hat before them, and making the beat-4 stab louder.
- Measured, not heard.

## Beat map (one beat = 60/128 s)
Items 0 to 72 (8 beats each), recap 72 to 84, end card 84 to 98.

## End card (v2, 11 November 2026)
Sunyyan rejected the yellow demo card and the phone scene (past papers page) and had both removed. He also turned down five colourful concepts (in `concepts/`). The recap now cuts straight to a pure black card with no border:
- logo, top middle
- "Save this reel" and "share it with a friend"
- "Follow SJ Academy for O/A Level Success"
- sjacademy.pk and the WhatsApp number

The neon is all in the motion: the logo, "a friend", the follow line and the two contact pills switch on like neon tubes on the beat (0, 2.5, 4, 6, 7). A light sweep crosses the follow line on beat 8, and the glows pulse on every bar after that.

Fonts, on Sunyyan's instruction, an exception to the Poppins-only rule:
- Gilroy for "Save this reel". Commercial font from his installed fonts; confirm the licence.
- Poppins for the follow line.
- PT Mono (free, OFL) for the contacts.

Colours: brand yellow and orange as the neon.

## v2 render
`renders/economics-market-diagrams_v2.mp4`, 46.0 s. Sync is a median 16 ms, with 85% within 50 ms. -14.0 LUFS. `hyperframes check` passes.

## v3 render
`renders/economics-market-diagrams_v3.mp4`. Sunyyan asked for "Follow SJ Academy" to be the same size as "Save this reel". Poppins has a taller x-height than Gilroy (0.558 against 0.5 of the font size) and is wider, so at the same point size it looked bigger. It is now 86 px against Gilroy's 96 px, which matches the x-height. Sync is a median 18 ms, with 82% within 50 ms. -14.0 LUFS.

## v4 render
`renders/economics-market-diagrams_v4.mp4`. The end card is re-spaced so the five groups have equal gaps, measured from the frame at 120 px (±1): logo, message, rule, follow line, pills. Everything sits inside the Reels safe zone: content runs from y 305 to 1445 (zone 250 to 1500) and x 134 to 952 (zone 60 to 960). The pills are smaller: 640 × 108 px, text 42 px (were 740 × 128, 50 px).

## v5 render
`renders/economics-market-diagrams_v5.mp4`. "Follow SJ Academy" is down to Poppins 59 px, so it matches the width of "for O/A Level Success" (564 px against 566 px, measured). The groups are re-spaced with equal 130 px gaps. Content runs from y 296 to 1452, inside the safe zone.

## Finished
Sunyyan approved v5 on 11 November 2026. Moved to `✅ Finished/Videos/Reels & teaching/9 market diagrams.mp4`. Caption in `CAPTION.txt`. Still to do: confirm the Gilroy licence before posting.

## Second accuracy audit, 11 November 2026 (v6, replaces v5 in Finished)
Sunyyan asked for every frame to be checked again. All 18 scene states (mid-item and finished), the recap and the end card were reviewed from the finished video. Fixed:
- Item 3 said "A price change moves along the curve". A change in the price of a substitute or complement also shifts demand, so the box now says "A change in its own price moves along the curve".
- Items 8 and 9 showed only one type of externality each, under general titles. Now named "Negative production externality" and "Positive consumption externality" in the notes and the recap. (A negative consumption externality has SB below PB; a positive production externality has SC below PC.)
- "Qo: best output" is now "Qo: socially optimal".
- The recap diagrams now carry their curve labels (D, S, SC, PB and so on), so a screenshot can be read on its own.

Checked and unchanged: every shift direction, the old and new equilibria, the max price shortage and min price surplus, the tax and subsidy price order and gap, the welfare-loss triangles. `verify_markets.py` still passes. Item 6 is drawn as a specific tax, the syllabus 3.2.1 case.

Sync is a median 16 ms, with 87% within 50 ms. -14.0 LUFS.
