import os
import telebot
from database import initialize_db
from dotenv import load_dotenv
from datatime import handle_message
from keyboards import get_keyboard


# Инициализация базы данных
initialize_db()

# Загрузка переменных окружения из файла .env
load_dotenv(".env")
# Получение токена из переменных окружения
TOKEN = os.getenv("TOKEN")
# Инициализация бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я виртуальный помощник.\n"
                                      "Вы можете оставить заявку на прием к специалистам, УЗИ, анализы, массаж, "
                                      "соляная пещера. А также , вы можете отменить запись.\n"
                                      "Чтобы записаться, используйте команду /Registration\n"
                                      "Чтобы узнать подробнее об услугах, используйте команду /about\n"
                                      "Чтобы отменить запись, используйте команду /cancel")


# Подключение обработчиков из registration.py
bot.message_handler(commands=['Registration'])(lambda message: get_keyboard(bot, message))
bot.message_handler(func=lambda message: True)(lambda message: handle_message(bot, message))


# Запуск бота
bot.polling(none_stop=True)


