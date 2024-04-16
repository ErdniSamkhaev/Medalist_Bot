import os
import telebot
from database import initialize_db
from dotenv import load_dotenv
from date_time_handler import handle_message
from keyboards import get_keyboard


def initialize_bot():
    """Инициализация базы данных и конфигурации бота."""
    # Инициализация базы данных
    initialize_db()

    # Загрузка и получение конфигурации
    load_dotenv(".env")
    token = os.getenv("TOKEN")
    bot = telebot.TeleBot(token)
    return bot


def setup_handlers(bot):
    """Настройка обработчиков событий для бота."""

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        """Отправляет приветственное сообщение и информацию о командах."""
        bot.send_message(message.chat.id, "Привет! Я виртуальный помощник.\n"
                                          "Вы можете оставить заявку на прием к специалистам, УЗИ, анализы, массаж, "
                                          "соляная пещера. А также , вы можете отменить запись.\n"
                                          "Чтобы записаться, используйте команду /Registration\n"
                                          "Чтобы узнать подробнее об услугах, используйте команду /about\n"
                                          "Чтобы отменить запись, используйте команду /cancel")

    # Подключение обработчиков из других модулей
    bot.message_handler(commands=['Registration'])(lambda message: get_keyboard(bot, message))
    bot.message_handler(func=lambda message: True)(lambda message: handle_message(bot, message))


def run_bot():
    """Инициализация и запуск бота."""
    bot = initialize_bot()
    setup_handlers(bot)
    bot.polling(none_stop=True)


if __name__ == "__main__":
    run_bot()
