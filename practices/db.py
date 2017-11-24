from peewee import SqliteDatabase

db = SqliteDatabase('C:\\Users\\Admin\\Desktop\\Data\\carinfo.db')

def init_db():
    db.init('C:\\Users\\Admin\\Desktop\\Data\\carinfo.db')