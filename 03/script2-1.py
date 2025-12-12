def parse() -> list[str]:
    banks: list[str] = []

    with open("./03/input.txt", "r") as file:
        for line in file:
            banks.append(line.strip())

    return banks


def find_max_joltage(base: str, new_digit: str) -> str:
    max_joltage = -1
    batteries: str = base + new_digit

    for i in range(len(batteries)):
        copy = batteries[0:i] + batteries[i + 1 : len(batteries)]
        batteries_value = int(copy)
        if batteries_value > max_joltage:
            max_joltage = batteries_value

    return str(max_joltage)


def process(bank: str) -> int:
    base = bank[0:12]

    for i in range(len(bank) - 12):
        new_digit = bank[i + 12]
        base = find_max_joltage(base, new_digit)

    return int(base)


total = 0
for bank in parse():
    total += process(bank)

print(total)
