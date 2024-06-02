from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMAND


def set_default_commands(bot):
    """Настройка обработчиков событий для бота."""
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMAND]
    )
