# “Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop”


# Solution: we want two pointers, one which goes twice as fast as the other
# when the two meet, bring the slow pointer back to the beginning and move them at the 
# same time until they meet. This is the collision point 

def circular_linked_list(ll):
    slow = ll.head
    fast = ll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast and not fast.next:
        return None

    slow = ll.head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast 