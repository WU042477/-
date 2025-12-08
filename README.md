# Path Planning Project – BFS, Dijkstra and A* Algorithms

This project implements a grid-based path planning system using three classical search algorithms: **Breadth-First Search (BFS)**, **Dijkstra**, and **A\***.  
The program loads different map files, runs the selected search algorithm, and outputs:

- The computed path  
- Path cost (number of steps)  
- Number of expanded nodes  
- Runtime  
- A visualized grid with the path drawn on it  

The project is written in Python and organized in a clean, modular directory structure for clarity and maintainability.

---

## 📁 Project Structure

project/
│
├── algorithms/
│ ├── BFS.py
│ ├── dijkstra.py
│ └── astar.py
│
├── utils/
│ ├── grid.py
│ ├── path_utils.py
│ └── timer.py
│
├── maps/
│ ├── map1.txt
│ ├── map2.txt
│ └── map3.txt
│
├── main.py
└── README.md


---

## 🔍 Folder Description

### **algorithms/**
Contains implementations of:
- **BFS** – Layer-by-layer unweighted search  
- **Dijkstra** – Uniform-cost search  
- **A\*** – Heuristic search using Manhattan distance  

### **utils/**
Helper functions:
- **grid.py** → load maps & generate neighbors  
- **path_utils.py** → reconstruct path & print map  
- **timer.py** → timing utilities  

### **maps/**
Text-based maps containing:
- `1` → obstacle  
- `0` → free space  
- `S` → start  
- `G` → goal  

### **main.py**
Entry point of the project.  
Provides a menu to run:
- A single experiment  
- All algorithms on all maps  

---

## ▶ How to Run

### **1. Make sure the folder structure is preserved.**  
### **2. Install Python 3.8+.**
### **3. Run the project (recommended):**

```bash
python -m project.main

Or run directly from inside the project folder:
python main.py


(If relative imports cause warnings, use the -m method.)

🔧 Features
✔ Supports Multiple Algorithms

BFS — baseline shortest path in unweighted grids

Dijkstra — uniform-cost search

A* — heuristic search with Manhattan distance

Each algorithm returns:

found — whether a path exists

path — full coordinate sequence

cost — number of steps

expanded — number of expanded nodes

runtime — computation time

✔ Includes Multiple Maps

map1.txt — small and simple

map2.txt — maze-like structure

map3.txt — large open space

✔ Path Visualization

The program prints the map as:

S → start
G → goal
* → path
1 → wall
0 → free cell


Example:

S***00001
1*1*01101
1*1*****1
1000000G1
111111111

✔ Experiment Mode (Run All Algorithms)

You can run all algorithms on every map using:

Algorithm, Map, Found, Cost, Expanded, Time
BFS, map1.txt, True, 14, 58, 0.0031
Dijkstra, map1.txt, True, 14, 47, 0.0024
A*, map1.txt, True, 14, 13, 0.0010
...


Great for comparison and for academic reports/presentations.

🧠 Algorithms Overview
BFS

Explores nodes level by level

Guarantees shortest path in unweighted graphs

May expand many unnecessary nodes

Dijkstra

Uses a priority queue

Expands based on lowest cumulative cost

Equivalent to BFS when all edge costs = 1

A*

Adds a heuristic (Manhattan distance)

Guides search toward the target

Usually the fastest and most efficient

📝 Notes

This project focuses on software simulation only — no hardware needed.

Maps can be modified or extended freely.

The modular structure allows easy expansion (new heuristics, new algorithms, etc.).
