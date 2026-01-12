import argparse
import logging

from client.telegram import TgBot

parser = argparse.ArgumentParser(description="Бот для 2лтп")
parser.add_argument("bot_key", help="Токет бота")

if __name__ == '__main__':
    args = parser.parse_args()
    bot_key = args.bot_key
    if bot_key == '':
        logging.error('Ключ бота не задан!')
    else:
        tgBot = TgBot(bot_key)
