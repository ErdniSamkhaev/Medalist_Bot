import os

import telebot
from datetime import datetime, timedelta
from database import Client, initialize_db
from dotenv import load_dotenv


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
    bot.send_message(message.chat.id, "Привет! Я бот для записи на услуги. Чтобы записаться, используй команду /book.")


# Обработчик команды /book
@bot.message_handler(commands=['book'])
def handle_book(message):
    bot.send_message(message.chat.id, "Выбери услугу, на которую хочешь записаться:")
    # Здесь можно добавить клавиатуру с кнопками для выбора услуг


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Терапевт":
        book_service(message, "Терапевт")
    elif message.text == "УЗИ":
        book_service(message, "УЗИ")
    # Добавьте обработку других услуг


# Функция для записи на услугу
def book_service(message, service):
    client = Client.create(chat_id=str(message.chat.id), service=service, date_time=datetime.now())
    bot.send_message(message.chat.id, f"Ты успешно записан на {service}.")


# Запуск бота
bot.polling(none_stop=True)
