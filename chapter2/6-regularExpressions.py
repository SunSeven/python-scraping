from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src": re.compile("\.\./img/gifts/img.*\.jpg")})
# print(type(images[0]))
for image in images:
    print(image.attrs['src'])
