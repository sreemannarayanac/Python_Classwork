import requests as rs
from bs4 import BeautifulSoup as bs

page = rs.get('https://www.gitam.edu/')
src = page.content
soup = bs(src, 'lxml')


programs = []

for li in soup.find_all('li'):
    h5_tag = li.find_all('h5')
    print(h5_tag)

print(programs)