import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue stores tuples: (cumulative_cost, current_node, path)
    priority_queue = [(0, start, [start])]
    visited = {}

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        # Goal check occurs when popping from the queue
        if node == goal:
            return cost, path

        # Expand node if we haven't found a cheaper path to it
        if node not in visited or cost < visited[node]:
            visited[node] = cost

            for neighbor, weight in graph[node].items():
                new_cost = cost + weight
                if neighbor not in visited or new_cost < visited[neighbor]:
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return float("inf"), []

# Weighted graph adjacency list representation
graph = {
    'S': {'A': 2, 'B': 5},
    'A': {'C': 3, 'D': 1},
    'B': {'D': 1},
    'C': {'G': 2},
    'D': {'G': 4},
    'G': {}
}

cost, path = uniform_cost_search(graph, 'S', 'G')
print(f"Optimal Path: {' -> '.join(path)} | Total Cost: {cost}")
# Output: Optimal Path: S -> A -> D -> G | Total Cost: 7