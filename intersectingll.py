# Determine if two singly-linked lists intersect
# This is done by checking the node itself, not the node's value

def check_intersection(ll1, ll2):

    node_count = {}

    current = ll1.head

    while current is not None:
        node_count[current] = node_count.get(current, 0) + 1
        current = current.next

    new_current = ll2.head

    while new_current is not None:
        node_count[new_current] = node_count.get(new_current, 0) + 1
        new_current = new_current.next


    for node, count in node_count.items():
        if count > 1:
            return node
        else:
            return None