import pytz
import telebot
import re
from datetime import datetime, timezone, timedelta


# MY_ID_CHAT = 273224124
# bot = telebot.TeleBot(stg.TOKEN_TG_BOT)  # You can set parse_mode by default. HTML or MARKDOWN
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
#
# def test_send_message():
#     text = 'CI Test Message'
#     tb = telebot.TeleBot(stg.TOKEN_TG_BOT)
#     ret_msg = tb.send_message(MY_ID_CHAT, text)
#     assert ret_msg.message_id
#
#
# if current_time == '17:30:00':
#     test_send_message()
# LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo#int(str(LOCAL_TIMEZONE))
#
# tz = pytz.all_timezones
# date = datetime.now().date()
# strr = "12"
# time = datetime(hour=4, minute=20, year=2022, month=15, day=13)
# print(time)


LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo
print(LOCAL_TIMEZONE)
