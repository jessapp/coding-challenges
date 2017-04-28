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

# def contains_cycle(head):
#     slow_runner = head
#     fast_runner = head

#     while fast_runner is not None and fast_runner.next is not None:
#         slow_runner = slow_runner.next
#         fast_runner = fast_runner.next.next

#     if fast_runner == slow_runner:
#         return True

#     return False