import sys

# Read the grid from stdin
grid = [line.strip() for line in sys.stdin if line.strip()]

rows = len(grid)
cols = len(grid[0])

# 8-direction neighbor offsets (around a cell)
DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols

answer = 0

for r in range(rows):
    for c in range(cols):
        # We only care about @ cells
        if grid[r][c] != '@':
            continue

        # Count @ neighbors
        neigh_at = 0
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and grid[nr][nc] == '@':
                neigh_at += 1

        # Accessible condition: fewer than 4 @ neighbors
        if neigh_at < 4:
            answer += 1

print(answer)
