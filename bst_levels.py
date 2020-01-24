"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

def bst_levels(root):
    if not root:
        return []

    ret, current_level = [], [root]

    while current_level:
        ret.append([node.val for node in current_level])
        temp = []
        for node in current_level:
            temp.extend([node.left, node.right])

        current_level = [leaf for leaf in temp if leaf]

    return ret 
