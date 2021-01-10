import requests
from bs4 import BeautifulSoup as soup
import time
import random
import pandas as pd
import openpyxl

def state_scrape(url):
    page = requests.get(url)
    soup_object = soup(page.content, 'html.parser')

    #print(soup_object.prettify())

    tr_list = soup_object.find_all('tr')
    state = tr_list[3]
    fields = state.find_all('td')

    latitude = fields[4].get_text()
    longitude = fields[5].get_text()

    return latitude, longitude

def fifty_states():
    part1 = 'https://www.geonames.org/search.html?q='
    part3 = '&country='
    list_of_states_norm = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                           'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                           'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                           'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
                           'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                           'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
                           'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
                           'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    list_of_states_form = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                      'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
                      'Nevada', 'New+Hampshire', 'New+Jersey', 'New+Mexico', 'New+York', 'North+Carolina', 'North+Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode+Island',
                           'South+Carolina', 'South+Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West+Virginia', 'Wisconsin', 'Wyoming']

    result = []
    for ind, state in enumerate(list_of_states_form):
        url = part1 + state + part3
        lat, long = state_scrape(url)
        time.sleep(random.randint(1, 5))
        state_entry = [list_of_states_norm[ind], lat, long]
        result.append(state_entry)

    df = pd.DataFrame(result, columns = ['State', 'Latitude',' Longitude'])

    df.to_excel("states_coordinates.xlsx", index = False)

    print("Successfully created Excel File")

fifty_states()