from functools import cache

lines = open("input/04.txt").read().splitlines()


def split_card(line):
    winning = line.split(":")[1].split("|")[0].split()
    numbers = line.split(":")[1].split("|")[1].split()
    return winning, numbers


# part one
def eval_card(i):
    winning, numbers = split_card(lines[i])
    points = 0
    for number in numbers:
        if number in winning:
            points = points * 2 if points > 0 else 1
    return points


print(sum(eval_card(i) for i in range(len(lines))))


# part two
@cache
def eval_card(i):
    winning, numbers = split_card(lines[i])
    count = 0
    for number in numbers:
        if number in winning:
            i += 1
            count += 1 + eval_card(i)
    return count


print(sum(eval_card(i) for i in range(len(lines))) + len(lines))
