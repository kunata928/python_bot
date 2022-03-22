import telebot
from telebot import types

name = ''
surname = ''
age = 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot = telebot.TeleBot("2032032327:AAFoTSbbdRkdcZTD4Q2ASsX3nuUWobzJW8M", parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")


    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message.text == "/req":
            bot.send_message(message.from_user.id, "Прив, как тебя зовут?")
            bot.register_next_step_handler(message, reg_name)
        # bot.reply_to(message, message.text)
    def reg_name(message):
        global name
        name = message.text
        bot.send_message(message.from_user.id, "Назови фамилию")
        bot.register_next_step_handler(message, reg_surname)

    def reg_surname(message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, "Сколько лет")
        bot.register_next_step_handler(message, reg_age)

    def reg_age(message):
        global age
        age = message.text
        bot.send_message(message.from_user.id, "Your name, surname, age is {} {} {} ?".format(name, surname, str(age)))
        keyword = types.InlineKeyboardMarkup
        key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    bot.infinity_polling()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
