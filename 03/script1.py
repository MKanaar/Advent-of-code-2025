def parse() -> list[list[int]]:
    banks: list[list[int]] = []

    with open("./03/input.txt", "r") as file:
        for line in file:
            digits = [int(char) for char in line.strip()]
            banks.append(digits)

    return banks


def process(bank: list[int]) -> int:
    max_joltage = -1

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = bank[i] * 10 + bank[j]
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage


total = 0
for bank in parse():
    total += process(bank)

print(total)
