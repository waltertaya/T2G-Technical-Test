from collections import OrderedDict

def unique_chars_ordered(s):
    result = {}
    print(type(OrderedDict.fromkeys(s)))
    for c in OrderedDict.fromkeys(s):
        result[c] = s.count(c)
    return result

print(unique_chars_ordered('hello'))
print(unique_chars_ordered('interview'))
