from peewee import SqliteDatabase, Model, CharField, DateTimeField

db = SqliteDatabase('clients.db')


class Client(Model):
    chat_id = CharField(unique=True)
    service = CharField()
    date_time = DateTimeField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Client], safe=True)
