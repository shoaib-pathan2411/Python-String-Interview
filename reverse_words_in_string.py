def reverse_words_in_string(str1):
    words = str1.split()
    # print(str1)
    rev_all = ''
    for i in range(len(words)-1,-1,-1):
          rev_all += words[i] + ' '
    return rev_all
str1 = "hello this is python"
print(reverse_words_in_string(str1)) 