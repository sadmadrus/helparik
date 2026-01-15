from sqlalchemy import null

from storage import storage
from classes import Bot


def get_helpText():
    storage.get_helpText()

def getCommetnBytech(technology, user):
    comment = storage.getCommetnBytech(technology)
    if comment:
        return comment
    else:
        return 'Не найден комментарий'


def getHelpText():
    #TODO: 'описать получение помощи'
    pass


def doCommand(user, command):
    command_text = command.split(' ')
    if len(command_text[0]) == 0: return ''
    match command_text[0].lower():
        case '/start':
            print(user.id)
            result = storage.add_user(user.username, user.id, user.first_name, user.last_name)
        case '/stop':    result = storage.remove_user(user.id)
        case '/help':    result = getHelpText()
        case '/fttx':    result = getCommetnBytech('fttx', user)
        case '/pon':     result = getCommetnBytech('pon', user)
        case '/adsl':    result = getCommetnBytech('adsl', user)
        case '/docsis':  result = getCommetnBytech('docsis', user)
        case _:         result =  'Неопознаная команда'
    return result
