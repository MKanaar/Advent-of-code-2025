import math


def parse():
    output: list[tuple[int, int, int]] = []
    file = open("./08/input.txt", "r")
    for line in file.readlines():
        x, y, z = line.split(",")
        output.append((int(x), int(y), int(z)))

    return output


def get_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def get_all_distances(boxes: list[tuple[int, int, int]]) -> list[int]:
    distances: list[tuple[int, int, int]] = []
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            distances.append((get_distance(boxes[i], boxes[j]), i, j))

    distances.sort(key=lambda x: x[0])

    return distances


def process(boxes: list[tuple[int, int, int]]) -> int:
    circuits: list[list[int]] = []
    distances = get_all_distances(boxes)
    last_connection_indices: tuple[int, int] = (-1, -1)

    for i in range(len(distances)):
        _, a, b = distances[i]
        index_circuit_a = next(
            (i for i, circuit in enumerate(circuits) if a in circuit), None
        )
        index_circuit_b = next(
            (i for i, circuit in enumerate(circuits) if b in circuit), None
        )
        if index_circuit_a is None and index_circuit_b is None:
            circuits.append([a, b])
        elif index_circuit_a is not None and index_circuit_b is None:
            circuits[index_circuit_a].append(b)
            last_connection_indices = (a, b)
        elif index_circuit_a is None and index_circuit_b is not None:
            circuits[index_circuit_b].append(a)
            last_connection_indices = (a, b)
        elif index_circuit_a is not index_circuit_b:
            circuits[index_circuit_a] += circuits[index_circuit_b]
            del circuits[index_circuit_b]
            last_connection_indices = (a, b)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            break

    return boxes[last_connection_indices[0]][0] * boxes[last_connection_indices[1]][0]


boxes = parse()
product = process(boxes)
print(product)
