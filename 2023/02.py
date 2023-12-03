lines = open("input/02.txt").read().splitlines()

# part one
count = 0
for line in lines:
    id = int(line.split(":")[0].split()[1])
    line = line.split(":")[1]
    line = line.replace(";", " ")
    line = line.replace(",", " ")
    line = line.split()
    for i in range(len(line) // 2):
        match line[2 * i + 1]:
            case "red":
                if int(line[2 * i]) > 12:
                    break
            case "green":
                if int(line[2 * i]) > 13:
                    break
            case "blue":
                if int(line[2 * i]) > 14:
                    break
    else:
        count += id
print(count)

# part two
powersum = 0
for line in lines:
    id = int(line.split(":")[0].split()[1])
    line = line.split(":")[1]
    line = line.replace(";", " ")
    line = line.replace(",", " ")
    line = line.split()
    max_red = 0
    max_green = 0
    max_blue = 0
    for i in range(len(line) // 2):
        match line[2 * i + 1]:
            case "red":
                max_red = max(max_red, int(line[2 * i]))
            case "green":
                max_green = max(max_green, int(line[2 * i]))
            case "blue":
                max_blue = max(max_blue, int(line[2 * i]))
    powersum += max_red * max_green * max_blue
print(powersum)
