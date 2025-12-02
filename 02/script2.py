def parse():
    output: list[tuple[int, int]] = []
    file = open("./2/input.txt", "r")
    input = file.read()
    ranges = input.split(',')
    for r in ranges:
        start, end = r.split('-')
        output.append((int(start), int(end)))
    return output

def process(id_range: tuple[int, int]) -> list[int]:
    wrong_ids = []
    start, end = id_range
    for id in range(start, end + 1):
        id_str = str(id)
        str_length = len(id_str)

        for length in range(1, (str_length // 2) + 1, 1):
            if str_length % length != 0:
                continue
            motif = id_str[:length]
            motif_repeated = motif * (str_length // length)
            if motif_repeated == id_str:
                wrong_ids.append(id)
                break

    return wrong_ids

total = 0
id_ranges = parse()
for r in id_ranges:
    wrong_ids = process(r)
    total += sum(wrong_ids)

print(total)