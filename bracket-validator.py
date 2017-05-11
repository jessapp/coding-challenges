# Write an efficient function that tells us whether or not an input string's openers 
# and closers are properly nested.

def bracket_validator(string):

    openers_and_closers = {")": "(",
                            "}", "{",
                            "]", "["}

    stack = []

    for char in string:
        if char in openers_and_closers.values():
            stack.append(char)
        elif char in openers_and_closers:
            if stack[-1] == openers_and_closers[char]:
                stack.pop()
            else:
                return False

    if stack == []:
        return True
    else:
        return False
