def find_duplicates_char(s):
    d = {}
    result = ''
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    # return d
    print(d)
    
    for k, v in d.items():
        if v > 1:
            result += k
    return result

print(find_duplicates_char('programming'))