# Representing the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # 1. Mark the current node as visited
    visited.add(start_node)
    print(start_node, end=" -> ")
    
    # 2. Recur for all unvisited neighboring nodes
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run the program starting from node 'A'
print("DFS Traversal Order:")
dfs(graph, 'A')
print("End")