import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены, так как отсутствует файл .env.')
else:
    load_dotenv()


BOT_TOKEN = os.getenv('TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMAND = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку')
)
