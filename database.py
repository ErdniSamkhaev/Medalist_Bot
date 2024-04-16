from peewee import SqliteDatabase, Model, CharField, DateTimeField

# Определение объекта базы данных
db = SqliteDatabase('clients.db')


class Client(Model):
    """Модель клиента для хранения информации в базе данных."""
    chat_id = CharField(unique=True)  # Уникальный идентификатор чата для связи с пользователем
    service = CharField()             # Услуга, которую выбрал клиент
    date_time = DateTimeField()       # Дата и время записи на услугу

    class Meta:
        database = db  # Привязка модели к определенной базе данных


def initialize_db():
    """Подключает к базе данных и создает таблицы, если они еще не созданы."""
    try:
        db.connect()
        db.create_tables([Client], safe=True)  # Создание таблицы, если она еще не существует
    except Exception as e:
        print(f"При подключении к базе данных произошла ошибка: {e}")
