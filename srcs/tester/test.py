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

strr = "at 08:30 20 05 2022 go to hour gym"
text = ""
date = datetime.now().date()
res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])\s*((\d{1,2})[-:\/\ ](\d{2})[-\/\ ](\d{4}))(.*)', strr)
if res:
    try:
        date_time = datetime(hour=int(res.group(1)), minute=int(res.group(2)),
                year=int(res.group(6)), month=int(res.group(5)), day=int(res.group(4)))
        text = res.group(7)
    except:
        date_time = datetime(hour=int(res.group(1)), minute=int(res.group(2)),
                             year=date.year, month=date.month, day=date.day)
        text = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr).group(3)
else:
    res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr)
    date_time = datetime(hour=int(res.group(1)), minute=int(res.group(2)),
                         year=date.year, month=date.month, day=date.day)
    text = res.group(3)
print("date time =", date_time, '\n', 'text =', text)