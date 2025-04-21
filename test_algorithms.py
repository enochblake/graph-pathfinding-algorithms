from graph_data import graph, heuristic
from astar import a_star
from simulated_annealing import simulated_annealing

def test_pathfinding():
    print("A* Search Path:")
    path = a_star(graph, heuristic, 'A', 'E')
    print(path)

    print("\nSimulated Annealing Path:")
    sa_path = simulated_annealing(graph, 'A', 'E')
    print(sa_path)

if __name__ == "__main__":
    test_pathfinding()
