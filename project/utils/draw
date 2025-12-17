# project/utils/visualization.py

def _overlay_path(grid, path, start, goal, path_mark="*"):
    """Return a copied grid with path overlaid (non-destructive)."""
    g = [row[:] for row in grid]

    if path:
        for cell in path:
            if not (isinstance(cell, tuple) and len(cell) == 2):
                continue
            r, c = cell
            if (r, c) != start and (r, c) != goal:
                g[r][c] = path_mark

    sr, sc = start
    gr, gc = goal
    g[sr][sc] = "S"
    g[gr][gc] = "G"
    return g


def print_map_raw(grid, start, goal):
    """
    Figure 1: Raw/original map (no path), just show the map as stored.
    """
    g = [row[:] for row in grid]
    sr, sc = start
    gr, gc = goal
    g[sr][sc] = "S"
    g[gr][gc] = "G"
    for row in g:
        print("".join(row))


def print_map_semi_pretty(grid, path, start, goal):
    """
    Figure 2: Semi-pretty (no color).
    - Wall (#) -> █
    - Free (.) -> ·
    - Path (*) -> *
    """
    g = _overlay_path(grid, path, start, goal, path_mark="*")

    def render(ch: str) -> str:
        if ch == "#":
            return "█"
        if ch == ".":
            return "·"
        if ch == "*":
            return "*"
        return ch  # S, G

    for row in g:
        print("".join(render(ch) for ch in row))


def print_map_pretty(grid, path, start, goal, use_color=True, show_legend=True):
    """
    Figure 3: Final pretty (Unicode + optional ANSI color)
    - Wall: █ (grey)
    - Free: · (light)
    - Path: • (yellow)
    - Start: S (green)
    - Goal: G (red)
    """
    g = _overlay_path(grid, path, start, goal, path_mark="*")

    RESET = "\033[0m"

    def paint(text: str, code: str) -> str:
        if not use_color:
            return text
        return f"\033[{code}m{text}{RESET}"

    def render(ch: str) -> str:
        if ch == "#":
            return paint("█", "90")      # grey
        if ch == ".":
            return paint("·", "37")      # light
        if ch == "*":
            return paint("•", "93")      # yellow
        if ch == "S":
            return paint("S", "92")      # green
        if ch == "G":
            return paint("G", "91")      # red
        return ch

    for row in g:
        print("".join(render(ch) for ch in row))

    if show_legend:
        print("Legend: █=Wall  ·=Free  •=Path  S=Start  G=Goal")
