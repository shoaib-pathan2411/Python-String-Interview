def is_anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    print(s1)
    print(s2)
    return sorted(s1) == sorted(s2)

print(is_anagram('listeN', 'siLent'))
print(is_anagram('heLlo', 'wOrld'))