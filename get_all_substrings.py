"""
Get all substrings of a string, including single letters
"""

def get_subs(string):
    subs = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub = string[i:j+1]
            subs.append(sub)

    return subs 