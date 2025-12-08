from collections import deque
import time

from ..utils.grid import get_neighbors
from ..utils.path_utils import reconstruct_path


def bfs(grid, start, goal):
   

    t0 = time.time()

    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    came_from = {}
    expanded = 0

    while queue:
        current = queue.popleft()
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
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    t1 = time.time()
    return {
        "found": False,
        "path": None,
        "cost": None,
        "expanded": expanded,
        "runtime": t1 - t0
    }
