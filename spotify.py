
import os
import spotipy
import spotipy.oauth2 as oauth2
import json

# https://github.com/plamere/spotipy/issues/194#issuecomment-317192954
credentials = oauth2.SpotifyClientCredentials(
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"])

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

name = "blade runner tears in the rain"
results = spotify.search(q='track:' + name, type='track')


from pprint import pprint

track_id = results["tracks"]["items"][0]["id"]
pprint(track_id)


track = spotify.track(track_id)


audio_analysis = spotify.audio_analysis(track_id)
audio_features = spotify.audio_features(track_id)



pprint(audio_features)
# print(json.dumps(audio_analysis))