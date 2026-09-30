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


def greedy_best_first_search(start, goal):

    open_list = [start]
    visited = set()

    parent = {
        start: None
    }

    while open_list:

        # Select node with smallest heuristic value
        current = min(
            open_list,
            key=lambda node: heuristic[node]
        )

        open_list.remove(current)

        print("Selected:", current,
              "h =", heuristic[current])

        # Goal check
        if current == goal:
            print("Goal reached!")
            break

        visited.add(current)

        # Add neighbours
        for neighbour in graph[current]:

            if neighbour not in visited and neighbour not in open_list:

                open_list.append(neighbour)
                parent[neighbour] = current

        print("OPEN:", open_list)
        print()

    # Construct path
    if goal in parent:

        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("Final Path:")
        print(" -> ".join(path))

    else:
        print("No path found.")


# Run the algorithm
greedy_best_first_search('S', 'L')