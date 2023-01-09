import math

def process_input(_input):
    with open("day_01_input.txt") as file:
        lines = [int(line.strip()) for line in file]
        return lines

def process_list(masses):
    total = 0
    for i in masses:
        while i > 0:
            i = math.floor(i / 3) - 2
            if i <= 0:
                break
            total += i 
    return total
