"""Given linked list, reverse the nodes in this linked list in place.

Iterative solution doctest:
    
    >>> ll1 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll1.as_string()
    '123'
    >>> reverse_linked_list_in_place(ll1)
    >>> ll1.as_string()
    '321'

Recursive solution doctest:

    >>> ll2 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll2.as_string()
    '123'
    >>> reverse_linked_list_in_place_rec(ll2)
    >>> ll2.as_string()
    '321'
"""


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Iteration solution.
def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    current = lst.head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = head

    lst.head = prev


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
