"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

# Write a function to check if a number is prime
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Use the above function to populate a list of primes
def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []

    num = 2

    while count > 0:

        if is_prime(num):
            primes.append(num)
            count -= 1

        num += 1

    return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
