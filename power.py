# Write a function that returns a base to the power of an exponent, 
# without using the ** operator

def power(base, exp, running_total=1):

    if exp == 1:
        return running_total * base

    if exp == 0:
        return 1

    return power(base, exp -1, running_total * base)

print power(2, 3)

print power(4, 0)

print power(5, 2)
