import re

input = open("input/03.txt").read().replace("\n", "")

pattern = r"mul\((\d+),(\d+)\)"
filter = r"don't\(\).*?(do\(\)|$)"

# part one
print(sum(int(a) * int(b) for a, b in re.findall(pattern, input)))

# part two
print(sum(int(a) * int(b) for a, b in re.findall(pattern, re.sub(filter, "", input))))
