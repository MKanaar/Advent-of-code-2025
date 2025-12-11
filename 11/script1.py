def parse():
    output: list[tuple[str, list[str]]] = []
    file = open("./11/input.txt", "r")
    for line in file.readlines():
        parts = line.strip().split(" ")
        device = parts[0][:-1]
        output_devices = parts[1:]
        output.append((device, output_devices))

    return output


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
