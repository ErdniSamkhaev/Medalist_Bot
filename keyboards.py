from telebot import types


def get_keyboard(bot, message):
    # Создаем клавиатуру с выбором услуги
    keyboard_service = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Терапевт')
    button2 = types.KeyboardButton('УЗИ')
    button3 = types.KeyboardButton('Гинеколог')
    button4 = types.KeyboardButton('Нейропсихолог')
    button5 = types.KeyboardButton('Лабораторные исследования')
    button6 = types.KeyboardButton('Массаж')
    button7 = types.KeyboardButton('Соляная пещера')
    keyboard_service.add(button1, button2, button3, button4, button5, button6, button7)

    # Отправляем сообщение с клавиатурой для выбора услуги
    bot.send_message(message.chat.id, "Выбери услугу, на которую хотите записаться:", reply_markup=keyboard_service)

