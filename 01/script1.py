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


def process(current_value: int, rotation: int) -> int:
    return (current_value + rotation) % 100


counter = 0
current_value = 50
for rotation in parse():
    current_value = process(current_value, rotation)
    if current_value == 0:
        counter += 1

print(counter)
