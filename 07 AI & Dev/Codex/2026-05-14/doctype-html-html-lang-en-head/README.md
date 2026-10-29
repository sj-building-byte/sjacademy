# SJ Academy Quiz Tool

This version keeps the quiz interface in `index.html` and stores question data in `questions.json`.

## Files

- `index.html` - frontend only
- `questions.json` - editable question bank
- `tools/extract-question-bank.mjs` - optional converter for your original hardcoded HTML file

## Add Or Edit Questions

Edit `questions.json`. Each chapter looks like this:

```json
{
  "id": 1,
  "title": "Enterprise",
  "unit": 1,
  "level": "AS",
  "questions": [
    {
      "q": "Question text",
      "opts": ["Option A", "Option B", "Option C", "Option D"],
      "ans": 1,
      "explain": "Explanation shown after answering."
    }
  ]
}
```

`ans` is zero-based:

- `0` = first option
- `1` = second option
- `2` = third option
- `3` = fourth option

## Important

Because the page uses `fetch('questions.json')`, open it through a web server rather than by double-clicking the HTML file.

For local testing, run:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Convert The Full Original HTML

If you have the original hardcoded file saved locally, put it in this folder as `original.html`, then run:

```bash
node tools/extract-question-bank.mjs original.html questions.json
```

That will replace `questions.json` with the full extracted question bank while keeping `index.html` clean.
