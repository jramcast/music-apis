# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from pprint import pprint

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]


def main():
    # # Disable OAuthlib's HTTPS verification when running locally.
    # # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # client_secrets_file = "youtube_oauth_secret.json"

    # Get token from: https://console.developers.google.com/apis/credentials
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=os.environ["YOUTUBE_API_KEY"])

    request = youtube.search().list(
        q="Vangelis tears in the rain",
        part="snippet"
    )
    response = request.execute()

    print("VIDEO ---------")
    pprint(response["items"][0])

    video_id = response["items"][0]["id"]["videoId"]

    print("COMMENTS THREAD -------------")
    request = youtube.commentThreads().list(
        videoId=video_id,
        part="snippet"
    )
    response = request.execute()
    pprint(response["items"])

if __name__ == "__main__":
    main()