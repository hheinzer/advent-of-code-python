import re, math

lines = open("input/08.txt").read().splitlines()

# parse input
steps = lines[0]
network = {}
for line in lines[2:]:
    node, left, right = re.findall(r"[A-Z,1-9]{3}", line)
    network[node] = {"L": left, "R": right}

# part one
node = "AAA"
count = 0
while node != "ZZZ":
    for step in steps:
        node = network[node][step]
        count += 1
print(count)

# part two
nodes = [node for node in network if node[-1] == "A"]
counts = [0] * len(nodes)
for i, node in enumerate(nodes):
    while node[-1] != "Z":
        for step in steps:
            node = network[node][step]
            counts[i] += 1
print(math.lcm(*counts))
