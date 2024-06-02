from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, "Привет! Я виртуальный помощник.\n"
                                      "Вы можете оставить заявку на прием к специалистам, УЗИ, анализы, массаж, "
                                      "соляная пещера."
                                      "А также , вы можете отменить запись.\n"
                                      "Чтобы записаться, используйте команду /Registration\n"
                                      "Чтобы узнать подробнее об услугах, используйте команду /about\n"
                                      "Чтобы отменить запись, используйте команду /cancel")
