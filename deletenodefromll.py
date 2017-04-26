# Delete a node from a singly-linked list , given only a variable pointing to that node.

  # class LinkedListNode:

  #   def __init__(self, value):
  #       self.value = value
  #       self.next  = None


def delete_node(self, value):

    if current.value == value:
        current = current.next

    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next
        current = current.next