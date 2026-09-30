# A* Search Algorithm

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': ['J'],
    'I': ['K'],
    'J': ['L'],
    'K': ['L'],
    'L': []
}

# Heuristic values: h(n)
heuristic = {
    'S': 12,
    'A': 10,
    'B': 7,
    'C': 8,
    'D': 6,
    'E': 5,
    'F': 9,
    'G': 7,
    'H': 4,
    'I': 6,
    'J': 3,
    'K': 2,
    'L': 0
}


def a_star(start, goal):

    # OPEN list
    open_list = [start]

    # Nodes already explored
    closed_list = set()

    # Cost from start to each node
    g_cost = {
        start: 0
    }

    # Parent of each node
    parent = {
        start: None
    }

    while open_list:

        # Select node with smallest f(n)
        current = min(
            open_list,
            key=lambda node: g_cost[node] + heuristic[node]
        )

        open_list.remove(current)

        # Calculate f(n)
        f_cost = g_cost[current] + heuristic[current]

        print(
            "Selected:",
            current,
            "g =", g_cost[current],
            "h =", heuristic[current],
            "f =", f_cost
        )

        # Goal reached
        if current == goal:
            print("\nGoal reached!")
            break

        closed_list.add(current)

        # Explore neighbours
        for neighbour in graph[current]:

            # Every edge has cost 1
            new_g_cost = g_cost[current] + 1

            # Ignore already explored nodes
            if neighbour in closed_list:
                continue

            # If new node or cheaper path found
            if (
                neighbour not in g_cost
                or new_g_cost < g_cost[neighbour]
            ):

                g_cost[neighbour] = new_g_cost

                parent[neighbour] = current

                if neighbour not in open_list:
                    open_list.append(neighbour)

        print("OPEN:", open_list)
        print()

    # Construct final path
    if goal in parent:

        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("Final Path:")
        print(" -> ".join(path))

        print("Total Cost:", g_cost[goal])

    else:
        print("No path found.")


# Run A*
a_star('S', 'L')