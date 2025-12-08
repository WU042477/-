from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent   # project/


def load_map_from_txt(name: str):
    """
    name: 例如 'map1.txt'
    返回: grid, start, goal
    """
    path = BASE_DIR / "maps" / name

    grid = []
    start = None
    goal = None

    with path.open("r", encoding="utf-8") as f:
        rows = f.read().strip().splitlines()

    for r, line in enumerate(rows):
        row = []
        for c, ch in enumerate(line):
            if ch == "1":
                row.append(1)
            elif ch == "0":
                row.append(0)
            elif ch == "S":
                start = (r, c)
                row.append(0)
            elif ch == "G":
                goal = (r, c)
                row.append(0)
        grid.append(row)

    return grid, start, goal


def get_neighbors(grid, node):
    (x, y) = node
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    result = []
    rows = len(grid)
    cols = len(grid[0])

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            result.append((nx, ny))

    return result
