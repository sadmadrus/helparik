from abc import ABC, abstractmethod
from typing import Any


class Bot(ABC):
    def __init__(self, bot_key):
        self.bot_key = bot_key

    def SendMessage(self, message):
        pass

# Список команд для Telegram (для set_my_commands)
main_menu = [
    {"command": "start", "description": "Запустить бота"},
    {"command": "help", "description": "Показать помощь"},
    {"command": "comments", "description": "Комментарии к оборудованию"},
    {"command": "stop", "description": "Остановить бота"},
    {"command": "timer", "description": "Управление таймером"},
]

technologies = [
    {"command": "pon", "description": "Подключение по оптике"},
    {"command": "fttx", "description": "Подключение по витой паре"},
    {"command": "adsl", "description": "ADSL"},
    {"command": "docsis", "description": "DOCSIS"},
]

