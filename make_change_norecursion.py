# Given an amount (in cents) and a list of coin denominations, return the number of ways to make change from those denominations


def make_change(amount, denominations):

    # Initialize a list of zeroes which is one item greater than the amount 
    ways_of_doing_n_cents = [0] * (amount + 1)

    # the first item of that list is 0
    ways_of_doing_n_cents[0] = 1

    print ways_of_doing_n_cents

    # for each coin in the list of denomniations 
    for coin in denominations:
        print "Coin %s" % coin
        # for each amount in the range between that coin and amount + 1 
        for higher_amount in xrange(coin, amount + 1):
            print "Higher_amount %s" % higher_amount
            # the remainder is equal to that amount minus the value of the coin 
            remainder = higher_amount - coin
            print "Remainder %s - %s = %s" % (higher_amount, coin, remainder)
            # Add the value of the index at the amount of the remainder to the index at the value of the higher amount  
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[remainder]
            print ways_of_doing_n_cents[higher_amount]
            print ways_of_doing_n_cents

    return ways_of_doing_n_cents[amount]



print make_change(4, [1, 2, 3])