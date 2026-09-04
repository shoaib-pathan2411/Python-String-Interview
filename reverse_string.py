# def reverse_string(str):
#     s = str[::-1]
#     return s

# print(reverse_string('hello'))

def reverse_string(str):
    rev_str = ''
    for i in str:
        rev_str = i + rev_str

    return rev_str
print(reverse_string('hello world'))
