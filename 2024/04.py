def diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    diags = []
    for d in range(-(rows - 1), cols):
        diag = [grid[r][r - d] for r in range(max(0, d), min(rows, cols + d)) if 0 <= r - d < cols]
        diags.append("".join(diag))
    return diags


horizontal = open("input/04.txt").read().splitlines()
vertical = list(map("".join, zip(*horizontal)))
diagonals1 = diagonals(horizontal)
diagonals2 = diagonals([line[::-1] for line in horizontal])

chunks = []
for i in range(len(horizontal) - 2):
    for j in range(len(horizontal[0]) - 2):
        chunks.append([line[j : j + 3] for line in horizontal[i : i + 3]])

# part one
count = 0
for grid in (horizontal, vertical, diagonals1, diagonals2):
    for line in grid:
        for string in ("XMAS", "SAMX"):
            count += line.count(string)
print(count)

# part two
count = 0
for chunk in chunks:
    d1 = "".join(chunk[i][i] for i in range(3))
    d2 = "".join(chunk[i][2 - i] for i in range(3))
    if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
        count += 1
print(count)
