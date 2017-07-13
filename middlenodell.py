# find the middle node in a linked list in one pass

def find_middle(head):

    fast = head
    slow = head

    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        else:
            break

    return slow


# Or, less space efficient

def find_middle(head):

    # nodes = []

    # while head:
    #     nodes.append(head)
    #     head = head.next

    # mid = len(nodes/2)

    # return nodes[mid]