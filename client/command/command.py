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
    match command_text[0].lower():
        case 'start':   storage.add_user(user.name, user.id, user.first_name, user.last_name)
        case 'stop':    storage.remove_user(user.id)
        case 'help':    getHelpText()
        case 'fttx':    getCommetnBytech('fttx', user)
        case 'pon':     getCommetnBytech('pon', user)
        case 'adsl':    getCommetnBytech('adsl', user)
        case 'docsis':  getCommetnBytech('docsis', user)
        case _: return 'Неопознаная команда'