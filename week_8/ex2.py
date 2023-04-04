import requests
import cloudscraper
from bs4 import BeautifulSoup

artist_hrefs = []
artist_dict = {}

url = "http://www.moma.org"
base_url = "https://www.moma.org/artists"
pages = [1,2]
for page in pages:
    params = {"exhibition_id": 5224, "page":page}

    options = {'page': 1, 'perpage': 83}
    scraper = cloudscraper.create_scraper()
    page = scraper.get(base_url, params=params)

    soup = BeautifulSoup(page.text, 'html.parser')

    artists_container = soup.find('section', {'data-grid': 'artists'})
    artists = artists_container.find_all("li")
    
    for artist in artists:
        link = artist.find('a')
        href = link['href']
        artist_hrefs.append(href)
for i in range(len(artist_hrefs)):
    artist_url = (f'{url}{artist_hrefs[i]}')
    artist_page = scraper.get(artist_url)
    soup = BeautifulSoup(artist_page.text, 'html.parser')
    name_container = soup.find('h1')
    name = name_container.find('span').text
    bio_container = soup.find('h2').find('span')
    bio = None
    if bio_container is not None:
        bio = bio_container.text
    works_container = soup.find('h2', {'id': 'works'})
    works = None
    if works_container is not None:
        works = works_container.find_parent('section').find('p').text.strip()
    artist_dict[name] = {'bio': bio, 'works': works}
print(artist_dict)