def parse():
    red_tiles: list[tuple[int, int]] = []
    file = open("./09/input.txt", "r")
    for line in file.readlines():
        coordinate = line.strip().split(",")
        red_tiles.append((int(coordinate[0]), int(coordinate[1])))

    return red_tiles


def get_green_tiles_on_path(red_tiles: list[tuple[int, int]]) -> list[tuple[int, int]]:
    green_tiles: list[tuple[int, int]] = []

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles) + 1):
            j %= len(red_tiles)

            tile1 = red_tiles[i]
            tile2 = red_tiles[j]

            if tile1[0] == tile2[0]:
                col = tile1[0]
                for row in range(min(tile1[1], tile2[1]) + 1, max(tile1[1], tile2[1])):
                    green_tiles.append((col, row))

            elif tile1[1] == tile2[1]:
                row = tile1[1]
                for col in range(min(tile1[0], tile2[0]) + 1, max(tile1[0], tile2[0])):
                    green_tiles.append((col, row))

    return green_tiles


def other_red_or_green_tiles_in_area(
    index1: int,
    index2: int,
    red_tiles: list[tuple[int, int]],
    green_tiles: list[tuple[int, int]],
) -> bool:
    tile1 = red_tiles[index1]
    tile2 = red_tiles[index2]

    x1 = min(tile1[0], tile2[0]) + 1
    x2 = max(tile1[0], tile2[0]) - 1
    y1 = min(tile1[1], tile2[1]) + 1
    y2 = max(tile1[1], tile2[1]) - 1

    if x1 > x2 or y1 > y2:
        return False

    for tile in red_tiles:
        if tile == tile1 or tile == tile2:
            continue
        if x1 <= tile[0] <= x2 and y1 <= tile[1] <= y2:
            return True

    for tile in green_tiles:
        if x1 <= tile[0] <= x2 and y1 <= tile[1] <= y2:
            return True

    return False


def get_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    width = abs(tile1[0] - tile2[0]) + 1
    height = abs(tile1[1] - tile2[1]) + 1
    return width * height


def process(red_tiles: list[tuple[int, int]]) -> int:
    biggest_area = -1
    green_tiles = get_green_tiles_on_path(red_tiles)

    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            area = get_area(red_tiles[i], red_tiles[j])
            if area > biggest_area and not other_red_or_green_tiles_in_area(
                i, j, red_tiles, green_tiles
            ):
                biggest_area = area

    return biggest_area


red_tiles = parse()
biggest_area = process(red_tiles)
print(biggest_area)
