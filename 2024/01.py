from collections import Counter

lines = [list(map(int, line.split())) for line in open("input/01.txt")]
left, right = map(sorted, zip(*lines))

# part one
print(sum(abs(a - b) for a, b in zip(left, right)))

# part two
left, right = map(Counter, (left, right))
print(sum(count * value * right[value] for value, count in left.items()))
