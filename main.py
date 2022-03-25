import telebot
import requests
# import pyTelegramBotAPI
# from telegram import Updater, CommandHandler

TOKEN = "2032032327:AAFoTSbbdRkdcZTD4Q2ASsX3nuUWobzJW8M"

url = 'https://openexchangerates.org/api/latest.json?app_id=1220e55ab6db41adb27d87036ec6dd40'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json


WEATHER_URL = 'http://api.weatherstack.com/current?access_key=11c620b45d1e94840308f10d8fc44724'
WEATHER_PARAMS0 = {'query':'Istanbul'}#Cape Town
WEATHER_PARAMS1 = {'query':'Krakow'}#Cape Town
WEATHER_PARAMS2 = {'query':'Moskva'}#Cape Town



# print(weather.json()['current']['temperature']) # will print only the temperature; print without indexing to see all the values returned!
# Retrieve values from API

pln_rate = data['rates']['PLN']
eur_rate = data['rates']['EUR']
rub_rate = data['rates']['RUB']
try_rate = data['rates']['TRY']

def return_weather():
    weather0 = requests.get(WEATHER_URL, params=WEATHER_PARAMS0)
    weather1 = requests.get(WEATHER_URL, params=WEATHER_PARAMS1)
    weather2 = requests.get(WEATHER_URL, params=WEATHER_PARAMS2)
    curr0_temp = weather0.json()['current']['temperature']
    curr1_temp = weather1.json()['current']['temperature']
    curr2_temp = weather2.json()['current']['temperature']
    return 'Hello. The current temperature in \nIstanbul is: '+str(curr0_temp)+" celsius,\nKrakow is: "+str(curr1_temp)+\
           " celsius,\nMoscow is: "+str(curr2_temp)+" celsius."


def return_rates():
    return "Hello. Today, USD conversion rates are as follows: USD->PLN = "+str(pln_rate)+", USD->EUR = "+str(eur_rate)+\
           ", USD->RUB = "+str(rub_rate)+", USD->TRY = "+str(try_rate)


def weather(message, bot):
    bot.send_message(message.from_user.id, text=return_weather())


def currency(message, bot):
    bot.send_message(message.from_user.id, text=return_rates())


def start(message, bot):
    bot.send_message(message.from_user.id, text='Hi! I respond to /weather and /currency. Try these!')


def main():
    bot = telebot.TeleBot(TOKEN)  # You can set parse_mode by default. HTML or MARKDOWN

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        start(message, bot)

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message.text == "/weather":
            weather(message, bot)
        elif message.text == "/currency":
            currency(message, bot)
        else:
            start(message, bot)

    # PORT = int(os.environ.get('PORT', '443'))
    # HOOK_URL = 'YOUR-CODECAPSULES-URL-HERE' + '/' + TOKEN
    # bot.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    # bot.idle()
    bot.infinity_polling()


if __name__ == '__main__':
    main()
