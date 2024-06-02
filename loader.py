from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)


# def setup_handlers(bot):
#     """Настройка обработчиков событий для бота."""
#     @bot.message_handler(commands=['start'])
#     def handle_start(message):
#         """Отправляет приветственное сообщение и информацию о командах."""
#         bot.send_message(message.chat.id, "Привет! Я виртуальный помощник.\n"
#                                           "Вы можете оставить заявку на прием к специалистам, УЗИ, анализы, массаж, "
#                                           "соляная пещера. А также , вы можете отменить запись.\n"
#                                           "Чтобы записаться, используйте команду /Registration\n"
#                                           "Чтобы узнать подробнее об услугах, используйте команду /about\n"
#                                           "Чтобы отменить запись, используйте команду /cancel")
#
#         @bot.message_handler(commands=['Registration'])
#         def handle_registration(message):
#             pass
#
#         @bot.message_handler(commands=['about'])
#         def handle_about(message):
#             pass
#
#         @bot.message_handler(commands=['cancel'])
#         def handle_cancel(message):
#             pass
#
#
# # здесь подгружаются переменные для импорта
