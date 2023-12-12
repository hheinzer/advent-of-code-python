from functools import cache


@cache
def count(config: str, numbers: tuple[int, ...]) -> int:
    if config == "":
        return 1 if len(numbers) == 0 else 0
    if len(numbers) == 0:
        return 0 if "#" in config else 1
    subtotal = 0
    if config[0] in ".?":
        subtotal += count(config[1:], numbers)
    if config[0] in "#?":
        if (
            # there must be enough springs left in config
            numbers[0] <= len(config)
            # all springs in block must be broken
            and "." not in config[: numbers[0]]
            # the block must be at end of config, or followed working spring
            and (numbers[0] == len(config) or config[numbers[0]] != "#")
        ):
            subtotal += count(config[numbers[0] + 1 :], numbers[1:])
    return subtotal


lines = open("input/12.txt").read().splitlines()

# pre-process
configs = [line.split()[0] for line in lines]
numbers = [tuple(map(int, line.split()[1].split(","))) for line in lines]

# part one
print(sum(count(config, number) for config, number in zip(configs, numbers)))

# part two
configs = ["?".join([config] * 5) for config in configs]
numbers = [number * 5 for number in numbers]
print(sum(count(config, number) for config, number in zip(configs, numbers)))
