import instaloader
import json
from datetime import datetime

L = instaloader.Instaloader()

# Load profile
profile = instaloader.Profile.from_username(L.context, "sjacademypk")

data = {
    "username": profile.username,
    "full_name": profile.full_name,
    "biography": profile.biography,
    "external_url": profile.external_url,
    "followers": profile.followers,
    "followees": profile.followees,
    "mediacount": profile.mediacount,
    "is_verified": profile.is_verified,
    "profile_pic_url": profile.profile_pic_url,
    "posts": []
}

count = 0
for post in profile.get_posts():
    if count >= 30:
        break
    
    post_data = {
        "date": post.date.isoformat(),
        "typename": post.typename,  # GraphImage, GraphVideo, GraphSidecar
        "caption": post.caption,
        "likes": post.likes,
        "comments": post.comments,
        "video_view_count": post.video_view_count,
        "is_video": post.is_video,
    }
    data["posts"].append(post_data)
    count += 1

with open("sjacademy_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data fetched successfully!")
