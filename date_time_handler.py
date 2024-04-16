from telebot import types
from registration import book_service
from workDay import selected_services, service_times, week_days, selected_days


def handle_message(bot, message):
    """Обрабатывает входящие сообщения и управляет процессом регистрации услуг."""
    chat_id = message.chat.id

    if chat_id not in selected_services:
        handle_service_selection(bot, message)
    elif chat_id not in selected_days:
        handle_day_selection(bot, message, chat_id)
    else:
        finalize_booking(bot, message, chat_id)


def handle_service_selection(bot, message):
    """Обрабатывает выбор услуги пользователем."""
    if message.text in service_times:
        selected_services[message.chat.id] = message.text
        send_day_keyboard(bot, message)
    else:
        bot.send_message(message.chat.id, "Выберите услугу из списка.")


def send_day_keyboard(bot, message):
    """Отправляет пользователю клавиатуру для выбора дня."""
    keyboards_days = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for day in week_days:
        keyboards_days.add(types.KeyboardButton(day))
    bot.send_message(message.chat.id, "Выберите день:", reply_markup=keyboards_days)


def handle_day_selection(bot, message, chat_id):
    """Обрабатывает выбор дня пользователем."""
    if message.text in week_days:
        selected_days[chat_id] = message.text
        send_time_keyboard(bot, message, chat_id)
    else:
        bot.send_message(message.chat.id, "Выберите день из списка.")


def send_time_keyboard(bot, message, chat_id):
    """Отправляет пользователю клавиатуру для выбора времени."""
    available_times = service_times[selected_services[chat_id]]
    keyboard_time = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for time in available_times:
        keyboard_time.add(types.KeyboardButton(time))
    bot.send_message(message.chat.id, "Выберите удобное время:", reply_markup=keyboard_time)


def finalize_booking(bot, message, chat_id):
    """Завершает процесс бронирования и сбрасывает выбранное состояние."""
    if message.text in service_times[selected_services[chat_id]]:
        book_service(bot, message, selected_services[chat_id], selected_days[chat_id], message.text)
        # Сбрасываем выбранную услугу и день
        del selected_services[chat_id]
        del selected_days[chat_id]
    else:
        bot.send_message(message.chat.id, "Выберите время из предложенных вариантов.")
