import random
import math

def simulated_annealing(graph, start, goal, temp=10000, cooling_rate=0.003):
    current_path = [start]
    current_node = start
    visited = set(current_path)
    total_cost = 0

    while current_node != goal:
        neighbors = [node for node in graph[current_node] if node not in visited]
        if not neighbors:
            break

        next_node = random.choice(neighbors)
        cost = graph[current_node][next_node]
        delta = cost - total_cost

        if delta < 0 or math.exp(-delta / temp) > random.random():
            current_path.append(next_node)
            visited.add(next_node)
            total_cost += cost
            current_node = next_node

        temp *= 1 - cooling_rate

    if current_node == goal:
        return current_path
    else:
        return None
