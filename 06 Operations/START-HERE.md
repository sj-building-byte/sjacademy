# Operations: start here

Most operations data lives in Google Sheets, not in this folder. Reach them through the Google Sheets connector:
- Lead Tracker (Leads, Demo queue, Enrolled students; Apps Script automation across nine tabs).
- Finance sheet: being rebuilt (see "Finance tracker" below).
- Class timetable sheet: feeds the website timetable and the homepage class finder.
- "SJ Academy - Page Rebuild & Marketing Tracker".

## Finance tracker (rebuilt 4 November 2026)

Built in "Copy of SJ Business Sheet - 2026" (sheet ID `17wrBrhR-M_RQ1EpOaqYmla0sT5r8z1pgaBSo-U2grG8`). The original "SJ Business Sheet - 2026" is untouched. Once this copy is signed off, it becomes the one finance file.

Financial year: June to May. Amounts in PKR.

Tabs:
- `Dashboard`: pick a month in the yellow cell. Shows fees, teachers' share, running costs, profit, drawings, month by month for the year, costs by category, teacher pay owed against paid, and enrolled students with no fee entered.
- `Fees in`: one row per payment (Date, Student, Class, Month, Amount, Note). Teacher and teacher share fill in by themselves.
- `Money out`: one row per payment (Date, Month, Category, Paid to, Amount, Note). Teacher pay goes here with category "Teacher pay"; partner withdrawals go under "Partner drawings", not as a cost.
- `Teachers`: one row per class with its teacher and share %. Yellow rows still need confirming.
- `Lists`: dropdown sources. Column A pulls students from the Leads Tracker with IMPORTRANGE (needs a one-time "Allow access" click).
- Every tab starting with `Old`: the previous sheet, kept for reference. Nothing new goes there.

How profit is worked out: fees minus the teachers' share of those fees minus running costs. Teacher pay rows in Money out only feed "Paid" and "Still due".

June to November 2026 were brought in as monthly totals per class from Old Revenue and Old Expenses 2026 and match the old totals. November was partial on 4 November.

Next:
- Confirm the yellow rows in `Teachers` (Biology practicals share, Sir Basharat, Sir Khawar, Teachwink, Miss Zahida Maheen, the A2 Physics teacher's name, Miss Asmat and Miss Azmat).
- Check that the October teacher pay rows were actually paid.
- At switchover, re-import November from the original sheet, then stop using the old tabs.
- Later: have the Leads Tracker's fee ticks read from `Fees in` instead of being ticked by hand.

## What is here
- `Finance/`: bill template, and an empty git repo from the earlier finance sheet work.
- `Project Manager tool/`: a small internal project manager web page.

Hiring documents, offer letters and ID scans are in `SJ Academy - Private/Team & Hiring`, not here.
