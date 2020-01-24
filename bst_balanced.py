def get_height(node):
    if node is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1 

def is_bst_balanced(node):
    if node is None:
        return True

    height_diff = abs(get_height(root.left) - get_height(root.right))
    if height_diff > 1:
        return False
    return is_bst_balanced(root.left) and is_bst_balanced(root.right)

