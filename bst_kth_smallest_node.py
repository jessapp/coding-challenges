# Find the kth smallest node in a BST

# Iterative:

def get_kth_smallest_iterative(root, k):
    stack = []
    while root and stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val
        root = root.right

# Recursive:

def get_count(node):
    if not node:
        return 0
    return get_count(node.left) + get_count(node.right) + 1

def get_kth_smallest_recursive(root, k):
    count = get_count(root.left)

    if count == k - 1:
        return root.val
    elif count > k - 1:
        return get_kth_smallest(root.left, k)
    else:
        return get_kth_smallest(root.right, k)