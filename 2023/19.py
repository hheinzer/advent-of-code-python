import re
import math

lines = open("input/19.txt").read().splitlines()
workflows, ratings = lines[: lines.index("")], lines[lines.index("") + 1:]

wf = {}
for workflow in workflows:
    key, rules = workflow[:-1].split("{")
    rules = rules.split(",")
    wf[key] = rules


def rate(key, x, m, a, s):
    rules = wf[key]
    for rule in rules[:-1]:
        cond, action = rule.split(":")
        if eval(cond):
            break
    else:
        action = rules[-1]
    if action in wf:
        return rate(action, x, m, a, s)
    return action == "A"


def count(key, part):
    ipart = {"x": 0, "m": 1, "a": 2, "s": 3}
    rules = wf[key]
    total = 0
    for rule in rules[:-1]:
        cond, action = rule.split(":")
        var, op, val = cond[0], cond[1], cond[2:]

        split = part.copy()
        if op == "<":
            split[ipart[var]] = (split[ipart[var]][0], int(val) - 1)
            part[ipart[var]] = (int(val), part[ipart[var]][1])
        else:
            split[ipart[var]] = (int(val) + 1, split[ipart[var]][1])
            part[ipart[var]] = (part[ipart[var]][0], int(val))

        if action in wf:
            total += count(action, split)
        elif action == "A":
            total += math.prod(r[1] - r[0] + 1 for r in split)

    action = rules[-1]
    if action in wf:
        total += count(action, part)
    elif action == "A":
        total += math.prod(r[1] - r[0] + 1 for r in part)

    return total


# part one
total = 0
for rating in ratings:
    x, m, a, s = map(int, re.findall(r"(\d+)", rating))
    if rate("in", x, m, a, s):
        total += sum(map(int, [x, m, a, s]))
print(total)

# part two
print(count("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))
