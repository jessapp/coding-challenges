def sum_lists(ll1, ll2):
    p1 = ll1.head
    p2 = ll2.head
    carry = 0
    final_list = LinkedList()
    while (p1 != 0) or (p2 != 0) or (carry !=0):
        Sum = carry
        If p1 != 0:
            Sum += p1.value
            p1 = p1.next
        Elif p2 != 0:
            Sum += p2.value
            p1 = p2.next 
        final_list.add_node(sum %10)
        carry = sum / 10
    return final_list 
