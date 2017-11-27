from peewee import SqliteDatabase

from utils import parse_home_dir

db = SqliteDatabase(parse_home_dir('data', 'carinfo.db'))

def init_db():
    db.init(parse_home_dir('data', 'carinfo.db'))