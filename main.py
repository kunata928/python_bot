import telebot
import requests
import settings as stg
import srcs.GeoBot.parser_text_reminder


def return_weather():
    weather0 = requests.get(stg.WEATHER_URL, params=stg.WEATHER_PARAMS0)
    weather1 = requests.get(stg.WEATHER_URL, params=stg.WEATHER_PARAMS1)
    weather2 = requests.get(stg.WEATHER_URL, params=stg.WEATHER_PARAMS2)
    curr0_temp = weather0.json()['current']['temperature']
    curr1_temp = weather1.json()['current']['temperature']
    curr2_temp = weather2.json()['current']['temperature']
    return 'Hello. The current temperature in \nIstanbul is: '+str(curr0_temp)+" celsius,\nKrakow is: "+str(curr1_temp)+\
           " celsius,\nMoscow is: "+str(curr2_temp)+" celsius."


def return_rates():
    data = requests.get(stg.EXCHANGE_URL)  # requests data from API
    data = data.json()
    pln_rate = data['rates']['PLN']
    eur_rate = data['rates']['EUR']
    rub_rate = data['rates']['RUB']
    try_rate = data['rates']['TRY']
    return "Hello. Today, USD conversion rates are as follows: USD->PLN = "+str(pln_rate)+", USD->EUR = "+str(eur_rate)+\
           ", USD->RUB = "+str(rub_rate)+", USD->TRY = "+str(try_rate)


def weather(message, bot):
    bot.send_message(message.from_user.id, text=return_weather())


def currency(message, bot):
    bot.send_message(message.from_user.id, text=return_rates())


def start(message, bot):
    bot.send_message(message.from_user.id, text='Hi! I respond to /weather and /currency. Try these!')


def add_remind(message, bot):
    bot.send_message(message.from_user.id, text='If you want to add a remind, type message like: '"<After> <time> <msg>"
                                                '"After 5 h/min remind to drink water"')
    bot.register_next_step_handler(message, bot, req_reminde)


def parse_message(str):
    pass


def req_reminde(message, bot):
    parse_message(message.text)


def show_list_reminds(message, bot):
    pass


def remove_remind(message, bot):
    pass


def main():
    bot = telebot.TeleBot(stg.TOKEN_TG_BOT)  # You can set parse_mode by default. HTML or MARKDOWN

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        start(message, bot)

    @bot.message_handler(commands=['add', 'list', 'remove'])
    def set_reminder(message):
        if message.text == "/add":
            add_remind(message, bot)
        elif message.text == "/list":
            show_list_reminds(message, bot)
        elif message.text == "/remove":
            remove_remind(message, bot)

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message.text == "/weather":
            weather(message, bot)
        elif message.text == "/currency":
            currency(message, bot)
        else:
            start(message, bot)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
