# Find a path from one word to another using a word ladder

def is_diff(str1, str2):
    """Checks if two strings are different by only one character"""
    if len(str1) != len(str2):
        return False

    count = 0

    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

    if count == 1:
        return True

    return False


def transform(words, start, end):
    """Takes in a list of words, a starting word, and an ending word
    and checks for a path between the two."""

    # Begin with with a list containing the starting point
    potential_answer = [start]
    print "potential_answer", potential_answer

    results = []
    print "results", results


    def recursion(start_, end_):

        # If the start and end points are the same, add the potential answer
        # To the final list
        if start_ == end_:
            results.append(list(potential_answer))
            return

        # For each word in the list of words
        for word in words:
            print "word", word
            # If the word is off by one character from the starting point
            # And it isn't already in the potential answer
            if is_diff(word, start_) and word not in potential_answer:
                # Add it to the potential answer
                potential_answer.append(word)
                print "appended potential answer", potential_answer
                # recurse with that word as the starting point
                recursion(word, end_)
                print "recursing"
                # and then remove it from the potenential answer
                popped = potential_answer.pop()
                print "popped", popped

    # Run the recursion sub-function with the given start and end point
    recursion(start, end)
    
    return results


words = set(['damp', 'camp', 'came', 'dame', 'lame', 'lime', 'like'])
for answer in transform(words, 'damp', 'lame'):
    print(answer)