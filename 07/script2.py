def parse():
    output: list[str] = []
    file = open("./07/input.txt", "r")
    for line in file.readlines():
        output.append(line.strip())

    start = output[0].find("S")

    return output, start


def process(grid: list[str], start: int):
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
