lines = open("input/18.txt").read().splitlines()
plan = [line.split() for line in lines]

def compute(path):
    del path[-1]

    length = 0
    for i in range(len(path) - 1):
        length += abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1])
    length += abs(path[-1][0] - path[0][0]) + abs(path[-1][1] - path[0][1])

    # shoelace formula
    area = 0
    for i in range(len(path) - 1):
        area += path[i][0] * path[i + 1][1] - path[i + 1][0] * path[i][1]
    area += path[-1][0] * path[0][1] - path[0][0] * path[-1][1]
    area = abs(area) // 2

    # Pick's theorem
    return area - length // 2 + 1 + length

# part one
move = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
path = [(0, 0)]
for d, n, _ in plan:
    path.append((path[-1][0] + int(n) * move[d][0], path[-1][1] + int(n) * move[d][1]))
print(compute(path))

# part two
move = {"0": (0, 1), "2": (0, -1), "3": (-1, 0), "1": (1, 0)}
path = [(0, 0)]
for _, _, h in plan:
    d, n = h[-2], int(h[2:-2], 16)
    path.append((path[-1][0] + int(n) * move[d][0], path[-1][1] + int(n) * move[d][1]))
print(compute(path))

