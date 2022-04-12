import folium
import pandas as pd


csv_path = "C:/Users/Dr. Imran Nooraddin/PycharmProjects/SolarShare/lat_lng.csv"
data = pd.read_csv(csv_path, encoding = 'latin-1')
print(data)
m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)

# # # # ADD MARKERS TO MAP # # # #

for i in range(0, len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lng']],
      popup=data.iloc[i]['city'],
   ).add_to(m)

m.save('C:/Users/Dr. Imran Nooraddin/PycharmProjects/SolarShare/Solar_Share_Map_With_Markers.html')

