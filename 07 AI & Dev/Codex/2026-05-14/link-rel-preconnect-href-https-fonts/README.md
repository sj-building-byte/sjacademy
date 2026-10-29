# Google Sheet timetable setup

Use [google-sheet-timetable.html](/Users/sunyyanjunaid/Documents/Codex/2026-05-14/link-rel-preconnect-href-https-fonts/google-sheet-timetable.html) as the replacement for the current embedded timetable block.

## 1. Create one spreadsheet with four tabs

Name the tabs exactly:

1. `O Level`
2. `AS Level`
3. `A2 Level`
4. `Lab Practical`

## 2. Use this layout inside each tab

The first row is the header row. The first column must be `Time`. Every remaining column becomes a timetable day.

```text
Time | Mon | Tue | Wed | Thu | Fri | Sat
3:00 - 4:00 PM | Eng || Urdu online | Phys / Biz || Urdu + Isl online | Eng || Urdu online | Phys / Biz || Urdu + Isl online |  |
4:00 - 5:00 PM | Maths | Chem / Econ || Pak St + Phys online | Maths | Chem / Econ || Pak St + Phys online | Maths |
```

Rules:

- Put the main class name first.
- Add secondary text after `||`.
- Leave a cell empty to show the dash state.
- Use only the days you need in each tab. `Lab Practical` can be `Wed | Thu | Fri | Sat | Sun`.

## 3. Make the sheet readable by the website

The timetable uses Google’s spreadsheet query interface. The spreadsheet must be viewable publicly or published in a way your website visitors can read.

## 4. Add your spreadsheet ID

In [google-sheet-timetable.html](/Users/sunyyanjunaid/Documents/Codex/2026-05-14/link-rel-preconnect-href-https-fonts/google-sheet-timetable.html), replace:

```js
spreadsheetId: 'PASTE_GOOGLE_SHEET_ID_HERE'
```

with the ID from your Google Sheets URL.

## 5. If your tab names differ

Change the `sheetName` values in the `CONFIG.levels` object near the bottom of the file.

Once connected, edits made in Google Sheets become the source of truth for the live timetable. The page re-queries the active tab every 5 minutes and also fetches fresh data whenever someone switches tabs. Google may still introduce a short delay before newly edited sheet data appears publicly.
