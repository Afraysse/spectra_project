#!/usr/bin/python

import os
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
    video_response = youtube.videos().list(part='snippet',
                                           regionCode=regioncode,
                                           hl="en",
                                           maxResults=10,
                                           chart="mostPopular"
                                           ).execute()

    print video_response

    # videos = []

    # # Add each result to the list, and then display the list of matching videos.
    # for video_result in video_response.get("items", []):
    #   videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
    #                           video_result["recordingDetails"]["location"]["latitude"],
    #                           video_result["recordingDetails"]["location"]["longitude"]))

    # print "Videos:\n", "\n".join(videos), "\n"




