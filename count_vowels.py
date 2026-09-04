def count_vowels(str):
    count = 0
    vowels = 'sioue'
    for char in str:
        if char in vowels:
            count += 1
    return count
print(count_vowels('hello'))