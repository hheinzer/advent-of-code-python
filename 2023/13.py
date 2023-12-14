lines = open("input/13.txt").read().split("\n\n")
patterns = [line.strip().split("\n") for line in lines]
patterns = [[[0 if x == "." else 1 for x in y] for y in z] for z in patterns]

# part one and two
total1, total2 = 0, 0
for pattern in patterns:
    for fac, pat in [(100, pattern), (1, list(zip(*pattern)))]:
        for i in range(1, len(pat)):
            n = min(i, len(pat) - i)
            up, down = pat[i - n : i], pat[i : i + n][::-1]
            diff = sum(sum(abs(x - y) for x, y in zip(a, b)) for a, b in zip(up, down))
            if diff == 0:
                total1 += fac * i
            if diff == 1:
                total2 += fac * i
print(total1)
print(total2)
