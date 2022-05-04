import telebot
import settings as stg
import command_add_remind
import commands_list_remove as lr
import weather_rates
import psycopg2
from telebot import types
from psycopg2 import Error

MY_ID_CHAT = 273224124
bot = telebot.TeleBot(stg.TOKEN_TG_BOT)  # You can set parse_mode by default. HTML or MARKDOWN


def weather(message):
    bot.send_message(message.from_user.id, text=weather_rates.return_weather())


def currency(message):
    bot.send_message(message.from_user.id, text=weather_rates.return_rates())


def start(message):
    bot.send_message(message.from_user.id, text='Hi! I respond to /add /list and /remove reminds. Try these!')


def parse_and_set_remind_job(message):
    answer_to_user = command_add_remind.message_processing(message)
    bot.send_message(message.from_user.id, text=answer_to_user)


def add_remind(message):
    db_connection = 0
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()

        db_object.execute(f"SELECT count(id) "
                          f"FROM reminds "
                          f"WHERE user_id = {message.from_user.id}")
        result = int(db_object.fetchone()[0])
        print(result)
        if result >= 10:
            bot.send_message(message.from_user.id, text='You reach the limit reminds. /remove some reminds')
        else:
            bot.send_message(message.from_user.id,
                             text='If you want to add a remind, type message like: '"<After> <time> <msg>"
                                  '" After 5 h/min remind to drink water"')
            bot.register_next_step_handler(message, parse_and_set_remind_job)
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")


def show_list_reminds(message):
    message_text = lr.list_users_reminds(message.from_user.id)
    bot.send_message(message.from_user.id, text=message_text)


def remove_remind(message):
    list_reminds = lr.list_users_reminds(message.from_user.id).split('\n')[1:-1]
    if list_reminds:
        inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
        for l in list_reminds:
            inline_kb_full.add(types.InlineKeyboardButton(l, callback_data='btn_id'+str(l.split()[0])))
            print('btn_id'+str(l.split()[0]))
        bot.send_message(message.from_user.id, text='Choose remind you want to delete:', reply_markup=inline_kb_full)
    else:
        bot.send_message(message.from_user.id, text="You have no reminds. Try /add command!")


all_commands_dict = {'add': add_remind, 'list': show_list_reminds, 'remove': remove_remind}


def main():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        start(message)

    @bot.message_handler(commands=['add', 'list', 'remove'])
    def set_reminder(message):
        all_commands_dict[message.text[1:]](message)

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message.text == "/weather":
            weather(message)
        elif message.text == "/currency":
            currency(message)
        else:
            start(message)

    @bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('btn_id'))
    def process_callback_kb1btn1(callback_query: types.CallbackQuery):
        id_remind = int(callback_query.data[6:])
        status = lr.remove_remind(id_remind)
        if status:
            bot.send_message(callback_query.from_user.id, text='success')
        else:
            bot.send_message(callback_query.from_user.id, text='fail')

    bot.infinity_polling()


if __name__ == '__main__':
    main()
