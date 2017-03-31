def Delete(head, position):
    current = head

    if position == 0:
        return head.next

    while position - 1 > 0:
        position = position -1
        head = head.next
    
    head.next = head.next.next


    return current