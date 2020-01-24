#reverse a linked list in place

  # class LinkedListNode:

  #   def __init__(self, value):
  #       self.value = value
  #       self.next  = None


def reverse_in_place(head):

  prev = None

  while head:
    current = head 
    head = head.next
    current.next = prev
    prev = current 

  return prev 