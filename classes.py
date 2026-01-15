from abc import ABC, abstractmethod
from typing import Any


class Bot(ABC):
    def __init__(self, bot_key):
        self.bot_key = bot_key

    @abstractmethod
    def GetCommand(self):
        pass
    def SendMessage(self, message):
        pass
