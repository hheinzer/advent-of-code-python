lines = open("test/22.txt").read().splitlines()
bricks = [[list(map(int, ab.split(",")))
           for ab in line.split("~")] for line in lines]


def overlap(a, b):
    return max(a[0][0], b[0][0]) <= min(a[1][0], b[1][0]) \
        and max(a[0][1], b[0][1]) <= min(a[1][1], b[1][1])


# drop bricks
bricks.sort(key=lambda x: x[0][2])
for i, a in enumerate(bricks):
    zmax = 1
    for b in bricks[:i]:
        if overlap(a, b):
            zmax = max(zmax, b[1][2] + 1)
    a[1][2] -= a[0][2] - zmax
    a[0][2] = zmax
bricks.sort(key=lambda x: x[0][2])

# find supporting bricks
brick_supports = {i: set() for i in range(len(bricks))}
brick_is_supported_by = {i: set() for i in range(len(bricks))}
for i, a in enumerate(bricks):
    for j, b in enumerate(bricks[:i]):
        if overlap(a, b) and a[0][2] == b[1][2] + 1:
            brick_supports[j].add(i)
            brick_is_supported_by[i].add(j)
print(brick_supports)
print(brick_is_supported_by)

# part one
total = 0
for i in range(len(bricks)):
    if all(len(brick_is_supported_by[j]) >= 2 for j in brick_supports[i]):
        total += 1
print(total)

# part two
total = 0
for i in range(len(bricks)):
    q = [j for j in brick_supports[i] if len(brick_is_supported_by[j]) == 1]
    falling = set(q)
    falling.add(i)
    while q:
        j = q.pop(0)
        for k in brick_supports[j] - falling:
            if brick_is_supported_by[k] <= falling:
                q.append(k)
                falling.add(k)
    total += len(falling) - 1
print(total)
