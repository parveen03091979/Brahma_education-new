import requests
def post_to_facebook(page_id, access_token, message, video_url):
    url = f"https://graph.facebook.com/{page_id}/videos"
    data = {"description": message, "file_url": video_url, "access_token": access_token}
    return requests.post(url, data=data).json()
def post_to_instagram(access_token, insta_user_id, video_url, caption):
    url = f"https://graph.facebook.com/v19.0/{insta_user_id}/media"
    data = {"media_type": "REELS", "video_url": video_url, "caption": caption, "access_token": access_token}
    container = requests.post(url, data=data).json()
    publish_url = f"https://graph.facebook.com/v19.0/{insta_user_id}/media_publish"
    return requests.post(publish_url, data={"creation_id": container.get('id'), "access_token": access_token}).json()