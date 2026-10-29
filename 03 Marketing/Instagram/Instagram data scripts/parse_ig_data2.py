import json

with open("ig_data.json") as f:
    data = json.load(f)

def find_parent_with_key(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            return obj
        for k, v in obj.items():
            result = find_parent_with_key(v, key)
            if result is not None:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = find_parent_with_key(item, key)
            if result is not None:
                return result
    return None

profile = find_parent_with_key(data, "biography")
if profile:
    print(f"Username: {profile.get('username')}")
    print(f"Full Name: {profile.get('full_name')}")
    print(f"Bio: {repr(profile.get('biography'))}")
    print(f"External URL: {profile.get('external_url')}")
    print(f"Followers: {profile.get('edge_followed_by', {}).get('count')}")
    print(f"Posts Count: {profile.get('edge_owner_to_timeline_media', {}).get('count')}")
    
    timeline = profile.get("edge_owner_to_timeline_media", {})
    edges = timeline.get("edges", [])
    print(f"\nFound {len(edges)} posts:")
    for edge in edges:
        node = edge.get("node", {})
        typename = node.get("__typename")
        likes = node.get("edge_liked_by", {}).get("count", node.get("edge_media_preview_like", {}).get("count"))
        comments = node.get("edge_media_to_comment", {}).get("count")
        video_views = node.get("video_view_count")
        captions = node.get("edge_media_to_caption", {}).get("edges", [])
        caption = captions[0].get("node", {}).get("text", "") if captions else ""
        caption_head = caption.replace('\n', ' ')[:60]
        print(f"- {typename} | Likes: {likes} | Comments: {comments} | Views: {video_views} | Caption: {caption_head}...")
else:
    print("No biography found.")
