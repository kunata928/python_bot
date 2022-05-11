from datetime import datetime, timedelta
import re


FILENAME = "test_parser.txt"


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


def case_at(strr):
    date = datetime.now().date()
    res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr)
    if res:
        date_time = datetime(hour=res.group(1), minute=res.group(2), year=date.year, month=date.month, day=date.day)
    print(date_time)
    return date_time, res.group(3)


def parse_message(strr):
    strr = strr.lower()
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m)\s*', strr):
        time_text = case_after(strr[strr.find("after") + len("after"):])
    elif re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr) or\
            re.search(r'\s*at\s*(0[0-9]|1[0-9]|2[0-3]|[0-9])(.*)', strr):
        time_text = case_at(strr)
    else:
        return 0
    return {'time_date': time_text[0], 'text': time_text[1]}


def check_tests(filename):
    tests_marks = [[]]
    pull_tests = open(filename, 'r')
    i = 1
    for test in pull_tests:
        try:
            parse_message(test)
            tests_marks.append([i, test, "ok"])
        except:
            tests_marks.append([i, test, "NO"])
    pull_tests.close()
    return tests_marks


if __name__ == "__main__":
    # res = check_tests(FILENAME)
    strr = "at 10 59 go to hour gym"
    print("Input text: " + strr)
    res = re.search(r'\s*at\s*([0-9]|0[0-9]|1[0-9]|2[0-3])[:.\-, ]([0-5][0-9])(.*)', strr)
    res2 = re.search(r'\s*at\s*(0[0-9]|1[0-9]|2[0-3]|[0-9])(.*)', strr)
    print(res.group(1), res.group(2), res.group(3))
    # parse_message(strr)
    # print(str[str.lower().find("after") + len("after"):])
    # res = 0
    # print(res)