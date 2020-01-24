"""
Given a singly linked list, group all odd nodes together followed 
by the even nodes. Please note here we are talking about the node 
number and not the value in the nodes.

You should try to do it in place. 
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
"""

def even_odd_ll(head):
    if not head or not head.next or not head.next.next:
        return head 

    odd_head = head
    even_head = head.next
    even_head_pointer = even_head

    while even_head and even_head.next:
        odd_head.next = even_head.next
        odd_head = odd_head.next
        even_head.next = odd_head.next
        even_head = even_head.next 

    odd_head.next = even_head_pointer

    return head 