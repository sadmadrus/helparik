from sqlalchemy import null

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
    for cmd in classes.BOT_COMMANDS:
        markup.row(telebot.types.KeyboardButton(f"/{cmd['command']}"))

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
    cmd = command.strip().lower()

    match cmd:
        case 'start':
            storage.add_user(user.username, user.id, user.first_name, user.last_name)
            return {
                "text": f"Привет, {user.first_name}! Выбери технологию:",
                "reply_markup": get_main_menu()  # ✅ Клавиатура будет показана
            }
        case 'help':
            return {
                "text": "Доступные команды: /start, /help, /pon, /fttx, /adsl, /docsis",
                "reply_markup": get_main_menu()  # ✅ Клавиатура остаётся
            }
        case 'pon' | 'fttx' | 'adsl' | 'docsis':
            comments = storage.getCommetnBytech(cmd)
            text = '\n'.join([c.comment for c in comments]) if comments else "Комментарии не найдены"
            return {
                "text": f"Информация по {cmd.upper()}:\n{text}",
                "reply_markup": get_main_menu()  # ✅ Инлайн-кнопки
            }
        case _:
            return {"text": "Неизвестная команда"}

