def parse() -> tuple[list[str], int]:
    grid: list[str] = []

    with open("./07/input.txt", "r") as file:
        for line in file:
            grid.append(line.strip())

    start = grid[0].find("S")

    return grid, start


def process(grid: list[str], start: int) -> int:
    paths: list[int] = [0] * len(grid[0])
    paths[start] = 1

    for row in range(2, len(grid), 2):
        new_paths = [0] * len(grid[0])
        for col in range(len(grid[0])):
            if grid[row][col] == "^" and paths[col] > 0:
                new_paths[col - 1] += paths[col]
                new_paths[col + 1] += paths[col]
            elif paths[col] > 0:
                new_paths[col] += paths[col]
        paths = new_paths

    return sum(paths)


grid, start = parse()
count = process(grid, start)
print(count)
