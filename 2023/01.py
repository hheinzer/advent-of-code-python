lines = open("input/01.txt").read().splitlines()

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def firstnum(string, nums):
    indices = [string.find(num) for num in nums]
    return nums[indices.index(min([index for index in indices if index != -1]))]


def lastnum(string, nums):
    indices = [string.rfind(num) for num in nums]
    return nums[indices.index(max([index for index in indices if index != -1]))]


def rint(string):
    for number, digit in zip(numbers, digits):
        string = string.replace(number, digit)
    return int(string)


# part one
nums = digits
print(sum(int(firstnum(line, nums) + lastnum(line, nums)) for line in lines))

# part two
nums += numbers
print(sum(rint(firstnum(line, nums) + lastnum(line, nums)) for line in lines))
