from collections import deque

def breadth_first_search(graph, start_node, goal_node):
    # Queue stores the path to the node to easily reconstruct it later
    queue = deque([[start_node]])
    
    # Set to keep track of visited nodes to avoid infinite loops/cycles
    visited = set([start_node])
    
    print(f"Starting BFS from node: {start_node}")
    
    while queue:
        # Dequeue the first path from the front of the line (FIFO)
        path = queue.popleft()
        
        # Get the last node from the current path
        current_node = path[-1]
        print(f"Visiting node: {current_node}")
        
        # Goal Test: Check if we reached our target
        if current_node == goal_node:
            return path
            
        # Expansion: Check all adjacent neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path extending to the neighbor and enqueue it
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None # Return None if no path to the goal exists

# --- Example AI State Space (Graph Representation) ---
# Visualizing a small roadmap or state tree
'''ai_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    '': [],
    'F': [],
    'G': []
}'''
ai_graph = {
    'G': ['A', 'B'],  # Godown starting point
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['S'],
    'D': ['S'],
    'E': ['F'],
    'F': ['S'],       # Destination Store
    'S': []           
}

# Find the shortest path from 'A' to 'F'
shortest_path = breadth_first_search(ai_graph, start_node='G', goal_node='S')

print("\n--- Search Result ---")
if shortest_path:
    print(f"Goal reached! Shortest path: {' -> '.join(shortest_path)}")
else:
    print("Goal could not be reached.")