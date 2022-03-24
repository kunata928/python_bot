import requests

url = 'https://openexchangerates.org/api/latest.json?app_id=1220e55ab6db41adb27d87036ec6dd40'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

WEATHER_URL = 'http://api.weatherstack.com/current?access_key=11c620b45d1e94840308f10d8fc44724'
WEATHER_PARAMS = {'query':'Cape Town'}

weather = requests.get(WEATHER_URL, params=WEATHER_PARAMS)

# print(weather.json()['current']['temperature']) # will print only the temperature; print without indexing to see all the values returned!
# Retrieve values from API
curr_temp = weather.json()['current']['temperature']
cad_rate = data['rates']['CAD']
eur_rate = data['rates']['EUR']
rub_rate = data['rates']['RUB']


def return_weather():
    print('Hello. The current temperature in Cape Town is: '+str(curr_temp)+" celsius.")


def return_rates():
    print("Hello. Today, USD conversion rates are as follows: USD->CAD = "+str(cad_rate)+
    ", USD->EUR = "+str(eur_rate)+", USD->RUB = "+str(rub_rate))


return_weather()

return_rates()