import requests
import cloudscraper
from bs4 import BeautifulSoup

artist_names = []

base_url = "https://www.moma.org/artists"
pages = [1,2]
for page in pages:
    params = {"exhibition_id": 5224, "page":page}

    options = {'page': 1, 'perpage': 83}
    scraper = cloudscraper.create_scraper()
    page = scraper.get(base_url, params=params)

    soup = BeautifulSoup(page.text, 'html.parser')

    artists_container = soup.find('section', {'data-grid': 'artists'})
    artists = artists_container.find_all('li')
    for artist in artists:
        artist_names.append(artist.find('h3').text.strip())
print(artist_names)
print(len(artist_names))

    # all_artist = artists_container.find('a', {'data-gtm': 'clicks on artist'})
    # for artist in all_artist:
    #   link = artist.find('href')
    #   all_artist_hrefs.append(link)
    # print(all_artist_hrefs)