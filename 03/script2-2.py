def parse() -> list[list[int]]:
    banks: list[list[int]] = []

    with open("./03/input.txt", "r") as file:
        for line in file:
            digits = [int(char) for char in line.strip()]
            banks.append(digits)

    return banks


def find_max_battery(bank: list[int], start: int, end: int) -> tuple[str, int]:
    max_battery = max(bank[start : end + 1])
    max_index = bank.index(max_battery, start, end + 1)

    return str(max_battery), max_index + 1


def process(bank: list[int]) -> int:
    joltage_str = ""
    start = 0

    for end in range(len(bank) - 12, len(bank)):
        battery, start = find_max_battery(bank, start, end)
        joltage_str += battery

    return int(joltage_str)


total = 0
for bank in parse():
    total += process(bank)

print(total)
