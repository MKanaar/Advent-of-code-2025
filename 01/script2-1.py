def parse() -> list[int]:
    rotations: list[int] = []

    with open("./01/input.txt", "r") as file:
        for line in file:
            direction = line[0]
            value = int(line[1:].strip())
            if direction == "R":
                rotations.append(value)
            else:
                rotations.append(-value)

    return rotations


def process(current_value: int, rotation: int) -> tuple[int, int]:
    zero_clicks = 0
    zero_clicks += abs(rotation) // 100

    if rotation < 0:
        if abs(rotation) % 100 >= current_value and current_value != 0:
            zero_clicks += 1
    else:
        if rotation % 100 + current_value >= 100:
            zero_clicks += 1

    return ((current_value + rotation) % 100, zero_clicks)


counter = 0
current_value = 50
for rotation in parse():
    current_value, zero_clicks = process(current_value, rotation)
    counter += zero_clicks

print(counter)
