import requests
from bs4 import BeautifulSoup
from models import Medications

# !!! run this code once to scrape and save the data to the medications database

# instantiate the Medications class (database). See models.py
db = Medications()

# initialize medications list for top side effect searches on Drugs.com
drugs = [
    'adderall','amlodipine', 'brilinta', 'buspirone', 'chloroquine',
    'cyclobenzaprine', 'cymbalta', 'doxycycline', 'dupixent', 'entresto', 
    'entyvio', 'farxiga', 'fluoxetine', 'gabapentin', 'gilenya', 
    'humira', 'hydroxychloroquine', 'imbruvica', 'invokana', 
    'januvia', 'jardiance', 'kevzara', 'lexapro', 'lisinopril',
    'losartan', 'meloxicam', 'metformin', 'methadone', 'methotrexate', 
    'metoprolol', 'onpattro', 'otezla', 'ozempic', 'prednisone', 
    'rybelsus', 'sertraline', 'tamiflu', 'tramadol', 'trazodone', 
    'wellbutrin', 'xanax', 'zoloft'
]


def scrape_side_effects(tag):
    """
    Scrapes the common side effets from Drugs.com for a given medication name and saves the 
    drug name and its side effects to medications.db
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    url = f'https://www.drugs.com/sfx/{tag}-side-effects.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    side_effects = ""

    # find all unordered lists from the HTML and store them in a list
    uls = soup.find_all('ul') 

    # loop through all the uls to parse/clean the scraped text and add to the side_effects list
    for ul in uls[4:6]:
        for li in ul.find_all('li'):
            side_effects += li.text.strip('\n') + "; " # clean text and add to to side_effects list
        
    # insert & commit the the data to the database
    db_entry = (str(tag), side_effects) # creates a drug name & side effects database entry using a tuple
    db.insert(db_entry) # calls the insert() function from module to insert/commit the entry to the database


# iterate through the drugs list and insert drug and side effects in the database by calling the scrape_side_effects() function
for drug in drugs:
    scrape_side_effects(drug)

print('complete')
