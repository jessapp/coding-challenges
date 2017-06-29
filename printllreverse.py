# Print elements in a linked list in reverse order

def reverse_ll(head):

    if head == None:
        return

    reverse_ll(head.next)
    print head.data