#!/usr/bin/env python3

def capitalize_1st_letter(s):
    result = ''
    for string in s.split():
        result += string.capitalize() + ' '
    return result.strip()


if __name__ == '__main__':
    s = 'hello'
    print(capitalize_1st_letter(s))
    s = 'i love programming'
    print(capitalize_1st_letter(s))
