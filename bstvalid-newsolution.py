# def check_balanced(root, lower_bound=-float('inf'), upper_bound=float('inf')):
    
#     # base case - there is no tree, return true
#     if root.data == None:
#         return True
    
#     # If the root exceeds either bound, the tree is not valid 
#     if root.data >= upper_bound or root.data <= lower_bound:
#         return False
    
#     return check_balanced(root.left, lower_bound, root.value) and check_balanced(root.right, root.value, upper_bound)
    

# if you can't use the infinity shortcut, try this:

def check_balanced(root, lower_bound=None, upper_bound=None):

    if root.data == None:
        return True

    # if you don't have either bound yet, go on to the next node
    if not upper_bound and not lower_bound:
        return check_balanced(root.left, root.data, lower_bound) and check_balanced(root.right, upper_bound, root.data)
    
    # if you have the lower bound, check against that
    elif not upper_bound:
        if root.data < lower_bound:
            return False
    
    # if you have the upper bound, check against that
    elif not lower_bound:
        if root.data > upper_bound:
            return False

    # If you have both bounds, check the node in question against them
    if upper_bound and lower_bound:
        if root.data < lower_bound or root.data > upper_bound:
            return False

    # Check if both sides are true
    return check_balanced(root.left, root.data, lower_bound) and (root.right, upper_bound, root.data)