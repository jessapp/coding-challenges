# Remove duplicates from a linked list 

class LinkedList(object):

    def __init__(self):
        self.head = None

    def remove_duplicates(head):

        if head is None:
            raise Exception('No head')

        seen = set(head.data)

        current = head

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next

            seen.add(current.data)
            current = current.next

        return


    def alternate_remove_duplicates(head):
        # Runtime: O(n^2)

        current = head

        # Outer loop advances current 
        while current is not None:
            
            runner = current

            # Inner loop advances runner 
            while runner.next is not None:

                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next