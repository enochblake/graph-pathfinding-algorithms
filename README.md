# 🔍 Graph Pathfinding Algorithms Visualizer

This project demonstrates two powerful graph pathfinding algorithms: **A\*** and **Simulated Annealing**. It provides visual comparisons of both algorithms' outputs on a graph defined in a JSON file.

---

## 📌 Features

- **A\* Search Algorithm**  
  An optimal pathfinding algorithm using cost + heuristic to determine the shortest path.

- **Simulated Annealing**  
  A probabilistic technique to approximate the shortest path, useful in large or complex graphs.

- **Graph Visualization**  
  Uses `networkx` and `matplotlib` to display:
  - Nodes and weighted edges
  - Paths discovered by each algorithm:
    - A\* in **Green**
    - Simulated Annealing in **Orange Dashed**

- **JSON-based Input**  
  Easily configurable graph via `sample_graph.json`.

---

## 🛠 Technologies Used

- **Python** – Programming language used
- **NetworkX** – For graph structures and operations
- **Matplotlib** – For visual representation
- **JSON** – For loading the graph data

---

## 📂 Project Structure

## How to Run
**Clone the repository**
git clone https://github.com/enochblake/graph-pathfinding-algorithms.git
cd graph-pathfinding-algorithms

**Install dependencies**
pip install matplotlib networkx

**Run the program**
python main.py
The program will display a graph and highlight both A* and Simulated Annealing paths visually.

## Future Improvements
Add support for directed/undirected toggle

Implement Dijkstra’s and BFS algorithms for comparison

Interactive GUI for dynamic graph creation

Animation of step-by-step pathfinding progress

👨‍💻 Author
Enoch Kibet


