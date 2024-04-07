from telebot import types
from registration import book_service
from workDay import selected_services, service_times, week_days, selected_days


def handle_message(bot, message):
    chat_id = message.chat.id
    if chat_id not in selected_services:
        if message.text in service_times:
            selected_services[chat_id] = message.text
            # Отправляем клавиатуру с выбором дня
            keyboards_days = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            for day in week_days:
                button_day = types.KeyboardButton(day)
                keyboards_days.add(button_day)
            bot.send_message(message.chat.id, "Выберите день:", reply_markup=keyboards_days)
        else:
            bot.send_message(message.chat.id, "Выберите услугу из списка.")
    elif chat_id not in selected_days:
        if message.text in week_days:
            selected_days[chat_id] = message.text
            # Получаем доступное время для выбранной услуги
            available_times = service_times[selected_services[chat_id]]
            # Отправляем клавиатуру с выбором времени
            keyboard_time = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            for time in available_times:
                button_time = types.KeyboardButton(time)
                keyboard_time.add(button_time)
            bot.send_message(message.chat.id, "Выберите удобное время:", reply_markup=keyboard_time)
        else:
            bot.send_message(message.chat.id, "Выберите услугу из списка.")
    else:
        if message.text in service_times[selected_services[chat_id]]:
            selected_time = message.text
            book_service(bot, message, selected_services[chat_id], selected_days[chat_id], selected_time)
            # Сбрасываем выбранную услугу
            del selected_services[chat_id]
            del selected_days[chat_id]
        else:
            bot.send_message(message.chat.id, "Выберите время из предложенных вариантов.")
