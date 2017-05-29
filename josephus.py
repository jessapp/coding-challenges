"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""

class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)

    def make_list(self, n):
        """Constructs a circular doubly-linked list"""

        # Makes the first node
        first = node = prev = Node(1)

        # Makes the rest of the nodes
        for i in range(2, n + 1):

            node = Node(i, prev=prev)
            prev.next = node
            prev = node

        node.next = first
        first.prev = node

        return first


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    # make list

    node = Node.make_list(num_people)


    # skip every node that is "killed" until there is only 1 node left

    while node.next != node:

        for i in range(kill_every - 1):
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

        node = node.next

    return node.data


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
