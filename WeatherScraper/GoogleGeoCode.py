# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:13:18 2020

@author: Clayton Williams

simple api call to fetch data from Google geocoding api in json format.
"""

import requests
import json



def get_coordinates(userzip):
    BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    API_KEY = 'AIzaSyAhkEuSPYE0P8WMbnt0bI8YVJZvf7IMvjw'
    userzip = '92870'
    zip_data = requests.get(BASE_URL + "components=country:US%7Cpostal_code:"
                       + userzip + "&key=" + API_KEY)
    
    
    zip_data = zip_data.json()
    long_lat = zip_data["results"][0]["geometry"]["location"]
    return long_lat
