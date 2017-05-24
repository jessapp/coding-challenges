# calculate x to the power of n in less than O(n) time
# Also known as Exponential Squaring

def pow_recurisve(x, n):

    # Base case: if n is 1, return x
    if n == 1:
        return x

    # If n is even, recurse where x is x ^ 2 and n is halved
    if n % 2 == 0:
        return pow_recurisve(x * x, n / 2)
    # Otherwise, recurse given the following parameters
    else:
        return x * pow_recurisve(x * x, (n-1) / 2)


def pow_iterative(x, n):

    r = 1

    while n:
        print "n", n
        if n % 2 == 1:

            r *= x
            print "r", r
            n -= 1
            print "new n", n
        x *= x
        print "x", x
        n /= 2
        print "new n again", n

    return r


print pow_iterative(5, 5)
print pow_recurisve(5, 5)