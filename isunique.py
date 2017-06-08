# Implement an algorithm to see if a string has all unique characters

def is_unique(string):

    if len(string) <= 1:
        return True

    string_set = set(string)

    if len(string_set) == len(string):
        return True
    else:
        return False