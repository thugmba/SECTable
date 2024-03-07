from bs4 import BeautifulSoup
import requests
import pandas as pd

email="thugmba@gmail.com"
website="http://www.thu.edu.tw"
headers = { "User-Agent": f"{website} {email}"}

url = 'https://www.sec.gov/ixviewer/ix.html?doc=/Archives/edgar/data/0000320193/000032019323000106/aapl-20230930.htm#i1cb1ba018cb1455aa66bd3f9ab0c5b1a_73'
response = requests.get(url,headers=headers)

# Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first occurrence of the text you're looking for
target_text = "In millions, except number of shares, which are reflected in thousands, and per-share amounts"
target_text = "CONSOLIDATED STATEMENTS OF OPERATIONS"
target_element = soup.find(string=target_text)

# Find the first table tag after the target text
table_after_text = target_element.find_next('table')

# Now you have the first table tag after the specified text
print(table_after_text)