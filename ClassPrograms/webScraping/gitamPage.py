import requests as rs
from bs4 import BeautifulSoup as bs

page = rs.get('https://www.gitam.edu/')
src = page.content
soup = bs(src, 'lxml')


programs = []

for li in soup.find_all('li'):
    a_tag = li.find('a')
    if a_tag:
        img_tag = a_tag.find('img')
        if img_tag:
            (img_tag.attrs['title'])
        else:
            continue

print(programs)