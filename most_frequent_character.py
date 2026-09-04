def most_frequent_character(s):
    d = {}
    for char in s:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1
    # return d
    max_char = None
    max_count = 0

    for key in d:
        if d[key] > max_count:
            max_count = d[key]
            max_char = key
    return max_char

print(most_frequent_character('hello'))
print(most_frequent_character("banana"))