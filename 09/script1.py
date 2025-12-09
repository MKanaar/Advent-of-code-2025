def parse():
    output: list[tuple[int, int]] = []
    file = open("./09/input.txt", "r")
    for line in file.readlines():
        coordinate = line.strip().split(",")
        output.append((int(coordinate[0]), int(coordinate[1])))

    return output


def get_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    width = abs(tile1[0] - tile2[0]) + 1
    height = abs(tile1[1] - tile2[1]) + 1
    return width * height


def process(red_tiles: list[tuple[int, int]]) -> int:
    biggest_area = -1
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            area = get_area(red_tiles[i], red_tiles[j])
            if area > biggest_area:
                biggest_area = area

    return biggest_area


red_tiles = parse()
biggest_area = process(red_tiles)
print(biggest_area)
