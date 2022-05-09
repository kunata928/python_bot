import pytz
import telebot
from datetime import datetime, timezone


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
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

tz = pytz.all_timezones

print(LOCAL_TIMEZONE)