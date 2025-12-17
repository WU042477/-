def reconstruct_path(came_from, start, goal):
    
    if goal not in came_from and goal != start:
        return None

    current = goal
    path = [current]

    while current != start:
        current = came_from.get(current)
        if current is None:
            return None
        path.append(current)

    path.reverse()
    return path


def print_grid_with_path(grid, path, start, goal):
    g = [row[:] for row in grid]

    if not path:
        sr, sc = start
        gr, gc = goal
        g[sr][sc] = "S"
        g[gr][gc] = "G"
        for row in g:
            print("".join(str(x) for x in row))
        return

    for cell in path:
        if cell is None:
            continue
        if not (isinstance(cell, tuple) and len(cell) == 2):
            continue

        r, c = cell
        if (r, c) != start and (r, c) != goal:
            g[r][c] = "*"

    sr, sc = start
    gr, gc = goal
    g[sr][sc] = "S"
    g[gr][gc] = "G"

    for row in g:
        print("".join(str(x) for x in row))
