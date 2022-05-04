import requests
import settings as stg


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
