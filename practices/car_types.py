import logging

from urllib.request import urlopen
from bs4 import BeautifulSoup

from models import CarInfo
from db import init_db, db
from utils import parse_home_dir

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=parse_home_dir('scraping_error.log'),
                    filemode='w')

def car_type(url, tagclass='interval01-list-cars'):
    page = urlopen(url)
    car_obj = BeautifulSoup(page.read(), 'lxml')

    divs = car_obj.find_all('div', class_=tagclass)
    title_tag = car_obj.find('h3', {'class': 'tab-title'})
    guard_prices_divs = car_obj.findAll('div', {'class': 'interval01-list-guidance'})
    # print(guard_prices_divs)
    models, prices = [], []
    try:
        title = title_tag.get_text()
    except (IndexError, AttributeError):
        title = '未知车品牌'

    for div in divs:
        if div.a:
            models.append(div.a.contents[0])

    for price in guard_prices_divs:
        try:
            prices.append(price.div.get_text().strip())
        except Exception:
            pass

    # return title, types, prices
    # print(title + ':')
    # for car_type, price in zip(types, prices):
    #     print('-->', car_type, price)
    init_db()
    with db.atomic():
        for model, price in zip(models, prices):
            try:
                CarInfo.get(CarInfo.brand == title, CarInfo.model == model)
            except Exception as e:
                logging.error(e)
                CarInfo.create(brand=title, model=model, price=price)
            else:
                CarInfo.update(price=price).where(CarInfo.brand == title,
                                                  CarInfo.model == model).execute()


# if __name__ == '__main__':
#
#     car, car_types, guard_prices = car_type('https://www.autohome.com.cn/3872/#pvareaid=101487')
#     print(car + ':')
#     for car_type, price in zip(car_types, guard_prices):
#         print('-->', car_type, price)