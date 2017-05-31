# Implement an LRU data structure 

class LinkedListNode(object):
    """Nodes for Linked List aspect of LRU"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class LinkedList(object):
    """Linked List class for LRU"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = LinkedListNode(data)

        # Head is the first thing in our cache
        if self.head is None:
            self.head = new_node

        # new items are added to the tail 
        if self.tail is not None:
            self.tail.next = new_node

    def remove(self, data):

        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next

                if current.next is None:
                    self.tail = current
                return

            else:
                current = current.next

class LRU(object):
    """Implements an LRU using a doubly-linked list and a dictionary"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.LRU = LinkedList()

    def add_to_cache(self, key, value):

        # add a new node to the LRU

        new_node = self.LRU.append(key)

        # add the key/value to the cache, if the cache hasn't been exceeded

        if len(self.cache) < self.capacity:
            self.cache[key] = value

        else:
            # find the least recently used node
            head = self.LRU.head

            #remove from cache
            del self.cache[head.data]

            #remove from LRU
            self.LRU.remove(head.data)

            # finally, add the new node to the cache 
            self.cache[key] = value

        def move_node_up(self, data):
            """If a node is already in the cache but it's been 'used' again, move it to the tail of the ll"""

            # Start with the head of the LL
            current = self.LRU.head

            # Go through the list to find the node
            while current.next is not None:

                # when you find the node, skip over it to remove it
                if current.data == data:

                    current.prev = current.next

                current = current.next

            # finally, add it back to the end of the LRU
            self.LRU.append(data)





