def first_non_repeating(s):
    d= {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char]= 1
    print(d)

    # for char in s:
    #     if d[char] == 1:
    #         return char
    # return None
    for k, v in d.items():
        if v == 1:
            return k
    return None

print(first_non_repeating('swiss'))