def count_words(s):
    count = 0
    for i in s:
        count = count + 1
    return count

print(count_words('hello'))

def count_words(s):
    return len(s)

print(count_words('hello'))