"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

def invert_binary_tree(root):
    if root:
        root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
        return root 