# Write a function to find the 2nd largest element in a binary search tree

#   class BinaryTreeNode:

#     def __init__(self, value):
#         self.value = value
#         self.left  = None
#         self.right = None

#     def insert_left(self, value):
#         self.left = BinaryTreeNode(value)
#         return self.left

#     def insert_right(self, value):
#         self.right = BinaryTreeNode(value)
#         return self.right


# To find largest node: 

def find_largest(root):

    current = root

    while current:
        if not current.right:
            return current.value
        current = current.right
   

def find_second_largest(root, parent=None):

    # Raise exception if tree isn't large enough
    if root == None or (root.left == None and root.right == None):
        raise Exception('Tree requires at least two nodes')

    current = root

    while current:

        # If there is a left subtree but not a right subtree, the second largest element is the largest in the left subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # If the next right value is the last right value, and there is no left subtree, this is the second to largest value
        if current.right and not current.left.right and not current.right.right:
            return current.value

        current = current.right

   