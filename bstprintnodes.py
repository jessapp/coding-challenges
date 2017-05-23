# print all nodes in binary search tree

def print_all_nodes(self):

    to_print = [self]

    while to_visit is not None:

        current = to_print.pop()

        print current

        to_print.extend(current.children)