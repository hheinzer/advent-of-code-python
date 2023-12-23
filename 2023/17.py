from heapq import heappush, heappop

lines = open("input/17.txt").read().splitlines()
grid = [list(map(int, line)) for line in lines]
li, lj = len(grid), len(grid[0])

def compute(nmax, nmin=0):
    heap = [(0, 0, 0, 0, 0, 0)]
    seen = set()
    while heap:
        loss, i, j, di, dj, n = heappop(heap)

        if i == li - 1 and j == lj - 1 and n >= nmin:
            return loss

        if (i, j, di, dj, n) in seen:
            continue

        seen.add((i, j, di, dj, n))

        if n < nmax and (di, dj) != (0, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < li and 0 <= nj < lj:
                heappush(heap, (loss + grid[ni][nj], ni, nj, di, dj, n + 1))

        if n >= nmin or (di, dj) == (0, 0):
            for ndi, ndj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (ndi, ndj) == (di, dj) or (ndi, ndj) == (-di, -dj):
                    continue

                ni, nj = i + ndi, j + ndj
                if 0 <= ni < li and 0 <= nj < lj:
                    heappush(heap, (loss + grid[ni][nj], ni, nj, ndi, ndj, 1))

# part one
print(compute(3))

# part tow
print(compute(10, 4))
