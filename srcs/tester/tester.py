FILENAME = "test_parser.txt"


def parse_test(str):
    if "in" in str.lower():
        pass
    elif "after" in str.lower():
        pass
    pass


def check_tests(filename):
    tests_marks = [[]]
    pull_tests = open(filename, 'r')
    i = 1
    for test in pull_tests:
        try:
            parse_test(test)
            tests_marks.append([i, test, "ok"])
        except:
            tests_marks.append([i, test, "NO"])
    pull_tests.close()
    return tests_marks


if __name__ == "__main__":
    res = check_tests(FILENAME)
    print(res)