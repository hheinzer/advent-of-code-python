from functools import reduce

lines = open("input/06.txt").read().splitlines()

time = [int(val) for val in lines[0].split(":")[1].split()]
dist = [int(val) for val in lines[1].split(":")[1].split()]


def s(t, T):
    return t * (T - t)


def count(T, D): # Oh mein Gott, pq-Formel :O
    t0 = (T - (T**2 - 4 * D) ** 0.5) / 2
    t1 = (T + (T**2 - 4 * D) ** 0.5) / 2
    t0 = min(t for t in range(round(t0) - 2, round(t0) + 2) if s(t, T) > D)
    t1 = max(t for t in range(round(t1) - 2, round(t1) + 2) if s(t, T) > D)
    return t1 - t0 + 1


# part one
print(reduce(lambda a, b: a * b, [count(T, D) for T, D in zip(time, dist)]))

# part two
print(count(int("".join(map(str, time))), int("".join(map(str, dist)))))
