import telebot
import settings as stg
import time_zone as tz
import command_add_remind
import commands_list_remove as lr
import weather_rates
from telebot import types

MY_ID_CHAT = 273224124
bot = telebot.TeleBot(stg.TOKEN_TG_BOT)  # You can set parse_mode by default. HTML or MARKDOWN


def weather(message):
    bot.send_message(message.from_user.id, text=weather_rates.return_weather())


def currency(message):
    bot.send_message(message.from_user.id, text=weather_rates.return_rates())


def start(message):
    bot.send_message(message.from_user.id, text='Hi! I respond to:\n/add /list and /remove reminds.\nAlso I can '
                                                'set your /timezone. Default is UTC +3.  Try these!')


def parse_and_set_remind_job(message):
    answer_to_user = command_add_remind.message_processing(message)
    bot.send_message(message.from_user.id, text=answer_to_user)


def add_remind(message):
    result = command_add_remind.count_reminds_for_user(message.from_user.id)
    print(result)
    if result == -1:
        bot.send_message(message.from_user.id, text='There is some troubles with bot :(')
    elif result >= stg.REMINDS_LIMIT:
        bot.send_message(message.from_user.id, text='You reach the limit of reminds. /remove some reminds')
    else:
        bot.send_message(message.from_user.id,
                         text='If you want to add a remind, type message like: \n"<After/At> <time> <msg>" \n'
                              '"After 5 h/min remind to drink water"\n'
                              '"At 18.30 go to home"\n')
        bot.register_next_step_handler(message, parse_and_set_remind_job)


def show_list_reminds(message):
    message_text = lr.list_users_reminds(message.from_user.id)
    bot.send_message(message.from_user.id, text=message_text)


def remove_remind(message):
    list_reminds = lr.list_users_reminds(message.from_user.id).split('\n')[1:-1]
    if list_reminds:
        inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
        for remind in list_reminds:
            inline_kb_full.add(types.InlineKeyboardButton(remind, callback_data='btn_id'+str(remind.split()[0])))
            print('btn_id'+str(remind.split()[0]))
        bot.send_message(message.from_user.id, text='Choose remind you want to delete:', reply_markup=inline_kb_full)
    else:
        bot.send_message(message.from_user.id, text="You have no reminds. Try /add command!")


def set_new_tz(message):
    text_message = tz.set_tz_DB(message.from_user.id, message.text)
    bot.send_message(message.from_user.id, text=text_message)


def change_tz(message):
    user_tz = tz.show_user_tz(message.from_user.id)
    sign = '+' if user_tz >= 0 else ''
    bot.send_message(message.from_user.id, text="Now your timezone is UTC " + sign + str(user_tz) + " \n" +
                     "Input new timezone (for example +3 or -11):")
    bot.register_next_step_handler(message, set_new_tz)


all_commands_dict = {'add': add_remind, 'list': show_list_reminds, 'remove': remove_remind, 'timezone': change_tz}


def main():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        start(message)

    @bot.message_handler(commands=['add', 'list', 'remove', 'timezone'])
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
        id_remind = int(callback_query.data[len('btn_id'):])
        status = lr.remove_remind(id_remind)
        if status:
            bot.send_message(callback_query.from_user.id, text='success')
        else:
            bot.send_message(callback_query.from_user.id, text='fail')

    bot.infinity_polling()


if __name__ == '__main__':
    main()
