import re
import json

with open("ig_page.html", "r") as f:
    content = f.read()

# Look for large JSON blobs
for match in re.finditer(r'<script type="application/json" data-sjs>([^<]+)</script>', content):
    print("Found JSON blob of length:", len(match.group(1)))

for match in re.finditer(r'<script type="application/json" data-requireidentity="[^"]*">([^<]+)</script>', content):
    print("Found JSON blob of length:", len(match.group(1)))
