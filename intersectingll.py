# Determine if two singly-linked lists intersect
# This is done by checking the node itself, not the node's value

def check_intersection(ll1, ll2):

    node_count = {}

    current = ll1.head

    while current is not None:
        node_count[current] = node_count.get(current, 0) + 1
        current = current.next

    new_current = ll2.head

    while new_current is not None:
        node_count[new_current] = node_count.get(new_current, 0) + 1
        new_current = new_current.next


    for node, count in node_count.items():
        if count > 1:
            return node
        else:
            return None

# def intersecting_ll(ll1, ll2):

#     ll1_count = 0
#     ll2_count = 0

#     ll1_head = ll1.head 
#     ll2_head = ll2.head 

#     while ll1_head:
#         ll1_count += 1
#         ll1_head = ll1_head.next 

#     while ll2_head:
#         ll2_head += 1
#         ll2_head = ll2_head.next 

#     diff = abs(ll1_count - ll2_count)

#     ll1_head = ll1.head 
#     ll2_head = ll2.head 

#     if ll1_count > ll2_count:
#         for i in range(diff):
#             ll1_head = ll1_head.next
#     elif ll2_count > ll1_count:
#         for i in range(diff):
#             ll2_head = ll2_head.next

#     while ll1_head:
#         if ll1_head == ll2_head:
#             return ll2_head

#     return None
