from unittest import TestCase, main
from playhouse.shortcuts import model_to_dict

from models import CarInfo
from db import init_db, db

def select(brand):
    return CarInfo.select().where(CarInfo.brand.contains(brand))

class TestSelect(TestCase):
    def test_select(self):
        cars = select(brand='奥迪A4')
        with db.atomic():
            for car in cars:
                print(model_to_dict(car))
        self.assertFalse(len(cars) == 0, '未查询到车品牌型号')

if __name__ == '__main__':
    init_db()
    main()
