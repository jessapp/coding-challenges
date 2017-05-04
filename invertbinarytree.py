# invert a binary tree

def invert_tree(self, root):
    if root is not None:
        temp = root.left
        root.left = invert_tree(root.right)
        root.right = invert_tree(temp)


    return root 