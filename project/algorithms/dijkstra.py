import heapq
import time

from ..utils.grid import get_neighbors
from ..utils.path_utils import reconstruct_path

def dijkstra(grid, start, goal):

    t0 = time.time()

    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}

    came_from = {}

    expanded = 0

    visited = set()

    while pq:
        current_g, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
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
          
            new_g = current_g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                came_from[neighbor] = current
                heapq.heappush(pq, (new_g, neighbor))

    t1 = time.time()
    return {
        "found": False,
        "path": None,
        "cost": None,
        "expanded": expanded,
        "runtime": t1 - t0
    }