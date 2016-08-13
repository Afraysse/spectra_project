import os

# YouTube Data API setup ######################################################

#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.environ["YOUTUBE_DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

###############################################################################


def youtube_search(regioncode):
    """Get the top 10 most popular YouTube videos for a specific region."""

    # Set up and make call to YouTube API
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    response = youtube.videos().list(part='snippet, statistics',
                                     regionCode=regioncode,
                                     hl="en",
                                     maxResults=10,
                                     chart="mostPopular"
                                     ).execute()

    # Extract information for each video and make a list of video objects
    videos = []

    for video in response.get("items", []):
        vid = {}

        vid["title"] = video["snippet"]["title"]
        vid["description"] = video["snippet"]["description"]
        vid["thumbnail_url"] = video["snippet"]["thumbnails"]["default"]["url"]
        vid["viewcount"] = video["statistics"]["viewCount"]
        vid["likecount"] = video["statistics"]["likeCount"]
        vid["dislikecount"] = video["statistics"]["dislikeCount"]

        videos.append(vid)

    return videos
