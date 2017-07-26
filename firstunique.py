# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.


def first_non_repeat(string):

    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    for index, char in enumerate(string):
        if counts[char] == 1:
            return index


    return -1 


print first_non_repeat("aabbcc")
print first_non_repeat("bubble")