import requests
from bs4 import BeautifulSoup
import time

def get_count():
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=10.82,7.52,72.15,76.66&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1"

    # Request with fake header, otherwise you will get an 403 HTTP error
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Parse the JSON
    data = r.json()
    counter = 0

    # Iterate over the elements to get the number of visible  flights in the region
    for element in data["stats"]["visible"]:
        counter += data["stats"]["visible"][element]

    return counter

while True:
    print(get_count())
    time.sleep(5)