import numpy as np


def compute_total_distance(universe, rows, cols, scale):
    galaxies = np.where(universe == 1)
    galaxies = [
        (
            a[0] + (scale - 1) * np.count_nonzero(rows <= a[0]),
            a[1] + (scale - 1) * np.count_nonzero(cols <= a[1]),
        )
        for a in zip(*galaxies)
    ]
    total = 0
    for i, a in enumerate(galaxies):
        for j, b in enumerate(galaxies):
            total += abs(a[0] - b[0]) + abs(a[1] - b[1]) if i <= j else 0
    return total


lines = open("input/11.txt").read().splitlines()
universe = np.array([[1 if char == "#" else 0 for char in line] for line in lines])

# find empty rows and columns
rows = np.array([i for i in range(universe.shape[0]) if all(universe[i, :] == 0)])
cols = np.array([i for i in range(universe.shape[1]) if all(universe[:, i] == 0)])

# part one
print(compute_total_distance(universe, rows, cols, 2))

# part two
print(compute_total_distance(universe, rows, cols, 1000000))
