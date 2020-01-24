import sys

# Recursive solution: we need to compare the root to a min and max. 
# Since those values are not provided initially, we need to subsitute
# in infinity
def validate_bst_recursive(root):
    def _check(root, min_amount, max_amount):
        if not root:
            return True

        if not min_amount < root < max_amount:
            return False

        return (
            check(root.left, min_amount, root.data) and
            check(root.right, root.data, max_amount)
        )
    return _check(root, float('-inf'), float('+inf'))


# With a stack, you don't need recursion - less expensive
# Same idea - compare the min and max against infinity initially
def validate_bst_stack(root):
    if not root:
        return True

    stack = [float('-inf'), root.data, float('+inf')]

    while stack:
        min_amount, root, max_amount = stack.pop()
        if not min_amount < root < max_amount:
            return False

        if root.left:
            stack.append(root.left, min_amount, root.data)

        if root.right:
            stack.append(root.right, root.data, max_amount)

    return True