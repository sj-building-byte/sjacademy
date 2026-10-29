"""Builds ../index.html from index.template and captions.json (word timings from the voiceover)."""
import json
from pathlib import Path
here = Path(__file__).parent
t = (here / "index.template").read_text()
caps = json.loads((here / "captions.json").read_text())
(here.parent / "index.html").write_text(t.replace("{{CAPS}}", json.dumps(caps)))
print("built index.html with", len(caps), "caption phrases")
