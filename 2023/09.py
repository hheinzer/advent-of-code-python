lines = open("input/09.txt").read().splitlines()


def get_value(line: str, which: str) -> int:
    seqs = [[int(val) for val in line.split()]]
    while not all(value == 0 for value in seqs[-1]):
        seqs.append([seqs[-1][i + 1] - seqs[-1][i] for i in range(len(seqs[-1]) - 1)])
    value = 0
    for seq in seqs[::-1][1:]:
        match which:
            case "next":
                value = seq[-1] + value
            case "prev":
                value = seq[0] - value
    return value


# part one
print(sum(get_value(line, "next") for line in lines))

# part two
print(sum(get_value(line, "prev") for line in lines))
