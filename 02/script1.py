def parse():
    output: list[tuple[int, int]] = []
    file = open("./02/input.txt", "r")
    input = file.read()
    ranges = input.split(",")
    for r in ranges:
        start, end = r.split("-")
        output.append((int(start), int(end)))
    return output


def process(id_range: tuple[int, int]) -> list[int]:
    wrong_ids = []
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
for r in id_ranges:
    wrong_ids = process(r)
    total += sum(wrong_ids)

print(total)
