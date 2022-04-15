import os

# heroku = 1
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
TOKEN_TG_BOT = os.environ['TOKEN_TG_BOT']
TOKEN_EXCHANGE = os.environ['TOKEN_EXCHANGE']
TOKEN_WEATHER = os.environ['TOKEN_WEATHER']

# if heroku:
#     from boto.s3.connection import S3Connection
#     s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
#     TOKEN_TG_BOT = os.environ['TOKEN_TG_BOT']
#     TOKEN_EXCHANGE = os.environ['TOKEN_EXCHANGE']
#     TOKEN_WEATHER = os.environ['TOKEN_WEATHER']
# else:
#     dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#     if os.path.exists(dotenv_path):
#         from dotenv import load_dotenv
#         load_dotenv(dotenv_path=dotenv_path)
#     TOKEN_TG_BOT = os.environ.get("TOKEN_TG_BOT")
#     TOKEN_EXCHANGE = os.environ.get("TOKEN_EXCHANGE")
#     TOKEN_WEATHER = os.environ.get("TOKEN_WEATHER")

EXCHANGE_URL = 'https://openexchangerates.org/api/latest.json?app_id='+TOKEN_EXCHANGE
WEATHER_URL = 'http://api.weatherstack.com/current?access_key='+TOKEN_WEATHER

WEATHER_PARAMS0 = {'query':'Istanbul'}
WEATHER_PARAMS1 = {'query':'Krakow'}
WEATHER_PARAMS2 = {'query':'Moskva'}