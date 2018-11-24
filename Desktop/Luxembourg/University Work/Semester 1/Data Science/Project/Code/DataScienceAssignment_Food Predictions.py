# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:13:31 2018

@author: tusha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('food-world-cup-data (utf8).csv')
Loc_data = dataset["Location (Census Region)"].unique()

np.savetxt("Unique Locations.csv", Loc_data, delimiter=",", fmt='%s')

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_locations2", timeout=3)
Loc_cord = dict(zip(Loc_data, pd.Series(Loc_data).apply(geolocator.geocode)))
dataset["city_cord"] = dataset["Location (Census Region)"].map(Loc_cord)
dataset["LAT"] = dataset["city_cord"].apply(lambda x: (x.latitude))
dataset["LONG"] = dataset["city_cord"].apply(lambda x: (x.longitude))
gmap =  gmplot.GoogleMapPlotter(38.9072, 77.0369)
gmap.heatmap(dataset["LAT"], dataset["LONG"])
gmap.draw("My_heatmap3.html")

geolocator = Nominatim(user_agent="my_locations2", timeout=3)
location1 = geolocator.geocode(Loc_data[1])
dataset["coord"] = dataset["Location (Census Region)"].apply(geolocator.geocode)    

print(location.address)
print(location1.latitude, location1.longitude)
print(location.raw)



import gmplot

gmap =  gmplot.GoogleMapPlotter(ladata["LAT"], ladata["LON"], 10)

import itertools

gmap.heatmap(ladata["LAT"], ladata["LON"])
gmap.draw("My_heatmap2.html")

gmap.heatmap(itertools.repeat(location.latitude, 5), itertools.repeat(location.longitude, 5))
gmap.draw("My_heatmap1.html")