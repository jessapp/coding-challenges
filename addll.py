# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single 
# digit. Add the two numbers and return it as a linked list.

class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node


def add_ll(ll1, ll2):

    current1 = ll1.head

    current2 = ll2.head

    first_vals = []

    final_lst = LinkedList()

    while current1:
        first_vals.append(current1.data)
        current1 = current1.next

    while current2:
        to_add = first_vals.pop(0)
        total = current2.data + to_add
        final_lst.append(total)
        current2 = current2.next

    return final_lst



