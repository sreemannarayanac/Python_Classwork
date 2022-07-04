import requests as rs
from bs4 import BeautifulSoup as bs

result = rs.get('https://www.google.com/')

print(result.status_code)