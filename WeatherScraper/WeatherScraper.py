'''
Project: Scrape and search the web for the Zip Codes of a city and search the real-time
temperature at any given moment. Then display the temperature over a city map 
using longitude and latitude.
'''

import requests
from bs4 import BeautifulSoup
import GoogleWeatherSearch
import time
import GoogleGeoCode

city = input("Please enter the city you'd like to see the temperatures of: ")
state = input("Please enter the two letter abbreviation of the state the city is located in: ")


try:
    city = city.replace(" ", '-')
    
except:
    
    city = city;

tempByZip = {};
counter = 0;
ocounter = 0;
t0 = time.time()

page = requests.get('https://www.zip-codes.com/city/' + state + '-' + city + '.asp') #This URL contains all Zip Codes for the city.

soup = BeautifulSoup(page.text, 'html.parser')

raw_table_data = soup.find(id='tblZIP') #Finding the table in the HTML code for the previous URL
raw_table_data_list = raw_table_data.find_all('a')

for list_items in raw_table_data_list:
    names = list_items.contents[0] #These individual names are the rows in the table
    if names.find('ZIP Code') == 0:
        zipcode = names[9::] #Grabbing just the Zip Code
        try:
            temperature = GoogleWeatherSearch.google_search(zipcode) #Using a GoogleWeatherSearch function from another imported file
            tempByZip[zipcode] = temperature
            
        except: #This checks if google is rejecting too often
            counter += 1;
            if counter == 5:
                break
                print("Google is rejecting too often")
            else:
                continue

print(tempByZip)

t1 = time.time()

print(t1-t0);
