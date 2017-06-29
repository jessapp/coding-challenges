# Calculate the depth of a binary tree


def height(root):
    if root is None:
        return 0
    else:
        return max(height(self.left), height(self.right)) + 1