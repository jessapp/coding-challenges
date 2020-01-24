"""Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""

def return_sum(root, l, r):
    if not root:
        return 0

    elif root.value < l:
        return return_sum(root.right, l, r)
    elif root.value > r:
        return return_sum(root.left, l, r)

    return root.value + return_sum(root.right, l, r) + return_sum(root.left, l, r)