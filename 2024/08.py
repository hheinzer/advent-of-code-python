from itertools import combinations

grid = [list(line.strip()) for line in open("input/08.txt")]
nr, nc = len(grid), len(grid[0])
freqs = list(set(sum(grid, [])) - {"."})


def inside(p):
    return 0 <= p[0] < nr and 0 <= p[1] < nc


def locations(start, stop):
    loc = set()
    for f in freqs:
        pos = [(i, line.index(f)) for i, line in enumerate(grid) if f in line]
        for a, b in combinations(pos, 2):
            dr, dc = b[0] - a[0], b[1] - a[1]
            l1, l2, n = a, b, start
            while inside(l1) or inside(l2):
                l1 = (a[0] - n * dr, a[1] - n * dc)
                l2 = (b[0] + n * dr, b[1] + n * dc)
                if inside(l1):
                    loc.add(l1)
                if inside(l2):
                    loc.add(l2)
                if stop is not None and n >= stop:
                    break
                n += 1
    return loc


# part one
print(len(locations(1, 1)))

# part two
print(len(locations(0, None)))
