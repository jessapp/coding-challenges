# Are two nodes in a graph connected?

class Graph(object):

    def breadth_first_search(self, node1, node2):
        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(node1)
        seen.add(node1)


        while not possible_nodes.is_empty():
            node = possible_nodes.dequeue()
            if node is node2:
                return True
            else:
                for child in node.adjacent - seen:
                    possible_nodes.enqueue(child)
                    seen.add(child)
        return False


    def depth_first_search(self, node1, node2, seen=None):
        if not seen:
            seen = set()

        if node1 is node2:
            return True

        seen.add(node1)
        for node in node1.adjacent:

            if person not in seen:
                if self.depth_first_search(person, node2, seen):
                    return True
        return False 