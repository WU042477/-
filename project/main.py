from .algorithms.BFS import bfs
from .algorithms.dijkstra import dijkstra
from .algorithms.astar import a_star

from .utils.grid import load_map_from_txt
from .utils.path_utils import print_grid_with_path
from .utils.visualization import print_map_raw, print_map_semi_pretty, print_map_pretty

MAPS = {
    "1": ("maps/map1.txt", "Map 1 (Easy)"),
    "2": ("maps/map2.txt", "Map 2 (Maze)"),
    "3": ("maps/map3.txt", "Map 3 (Large)"),
}

ALGORITHMS = {
    "1": ("BFS", bfs),
    "2": ("Dijkstra", dijkstra),
    "3": ("A*", a_star),
}


def choose_map():
    print("\nSelect a map:")
    print("1. map1.txt  (Easy)")
    print("2. map2.txt  (Maze)")
    print("3. map3.txt  (Large)")
    choice = input("Enter 1/2/3: ").strip()

    if choice not in MAPS:
        print("Invalid input. Defaulting to map1.txt (Easy).")
        choice = "1"

    return MAPS[choice]


def choose_algorithm():
    print("\nSelect an algorithm:")
    print("1. BFS")
    print("2. Dijkstra")
    print("3. A*")
    choice = input("Enter 1/2/3: ").strip()

    if choice not in ALGORITHMS:
        print("Invalid input. Defaulting to BFS.")
        choice = "1"

    return ALGORITHMS[choice]


def safe_load_map(map_path):
    grid, start, goal = load_map_from_txt(map_path)

    if not grid:
        print(f"[ERROR] Failed to load map (empty grid): {map_path}")
        return None, None, None

    if start is None or goal is None:
        print(f"[ERROR] start/goal not found in: {map_path}")
        print(f"        start={start}, goal={goal}")
        print("        Ensure the map contains exactly one 'S' and one 'G'.")
        return None, None, None

    return grid, start, goal


def run_single():
    map_path, map_desc = choose_map()
    grid, start, goal = safe_load_map(map_path)
    if grid is None:
        return

    algo_name, algo_fn = choose_algorithm()

    print(f"\nRunning {algo_name} on {map_desc} ...")
    result = algo_fn(grid, start, goal)

    print("\n========== Result ==========")
    print(f"Algorithm:      {algo_name}")
    print(f"Map:            {map_desc} ({map_path})")
    print(f"Path found:     {result.get('found')}")
    print(f"Path cost:      {result.get('cost')}")
    print(f"Expanded nodes: {result.get('expanded')}")
    print(f"Runtime:        {result.get('runtime', 0.0):.6f} s")
    print("============================\n")

    if result.get("found"):
    path = result.get("path")

    print("\n========== Visualization ==========")

    print("\n[Figure 1] Original Map (raw):\n")
    print_map_raw(grid, start, goal)

    print("\n[Figure 2] Semi-pretty Map (symbols enhanced):\n")
    print_map_semi_pretty(grid, path, start, goal)

    print("\n[Figure 3] Final Pretty Map (color + symbols):\n")
    print_map_pretty(grid, path, start, goal, use_color=True, show_legend=True)

    print("===================================\n")
else:
    print("No path found. Visualization skipped.")



def run_all_experiments():
    algorithms = [
        ("BFS", bfs),
        ("Dijkstra", dijkstra),
        ("A*", a_star),
    ]

    print("\nAlgorithm, Map, PathFound, Cost, Expanded, RuntimeSeconds")

    for _, (map_path, map_desc) in MAPS.items():
        grid, start, goal = safe_load_map(map_path)
        if grid is None:
            continue

        for name, fn in algorithms:
            result = fn(grid, start, goal)
            print(
                f"{name}, {map_desc}, {result.get('found')}, "
                f"{result.get('cost')}, {result.get('expanded')}, "
                f"{result.get('runtime', 0.0):.6f}"
            )


def main():
    while True:
        print("\n=== Path Planning System ===")
        print("1. Run once")
        print("2. Run all experiments")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            run_single()
        elif choice == "2":
            run_all_experiments()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":

    main()
