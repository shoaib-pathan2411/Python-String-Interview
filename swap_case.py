#if lower then make it upper if upper make it lower
def swap_case(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
print(swap_case('heLlO123'))

## without built in methods

def swap_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char)-32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char)+32)
        else:
            result += char
    return result
print(swap_case('HeLlO3214'))