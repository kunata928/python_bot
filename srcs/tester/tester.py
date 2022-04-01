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
    set_time(data_after_parse)


def parse_text(strr):
    strr = strr.lower()
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m)\s*', strr):
        case_after(strr[strr.find("after") + len("after"):])
    elif 0:
        pass
    else:
        print("try again smth like that: 'After 10 min remind make coffee'")


def check_tests(filename):
    tests_marks = [[]]
    pull_tests = open(filename, 'r')
    i = 1
    for test in pull_tests:
        try:
            parse_text(test)
            tests_marks.append([i, test, "ok"])
        except:
            tests_marks.append([i, test, "NO"])
    pull_tests.close()
    return tests_marks


if __name__ == "__main__":
    # res = check_tests(FILENAME)
    strr = "After 10 m go to gym"
    print("Input text: " + strr)
    parse_text(strr)
    # print(str[str.lower().find("after") + len("after"):])
    # res = 0
    # print(res)
