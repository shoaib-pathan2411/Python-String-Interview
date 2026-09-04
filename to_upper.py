def to_upper(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char)- 32)

        else:
            result += char
    return result

print(to_upper('helLo'))

def to_lower(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char)+ 32)
        else:
            result += char
    return result

print(to_lower('HELlO'))