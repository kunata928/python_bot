from datetime import datetime
import re

now = datetime.now()
print(now)

FILENAME = "test_parser.txt"


def case_after(strr):
    print(strr)
    try:
        re.search(r'\d+', strr)
        num = re.search(r'\d+', strr).group()
    except:
        num = -1
    print(num)


def parse_text(strr):
    if re.search(r'\s*after\s*\d+\s*(hours|minutes|hour|minute|min|h|m|)\s*', strr.lower()):
        print("after in strr")
        case_after(strr[strr.lower().find("after") + len("after"):])
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
    strr = "after 10 min remind make coffee "
    parse_text(strr)
    # print(str[str.lower().find("after") + len("after"):])
    # res = 0
    # print(res)
