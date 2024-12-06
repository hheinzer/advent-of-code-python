grid = [list("o" + line.strip() + "o") for line in open("input/06.txt")]
grid.insert(0, ["o"] * len(grid[0]))
grid.append(["o"] * len(grid[0]))

start = next((i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == "^")

# part one
pos, dir, seen = start, (-1, 0), set()
while grid[pos[0]][pos[1]] != "o":
    seen.add(pos)
    while grid[pos[0] + dir[0]][pos[1] + dir[1]] == "#":
        dir = (dir[1], -dir[0])
    pos = (pos[0] + dir[0], pos[1] + dir[1])
print(len(seen))

# part two
count = 0
for obstacle in seen - set(start):
    pos, dir, path = start, (-1, 0), set()
    while grid[pos[0]][pos[1]] != "o":
        path.add((pos, dir))
        while (
            grid[pos[0] + dir[0]][pos[1] + dir[1]] == "#"
            or (pos[0] + dir[0], pos[1] + dir[1]) == obstacle
        ):
            dir = (dir[1], -dir[0])
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        if (pos, dir) in path:
            count += 1
            break
print(count)
