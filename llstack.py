# Implement a stack using linked lists.

class Stack(object):

    def __init__(self, data):
        # initializes nodes
        self.data = data
        self.next = None

    def push(self, data):
        self.next = data

    def pop(self):

        current = self

        # While two nodes forward exists, walk through the list
        while current.next.next is not None:
            current = current.next

        # Isolate the last node to return it
        last_node = current.next.next

        # Delete it from the linked list
        current.next.next = None

        return last_node
