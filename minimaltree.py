# Minimal tree
# Given a sorted array in increasing order with unique integer elements, write an algorithm
# to create a BST with minimal height 
# assuming TreeNode class

def create_minimal_tree(lst):

    half = len(lst)/2

    node = TreeNode(lst[half])

    node.left = create_minimal_tree(lst[:half - 1])
    node.right = create_minimal_tree(lst[half + 1:])

    return node