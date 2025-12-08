import heapq
import time

from ..utils.grid import get_neighbors
from ..utils.path_utils import reconstruct_path

def heuristic(a, b):
   
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):

    t0 = time.time()

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {start: 0}

    came_from = {}

    expanded = 0

    closed_set = set()

    while open_set:
      
        current_f, current = heapq.heappop(open_set)

        if current in closed_set:
            continue
        closed_set.add(current)
        expanded += 1

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            t1 = time.time()
            return {
                "found": True,
                "path": path,
                "cost": len(path) - 1,
                "expanded": expanded,
                "runtime": t1 - t0
            }

        for neighbor in get_neighbors(grid, current):
           
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current

                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    t1 = time.time()
    return {
        "found": False,
        "path": None,
        "cost": None,
        "expanded": expanded,
        "runtime": t1 - t0
    }