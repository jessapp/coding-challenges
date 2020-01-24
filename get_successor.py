# Write an algorithm to find the "next" node (in-order traversal) of a bst

def in_order_successor(node):
    if not node:
        return None

    # If the node has a right tree, return leftmost succssor of right tree
    if node.right:
        return get_leftmost_child(node.right)
    else:
        current = node
        parent = current.parent

        # Go up until we're on the left instead of the right
        while parent and parent.left != current:
            current = parent
            parent = parent.parent

        return parent

def get_leftmost_child(node):
    if not node:
        return None

    while node.left:
        n = n.left

    return n