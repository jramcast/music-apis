
import os
import spotipy
import spotipy.oauth2 as oauth2
import json
from pprint import pprint


# https://github.com/plamere/spotipy/issues/194#issuecomment-317192954
credentials = oauth2.SpotifyClientCredentials(
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"])

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


results = spotify.user

pprint(results)


