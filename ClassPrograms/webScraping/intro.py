import requests as rs
from bs4 import BeautifulSoup

result = rs.get('https://www.gitam.edu/')

# print(result.status_code) if 200 page is opening

src = result.content # Gets source code

soup = BeautifulSoup(src, 'lxml')

headers = soup.find_all('ul')
print(headers)