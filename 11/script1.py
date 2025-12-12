def parse() -> list[tuple[str, list[str]]]:
    server_rack: list[tuple[str, list[str]]] = []

    with open("./11/input.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            device = parts[0][:-1]
            output_devices = parts[1:]
            server_rack.append((device, output_devices))

    return server_rack


def find_paths_recursive(
    server_rack: list[tuple[str, list[str]]], path: list[str], total_paths: int
) -> int:
    current_device = -1

    for i, (device, _) in enumerate(server_rack):
        if device == path[-1]:
            current_device = i
            break

    for output_device in server_rack[current_device][1]:
        if output_device in path:
            continue
        if output_device == "out":
            return total_paths + 1
        else:
            new_path = path + [output_device]
            total_paths = find_paths_recursive(server_rack, new_path, total_paths)

    return total_paths


def process(server_rack: list[tuple[str, list[str]]]) -> int:
    return find_paths_recursive(server_rack, ["you"], 0)


server_rack = parse()
paths = process(server_rack)
print(paths)
