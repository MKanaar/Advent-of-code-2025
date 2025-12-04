def parse():
    output: list[list[int]] = []
    file = open("./04/input.txt", "r")
    for line in file.readlines():
        output.append(list(line.strip()))

    return output


def get_adjacent_papers(grid: list[list[int]], row: int, col: int) -> int:
    adjacent = 0

    if row > 0 and col > 0 and grid[row - 1][col - 1] == "@":
        adjacent += 1  # Top-left
    if row > 0 and grid[row - 1][col] == "@":
        adjacent += 1  # Top
    if row > 0 and col < len(grid[row]) - 1 and grid[row - 1][col + 1] == "@":
        adjacent += 1  # Top-right
    if col < len(grid[row]) - 1 and grid[row][col + 1] == "@":
        adjacent += 1  # Right
    if (
        row < len(grid) - 1
        and col < len(grid[row]) - 1
        and grid[row + 1][col + 1] == "@"
    ):
        adjacent += 1  # Bottom-right
    if row < len(grid) - 1 and grid[row + 1][col] == "@":
        adjacent += 1  # Bottom
    if row < len(grid) - 1 and col > 0 and grid[row + 1][col - 1] == "@":
        adjacent += 1  # Bottom-left
    if col > 0 and grid[row][col - 1] == "@":
        adjacent += 1  # Left

    return adjacent


def get_removed(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current = grid[row][col]
            if current == ".":
                continue

            adjacent = get_adjacent_papers(grid, row, col)
            if adjacent < 4:
                count += 1
                grid[row][col] = "."

    return count, grid


def process(grid: list[list[int]]) -> int:
    count = 0
    while True:
        removed, grid = get_removed(grid)
        if removed == 0:
            break
        count += removed

    return count


accessible = 0
grid = parse()
accessible = process(grid)
print(accessible)
