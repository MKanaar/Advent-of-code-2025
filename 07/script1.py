def parse() -> tuple[list[str], int]:
    grid: list[str] = []

    with open("./07/input.txt", "r") as file:
        for line in file:
            grid.append(line.strip())

    start = grid[0].find("S")

    return grid, start


def process(grid: list[str], start: int) -> int:
    splits = 0
    beams: list[bool] = [False] * len(grid[0])
    beams[start] = True

    for row in range(2, len(grid), 2):
        for col in range(len(grid[0])):
            if grid[row][col] == "^" and beams[col]:
                splits += 1
                beams[col - 1] = True
                beams[col + 1] = True
                beams[col] = False

    return splits


grid, start = parse()
count = process(grid, start)
print(count)
