# def remove_digits(s):
#     result = ''
#     for char in s:
#         if not char.isdigit():
#             result += char
#     return result

# print(remove_digits('hello123'))

## without builtin methods
def remove_digits(s):
    result = ''
    for char in s:
        # if not ('0' <= char <= '9'):
        #     result += char
        if char.isdigit() == False:
            result += char
    return result
print(remove_digits('python1234'))