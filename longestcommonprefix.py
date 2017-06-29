#Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strings):

    if not strings:
        return ''

    min_count = len(strings[0])

    shortest = strings[0]

    for string in strings:
        if len(string) < min_count:
            min_count = len(string)
            shortest = string

    for i in range(len(shortest)):
        for string in strings:
            if string[i] != shortest[i]:
                if i > 0:
                    return shortest[:i]
                else:
                    return ''
        return shortest

