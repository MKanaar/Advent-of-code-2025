import math


def parse() -> list[tuple[int, int, int]]:
    box_positions: list[tuple[int, int, int]] = []

    with open("./08/input.txt", "r") as file:
        for line in file:
            x, y, z = line.split(",")
            box_positions.append((int(x), int(y), int(z)))

    return box_positions


def get_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def get_all_distances(
    boxes: list[tuple[int, int, int]],
) -> list[tuple[float, int, int]]:
    distances: list[tuple[float, int, int]] = []

    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            distances.append((get_distance(boxes[i], boxes[j]), i, j))

    distances.sort(key=lambda x: x[0])

    return distances


def process(boxes: list[tuple[int, int, int]]) -> int:
    circuits: list[list[int]] = []
    distances = get_all_distances(boxes)
    connections = 10 if len(boxes) == 20 else 1000

    for i in range(connections):
        _, a, b = distances[i]
        index_circuit_a = next(
            (i for i, circuit in enumerate(circuits) if a in circuit), None
        )
        index_circuit_b = next(
            (i for i, circuit in enumerate(circuits) if b in circuit), None
        )
        if index_circuit_a is None:
            if index_circuit_b is None:
                circuits.append([a, b])
            else:
                circuits[index_circuit_b].append(a)
        else:
            if index_circuit_b is None:
                circuits[index_circuit_a].append(b)
            elif index_circuit_a is not index_circuit_b:
                circuits[index_circuit_a] += circuits[index_circuit_b]
                del circuits[index_circuit_b]

    circuits.sort(key=lambda x: len(x), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


boxes = parse()
product = process(boxes)
print(product)
