import datetime
import threading
from typing import Any
import storage.storage


def check_events(bot_instance) -> Any:
    print("Проверка событий запущена")
    try:
        # Выбираем записи, где event_time <= текущее время
        events = storage.storage.getEvents()

        print(f"Найдено {len(events)} событий на {datetime.datetime.now()}")

        # Обработка найденных записей
        for event in events:
            print(f"Обработка события ID: {event.id}")
            bot_instance.SendMessage(event.user_id, event.message)
            storage.storage.removeEvent(event.id)

    except Exception as e:
        print(f"Ошибка при проверке событий: {e}")
    finally:
        # Планируем следующий запуск через 60 секунд
        timer = threading.Timer(60.0, check_events, args=(bot_instance,))
        timer.daemon = True
        timer.start()


def start_cron(bot_instance):
    # Запускаем первую проверку через 1 секунду
    timer = threading.Timer(1.0, check_events, args=(bot_instance,))
    timer.daemon = True
    timer.start()