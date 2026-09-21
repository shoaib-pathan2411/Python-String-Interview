# def expand_string(s):
#     result = ''
#     i = 0
#     while i < len(s):
#         char = s[i]
#         # if i + 1 < len(s) and '0' <= s[i+1] <= '9':
#         if i + 1 < len(s) and s[i+1].isdigit():
#             count = int(s[i+1]) 
#             result += char * count
#             i += 2
#         else:
#             result += char
#             i += 1
#     return result
# print(expand_string('a2b3c4de1f2'))


def expand_string(str):
  result = []
  i = 0
  while i < len(str):
    if i + 1 < len(str):
      char = str[i]
      nxt = str[i+1]
      if char.isalpha() and nxt.isdigit():
        result.append(char * int(nxt))
        i += 2
      elif char.isdigit() and nxt.isalpha():
        result.append(nxt * int(char))
        i += 2
      else:
        result.append(char)
        i += 1
    else:
      result.append(str[i])
      i += 1

  return ''.join(result)
        
print(expand_string('a2b3c4de1f2'))
print(expand_string('1a2b3c4de'))