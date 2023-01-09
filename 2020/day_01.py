with open('day_01_input.txt', 'r') as f:
    numbers = [int(line) for line in f.read().splitlines()]

def func(nums):
    for i in nums:
        for n in nums:
            if i + n == 2020:
                return i * n

print(func(numbers))
