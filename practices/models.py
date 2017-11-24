from peewee import *

from db import init_db, db

class ModelBase(Model):
    class Meta:
        database = db

class CarInfo(ModelBase):
    brand = CharField(max_length=50)
    model = CharField(max_length=100)
    price = CharField(max_length=20)
