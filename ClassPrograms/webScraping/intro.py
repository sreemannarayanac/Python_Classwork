import requests as rs
from bs4 import BeautifulSoup as bs

result = rs.get('https://www.gitam.edu/')

# print(result.status_code) if 200 page is opening

src = result.content # Gets source code

soup = bs(result, 'lxml')

headers = soup.findall('h1')
print(headers)