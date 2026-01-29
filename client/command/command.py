import datetime

import shlex
import classes
from storage import storage
import telebot
def get_helpText():
    return storage.get_helpText()

def getCommentByTech(technology):
    comments = storage.getCommetnBytech(technology)
    result = ''
    if comments is None:
        return 'Комментарии не найдены'
    for comment in comments:
        result += comment.comment + '\n'
    return result

def getHelpText():
    #TODO: 'описать получение помощи'
    pass
def get_main_menu():
    """
    Основная клавиатура — остаётся внизу всегда
    """
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for cmd in classes.main_menu:
        markup.row(telebot.types.KeyboardButton(f"/{cmd['command']}"))

    return markup
def build_inline_menu(menu_structure):
    markup = telebot.types.InlineKeyboardMarkup()
    if isinstance(menu_structure, list):
        for item in menu_structure:
            if isinstance(item, dict):
                # Используем ключ 'command' для кнопки
                markup.row(telebot.types.InlineKeyboardButton(f"/{item['command']}", callback_data=f"tech_{item['command']}"))
            else:
                # Если это просто строка
                markup.row(telebot.types.InlineKeyboardButton(f"/{item}", callback_data=f"tech_{item}"))
    return markup

def build_menu(menu_structure):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if isinstance(menu_structure, dict):
        for key in menu_structure.keys():
            markup.row(telebot.types.KeyboardButton(f"/{key}"))
    elif isinstance(menu_structure, list):
        for item in menu_structure:
            markup.row(telebot.types.KeyboardButton(f"/{item}"))
    return markup

def doCommand(user, command):
    cmdList = shlex.split(command.lower())
    match cmdList[0]:
        case 'start':
            storage.add_user(user.username, user.id, user.first_name, user.last_name)
            return {
                "text": f"Привет, {user.first_name}! Выбери технологию:",
                "reply_markup": get_main_menu()  # ✅ Клавиатура будет показана
            }
        case 'help':
            return {
                "text": "Доступные команды: /start, /help, /pon, /fttx, /adsl, /docsis, /timer",
                "reply_markup": get_main_menu()  # ✅ Клавиатура остаётся
            }
        case 'comments':
            return {
                "text": "Выберите технологию:",
                "reply_markup": build_inline_menu(classes.technologies)  #
            }
        case 'pon' | 'fttx' | 'adsl' | 'docsis':
            comments = storage.getCommetnBytech(cmdList[0])
            text = '\n'.join([c.comment for c in comments]) if comments else "Комментарии не найдены"
            return {
                "text": f"Информация по {cmdList[0].upper()}:\n{text}",
                "reply_markup": get_main_menu()  # ✅ Инлайн-кнопки
            }
        case 'timer':
            if len(cmdList) < 3:
                return {
                    "text": "Введите время в минутах и комментарий через пробел:\nПример: /timer 30 моя заметка",
                    "reply_markup": get_main_menu()
                }
            else:
                # Используем предоставленные аргументы
                try:
                    minutes = int(cmdList[1])
                    timer = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
                    message = ' '.join(cmdList[2:])  # Объединяем оставшиеся аргументы в комментарий

                    # Создаем событие
                    event = storage.addEvent(user.id, "remind", timer, message)
                    print(event)
                    return {
                        "text": f"Событие добавлено на {minutes} минут:\n{message}",
                        "reply_markup": get_main_menu()
                    }
                except ValueError:
                    return {
                        "text": "Ошибка: укажите корректное число минут",
                        "reply_markup": get_main_menu()
                    }
        case 'mycomments':
            return {
                "text": "Ваши комментарии:",
                "reply_markup": storage.GetCommetsByUserAndTechnology(user.id, cmdList[1].lower())  #
            },
        case 'addcomment':
            return {
                "text": "Введите комментарий:",
                "reply_markup": storage.addComment(user.id, cmdList[1].lower(), cmdList[2])  #
            }
        case _:
            return {"text": "Неизвестная команда"}

