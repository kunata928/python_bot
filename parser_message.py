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
    return set_time(data_after_parse), data_after_parse['text']


def parse_message(strr):
    strr = strr.lower()
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m)\s*', strr):
        time_text = case_after(strr[strr.find("after") + len("after"):])
    elif 0:
        pass
    else:
        return 0
    return {'time_date': time_text[0], 'text': time_text[1]}