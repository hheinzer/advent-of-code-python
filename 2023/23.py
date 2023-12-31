grid = open("input/23.txt").read().splitlines()
li, lj = len(grid), len(grid[0])
start = (0, 1)
end = (li - 1, lj - 2)


def grid_to_graph(grid):
    # find nodes where there is a fork in the path
    nodes = [start, end]
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < li and 0 <= nc < lj and grid[nr][nc] != "#":
                    neighbors += 1
            if neighbors >= 3:
                nodes.append((r, c))

    # transform grid into graph
    graph = {node: {} for node in nodes}
    for sr, sc in nodes:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}
        while stack:
            dist, r, c = stack.pop()
            if dist != 0 and (r, c) in nodes:
                graph[(sr, sc)][(r, c)] = dist
                continue
            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < li
                    and 0 <= nc < lj
                    and grid[nr][nc] != "#"
                    and (nr, nc) not in seen
                ):
                    stack.append((dist + 1, nr, nc))
                    seen.add((nr, nc))

    return graph


def dfs(graph, node, seen=set()):
    if node == end:
        return 0
    dist = -float("inf")
    seen.add(node)
    for nnode in graph[node]:
        if nnode not in seen:
            dist = max(dist, graph[node][nnode] + dfs(graph, nnode, seen))
    seen.remove(node)
    return dist


# part one
dirs = {
    ">": [(0, 1)],
    "<": [(0, -1)],
    "v": [(1, 0)],
    "^": [(-1, 0)],
    ".": [(0, 1), (0, -1), (1, 0), (-1, 0)],
}
graph = grid_to_graph(grid)
print(dfs(graph, start))

# part two
dirs = {
    ">": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "<": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "v": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "^": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    ".": [(0, 1), (0, -1), (1, 0), (-1, 0)],
}
graph = grid_to_graph(grid)
print(dfs(graph, start))
