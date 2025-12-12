def parse() -> list[tuple[int, int]]:
    id_ranges: list[tuple[int, int]] = []

    with open("./02/input.txt", "r") as file:
        input = file.read()
        ranges = input.split(",")
        for id_range in ranges:
            start, end = id_range.split("-")
            id_ranges.append((int(start), int(end)))

    return id_ranges


def process(id_range: tuple[int, int]) -> list[int]:
    wrong_ids: list[int] = []
    start, end = id_range

    for id in range(start, end + 1):
        id_str = str(id)
        str_length = len(id_str)
        if str_length % 2 != 0:
            continue
        middle = str_length // 2
        left, right = id_str[:middle], id_str[middle:]
        if left == right:
            wrong_ids.append(id)

    return wrong_ids


total = 0
id_ranges = parse()
for id_range in id_ranges:
    wrong_ids = process(id_range)
    total += sum(wrong_ids)

print(total)
