import telebot

from classes import Bot
from command import command

class TgBot(Bot):
    def __init__(self, bot_key):
       super().__init__(bot_key)
       self.bot = telebot.TeleBot(self.bot_key)
    @Bot.GetCommand
    def GetCommand(self):
        @self.bot.message_handler()
        def ReciveMessage(message):
            if self.bot.utils.is_command(message.text):
                command.doCommand(message.text)


