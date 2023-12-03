lines = open("input/03.txt").read().splitlines()

# padding
lines = [".." + line + ".." for line in lines]
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))


def has_symbol(i, j):
    has = False
    symbol = {}
    for ii in [i - 1, i, i + 1]:
        for jj in [j - 1, j, j + 1]:
            if not lines[ii][jj].isdigit() and lines[ii][jj] != ".":
                has = True
                symbol[(ii, jj)] = lines[ii][jj]
    return has, symbol


# part one and two
sum_nums = 0
gears = {}
for i in range(1, len(lines) - 1):
    num = "0"
    add_it = False
    symbols = {}
    for j in range(1, len(lines[0]) - 1):
        if lines[i][j].isdigit():
            num += lines[i][j]
            has, symbol = has_symbol(i, j)
            add_it |= has
            symbols.update(symbol)
        else:
            if add_it:
                sum_nums += int(num)
            for key, value in symbols.items():
                if value == "*":
                    if not key in gears:
                        gears[key] = [int(num)]
                    else:
                        gears[key] += [int(num)]
            num = "0"
            add_it = False
            symbols = {}
print(sum_nums)
print(sum(num[0] * num[1] for num in gears.values() if len(num) == 2))
