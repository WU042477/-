def reconstruct_path(came_from, start, goal):
    
    current = goal
    path = [current]

    while current != start:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def print_grid_with_path(grid, path, start, goal):
  
    g = [row[:] for row in grid]

    if path is not None:
        for r, c in path:
            g[r][c] = "*"

    sr, sc = start
    gr, gc = goal
    g[sr][sc] = "S"
    g[gr][gc] = "G"

    for row in g:
        print("".join(str(x) for x in row))
