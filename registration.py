from database import Client
from datetime import datetime
from telebot import types


# Функция для записи на услугу
def book_service(bot, message, service):
    client = Client.create(chat_id=str(message.chat.id), service=service, date_time=datetime.now())
    bot.send_message(message.chat.id, f"Вы успешно записаны к {service}.")


# Обработчик команды /Registration
def handle_book(bot, message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Терапевт')
    button2 = types.KeyboardButton('УЗИ')
    button3 = types.KeyboardButton('Гинеколог')
    button4 = types.KeyboardButton('Нейропсихолог')
    button5 = types.KeyboardButton('Лабораторные исследования')
    button6 = types.KeyboardButton('Массаж')
    button7 = types.KeyboardButton('Соляная пещера')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выбери услугу, на которую хочешь записаться:", reply_markup=keyboard)


# Обработчик текстовых сообщений
def handle_message(bot, message):
    if message.text == "Терапевт":
        book_service(bot, message, "Терапевту")
    elif message.text == "УЗИ":
        book_service(bot, message, "УЗИ")
    elif message.text == "Гинеколог":
        book_service(bot, message, "Гинекологу")
    elif message.text == "Нейропсихолог":
        book_service(bot, message, "Нейропсихологу")
    elif message.text == "Лабораторные исследования":
        book_service(bot, message, "Лабораторные исследования")
    elif message.text == "Массаж":
        book_service(bot, message, "Массаж")
    elif message.text == "Соляная пещера":
        book_service(bot, message, "Соляная пещера")
