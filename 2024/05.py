from functools import cmp_to_key

input = open("input/05.txt").read().splitlines()
updates = [line.split(",") for line in input if "," in line]

rules = dict()
for a, b in [line.split("|") for line in input if "|" in line]:
    rules[(a, b)] = -1
    rules[(b, a)] = 1

key = cmp_to_key(lambda a, b: rules.get((a, b), 0))

# part one
print(sum(int(u[len(u) // 2]) for u in updates if u == sorted(u, key=key)))

# part two
print(sum(int(sorted(u, key=key)[len(u) // 2]) for u in updates if u != sorted(u, key=key)))
