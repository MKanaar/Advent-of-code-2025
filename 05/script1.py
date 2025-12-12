def parse() -> tuple[list[tuple[int, int]], list[int]]:
    with open("./05/input.txt", "r") as file:
        ranges: list[tuple[int, int]] = []
        ids: list[int] = []
        for line in file:
            if line.strip() == "":
                continue
            if "-" in line:
                range = line.strip().split("-")
                ranges.append((int(range[0]), int(range[1])))
            else:
                ids.append(int(line.strip()))

    return ranges, ids


def process(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    count = 0

    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                count += 1
                break

    return count


ranges, ids = parse()
count = process(ranges, ids)
print(count)
