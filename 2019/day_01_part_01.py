import math

def process_input(_input):
    with open("day_01_input.txt") as file:
        lines = [int(line.strip()) for line in file]
        return lines

def process_list(masses):
    total = 0
    for i in masses:
        new_i = math.floor(i / 3) - 2 
        total += new_i
    return total
