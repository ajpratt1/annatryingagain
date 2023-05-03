import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import csv 
hrefs = []

url = 'https://nuforc.org/webreports/ndxevent.html'
base_url = 'https://nuforc.org/webreports'
scraper = cloudscraper.create_scraper()
page = scraper.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
all_rows = soup.find_all('tr')
for row in all_rows:
    anchor = row.find('a')
    if anchor is not None:
        hrefs.append(anchor["href"])

#remove last link in the list beause it's not usable data 
hrefs.pop()

occurences = []

# for href in hrefs:
for href in hrefs:
    full_url = f'{base_url}/{href}'
    scraper = cloudscraper.create_scraper()
    page = scraper.get(full_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        occurence = {
            "timestamp": cells[0].text.strip(),
            "city": cells[1].text.strip() ,
            "state": cells[2].text.strip(),
            "country": cells[3].text.strip(),
            "Shape": cells[4].text.strip(),
            "duration": cells[5].text.strip(),
            "summary": cells[6].text.strip(),
            "posted": cells[7].text.strip(),
            "images": cells[8].text.strip(),
        }
        if occurence['country'] == "USA":
            occurences.append(occurence)

with open('occurences.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'city', 'state', 'country', 'Shape', 'duration', 'summary', 'posted', 'images']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for occurence in occurences:
        writer.writerow(occurence)
print("finished")

date_find = soup.find('p')
dates = soup.find_all('td')