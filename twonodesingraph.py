# Given a directed graph, write a function that finds whether or not there is a
# route between two nodes 

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def get_length(self):
        return len(self.queue)


class GraphNode(object):
    def __init__(self):
        self.data = data
        self.neighbors = set()
        self.visited = False

    def add_node(self, node):
        self.neighbors[self.count] = node

    def get_nodes(self):
        return self.neighbors

class Graph(object):

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_route(self, head, second_node):

        # If the two nodes are the same, return True
        if head == second_node:
            return True

        queue = Queue()

        head.visited = True

        queue.enqueue(head)

        # While there is a queue
        while len(queue) != 0:
            # inspect the last element in the queue
            node = queue.dequeue
            if node != None:
                # get it's adjacent nodes
                adjacent = node.get_nodes()
                # For those nodes, if one is the node we're looking for, return true
                for i in range(len(adjacent)):
                    if adjacent[i].visited = False:
                        if adjacent[i] == second_node:
                            return True
                        # Otherwise, add it to the queue, and mark it as visited 
                        else:
                            queue.enqueue(adjacent[i])
                        adjacent[i].visited = True
        return False

