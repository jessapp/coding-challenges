"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    for i in range(1, len(alist)):

        j = i - 1
        while j >= 0 and alist[j] > alist[i]:
            j -= 1
        j += 1


        if j != i:
            alist[j:i + 1] = alist[i:i + 1] + alist[j:i]

    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
