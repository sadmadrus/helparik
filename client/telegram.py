import telebot

from classes import Bot
from command import command

class TgBot(Bot):
    def __init__(self, bot_key):
       super().__init__(bot_key)
       self.bot = telebot.TeleBot(self.bot_key)
    def GetCommand(self):
        @self.bot.message_handler()
        def reciveMessage(message):
            if self.bot.utils.is_command(message.text):
                command.doCommand(message.user, message.text)

    def SendMessage(self, message):
        self.bot.send_message(message.user.id, message.text)

    def polling(self, none_stop):
       self.polling(none_stop=True)
