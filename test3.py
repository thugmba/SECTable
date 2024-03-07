from bs4 import BeautifulSoup
import requests


headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
# Obtain HTML for search page
base_url = "https://www.sec.gov/Archives/edgar/data/200406/000020040621000057/jnj-20210704.htm"
edgar_resp = requests.get(base_url, headers=headers)
edgar_str = edgar_resp.text


soup = BeautifulSoup(edgar_str, 'html.parser')
s =  soup.find('span', recursive=True, string='SALES BY SEGMENT OF BUSINESS ')
t = s.find_next('table')
trs = t.find_all('tr')
for tr in trs:
    if tr.text:
        print(list(tr.stripped_strings))