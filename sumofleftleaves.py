# Sum of left leaves 

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

def sum_of_left_leaves(root):

    # Base case: node is none 
    if not root:
        return 0

    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_of_left_leaves(root.right)

    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)