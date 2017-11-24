from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    else:
        try:
            bsObj = BeautifulSoup(html.read())
            title = bsObj.body.h1
        except AttributeError as e:
            return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
