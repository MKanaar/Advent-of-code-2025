def parse():
    output: list[list[int]] = []
    file = open("./03/input.txt", "r")
    for line in file.readlines():
        digits = [int(char) for char in line.strip()]
        output.append(digits)

    return output


def process(bank: list[int]) -> int:
    max_joltage = -1
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = bank[i] * 10 + bank[j]
            if joltage > max_joltage:
                max_joltage = joltage

    # print(max_joltage)
    return max_joltage


total = 0
for bank in parse():
    total += process(bank)

print(total)
