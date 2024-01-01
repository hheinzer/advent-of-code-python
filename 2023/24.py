from itertools import combinations

import sympy as sp

lines = open("input/24.txt").read().splitlines()
pos = [list(map(int, line.split("@")[0].split(","))) for line in lines]
vel = [list(map(int, line.split("@")[1].split(","))) for line in lines]


def compute_2d_intersection(p0, v0, p1, v1):
    x1, x2, x3, x4 = p0[0], p0[0] + v0[0], p1[0], p1[0] + v1[0]
    y1, y2, y3, y4 = p0[1], p0[1] + v0[1], p1[1], p1[1] + v1[1]
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    s = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
    t = (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)
    return [x / denom, y / denom, s / denom, t / denom]


# part one
count = 0
for i, j in combinations(range(len(lines)), 2):
    inter = compute_2d_intersection(pos[i], vel[i], pos[j], vel[j])
    if (
        inter is not None
        and all(200000000000000 <= xy <= 400000000000000 for xy in inter[:2])
        and all(0 <= st for st in inter[2:])
    ):
        count += 1
print(count)

# part two
x, y, z, u, v, w = sp.symbols("x y z u v w")
eqns = []
for xi, yi, zi, ui, vi, wi in [[*p, *v] for p, v in zip(pos, vel)][:5]:
    eqns.append((x - xi) * (vi - v) - (y - yi) * (ui - u))
    eqns.append((y - yi) * (wi - w) - (z - zi) * (vi - v))
sol = sp.solve(eqns)[0]
print(sol[x] + sol[y] + sol[z])
