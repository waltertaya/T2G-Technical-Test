#!/usr/bin/env python3

def capitalize_1st_letter(s):
    result = ''
    for string in s.split():
        result += string.capitalize() + ' '
    return result.strip()


if __name__ == '__main__':
    example = ['hello', 'i love programming', 'python is easy']
    for i in example:
        print(f'Input: {i}')
        print(f'Output: {capitalize_1st_letter(i)}')
