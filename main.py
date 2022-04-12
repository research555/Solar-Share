import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration?oldformat=true'
table_class = 'wikitable sortable jquery=tablesorter'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find('table', {'class': 'wikitable'})

df = pd.read_html(str(tables))
df = pd.DataFrame(df[0])
print(df)