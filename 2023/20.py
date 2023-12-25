import math

lines = open("input/20.txt").read().splitlines()

# build network
network = {}
for line in lines:
    node, dest = line.split(" -> ")
    if node == "broadcaster":
        type = "b"
    else:
        type, node = node[0], node[1:]
    dest, state, src = dest.split(", "), False, {}
    network[node] = (type, dest, state, src)

# register sources
for node in network:
    _, dest, _, _ = network[node]
    for d in dest:
        if d in network:
            _, _, _, src = network[d]
            src[node] = False

# prepare history
history = []


def push_button(n):
    count_low, count_high = 0, 0
    update = [["button", False, "broadcaster"]]
    while update:
        sender, pulse, receiver = update.pop(0)
        if pulse == False:
            count_low += 1
        else:
            count_high += 1
        if pulse == True and receiver == "kz":
            history.append(n)
        if receiver in network:
            type, dest, state, src = network[receiver]
            match type:
                case "b":
                    for d in dest:
                        update.append([receiver, pulse, d])
                case "%":
                    if pulse == False:
                        state = not state
                        for d in dest:
                            update.append([receiver, state, d])
                        network[receiver] = (type, dest, state, src)
                case "&":
                    src[sender] = pulse
                    pulse = False if all(src.values()) else True
                    for d in dest:
                        update.append([receiver, pulse, d])
                    network[receiver] = (type, dest, state, src)
    return count_low, count_high


# part one
total_low, total_high = 0, 0
for n in range(1, 1001):
    count_low, count_high = push_button(n)
    total_low += count_low
    total_high += count_high
print(total_low * total_high)

# part two
for n in range(1001, 5000):
    push_button(n)
print(math.lcm(*history))
