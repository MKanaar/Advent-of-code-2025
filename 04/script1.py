def parse() -> list[str]:
    grid: list[str] = []

    with open("./04/input.txt", "r") as file:
        for line in file:
            grid.append(line.strip())

    return grid


def get_adjacent_papers(grid: list[str], row: int, col: int) -> int:
    adjacent = 0
    width = len(grid[row])
    height = len(grid)

    if row > 0 and col > 0 and grid[row - 1][col - 1] == "@":
        adjacent += 1  # Top-left
    if row > 0 and grid[row - 1][col] == "@":
        adjacent += 1  # Top
    if row > 0 and col < width - 1 and grid[row - 1][col + 1] == "@":
        adjacent += 1  # Top-right
    if col < width - 1 and grid[row][col + 1] == "@":
        adjacent += 1  # Right
    if row < height - 1 and col < width - 1 and grid[row + 1][col + 1] == "@":
        adjacent += 1  # Bottom-right
    if row < height - 1 and grid[row + 1][col] == "@":
        adjacent += 1  # Bottom
    if row < height - 1 and col > 0 and grid[row + 1][col - 1] == "@":
        adjacent += 1  # Bottom-left
    if col > 0 and grid[row][col - 1] == "@":
        adjacent += 1  # Left

    return adjacent


def process(grid: list[str]) -> int:
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current = grid[row][col]
            if current == ".":
                continue
            adjacent = get_adjacent_papers(grid, row, col)
            if adjacent < 4:
                count += 1

    return count


grid = parse()
accessible = process(grid)
print(accessible)
