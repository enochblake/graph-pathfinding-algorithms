def astar(graph, start, goal, heuristic):
    open_list = [start]
    closed_list = set()
    g = {start: 0}
    parents = {start: None}

    while open_list:
        # Choose the node with the lowest cost
        current = min(open_list, key=lambda x: g.get(x, float('inf')) + heuristic.get(x, float('inf')))

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue
            tentative_g = g[current] + cost

            if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                g[neighbor] = tentative_g
                parents[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None
