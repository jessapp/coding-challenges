# Find a path between two nodes in a directed graph

def find_path(graph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    shortest = None

    for node in graph[start]:

        if node not in path:

            new_path = find_path(graph, node, end, path)

            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

    return shortest