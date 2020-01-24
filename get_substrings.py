# Solution 1: Doesn't include single characters

# def get_substrings(string):
#     subs = []
#     for i in range(len(string)):
#         for j in range(i):
#             sub = string[j: i+1]
#             subs.append(sub)
#     return subs


# Solution 2: does include single characters 
def get_substrings(string):
    subs = []
    for i in range(len(string)):

        for j in range(i+1, len(string) + 1):

            sub = string[i:j]

            subs.append(sub)


    return subs
