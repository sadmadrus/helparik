import argparse
import threading

from client.telegram import TgBot
from cron.cron import check_events, start_cron

parser = argparse.ArgumentParser(description="Бот для 2лтп")
parser.add_argument("bot_key", help="Токен бота")

if __name__ == '__main__':
    args = parser.parse_args()
    bot_key = args.bot_key

    if not bot_key:
        print('Ключ бота не задан!')
    else:

        # Запускаем бота
        tgBot = TgBot(bot_key)
        print('Бот запущен')
        # Запускаем cron в отдельном потоке
        cron_thread = threading.Thread(target=start_cron, args=(tgBot,), daemon=True)
        cron_thread.start()

        # Ожидаем, чтобы основной поток не завершился
        try:
            while True:
                tgBot.polling(True)
        except KeyboardInterrupt:
            print("Бот остановлен")
