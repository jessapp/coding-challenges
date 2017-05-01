# Write a function kth_to_last_node() that takes an integer k and the head_node 
# of a singly linked list, and returns the kth to last node in the list.

  # class LinkedListNode:

  #   def __init__(self, value):
  #       self.value = value
  #       self.next  = None

  def kth_to_last(k, head_node):
    """Takes in k and the head node of a linked list and returns the kth to
    last node"""

    # Find length of list 
    current = head_node

    length = 1

    while current.next:
        current = current.next
        length += 1

    # Target node is the node at this position
    target = length - k

    # Walk through the list again to find the target node
    current = head_node

    for i in range(target):
        current = current.next

    return current
