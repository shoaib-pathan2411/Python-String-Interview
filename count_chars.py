def count_chars(s):
    d = {}
    for char in s:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1
    return d

print(count_chars('hello'))