import requests
import json
import sys

# pip install requests - 3rd party packages

# itunes - https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI
# /UnderstandingSearchResults.html#//apple_ref/doc/uid/TP40017632-CH8-SW1

if len(sys.argv) != 3:
    sys.exit("Usage Example: python api_basics.py dynamite+bts 1")

# song list with track price
response = requests.get("https://itunes.apple.com/search?entity=song&limit=15&term=" + sys.argv[1])
o_json = response.json()
for result in o_json['results']:
    print(result["trackName"], result["trackPrice"], sep="\t ")

# Query limited list of song by Artist by using the ArtistId and Entity for song
response = requests.get("https://itunes.apple.com/lookup?id=883131348&entity=song&limit=" + sys.argv[2])
o_json = response.json()
# json package for readable format the returned dictionary
print(json.dumps(o_json, indent=2))