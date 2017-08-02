# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of 
# all left subtree node values and the sum of all right subtree node values. 
# Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.


def findTilt(self, root):

    answer = 0

    def _sum(node):

        if not node: 
            return 0

        left, right = _sum(node.left), _sum(node.right)

        answer += abs(left - right)

        return node.val + left + right

    _sum(root)

    return answer