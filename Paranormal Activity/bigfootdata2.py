from bs4 import BeautifulSoup
from datetime import datetime as dt #! <==
import cloudscraper
import csv

#! EXTRA STUFF (Not necessary to program functionality) =========
header_set = [] # value for storing our headers (during discovery)
# Creates list of unique dict keys to use as headers for csv file
def find_headers(data):
    keys = data.keys()
    for key in keys:
        if key not in header_set:
            header_set.append(key)

# Re-prints on the last line
def back_print(string):
    print(string, end='\r')

# Class for logging info in terminal
class Logger:
    info = 'INFO'
    err = 'ERROR'
    def __init__(self, enabled):
        self.enabled = enabled

    def log(self, msg, level='DEBUG'):
        if self.enabled:
            print(f'level: "{level}" :: "{dt.now()}" :: msg: "{msg}"')

# Class for displaying spinner in terminal (useful for showing progress)
class Spinner:
    icons = ['.', 'o', 'O', '0']
    def __init__(self):
        self.current = 0

    def show(self):
        back_print(self.icons[self.current])
        self.next_icon()
    
    def next_icon(self):
        if self.current >= len(self.icons) - 1:
            self.current = 0
        else:
            self.current += 1
#! ==============================================================


#* NOTES ==================================
# Anything that is marked with this comment:
    #! <==
# can be removed without affecting the functionality of the program.
# I recommend either leaving them or removing all of them to avoid issues. 

#* VARIABLES ==================================
enable_logs = True # Change to True if you want to print terminal log statements

#? This was used initially to generate the header set values below.
#? No need to run it again, unless you really want to.
enable_find_headers = False

# Header values for csv file
headers = {'YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION DETAILS', 
           'NEAREST TOWN', 'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED', 'OTHER WITNESSES', 
           'OTHER STORIES', 'TIME AND CONDITIONS', 'ENVIRONMENT', 'DATE', 'A & G References'}

spinner = Spinner() #! <==
logger = Logger(enable_logs) #! <==

state_hrefs = []    # state hrefs
county_hrefs = []   # county hrefs
report_hrefs = []   # report hrefs
sighting_data = []  # sighting data

base_url = 'https://www.bfro.net'
subdir = 'gdb'  # target subdirectory

#* MAIN PROGRAM ==================================
start = dt.now() # Start time of program

#* Scrape for states
scraper = cloudscraper.create_scraper()
page = scraper.get(f'{base_url}/{subdir}')
soup = BeautifulSoup(page.text, 'html.parser')
# Remove limit if we want to get data from all tables (Canada + International)
tables = soup.find_all('table', {'class': 'countytbl'}, limit=2)
for table in tables:
    states = table.find_all('a')
    for state in states:
        state_hrefs.append(state['href'])

#* Scrape for counties (boroughs in AK) in each state
for sh in state_hrefs:
    page = scraper.get(f'{base_url}{sh}')
    soup = BeautifulSoup(page.text, 'html.parser')
    counties = soup.find_all('td', {'class': 'cs'})
    for county in counties:
        link = county.find('a')
        if link is not None:
            county_hrefs.append(link["href"])

#* Scrape for reports in each county
for ch in county_hrefs:
    page = scraper.get(f'{base_url}/{subdir}/{ch}')
    soup = BeautifulSoup(page.text, 'html.parser')
    reports = soup.find('ul').find_all('li', {'class': 'spaced'})
    for report in reports:
        link = report.find('a')
        if link is not None:
            report_hrefs.append(link["href"])

#* Scrape for sightings in each report; this is where majority data is pulled
for rh in report_hrefs:
    page = scraper.get(f'{base_url}/{subdir}/{rh}')
    soup = BeautifulSoup(page.text, 'html.parser')
    fields = soup.find_all('p')
    # Create dict to contain sighting data in KV format
    data = {}
    for field in fields:
        element = field.find('span', {'class': 'field'})
        if element and ('article' not in element):
            key = element.text.strip().replace(':', '')
            value = element.parent.text.replace(element.text, '').strip()
            data[key] = value
            if enable_find_headers: #! <==
                find_headers(data) #! <==

    sighting_data.append(data)
print("success!")

# #* Loop through sighting_data and create CSV file
# if 1 == 1:
#     # Open the CSV file in write mode
#     with open('bigfoot_sightings_US.csv', 'w', newline='', encoding='utf-8') as file:
#         # Create a CSV writer object
#         writer = csv.DictWriter(file, headers)
#         # Write the header row
#         writer.writeheader()
#         # Write the data to the CSV file
#         writer.writerows(sighting_data)
#         spinner.show()

