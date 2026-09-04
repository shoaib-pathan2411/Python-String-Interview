def comman_letters(str1,str2):
    result = ''
    for char in str1:
        if char in str2 and char not in result:
            result += char
    return result

print(comman_letters('s1','s2'))
print(comman_letters('Hello','World'))