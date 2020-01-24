"""
Find the lowest common ancestor of two nodes in a binary tree.
LCA is defined as the lowest node of which they are both leaves. 

        2
    1       3
        4       5  
                    6

On this tree, the lca of 6 and 1 would be 2
The lca of 4 and 5 would be 3


"""

def lca(root, node1, node2):
    # Base case - if the root doesn't exist, return None
    if not root:
        return None

    # Base case - validate the given nodes are not the root
    if root == node1 or root == node2:
        return root 

    # recurse on all left and right subtrees
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # if left and right both return truthy values, return the root
    if left and right:
        return root 

    if not left:
        return right

    if not right:
        return left
