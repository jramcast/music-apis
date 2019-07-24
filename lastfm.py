import os
import pylast
from pprint import pprint


lastfm = pylast.LastFMNetwork(
    api_key=os.environ["LASTFM_API_KEY"],
    api_secret=os.environ["LASTFM_API_SECRET"]
)

# Now you can use that object everywhere
user = lastfm.get_user("jimmydj2000")
print(user)


loved_tracks = user.get_loved_tracks(limit=5)
print("loved tracks count", len(loved_tracks))

print("LOVED TRACKS")
for loved in loved_tracks:
    pprint(loved.track.get_mbid())
    print(loved.track.artist, loved.track.title)
    print('************************')

print("TOP TAGS")
print([(each.item.name, each.weight) for each in user.get_top_tags()])
