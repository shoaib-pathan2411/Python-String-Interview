def count_vowels(str):
    count = 0
    vowels = 'aeiou'
    for char in str:
        if char in vowels:
            count += 1
    return count
print(count_vowels('hello'))

def vowels_present(str):
    vowels = 'aeiou'
    result = []
    for char in str:
        if char in vowels and char not in result:
            result.append(char)
    return ' '.join(result)
print(vowels_present('hello'))