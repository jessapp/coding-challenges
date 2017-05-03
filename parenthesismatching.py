# Write a function that, given a sentence like the one above, along with the 
# position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 10 (position of 
# the first parenthesis), the output should be 79 (position of the last parenthesis).

def match_parenthesis(string, paren_index):

    open_parens = 0

    position = paren_index + 1

    while position <= len(string) - 1:
        char = string[position]

        if char == "(":
            open_parens +=1
        elif char == ")":
            if open_parens == 0:
                return position
            else:
                open_parens -= 1

        position += 1