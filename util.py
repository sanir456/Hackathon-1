import pandas as pd, numpy as np
import requests
import json
import time
from geopy.geocoders import Nominatim

def nearby():
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode("IIIT Bangalore")  #User Location
    
    # printing address
    print(getLoc.address)
    
    # printing latitude and longitude
    coordinate = str(getLoc.latitude) + ', ' + str(getLoc.longitude) 
    #print("Latitude = ", getLoc.latitude, "\n")
    #print("Longitude = ", getLoc.longitude)
    keywords = ['restaurant']
    radius = '3000'
    api_key = 'AIzaSyB8FvSrC42tNEFdgap-rgrtXgovKcUlS4w' #insert your API key here
    restaurants = []
    rating = []
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
        respon = requests.get(url)
        jj = json.loads(respon.text)
        results = jj['results']
        for result in results:
            restaurants.append(result['name'])
            rating.append(result['rating'])
    return restaurants,len(restaurants),rating


        
  
# calling the Nominatim tool
