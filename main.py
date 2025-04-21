import json
import networkx as nx
import matplotlib.pyplot as plt
from astar import astar
from simulated_annealing import simulated_annealing

# Load graph
with open("sample_graph.json") as f:
    graph = json.load(f)

# Define heuristics
heuristic = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 0
}

# Run algorithms
start, goal = "A", "D"
astar_path = astar(graph, start, goal, heuristic)
sa_path = simulated_annealing(graph, start, goal)

# Display paths in console
print("A* Path Found:", astar_path)
print("Simulated Annealing Path Found:", sa_path)

# Build graph for visualization
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)

# Draw base graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Highlight A* path
if astar_path:
    astar_edges = list(zip(astar_path, astar_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=astar_path, node_color='green')
    nx.draw_networkx_edges(G, pos, edgelist=astar_edges, edge_color='green', width=2)

# Highlight Simulated Annealing path
if sa_path:
    sa_edges = list(zip(sa_path, sa_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=sa_path, node_color='orange')
    nx.draw_networkx_edges(G, pos, edgelist=sa_edges, edge_color='orange', width=2, style='dashed')

plt.title("A* Path (Green) vs Simulated Annealing Path (Orange Dashed)")
plt.tight_layout()
plt.show()
