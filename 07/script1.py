def parse():
    output: list[str] = []
    file = open("./07/input.txt", "r")
    for line in file.readlines():
        output.append(line.strip())

    start = output[0].find("S")

    return output, start


def process(grid: list[str], start: int):
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
