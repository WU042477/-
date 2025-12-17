from pathlib import Path


def load_map_from_txt(map_path):
    """
    map_path: e.g. 'maps/map1.txt' (relative to the project root)

    Symbols:
        '#' : obstacle / wall
        '.' : free space
        'S' : start
        'G' : goal
    """
    base_dir = Path(__file__).resolve().parent.parent  # .../project
    path = (base_dir / map_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"Map file not found: {path}")

    grid = []
    start = None
    goal = None

    with path.open("r", encoding="utf-8") as f:
        for r, line in enumerate(f):
            line = line.rstrip("\n")
            if not line:
                continue

            row = list(line)

            for c, ch in enumerate(row):
                if ch == "S":
                    start = (r, c)
                elif ch == "G":
                    goal = (r, c)

            grid.append(row)

    return grid, start, goal


def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def is_walkable(cell):
    return cell in (".", "S", "G")


def get_neighbors(grid, node):
    """
    4-connected neighbors (up/down/left/right) that are in bounds and walkable.
    """
    r, c = node
    candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

    neighbors = []
    for nr, nc in candidates:
        if in_bounds(grid, nr, nc) and is_walkable(grid[nr][nc]):
            neighbors.append((nr, nc))
    return neighbors
