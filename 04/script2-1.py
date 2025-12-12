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


def get_removable_cells(grid: list[str]) -> list[tuple[int, int]]:
    to_remove: list[tuple[int, int]] = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current = grid[row][col]
            if current == ".":
                continue
            adjacent = get_adjacent_papers(grid, row, col)
            if adjacent < 4:
                to_remove.append((row, col))

    return to_remove


def process(grid: list[str]) -> int:
    count = 0

    while removable := get_removable_cells(grid):
        for row, col in removable:
            grid[row] = grid[row][:col] + "." + grid[row][col + 1 :]
        count += len(removable)

    return count


grid = parse()
accessible = process(grid)
print(accessible)
