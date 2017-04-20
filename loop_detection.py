# Loop Detection
# Given a circular linked list, return the node at the beginning of the loop

# Or: Floyd's algorthim

class LinkedList(object):

    def __init__(self):
        self.head = None

    def detect_loop(head):

        if head is None:
            raise Exception('No head')

        nodes_seen = set()

        current = head

        while current:
            if current in nodes_seen:
                return current

            nodes_seen.add(current)
            current = current.next