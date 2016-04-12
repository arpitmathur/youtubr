#!/usr/bin/python

import json
import httplib2
import os
import sys
import sys
sys.path.insert(1, '/Library/Python/2.7/site-packages')
import isodate
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }}

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

categories = {};

categories["1"] = "Film & Animation"
categories["2"] = "Autos & Vehicles"
categories["10"] = "Music"
categories["15"] = "Pets & Animals"
categories["17"] = "Sports"
categories["18"] = "Short Movies"
categories["19"] = "Travel & Events"
categories["20"] = "Gaming"
categories["21"] = "Videoblogging"
categories["23"] = "Comedy"
categories["24"] = "Entertainment"
categories["25"] = "News & Politics"
categories["26"] = "Howto & Style"
categories["27"] = "Education"
categories["28"] = "Science & Technology"
categories["29"] = "Nonprofits & Activism"
categories["30"] = "Movies"
categories["31"] = "Anime/Animation"
categories["32"] = "Action/Adventure"
categories["33"] = "Classics"
categories["34"] = "Comedy"
categories["35"] = "Documentary"
categories["36"] = "Drama"
categories["37"] = "Family"
categories["38"] = "Foreign"
categories["39"] = "Horror"
categories["40"] = "Sci-Fi/Fantasy"
categories["41"] = "Thriller"
categories["42"] = "Shorts"
categories["43"] = "Shows"
categories["44"] = "Trailers"


with open('watch-history.json','r') as data_file:
        data = json.load(data_file)


videoID = []

for num in data:
    temp = str(num['snippet']['resourceId']['videoId'])
    videoID.append(temp)




flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  message=MISSING_CLIENT_SECRETS_MESSAGE,
  scope=YOUTUBE_READONLY_SCOPE)

storage = Storage("%s-oauth2.json" % sys.argv[0])
credentials = storage.get()

if credentials is None or credentials.invalid:
  flags = argparser.parse_args()
  credentials = run_flow(flow, storage, flags)

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  http=credentials.authorize(httplib2.Http()))

# Retrieve the contentDetails part of the channel resource for the
# authenticated user's channel.
# video_response = youtube.videos().list(
#     id='5L-RMaHdafA',
#     part='snippet, contentDetails'
#     ).execute()
# print video_response

myData = []
counter = 0
newFile = open('MyVideoData.json','w')
newFile.write('{')
newFile.write('"data": [')
for value in videoID:
    video_response = youtube.videos().list(
    id=value,
    part='snippet, contentDetails'
    ).execute()
    # print video_response
    # video_response.encode('ascii', 'ignore')

    for video_result in video_response.get("items", []):

        channelId = video_result["snippet"]["channelId"]
        results = youtube.channels().list(
            part="snippet",
            id=channelId).execute()
        for chanel in results.get("items", []):
            channel =  chanel["snippet"]["title"]
        category = int((video_result["snippet"]["categoryId"]))
        title = ((video_result["snippet"]["title"]))
        title = title.encode('utf-8')
        title = title.replace('"','\'')
        channel = channel.encode('utf-8')
        channel = channel.replace('"','\'')

        thumnailUrl = video_result["snippet"]["thumbnails"]["default"]["url"]
        thumnailUrl = thumnailUrl.encode('utf-8')

        duration = video_result['contentDetails']['duration']
        dur=isodate.parse_duration(duration)
        tuple = ((title),categories.get(str(category)),dur.total_seconds(),channel,thumnailUrl)
        myData.append(tuple)
    counter +=1
    if counter == 2000:
        break
temp = 0
for x in myData:
        newFile.write('{')
        newFile.write('"title":' + '"' + x[0] + '"' + ',')
        newFile.write('"Channel":' + '"' + xx[3] + '"' + ',')
        if tuple[1] is not None:
            newFile.write('"category":' + '"' + x[1] + '"'+ ',')
        else:
            newFile.write('"category":' + '" N/A"'+ ',')
        newFile.write('"Thumbnail Url":' + '"' + x[4] + '"' + ',')
        newFile.write('"duration":' + '"' + str(x[2]) + '"' + ',')
        newFile.write('"Number":' + '"' + str(temp+counter) + '"')

        newFile.write('},')
        temp -=1


newFile.write(']}')
