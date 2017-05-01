#reverse a linked list in place

  # class LinkedListNode:

  #   def __init__(self, value):
  #       self.value = value
  #       self.next  = None


def reverse_in_place(head):

    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    lst.head = prev

    return lst.head