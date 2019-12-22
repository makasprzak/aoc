import re


def is_within_range(number, range):
    p = re.compile('(\d+)-(\d+)')
    start, stop = p.findall(range)[0]
    return int(stop) > number > int(start)


def has_adjacent_digits(number):
    s_num = str(number)
    i = 2
    blacklisted = 'x'
    while i < len(s_num) + 1:
        if blacklisted != s_num[i-2]:
            blacklisted = 'x'
            if s_num[i-2] == s_num[i-1]:
                if i == len(s_num) or s_num[i-1] != s_num[i]:
                    return True
                else:
                    blacklisted = s_num[i]
        i+=1
    return False


def never_decreases(number):
    s_num = str(number)
    last_char = s_num[0]
    for c in s_num[1:]:
        if c < last_char:
            return False
        last_char = c
    return True

def is_six_digit(number):
    return len(str(number)) == 6

def count(given_range):
    p = re.compile('(\d+)-(\d+)')
    start, stop = p.findall(given_range)[0]
    c = 0
    start_i = int(start)
    stop_i = int(stop)
    for i in range(start_i, stop_i):
        if is_six_digit(i) and has_adjacent_digits(i) and never_decreases(i):
            c+=1
    return c
