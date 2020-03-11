import requests
from bs4 import BeautifulSoup
import GoogleSearch
from time import sleep
import pandas
import csv

tempByZip = {};
counter = 0;

page = requests.get('https://www.zip-codes.com/state/ca.asp')

soup = BeautifulSoup(page.text, 'html.parser')

raw_table_data = soup.find('table')
raw_table_data_list = raw_table_data.find_all('a')

for list_items in raw_table_data_list:
    names = list_items.contents[0]
    if names.find('ZIP Code') == 0:
        zipcode = names[9::]
        try:
            temperature = GoogleSearch.google_search(zipcode)
            tempByZip[zipcode] = temperature
            sleep(5)
        except:
            print("connection refused by server")
            counter = counter + 1;
            print(counter)
            if counter == 5:
                break
            else:
                continue
        
