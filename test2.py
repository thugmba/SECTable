from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://gcoins.net/en/catalog/view/45518'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#table = soup.find('table', attrs={'class':'subs noBorders evenRows'})
table = soup.find('table', attrs={'class':'storeItemBig storeItem noBorders'})
table_rows = table.find_all('tr')

data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    data.append(row_data)

df = pd.DataFrame(data)
print(df)
