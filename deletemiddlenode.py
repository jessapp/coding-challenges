# Given access to a node in the middle of a singly linked list (and not the head), delete that node
# The node will never be the first or last node in the linked list

def delete_middle_node(node):

    if node == None:
        raise Exception

    # Reassign the next node's data to the current node
    node.data = node.next.data

    # Delete the next node
    node.next = node.next.next

    return node