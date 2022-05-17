from datetime import datetime, timedelta
import re
import time_zone as tz


def set_time_after(data):
    now_utc = datetime.utcnow()
    print("Current time: ", now_utc)
    if re.search(r"(minutes|minute|min|m)", data["time_type"]):
        set_time_reminder = now_utc + timedelta(minutes=int(data["time"]))
    elif re.search(r"(hours|hour|h)", data["time_type"]):
        set_time_reminder = now_utc + timedelta(hours=int(data["time"]))
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
    return "after", set_time_after(data_after_parse), data_after_parse['text']


def case_at(strr, user_tz):
    text = ""
    date = datetime.utcnow().date()
    res = re.search(
        r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])\s*((\d{1,2})[-.:,\/\ ](\d{2})[-\/\ ](\d{4}))(.*)',
        strr)
    if res:
        try:
            date_time_utc = datetime(hour=int(res.group(1)), minute=int(res.group(2)),
                                 year=int(res.group(6)), month=int(res.group(5)), day=int(res.group(4)))\
                            - timedelta(hours=user_tz)
            text = res.group(7)
        except:
            date_time_utc = datetime(hour=(int(res.group(1))-user_tz) % 24, minute=int(res.group(2)),
                                 year=date.year, month=date.month, day=date.day)
            text = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr).group(3)
    else:
        res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr)
        date_time_utc = datetime(hour=(int(res.group(1))-user_tz) % 24, minute=int(res.group(2)),
                             year=date.year, month=date.month, day=date.day)
        text = res.group(3)
    return "at", date_time_utc, text


def parse_message(strr, user_tz):
    strr = strr.lower()
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m)\s*', strr):
        time_text = case_after(strr[strr.find("after") + len("after"):])
    elif re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr):
        time_text = case_at(strr, user_tz)
    else:
        return 0
    return {'type': time_text[0], 'time_date': time_text[1], 'text': time_text[2]}
