#!/usr/bin/python

import os
import json
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.environ["YOUTUBE_DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(regioncode):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the videos.list method to retrieve location details for each video.
    response = youtube.videos().list(part='snippet, statistics',
                                           regionCode=regioncode,
                                           hl="en",
                                           maxResults=10,
                                           chart="mostPopular"
                                           ).execute()

    video_objs = response["items"]

    videos = []

    for video in video_objs:
        vid = {}

        vid["title"] = video["snippet"]["title"]
        vid["description"] = video["snippet"]["description"]
        vid["thumbnail_url"] = video["snippet"]["thumbnails"]["default"]["url"]
        vid["channel"] = video["snippet"]["channelTitle"]
        vid["viewcount"] = video["statistics"]["viewCount"]
        # vid["likecount"] = video["statistics"]["likeCount"]
        # vid["dislikecount"] = video["statistics"]["dislikeCount"]

        videos.append(vid)

    return videos




