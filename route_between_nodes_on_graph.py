def route_between_two_nodes(node1, node2, graph):
    if start == end:
        return True

    queue = []

    for node in graph.get_nodes():
        node.state = "Unvisted"

    node1.state = "Visiting"

    queue.add(node1)

    while queue != []:
        node = queue.pop(0)
        if node != None:
            for adjacent_node in node.get_adjacent():
                if adjacent_node.state == "Unvisited":
                    if adjacent_node == node2:
                        return True
                    else:
                        adjacent_node.state = "Visiting"
                        queue.append(adjacent_node)
        node.state = "Visited"
    
    return False 