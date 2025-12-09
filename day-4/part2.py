import sys

grid = [list(line.strip()) for line in sys.stdin if line.strip()]
rows = len(grid)
cols = len(grid[0])

# Directions: 8 neighbors
dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

def count_neighbors(r, c):
    cnt = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            cnt += 1
    return cnt

removed_total = 0

while True:
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(r, c) < 4:
                    to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = '.'
    removed_total += len(to_remove)

print(removed_total)
