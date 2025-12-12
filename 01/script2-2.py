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
    one_click = 1 if rotation > 0 else -1

    for _ in range(abs(rotation)):
        if (current_value + one_click) % 100 == 0:
            zero_clicks += 1
        current_value = (current_value + one_click) % 100

    return (current_value, zero_clicks)


counter = 0
current_value = 50
for rotation in parse():
    current_value, zero_clicks = process(current_value, rotation)
    counter += zero_clicks

print(counter)
