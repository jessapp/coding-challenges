# Implement an algorithm to print all valid (properly opened and closed) combinations of 
# n pairs of parentheses

def parens(n, left=0, right=0, string=''):

    # base case
    if n == left and left == right:
        return {string}

    # Update = extend, for sets
    results = set()

    if left > right:
        results.update(parens(n, left, right + 1, string + ')'))

    if left < n:
        results.update(parens(n, left + 1, right, string + '('))

    return results


print parens(3)