def remove_specifc_char(s, ch):
    return s.replace(ch, '')
print(remove_specifc_char('hello', 'o'))


def remove_specifc_char(s,ch):
    result = ''
    for char in s:
        if char != ch:
            result = result + char
    return result
print(remove_specifc_char('hello', 'l'))