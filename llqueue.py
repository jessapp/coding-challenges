# Implement a queue using linked lists.

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self):
        # initializes ll
        self.head = None
        self.tail = None

    def enqueue(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):

        # grab first node
        first_node = self.head

        # reassign the head
        if self.head.next:
            self.head = self.head.next

        return first_node

