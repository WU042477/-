Path Planning Project – BFS, Dijkstra and A* Algorithms

This project implements a grid-based path planning system using several classical search algorithms: Breadth-First Search (BFS), Dijkstra, and A*.
The program loads different map files, runs the selected search algorithm, and outputs the resulting path, cost, number of expanded nodes, and runtime.

The project is written in Python and organized in a modular structure for clarity and maintainability.

📁 Project Structure
project/
│
├── algorithms/
│   ├── BFS.py
│   ├── dijkstra.py
│   └── astar.py
│
├── utils/
│   ├── grid.py
│   ├── path_utils.py
│   └── timer.py
│
├── maps/
│   ├── map1.txt
│   ├── map2.txt
│   └── map3.txt
│
├── main.py
└── README.md

🔍 Folder Description

algorithms/
Implementation of BFS, Dijkstra, and A* search algorithms.

utils/
Helper functions for grid loading, path reconstruction, printing paths, and general utilities.

maps/
Contains the test maps in .txt format.
Maps may include:

1 → obstacle

0 → free space

S → start

G → goal

main.py
Entry point of the program. Provides a simple menu to run a single experiment or all algorithms on all maps.

▶ How to Run
1. Make sure your folder structure is preserved.
2. Install Python 3.8+.
3. Run the program (module mode is recommended):
python -m project.main


or if the project folder is your working directory:

python main.py


(If relative imports cause warnings, use the first method.)

🔧 Features
✔ Supports multiple algorithms

BFS — baseline shortest path on unweighted grids

Dijkstra — uniform-cost search

A* — heuristic search with Manhattan distance

All algorithms return:

whether a path was found

the full path (as coordinates)

path cost (number of steps)

number of expanded nodes

total runtime

✔ Multiple maps included

maps/map1.txt – simple small map
maps/map2.txt – maze-like map
maps/map3.txt – large open-space map

✔ Path Visualization

When a path is found, the program prints the map with:

S → start

G → goal

* → path

1 → wall

0 → empty grid

✔ Experiment Mode

You can run all algorithms on all maps:

Algorithm, Map, Found, Cost, Expanded, Time
BFS, maps/map1.txt, True, 14, 58, 0.0031
Dijkstra, maps/map1.txt, True, 14, 47, 0.0024
A*, maps/map1.txt, True, 14, 13, 0.0010
...


This is useful for comparing performance and preparing reports or presentations.

🧠 Algorithms Overview
BFS

Expands nodes in layers

Guaranteed shortest path in unweighted grids

Often expands many unnecessary nodes

Dijkstra

Uses a priority queue

Explores based on lowest cumulative cost

Equivalent to BFS for uniform cost = 1

A*

Adds heuristic (Manhattan distance)

Focuses search toward the goal

Usually fastest with the least expanded nodes

📌 Example Output (A*)
Algorithm: A*
Found path: Yes
Cost: 26
Expanded nodes: 83
Runtime: 0.0024s

S***00001
1*1*01101
1*1*****1
1000000G1
111111111

📝 Notes

This project focuses on software simulation (no hardware required).

Maps can be replaced or extended for further testing.

The code is modular, so algorithms or heuristics can be extended easily.