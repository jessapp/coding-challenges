
def powerset(string):

    final = []

    # Base case: if there is nothing left in the string, return the final list
    if len(string) == 0:
        final.append("")
        return final

    # the first item in the string
    first = string[0]
    print "first", first

    # everything else in the string
    rem = string[1:]
    print "rem", rem

    # recurse to find all substrings
    words = powerset(rem)
    print "words", words

    final.extend(words)


    for word in words:
        final.append(first + word)

    return final

print powerset("Hello")
# print powerset(["1", "2", "3", "4"])