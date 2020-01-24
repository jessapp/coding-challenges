def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# def dfs_recursive(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


def bfs(graph, start):
    visited, queue = set(), [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited