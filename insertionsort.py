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

    # starting at the second number in the list
    for index in range(1, len(alist)):
        print "index", index

        # find the current value at that index
        current_value = alist[index]
        print "current val", current_value
        position = index

        # while the index is greater than 0 AND and previous number is greater than
        # the current number
        while position > 0 and alist[position - 1] > current_value:
            print "left val", alist[position - 1]
            # put the previous number at this position 
            alist[position] = alist[position - 1]
            # and move the position backward to the left
            position = position - 1
            print "position", position
            print "alist", alist

        # Once the number is 
        alist[position] = current_value
        print "current val", current_value

    return alist


print insertion_sort([32, 15, 67, 34, 9])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
