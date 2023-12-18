def hash(string):
    number = 0
    for char in string:
        number += ord(char)
        number *= 17
        number %= 256
    return number


sequence = open("input/15.txt").read().strip().split(",")

# part one
print(sum(hash(step) for step in sequence))

# part two
box = [[] for _ in range(256)]
for step in sequence:
    label, lense = step.split("=") if "=" in step else step.split("-")
    ibox = hash(label)
    if "-" in step and label in box[ibox]:
        ilabel = box[ibox].index(label)
        del box[ibox][ilabel : ilabel + 2]
    elif "=" in step:
        if label in box[ibox]:
            ilabel = box[ibox].index(label)
            box[ibox][ilabel + 1] = lense
        else:
            box[ibox] += [label, lense]
print(
    sum(
        (i + 1) * (j + 1) * int(lense)
        for i, lenses in enumerate(box)
        for j, lense in enumerate(lenses[1::2])
    )
)
