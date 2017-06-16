# Write code to partition a linked list around the value X. All nodes less than
# X go before X, and all greater than X go after X
# Assume Linked List node class
# Partition element can appear anywhere in the "greater than" half, doesn't have to be
# In the middle

def ll_partition(head, partition):

    lesser_than_start = None
    lesser_than_end = None

    greater_than_start = None
    greater_than_end = None

    current = head

    while current:
        if current < partition:
            if lesser_than_start == None:
                lesser_than_start = current
                lesser_than_end = current
            else:
                lesser_than_end.next = current
                lesser_than_end = current

        elif current >= partition:
            if greater_than_start == None:
                greater_than_start = current
                greater_than_end = current
            else:
                greater_than_end.next = current
                greater_than_end = current

        current = current.next

    # combine the two lists
    lesser_than_end.next = greater_than_start

    return lesser_than_start
