input = open("input/01.txt").read().splitlines()

expenses_l = [int(line) for line in input]
expenses_s = set(expenses_l)

# part one
for a in expenses_l:
    if 2020 - a in expenses_s:
        print(a * (2020 - a))
        break

# part two
for i, a in enumerate(expenses_l):
    for j, b in enumerate(expenses_l):
        if i != j and 2020 - a - b in expenses_s:
            print(a * b * (2020 - a - b))
            break
    else:
        continue
    break
