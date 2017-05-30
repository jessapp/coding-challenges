# Find the nth largest node in a BST

# First method: In-order traversal

def nodes_in_order(root):
    """Traverse tree in order, and append nodes to a list"""

    nodes = []

    if root:

        nodes_in_order(root.left)
        nodes.append(root.data)
        nodes_in_order(root.right)

    return nodes

# def nth_largest(node_lst, n):
#     """Search list for nth largest node"""

#     final_index = len(node_lst) - 1

#     target_index = final_index - n

#     for i in range(len(node_lst)):

#         if i == target_index:
#             return node_lst[i]

# Second method: Find which side of the tree it's supposed to be on

def count_nodes(root):

    to_count = [root]

    count = 0

    while to_count != []:
        current = root.pop()
        count += 1
        to_count.extend(current.children)

    # Total count minus the root itself
    return count 



def nth_largest(root, n):

    # Check how many nodes are on the right side
    right_count = count_nodes(root.right)

    if right_count == n:
        return root

    # If it's on the right side, search the right side
    elif right_count > n:


        nodes = nodes_in_order(root.right)

        final_index = len(nodes) - 1

        target_index = final_index - n

        for i in range(len(nodes)):

            if i == target_index:
                return node_lst[i]


    # Otherwise, search the left side
    else:

        new_n = n right_count

        nodes = nodes_in_order(root.left)

        final_index = len(nodes) - 1

        target_index = final_index - new_n

        for i in range(len(nodes)):

            if i == target_index:
                return node_lst[i]
        

