from datetime import datetime, timedelta
import re


def set_time(data):
    now = datetime.now()
    print("Current time: ", now)
    if re.search(r"(minutes|minute|min|m)", data["time_type"]):
        set_time_reminder = datetime.now() + timedelta(minutes=int(data["time"]))
    elif re.search(r"(hours|hour|h)", data["time_type"]):
        set_time_reminder = datetime.now() + timedelta(hours=int(data["time"]))
    print("Reminder time: ", set_time_reminder)
    return set_time_reminder


def case_after(strr):
    re.search(r'\d+', strr)
    num = re.search(r'\d+', strr).group()
    time_type = re.search(r"(hours|minutes|hour|minute|min|h|m)", strr).group()
    try:
        remains_text = strr[strr.find(time_type) + len(time_type):]
        if re.search(r"^\s", remains_text):
            remider_text = 'After {} {} {}.'.format(str(num), str(time_type), remains_text)
        else:
            remider_text = 'After {} {} remind.'.format(str(num), str(time_type))
    except:
        remider_text = 'After {} {} remind.'.format(str(num), str(time_type))
    data_after_parse = {'type': 'after', 'time': num, 'time_type': time_type, 'text': remider_text}
    print("After parsing: ", data_after_parse)
    return "after", set_time(data_after_parse), data_after_parse['text']


def case_at(strr):
    date = datetime.now().date()
    res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr)
    if res:
        date_time = datetime(hour=int(res.group(1)), minute=int(res.group(2)),
                             year=date.year, month=date.month, day=date.day)
    else:
        date_time = datetime.now()
    print(date_time)
    return "at", date_time, res.group(3)


def parse_message(strr):
    strr = strr.lower()
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m)\s*', strr):
        time_text = case_after(strr[strr.find("after") + len("after"):])
    elif re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr):
        time_text = case_at(strr)
    else:
        return 0
    return {'type': time_text[0], 'time_date': time_text[1], 'text': time_text[2]}

# выделить цифры
# вытянуть таймзону из бд
# по формуле установить время в бд
# # время в бд = время из сообщения - таймзона юзера
# скорректировать шедулер: now_dt - должно быть в UTC
# скоррректировать запись в бд для after (должно быть -tz локального устройства)