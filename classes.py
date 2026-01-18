from abc import ABC, abstractmethod
from typing import Any


class Bot(ABC):
    def __init__(self, bot_key):
        self.bot_key = bot_key

    def SendMessage(self, message):
        pass

# Список команд для Telegram (для set_my_commands)
BOT_COMMANDS = [
    {"command": "start", "description": "Запустить бота"},
    {"command": "help", "description": "Показать помощь"},
    {"command": "fttx", "description": "Информация по FTTX"},
    {"command": "pon", "description": "Информация по PON"},
    {"command": "adsl", "description": "Информация по ADSL"},
    {"command": "docsis", "description": "Информация по DOCSIS"},
    {"command": "stop", "description": "Остановить бота"},
    {"command": "timer", "description": "Управление таймером"},
]

