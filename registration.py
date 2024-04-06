from database import Client
from datetime import datetime


# Функция для записи на услугу
def book_service(bot, message, service, time):
    # Отправляем график
    send_schedule(bot, message.chat.id, service)
    # Записываем клиента
    Client.create(chat_id=str(message.chat.id), service=service, date_time=datetime.now())
    # Отправляем сообщение об успешной записи
    bot.send_message(message.chat.id, f"Вы успешно записаны к {service} на {time}.")


def send_schedule(bot, chat_id, service):
    # Здесь формируется график для выбранной услуги
    schedule = f"График для {service}:\nПонедельник: 9:00 - 17:00\nВторник: 9:00 - 17:00\nСреда: выходной\n..."
    bot.send_message(chat_id, schedule)
