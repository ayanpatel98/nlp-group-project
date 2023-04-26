# this file is for obtaining a list of 50 video ids from Youtube-Data-API

# https://developers.google.com/youtube/v3/docs/videos/list

import requests

api_key = "AIzaSyBA8PtncHpYv5H1RxAU0F3FnvhEg1F0-Rk"

# Set the API endpoint and parameters
url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "id","contentDetails"
    "channelId": "27",
    "maxResults": 500,
    "key": api_key
}

# Make the API request and retrieve the video IDs
response = requests.get(url, params=params).json()
video_ids = [item["id"]["videoId"] for item in response["items"]]

# Print the list of video IDs
print("IDS:",video_ids)