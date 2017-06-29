# Mirror a binary tree

def mirror(root):
    if root is None:
        return

    mirror(root.left)
    mirror(root.right)

    root.left, root.right = root.right, root.left