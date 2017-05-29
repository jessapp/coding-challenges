"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # Start with the distance from first hole to the first cafe, and from
    # the last hole to the last cafe:

    distances = [cafes[0], num_holes - cafes[-1] - 1]

    for i in range(1, len(cafes)):
        # between cafes: distance is half the distance to leftward cafe
        distances.append((cafes[i] - cafes[i - 1]) // 2)

    return max(distances)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
