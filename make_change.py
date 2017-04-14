# Given an amount (in cents) and a list of coin denominations, return the number of ways to make change from those denominations

def make_change(amount_left, denominations, current_index):

    # We hit the amount spot on with a coin

    if amount_left == 0:
        return 1

    # We overshot the amount

    if amount_left < 0:
        return 0

    # We've reached the end of the list of denominations
    if curent_index == len(denominations):
        return 0

    current_coin = denominations[current_index]

    num_possibilities = 0

    while amount_left <= 0:
        num_possibilities += make_change(amount_left, denominations, current_index + 1)
        amount_left -= current_coin

    return num_possibilities
