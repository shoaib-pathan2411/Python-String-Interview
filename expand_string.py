def expand_string(s):
    result = ''
    i = 0
    while i < len(s):
        char = s[i]
        if i + 1 < len(s) and '0' <= s[i+1] <= '9':
            count = int(s[i+1]) 
            result += char * count
            i += 2
        else:
            result += char
            i += 1
    return result
print(expand_string('a2b3c4de1f2'))