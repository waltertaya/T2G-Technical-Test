#!/usr/bin/env python3

def unique_chars(s):
    result = {}
    s_set = set(s)
    print(s_set)
    for c in s_set:
        result[c] = s.count(c)
    return result


if __name__ == '__main__':
    print(unique_chars('hello'))
    print(unique_chars('interview'))
