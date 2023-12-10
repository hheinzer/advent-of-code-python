import numpy as np

lines = open("input/10.txt").read().splitlines()


def compute_distance(map):
    map = map.copy()
    directions = {
        "|": [[-1, 0], [+1, 0]],
        "-": [[0, -1], [0, +1]],
        "L": [[-1, 0], [0, +1]],
        "J": [[-1, 0], [0, -1]],
        "7": [[+1, 0], [0, -1]],
        "F": [[+1, 0], [0, +1]],
    }
    map, pos = fill_start_tile(map)
    dist = -1 * np.ones(map.shape, dtype=int)
    dist[*pos] = 0
    next = [pos]
    while len(next) > 0:
        pos = next.pop(0)
        for dir in directions[map[*pos]]:
            new_pos = np.array(pos) + dir
            if map[*new_pos] != ".":
                if dist[*new_pos] == -1:
                    dist[*new_pos] = dist[*pos] + 1
                    next.append(new_pos)
    return dist


def fill_start_tile(map):
    pos = np.argwhere(map == "S")[0]
    up, down, left, right = "|7F", "|LJ", "-LF", "-J7"
    if map[pos[0] - 1, pos[1]] in up and map[pos[0] + 1, pos[1]] in down:
        map[*pos] = "|"
    elif map[pos[0], pos[1] - 1] in left and map[pos[0], pos[1] + 1] in right:
        map[*pos] = "-"
    elif map[pos[0] - 1, pos[1]] in up and map[pos[0], pos[1] + 1] in right:
        map[*pos] = "L"
    elif map[pos[0] - 1, pos[1]] in up and map[pos[0], pos[1] - 1] in left:
        map[*pos] = "J"
    elif map[pos[0] + 1, pos[1]] in down and map[pos[0], pos[1] - 1] in left:
        map[*pos] = "7"
    elif map[pos[0] + 1, pos[1]] in down and map[pos[0], pos[1] + 1] in right:
        map[*pos] = "F"
    return map, pos


def expand(map):
    map, pos = fill_start_tile(map)
    new_tile = {
        ".": np.array([[".", ".", "."], [".", ".", "."], [".", ".", "."]]),
        "|": np.array([[".", "|", "."], [".", "|", "."], [".", "|", "."]]),
        "-": np.array([[".", ".", "."], ["-", "-", "-"], [".", ".", "."]]),
        "L": np.array([[".", "|", "."], [".", "L", "-"], [".", ".", "."]]),
        "J": np.array([[".", "|", "."], ["-", "J", "."], [".", ".", "."]]),
        "7": np.array([[".", ".", "."], ["-", "7", "."], [".", "|", "."]]),
        "F": np.array([[".", ".", "."], [".", "F", "-"], [".", "|", "."]]),
    }
    new_map = np.zeros((map.shape[0] * 3, map.shape[1] * 3), dtype=str)
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            new_map[3 * i : 3 * i + 3, 3 * j : 3 * j + 3] = new_tile[map[i, j]]
    new_map[3 * pos[0] + 1, 3 * pos[1] + 1] = "S"
    return new_map


def floodfill(dist, pos):
    next = [pos]
    while len(next) > 0:
        pos = next.pop(0)
        for dir in [[-1, 0], [+1, 0], [0, -1], [0, +1]]:
            new_pos = np.array(pos) + dir
            if dist[*new_pos] == 1:
                dist[*new_pos] = 0
                next.append(new_pos)
    return dist


def contract(dist):
    new_dist = np.zeros((dist.shape[0] // 3, dist.shape[1] // 3), dtype=int)
    for i in range(new_dist.shape[0]):
        for j in range(new_dist.shape[1]):
            new_dist[i, j] = dist[3 * i + 1, 3 * j + 1]
    return new_dist


# pad input and create map
lines = ["." + line + "." for line in lines]
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))
map = np.array([[char for char in line] for line in lines])

# part one
print(compute_distance(map).max())

# part two
dist = compute_distance(expand(map))
dist[dist > -1] = 0
dist[[0, -1], :] = 0
dist[:, [0, -1]] = 0
dist[dist == -1] = 1
print(contract(floodfill(dist, [1, 1])).sum())
