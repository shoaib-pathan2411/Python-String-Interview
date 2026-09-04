def capitalize_first(s):
    return s[0].upper() + s[1:]

print(capitalize_first('hello'))

def capitalize_first_letter(s):
    if not s:
        return s
    first = s[0]
    print(first)
    if 'a' <= first <= 'z':
        first = chr(ord(first)-32)
    return first + s[1:]

print(capitalize_first_letter('hello'))