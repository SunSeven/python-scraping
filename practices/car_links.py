import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

from car_types import car_type

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

    # return links

    # links = content.find_all(lambda tag: 'href' in tag.attrs)
    # print(len(links))

if __name__ == '__main__':
    fetch_url_links('')
