def is_substring(s, sub):
    return sub in s
print(is_substring('hello', 'll'))
print(is_substring('hello', 'world'))
def is_substring(s, sub):
    n = len(s)
    m = len(sub)
    # print(n)
    # print(m)
    for i in range(n-m+1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break

        if match:
            return True
    return False
print(is_substring('hello', 'll'))