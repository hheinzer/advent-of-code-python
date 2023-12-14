def compute_load(lines, di=[-1], dj=[0]):
    ni, nj = len(lines), len(lines[0])
    for di, dj in zip(di, dj):
        load = 0
        for i in range(0, ni)[:: -di if di != 0 else 1]:
            for j in range(0, nj)[:: -dj if dj != 0 else 1]:
                if lines[i][j] == "O":
                    ii, jj = i, j
                    while (
                        0 <= ii + di < ni
                        and 0 <= jj + dj < nj
                        and lines[ii + di][jj + dj] == "."
                    ):
                        ii, jj = ii + di, jj + dj
                    lines[i][j], lines[ii][jj] = ".", "O"
                    load += ni - ii
    return load


def find_padding_period(sequence):
    n = len(sequence)
    for i in range(0, n):
        padding = sequence[:i]
        for j in range(i + 1, n + 1):
            period = sequence[i:j]
            if len(period) <= n - len(padding) - len(period):
                is_period = True
                for k in range(j, n - ((n - len(padding)) % len(period)), len(period)):
                    is_period &= sequence[k : k + len(period)] == period
                if is_period:
                    return padding, period


# preprocess
lines = open("input/14.txt").read().splitlines()
lines = [list(line) for line in lines]

# part one
print(compute_load(lines))

# part two
loads = [compute_load(lines, [-1, 0, 1, 0], [0, -1, 0, 1]) for _ in range(250)]
padding, period = find_padding_period(loads)
print(period[((1000000000 - 1) - len(padding)) % len(period)])
