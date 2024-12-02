reports = [list(map(int, line.split())) for line in open("input/02.txt")]


def check1(report):
    diffs = [b - a for a, b in zip(report[:-1], report[1:])]
    if all(diff > 0 for diff in diffs) or (all(diff < 0 for diff in diffs)):
        if all(1 <= abs(diff) <= 3 for diff in diffs):
            return 1
    return 0


def check2(report):
    if check1(report):
        return 1
    for i in range(len(report)):
        if check1(report[:i] + report[i + 1 :]):
            return 1
    return 0


# part one
print(sum(check1(report) for report in reports))

# part two
print(sum(check2(report) for report in reports))
