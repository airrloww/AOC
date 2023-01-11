def process_input(input_string):
    with open(input_string) as f:
        inputs = f.read()
        numbers = [int(item) for item in inputs.split(',')]
        return numbers


def result():
    codes = process_input("day_02_input.txt")
    codes[1] = 12
    codes[2] = 2
    for i in range(0, len(codes), 4):
        inputOne = codes[i+1]
        inputTwo = codes[i+2]
        output = codes[i+3]
        if codes[i] == 1:
            codes[output] = codes[inputOne] + codes[inputTwo]
        elif codes[i] == 2:
            codes[output] = codes[inputOne] * codes[inputTwo]
        elif codes[i] == 99:
            return codes[0]

print(result())