import numpy as np

grid = open("input/21.txt").read().splitlines()
li, lj = len(grid), len(grid[0])


def count_steps(grid, i, j, nmax):
    q = [[i, j, 0]]
    seen = set((i, j))
    count = 0
    while q:
        i, j, n = q.pop(0)
        if n > 0 and (n % 2) == (nmax % 2):
            count += 1
        if n == nmax:
            continue
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if grid[ni % li][nj % lj] != "#" and (ni, nj) not in seen:
                q.append([ni, nj, n + 1])
                seen.add((ni, nj))
    return count


# get start point
i0, j0 = next((i, j) for i, row in enumerate(grid)
              for j, c in enumerate(row) if c == "S")

# part one
print(count_steps(grid, i0, j0, 64))

# part two
assert li == lj
nmax = 26501365
xs, ys = [], []
for i in range(3):
    xs.append(i * li + nmax % li)
    ys.append(count_steps(grid, i0, j0, xs[-1]))
print(round(np.polyval(np.polyfit(xs, ys, 2), nmax)))
