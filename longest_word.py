def longest_word(s):
    words = s.split()
    # print(words)
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word('welcome to python'))