#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/14/2022
#This program is km

import pandas as pd
import folium

cuny = pd.read_csv(input('Name of csv file:'))
output = input('Enter output file:')
mapCUNY = folium.Map(location=[40.75, -74.125])
for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name).add_to(mapCUNY)
mapCUNY.save(outfile = output)