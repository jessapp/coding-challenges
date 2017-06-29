#Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strings):

    if not strings:
        return ''

    for i in range(len(strings[0])):
        for string in strings[1:]:
            # if i goes beyond the length of this string, or if the two letters
            # are not the same
            if i >= len(string) or string[i] != strings[0][i]:
                # return the first string up until that point
                return strings[0][:i]
    # if the first string is encompassed completely within the rest, return it            
    return strings[0]


print longest_common_prefix(["hello", "heaven", "heavy"])
