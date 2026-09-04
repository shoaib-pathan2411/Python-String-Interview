def remove_spaces(s):
    result = ''
    for char in s:
        if char != ' ':
            result = result + char
    return result
print(remove_spaces('he ll o'))

def remove_spaces1(s):
    result = ''
    for char in s:
        if char not in [' ', '\t', '\n']:
            result = result + char
    return result
print(remove_spaces1('he ll o'))
    