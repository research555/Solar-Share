"""

LLIST OF STUFF TRHAT NEEDS TOP HAPPEN


1. make table of sunlioght hours
2. make a map with pins for each city on the table

"""
import csv
import folium
from opencage.geocoder import OpenCageGeocode
import pandas as pd

# Make an empty map
csv_path = "C:/Users/Dr. Imran Nooraddin/PycharmProjects/SolarShare/Sunhours worldwide from wikipedia.csv"
data = pd.read_csv(csv_path, encoding='latin-1')       # Import CSV
cities = []
for index, row in data.iterrows():
    cities.append(row['City'])      # Appends all cities from df to a new list


geo_key = "0564512562944fa1b9a12b658169b564" # From OpenCage API
geocoder = OpenCageGeocode(geo_key)
query = 'Oslo'
results = geocoder.geocode(query)

city_lat = []
city_lng = []
i = 0
for city in cities:
    query = city
    results = geocoder.geocode(query)
    city_lat.append(results[0]['geometry']['lat'])
    city_lng.append(results[0]['geometry']['lng'])
    i += 1
    print(i)    # Always good with some feedback

rows = zip(city_lat, city_lng, cities)
new_csv_path = "C:/Users/Dr. Imran Nooraddin/PycharmProjects/SolarShare/lat_lng.csv"
with open(new_csv_path, 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)



m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
m.save('C:/Users/Dr. Imran Nooraddin/PycharmProjects/SolarShare/basic_folium_map.html')

# Show the map



