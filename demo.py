import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.amazon.in/robots.txt")
print(r.text)
