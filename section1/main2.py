def unique_chars_ordered(s):
    result = dict.fromkeys(s)
    for c in result.keys():
        result[c] = s.count(c)
    return result

print(unique_chars_ordered('hello'))
print(unique_chars_ordered('interview'))
