# DFS traversals:
# In order: Left, root, right
# - Traverse the left subtree
# - Visit the root
# - Traverse the right subtree

# - Used for: In the case of BSTs, gets the nodes in non-decreasing order

# Preorder: Root, left, right
# - Visit the root
# - Traverse the left subtree
# - Traverse the right subtree

# - Used for: creating a copy of the tree

# Postorder: Left, right, root
# - Traverse the left subtree
# - Traverse the right subtree
# - Visit the root

# - Used for: deleting the tree. 

class Node:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value = value


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


def print_pre_order(root):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)

def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)

# Check if two binary trees are identical
def check_equal(root1, root2):
    if not root1 and not root2:
        return True

    if root1.data == root2.data:
        return check_equal(root1.left, root2.left) and check_equal(root1. right, root2.right)

    return False

# Calculate the height of a binary tree. The height is defined as the longest
# path from the root to a leaf. 
# Interesting adjustment - if you don't want to count the root node, return -1 instead of 0

def calculate_depth(root):
    if not root:
        return 0

    return max(calculate_depth(root.left), calculate_depth.root.right) + 1

# Search a binary search tree for a given value

def search(root, key):
    if not root or root.value == key:
        return root

    if key < root.value:
        return search(root.left, key)
    elif key > root.value:
        return search(root.right, key)


# Insert a new key into a binary tree

def insert(root, new_node):
    if root is None:
        root = new_node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node 
            else:
                insert(root.right, node)

        else:
            if root.left is None:
                root.left = node
            else:
                insnert(root.left, node)

# Delete a node from a binary search tree
# If the node is a leaf, it just needs to be deleted.
