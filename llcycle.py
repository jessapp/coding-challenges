# You have a singly-linked list and want to check if it contains a cycle.

  # class LinkedListNode:

  #   def __init__(self, value):
  #       self.value = value
  #       self.next  = None

  def contains_cycle(head):
    all_nodes = set()

    current = head

    while current is not None:
        if current in all_nodes:
            return True
        all_nodes.add(current)
        current = current.next

    return False



# Alternate solution:

# def ll_cycle(ll):
#     slow = ll.head
#     fast = ll.head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if fast == slow:
#             break

#     if not fast and not fast.next:
#         return None

#     slow = ll.head

#     while slow != fast:
#         slow = slow.next
#         fast = fast.next

#     return slow 