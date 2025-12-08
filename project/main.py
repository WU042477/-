import time

from .algorithms.BFS import bfs
from .algorithms.dijkstra import dijkstra
from .algorithms.astar import a_star

from .utils.grid import load_map_from_txt
from .utils.path_utils import print_grid_with_path

def choose_map():
    print("\n请选择地图:")
    print("1. map1.txt  (简单地图)")
    print("2. map2.txt  (迷宫地图)")
    print("3. map3.txt  (大地图)")
    choice = input("输入数字 1/2/3: ")

    if choice == "1":
        return "map1.txt"
    elif choice == "2":
        return "map2.txt"
    elif choice == "3":
        return "map3.txt"
    else:
        print("输入无效，默认选择 map1")
        return "map1.txt"

def choose_algorithm():
    print("\n请选择算法:")
    print("1. BFS")
    print("2. Dijkstra")
    print("3. A*")
    choice = input("输入数字 1/2/3: ")

    if choice == "1":
        return "BFS", bfs
    elif choice == "2":
        return "Dijkstra", dijkstra
    elif choice == "3":
        return "A*", a_star
    else:
        print("输入无效，默认选择 BFS")
        return "BFS", bfs



def run_single():
    
    map_path = choose_map()

    grid, start, goal = load_map_from_txt(map_path)

    algo_name, algo_fn = choose_algorithm()

    print(f"\n正在运行 {algo_name} ...")
    result = algo_fn(grid, start, goal)

    print("\n========== 运行结果 ==========")
    print(f"算法: {algo_name}")
    print(f"找到路径: {result['found']}")
    print(f"路径步数: {result['cost']}")
    print(f"扩展节点: {result['expanded']}")
    print(f"运行时间: {result['runtime']:.6f} 秒")
    print("==============================\n")

    if result["found"]:
        print("路径图如下：\n")
        print_grid_with_path(grid, result["path"], start, goal)



def run_all_experiments():
    maps = ["maps/map1.txt", "maps/map2.txt", "maps/map3.txt"]
    algorithms = [
        ("BFS", bfs),
        ("Dijkstra", dijkstra),
        ("A*", a_star)
    ]

    print("\n算法, 地图, 找到路径, 步数, 扩展节点, 时间")

    for m in maps:
        grid, start, goal = load_map_from_txt(m)

        for name, fn in algorithms:
            result = fn(grid, start, goal)
            print(f"{name}, {m}, {result['found']}, "
                  f"{result['cost']}, {result['expanded']}, "
                  f"{result['runtime']:.6f}")


def main():
    while True:
        print("\n=== 路径规划系统 ===")
        print("1. 单次运行")
        print("2. 跑全部实验")
        print("3. 退出")

        choice = input("选择功能: ")

        if choice == "1":
            run_single()
        elif choice == "2":
            run_all_experiments()
        elif choice == "3":
            print("退出系统")
            break
        else:
            print("无效输入，请重新选择")


if __name__ == "__main__":
    main()
