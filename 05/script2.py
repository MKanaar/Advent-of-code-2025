def parse() -> list[tuple[int, int]]:
    with open("./05/input.txt", "r") as file:
        ranges: list[tuple[int, int]] = []
        for line in file:
            if line.strip() == "":
                continue
            if "-" in line:
                range = line.strip().split("-")
                ranges.append((int(range[0]), int(range[1])))

    return ranges


def combine_ranges(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int]:
    return min(range1[0], range2[0]), max(range1[1], range2[1])


def contains_overlap(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return not (range1[1] < range2[0] or range2[1] < range1[0])


def get_unique_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    unique_ranges: list[tuple[int, int]] = []

    for range in ranges:
        if range not in unique_ranges and range != (0, 0):
            unique_ranges.append(range)

    return unique_ranges


def process(ranges: list[tuple[int, int]]) -> int:
    for i in range(len(ranges) - 1):
        for j in range(i + 1, len(ranges)):
            if contains_overlap(ranges[i], ranges[j]):
                combined = combine_ranges(ranges[i], ranges[j])
                ranges[i] = (0, 0)
                ranges[j] = combined

    unique_ranges = get_unique_ranges(ranges)
    count = 0

    for unique_range in unique_ranges:
        count += unique_range[1] - unique_range[0] + 1

    return count


ranges = parse()
count = process(ranges)
print(count)
