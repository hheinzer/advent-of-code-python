grid = open("input/16.txt").read().splitlines()
nr, nc = len(grid), len(grid[0])

def count(r, c, dr, dc):
    seen = set()
    q = [(r, c, dr, dc)]

    def maybe_add(r, c, dr, dc):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    while q:
        r, c, dr, dc = q.pop(0)

        r += dr
        c += dc

        if r < 0 or nr <= r or c < 0 or nc <= c:
            continue

        ch = grid[r][c]
        if ch == "." or (ch == "-" and dr == 0) or (ch == "|" and dc == 0):
            maybe_add(r, c, dr, dc)
        elif ch == "/":
            dr, dc = -dc, -dr
            maybe_add(r, c, dr, dc)
        elif ch == "\\":
            dr, dc = dc, dr
            maybe_add(r, c, dr, dc)
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                maybe_add(r, c, dr, dc)

    return len({(r, c) for (r, c, _, _) in seen})

# part one
print(count(0, -1, 0, 1))

# part two
max_count = 0
for r in range(nr):
    max_count = max(max_count, count(r, -1, 0, 1))
    max_count = max(max_count, count(r, nc, 0, -1))
for c in range(nc):
    max_count = max(max_count, count(-1, c, 1, 0))
    max_count = max(max_count, count(nr, c, -1, 0))
print(max_count)
