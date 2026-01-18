import telebot


from classes import Bot, BOT_COMMANDS
from client.command import command
from storage import storage


class TgBot(Bot):
    def __init__(self, bot_key):
        super().__init__(bot_key)
        print('TgBot initialized')
        self.bot = telebot.TeleBot(self.bot_key)
        self.commands = [cmd["command"] for cmd in BOT_COMMANDS]  # ✅ создаём список команд
        self.set_bot_commands()
        self.register_handlers()
        self.bot.polling(none_stop=True)
    def register_handlers(self):
        """Устанавливаем команды в Telegram (чтобы отображались при /)"""
        if not self.commands:
            print('Команды не загружены')
            return
        @self.bot.message_handler(commands=self.commands)
        def receive_message(message):
            cmd = message.text[1:].lower()  # убираем '/'
            result = command.doCommand(message.from_user, cmd)
            # Поддержка кнопок
            if isinstance(result, dict):
                text = result.get("text", "")
                reply_markup = result.get("reply_markup")
                self.bot.reply_to(message, text, reply_markup=reply_markup)
            else:
                self.bot.reply_to(message, result)
    def set_bot_commands(self):
        try:
            bot_commands = [
                telebot.types.BotCommand(cmd["command"], cmd["description"])
                for cmd in BOT_COMMANDS
            ]
            self.bot.set_my_commands(bot_commands)
            print("✅ Команды установлены в Telegram")
        except Exception as e:
            print(f"Ошибка установки команд: {e}")
            raise  # Более явное сообщение об ошибке

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith('tech_'))
        def handle_callback(call):
            tech = call.data.split('_')[1]
            comments = storage.getCommetnBytech(tech)
            text = '\n'.join([c.comment for c in comments]) if comments else "Нет данных"
            self.bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"🔧 {tech.upper()}:\n{text}"
            )

    def get_main_menu(self):
        """
        Создаёт клавиатуру с кнопками
        """
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        markup.row('/pon', '/fttx')
        markup.row('/adsl', '/docsis')
        markup.row('/help', '/stop')
        return markup

    def get_inline_menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(
            telebot.types.InlineKeyboardButton('PON', callback_data='tech_pon'),
            telebot.types.InlineKeyboardButton('FTTX', callback_data='tech_fttx')
        )
        markup.row(
            telebot.types.InlineKeyboardButton('ADSL', callback_data='tech_adsl'),
            telebot.types.InlineKeyboardButton('DOCSIS', callback_data='tech_docsis')
        )
        return markup

    def SendMessage(self, chatId, message):
        self.bot.send_message(chatId, message)

    def polling(self, none_stop):
        self.bot.polling(none_stop)
