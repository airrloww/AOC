def process_input(input_string):
    with open(input_string) as f:
        inputs = f.read()
        numbers = [int(item) for item in inputs.split(',')]
        return numbers

def main(a_inputs):
    arr = a_inputs[:]
    for i in range(0, len(arr), 4):
        if arr[i] == 99:
            return arr[0]
        elif arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
        elif arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
    for verb in range(0, 100):
        for noun in range(0, 100):
            arr_inputs[1] = noun
            arr_inputs[2] = verb
            result = arr[0]

            if result == 19690720:
                print(100 * noun + verb)
                break


def solve():
    for verb in range(0, 100):
        for noun in range(0, 100):
            arr_inputs[1] = noun
            arr_inputs[2] = verb
            result = main(arr_inputs)

            if result == 19690720:
               return 100 * noun + verb


arr_inputs = process_input("day_02_input.txt")
print(solve())