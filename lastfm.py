import os
import pylast
from pprint import pprint


lastfm = pylast.LastFMNetwork(
    api_key=os.environ["LASTFM_API_KEY"],
    api_secret=os.environ["LASTFM_API_SECRET"],
    # username=os.environ["LASTFM_USERNAME"],
    # password_hash=pylast.md5(os.environ["LASTFM_PASSWORD"]),
)

# Now you can use that object everywhere
user = lastfm.get_user("jimmydj2000")
print(user)

print("TRack")
track = lastfm.get_track("Vangelis", "Tears in the rain")

print(track)
print(track.get_wiki_summary())


loved_tracks = user.get_loved_tracks(limit=5)
print("loved tracks count", len(loved_tracks))

print("LOVED TRACKS")
for loved in loved_tracks:
    pprint(loved.track.get_mbid())
    print(loved.track.artist, loved.track.title)
    print('************************')

print("TOP TAGS")
print([(each.item.name, each.weight) for each in user.get_top_tags()])
