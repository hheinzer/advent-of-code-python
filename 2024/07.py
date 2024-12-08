from itertools import product


def compute(operations, eqns):
    total = 0
    for eqn in eqns:
        val, nums = eqn[0], eqn[1:]
        for ops in product(operations, repeat=len(nums) - 1):
            res = nums[0]
            for op, num in zip(ops, nums[1:]):
                res = op(res, num)
            if res == val:
                total += val
                break
    return total


eqns = [list(map(int, line.strip().replace(":", "").split())) for line in open("input/07.txt")]

add = lambda a, b: a + b
mul = lambda a, b: a * b
cat = lambda a, b: int(f"{a}{b}")

# part one
print(compute([add, mul], eqns))

# part two
print(compute([add, mul, cat], eqns))
