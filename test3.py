#
# Extract consolidate statement of operations from sec.gov finantial report
#
# Brian Kim
# GMBA, Tunghai University
# 2024/03/08
#

from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

# URL for the company
base_url = "https://www.sec.gov/Archives/edgar/data/0000320193/000032019323000106/aapl-20230930.htm"
edgar_resp = requests.get(base_url, headers=headers)
edgar_str = edgar_resp.text

# Locate table in the html
soup = BeautifulSoup(edgar_str, 'html.parser')
s =  soup.find('span', recursive=True, string='CONSOLIDATED STATEMENTS OF OPERATIONS')
s =  soup.find('span', recursive=True, string='CONSOLIDATED STATEMENTS OF OPERATIONS')
t = s.find_next('table')

# Convert it to dataframe
data = []
for row in t.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
#        row_data.append(cell.text)
        cell_val = cell.text.replace(u'\xa0', u' ')
        if not cell_val == '$':
            row_data.append(cell_val)
    data.append(row_data)
df = pd.DataFrame(data)

# Select the column  
target_val = df.iloc[4:,1]
print(target_val)

# Save to CSV file
target_val.to_csv('apple.csv',  encoding='utf-8')
