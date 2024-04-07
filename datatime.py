from telebot import types
from registration import book_service


# Глобальная переменная для хранения выбранной услуги
selected_service = None


def handle_message(bot, message):
    global selected_service
    if selected_service is None:
        if message.text in ['Терапевт', 'УЗИ', 'Гинеколог', 'Нейропсихолог', 'Лабораторные исследования',
                            'Массаж', 'Соляная пещера']:
            selected_service = message.text
            # Отправляем клавиатуру с выбором времени
            keyboard_time = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_terapevt1 = types.KeyboardButton('8:00')
            button_terapevt2 = types.KeyboardButton('9:00')
            keyboard_time.add(button_terapevt1, button_terapevt2)
            bot.send_message(message.chat.id, "Выберите удобное время:", reply_markup=keyboard_time)
        else:
            bot.send_message(message.chat.id, "Выберите услугу из списка.")
    else:
        if message.text in ['8:00', '9:00']:
            selected_time = message.text
            book_service(bot, message, selected_service, selected_time)
            # Сбрасываем выбранную услугу
            selected_service = None
        else:
            bot.send_message(message.chat.id, "Выберите время из предложенных вариантов.")