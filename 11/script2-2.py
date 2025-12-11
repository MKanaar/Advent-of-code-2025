from collections import defaultdict, deque


def topological_sort(adjacency_list: dict[str, list[str]]) -> list[str]:
    incoming_connections = defaultdict(int)
    devices = set(adjacency_list.keys())

    for device, output_devices in adjacency_list.items():
        for output_device in output_devices:
            devices.add(output_device)
            incoming_connections[output_device] += 1
        incoming_connections.setdefault(device, incoming_connections.get(device, 0))

    queue = deque([device for device in devices if incoming_connections[device] == 0])
    order: list[str] = []

    while queue:
        device = queue.popleft()
        order.append(device)

        for output_device in adjacency_list.get(device, []):
            incoming_connections[output_device] -= 1
            if incoming_connections[output_device] == 0:
                queue.append(output_device)

    if len(order) != len(devices):
        return []

    return order


def parse():
    adjacency_list: dict[str, list[str]] = {}

    file = open("./11/input.txt", "r")
    for line in file.readlines():
        parts = line.strip().split(" ")
        device = parts[0][:-1]
        output_devices = parts[1:]
        adjacency_list[device] = output_devices

    topological_order = topological_sort(adjacency_list)

    return adjacency_list, topological_order


def process(adjacency_list: dict[str, list[str]], topological_order: list[str]) -> int:
    dp_table: dict[str, list[int]] = {
        device: [0, 0, 0, 0] for device in topological_order
    }
    dp_table["svr"][0] = 1

    for device in topological_order:
        if device == "out":
            continue

        for state in range(4):
            number_of_paths = dp_table[device][state]
            if number_of_paths == 0:
                continue

            for output_device in adjacency_list.get(device, []):
                new_state = state
                if output_device == "dac":
                    new_state |= 1
                elif output_device == "fft":
                    new_state |= 2
                dp_table[output_device][new_state] += number_of_paths

    return dp_table["out"][3]


adjacency_list, topological_order = parse()
paths = process(adjacency_list, topological_order)
print(paths)
