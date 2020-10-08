import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

