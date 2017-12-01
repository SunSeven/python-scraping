import re
import peewee

from urllib.request import urlopen
from bs4 import BeautifulSoup

from car_types import car_type
from db import db
from models import CarInfo

links = set()

def fetch_url_links(url):
    global links
    try:
        html = urlopen("https://www.autohome.com.cn/" + url)
    except Exception:
        pass
    else:
        content = BeautifulSoup(html.read(), 'lxml')

        for link in content.find_all('a', {'href': re.compile("^/[0-9]*/#pvareaid.*")}):
            newpage = link.attrs['href']
            if newpage not in links:
                print(newpage)
                links.add(newpage)
                car_type("https://www.autohome.com.cn/" + newpage)
                fetch_url_links(newpage)

if __name__ == '__main__':
    try:
        db.create_table(CarInfo)
    except peewee.OperationalError as e:
        print(e)
    fetch_url_links('')
