"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst, count=0):
    """Return number of items in a list, using recursion."""

    if lst == []:
        return count

    count += 1
    return count_recursively(lst[1:], count)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
