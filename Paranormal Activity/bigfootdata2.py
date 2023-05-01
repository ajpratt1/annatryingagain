from bs4 import BeautifulSoup
import cloudscraper
import csv

header_set = [] 

def find_headers(data):
    keys = data.keys()
    for key in keys:
        if key not in header_set:
            header_set.append(key)

def back_print(string):
    print(string, end='\r')

headers = {'YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION DETAILS', 
           'NEAREST TOWN', 'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED', 'OTHER WITNESSES', 
           'OTHER STORIES', 'TIME AND CONDITIONS', 'ENVIRONMENT', 'DATE', 'A & G References'}


state_hrefs = []    
county_hrefs = []   
report_hrefs = []  
sighting_data = []  

base_url = 'https://www.bfro.net'
subdir = 'gdb'  


scraper = cloudscraper.create_scraper()
page = scraper.get(f'{base_url}/{subdir}')
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table', {'class': 'countytbl'}, limit=2)
for table in tables:
    states = table.find_all('a')
    for state in states:
        state_hrefs.append(state['href'])

for sh in state_hrefs:
    page = scraper.get(f'{base_url}{sh}')
    soup = BeautifulSoup(page.text, 'html.parser')
    counties = soup.find_all('td', {'class': 'cs'})
    for county in counties:
        link = county.find('a')
        if link is not None:
            county_hrefs.append(link["href"])

for ch in county_hrefs:
    page = scraper.get(f'{base_url}/{subdir}/{ch}')
    soup = BeautifulSoup(page.text, 'html.parser')
    reports = soup.find('ul').find_all('li', {'class': 'spaced'})
    for report in reports:
        link = report.find('a')
        if link is not None:
            report_hrefs.append(link["href"])

for rh in report_hrefs:
    page = scraper.get(f'{base_url}/{subdir}/{rh}')
    soup = BeautifulSoup(page.text, 'html.parser')
    fields = soup.find_all('p')
    data = {}
    for field in fields:
        element = field.find('span', {'class': 'field'})
        if element and ('article' not in element):
            key = element.text.strip().replace(':', '')
            value = element.parent.text.replace(element.text, '').strip()
            data[key] = value

    sighting_data.append(data)
print("success!")

if 1 == 1:
    with open('bigfoot_sightings_US.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(sighting_data)

