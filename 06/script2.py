def parse() -> tuple[list[list[int]], list[str]]:
    grid: list[str] = []
    operators: list[str] = []

    with open("./06/input.txt", "r") as file:
        for line in file:
            elements = line.strip("\n")
            grid.append(elements)
            if elements[0] in ["+", "*"]:
                operators = elements.split()

    operands: list[list[int]] = []
    numbers: list[int] = []
    number: str = ""

    for col in range(len(grid[0])):
        rows = len(grid)
        for row in range(rows - 1, -1, -1):
            char = grid[row][col]
            if char.isdigit():
                number += char
            if row == 0 and number != "":
                numbers.append(int(number[::-1]))
                number = ""
            elif row == rows - 1 and char in ["+", "*"]:
                if not numbers:
                    continue
                operands.append(numbers)
                numbers = []

    operands.append(numbers)

    return operands, operators


def process(operands: list[list[int]], operators: list[str]) -> int:
    total = 0

    for i in range(len(operators)):
        operator = operators[i]
        if operator[0] == "+":
            total += sum(operands[i])
        elif operator[0] == "*":
            prod = 1
            for num in operands[i]:
                prod *= num
            total += prod

    return total


operands, operators = parse()
count = process(operands, operators)
print(count)
