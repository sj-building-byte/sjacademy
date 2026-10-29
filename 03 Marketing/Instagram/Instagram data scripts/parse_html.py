import re
import json

with open("ig_page.html", "r") as f:
    content = f.read()

# Try to find user profile info
profile_match = re.search(r'("biography":".*?","biography_with_entities":.*?})', content)
if profile_match:
    print("Found profile info!")
    try:
        # Wrap in brackets to make it a valid JSON or just extract fields using regex
        bio_match = re.search(r'"biography":"([^"]+)"', content)
        if bio_match:
            print(f"Bio: {bio_match.group(1)}")
            
        link_match = re.search(r'"external_url":"([^"]+)"', content)
        if link_match:
            print(f"Link: {link_match.group(1)}")
            
    except Exception as e:
        print(f"Error parsing json: {e}")

# Try to extract posts
posts_matches = re.finditer(r'("node":\s*\{"__typename":"GraphImage".*?\})', content)
posts = []
for p in posts_matches:
    print("Found post!")

# Usually posts are under edge_owner_to_timeline_media or something similar
timeline_match = re.search(r'("edge_owner_to_timeline_media":.*?)\}\}\}', content)
if timeline_match:
    print("Found timeline media")
    
