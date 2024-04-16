from telebot import types


def get_keyboard(bot, message, services=None):
    """Создает и отправляет клавиатуру для выбора услуги пользователем."""
    if services is None:
        services = ['Терапевт', 'УЗИ', 'Гинеколог', 'Нейропсихолог', 'Лабораторные исследования', 'Массаж',
                    'Соляная пещера']

    keyboard_service = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    # Добавление кнопок для каждой услуги
    for service in services:
        keyboard_service.add(types.KeyboardButton(service))

    # Отправка клавиатуры пользователю
    bot.send_message(message.chat.id, "Выбери услугу, на которую хотите записаться:", reply_markup=keyboard_service)
