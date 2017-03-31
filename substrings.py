# Given two strings, one list is a substring of the other. Return the difference between the two strings.
# s = main string
# t = substring


s_split = s.split()
t_split = t.split()

s_dict = {}
t_dict = {}

missing_words = []

for word in s_split:
    s_dict[word] = s_dict.get(word, 0) + 1

for word in t_split:
    t_dict[word] = t_dict.get(word, 0) + 1

for word in s_split:
    if word not in t_dict or t_dict[word] == 0:
        missing_words.append(word)
    else:
        t_dict[word] = t_dict[word] - 1
        s_dict[word] = s_dict[word] - 1

return missing_words