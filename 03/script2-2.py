def parse():
    output: list[list[int]] = []
    file = open("./03/input.txt", "r")
    for line in file.readlines():
        digits = [int(char) for char in line.strip()]
        output.append(digits)

    return output


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

    # print(joltage_str)
    return int(joltage_str)


total = 0
for bank in parse():
    total += process(bank)

print(total)
