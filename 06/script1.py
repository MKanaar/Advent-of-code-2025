def parse():
    columns: list[list[int]] = []
    operators: list[str] = []
    file = open("./06/input.txt", "r")
    for line in file.readlines():
        elements = line.strip().split()
        if elements[0] in ["+", "*"]:
            operators = elements
        else:
            numbers = [int(x) for x in elements]
            for i in range(len(numbers)):
                if len(columns) <= i:
                    columns.append([])
                columns[i].append(numbers[i])

    return columns, operators


def process(columns: list[list[int]], operators: list[str]) -> int:
    total = 0
    for i in range(len(operators)):
        operator = operators[i]
        if operator[0] == "+":
            total += sum(columns[i])
        elif operator[0] == "*":
            prod = 1
            for num in columns[i]:
                prod *= num
            total += prod

    return total


count = 0
columns, operators = parse()
count = process(columns, operators)
print(count)
