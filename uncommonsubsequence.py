# Given a group of two strings, you need to find the length of the longest uncommon subsequence of 
# this group of two strings. The longest uncommon subsequence is defined as the 
# longest subsequence of one of these strings and this subsequence should not be 
# any subsequence of the other strings.

# A subsequence is a sequence that can be derived from one sequence by deleting 
# some characters without changing the order of the remaining elements. Trivially, 
# any string is a subsequence of itself and an empty string is a subsequence of any string.

# The input will be two strings, and the output needs to be the length of the 
# longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.


def longest_uncommon_subsequence(string1, string2):

    if string1 == string2:
        return -1

    if len(string1) == len(string2) and string1 != string2:
        return len(string1)

    if len(string1) != leng(string2):
        return max(len(string1), len(string2))