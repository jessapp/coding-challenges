# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
# E.G. if you have a tree with D depth, you'll have D linked lists

def depth(tree):

    if tree == None:
        return 0

    if tree.left == None and tree.right == None:
        return 1

    else:
        left_depth = 1 + depth(tree.left)
        right_depth = 1 + depth(tree.right)
        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth


def tree_to_linked_lists(tree, lists={}. d=None):
    if d == None:
        d = depth(tree)

    if lists.get(d) == None:
        lists[d] = LinkedList(tree.val)
    else:
        lists[d].add(tree.val)
        if d == 1:
            return lists

    if tree.left != None:
        lists = tree_to_linked_lists(tree.left, lists, d-1)
    if tree.right != None:
        lists = tree_to_linked_lists(tree.right, lists, d-1)

    return lists 