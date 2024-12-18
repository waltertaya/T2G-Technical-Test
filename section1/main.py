#!/usr/bin/env python3
''' Program to capitalize the first letter of each word in a given string. '''

def capitalize_1st_letter(s):
    ''' Function to capitalize the first letter of each word in a given string. '''
    result = ''
    for string in s.split():
        result += string.capitalize() + ' '
    return result.strip()


if __name__ == '__main__':
    ''' Main function to test the above function. '''
    example = ['hello', 'i love programming', 'python is easy']
    for i in example:
        print(f'Input: {i}')
        print(f'Output: {capitalize_1st_letter(i)}')
