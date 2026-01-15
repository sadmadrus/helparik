import telebot

from classes import Bot
from client.command import command

class TgBot(Bot):
    def __init__(self, bot_key):
       super().__init__(bot_key)
       print('TgBot initialized')
       self.bot = telebot.TeleBot(self.bot_key)
       self.GetCommand()
    def GetCommand(self):
        @self.bot.message_handler(commands=['start', 'pon', 'fttx', 'adsl', 'docsis'])
        def reciveMessage(message):
            if message.text.startswith('/'):
                result = command.doCommand(message.from_user, message.text)
                print(result)
                self.SendMessage(message.chat.id, result)

    def SendMessage(self, chatId, message):
        self.bot.send_message(chatId, message)

    def polling(self, none_stop):
        self.bot.polling(none_stop)
