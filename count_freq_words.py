def count_freq_words(str1):
    words = str1.split()
    # print(words)
    d = {}
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

    return d
        

print(count_freq_words('i am going to school school'))
print(count_freq_words("python django python django python"))