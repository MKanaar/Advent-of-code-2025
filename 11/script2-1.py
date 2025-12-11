from collections import deque


def get_min_depths(adjacency_list: dict[str, list[str]]) -> dict[str, int]:
    all_devices: set[str] = set(adjacency_list.keys())
    for output_devices in adjacency_list.values():
        all_devices.update(output_devices)

    min_depths = {device: float("inf") for device in all_devices}
    min_depths["svr"] = 0
    queue = deque(["svr"])

    while queue:
        device = queue.popleft()
        for child in adjacency_list.get(device, []):
            if min_depths[child] == float("inf"):
                min_depths[child] = min_depths[device] + 1
                queue.append(child)

    min_depth_out = int(
        min(
            min_depths[device]
            for device, outputs in adjacency_list.items()
            if "out" in outputs
        )
        + 1
    )

    return {
        "dac": int(min_depths["dac"]),
        "fft": int(min_depths["fft"]),
        "out": min_depth_out,
    }


def get_max_depths(adjacency_list: dict[str, list[str]]) -> dict[str, int]:
    all_devices: set[str] = set(adjacency_list.keys())
    for output_devices in adjacency_list.values():
        all_devices.update(output_devices)

    max_depths: dict[str, int] = {device: -1 for device in all_devices}
    max_depths["svr"] = 0
    queue = deque([("svr", 0)])

    while queue:
        device_name, current_depth = queue.popleft()

        if device_name == "out":
            continue

        for output_device in adjacency_list.get(device_name, []):
            new_depth = current_depth + 1
            if new_depth > max_depths[output_device]:
                max_depths[output_device] = new_depth
                queue.append((output_device, new_depth))

    max_depth_out = int(
        max(
            max_depths[device]
            for device, outputs in adjacency_list.items()
            if "out" in outputs
        )
        + 1
    )

    return {
        "dac": int(max_depths["dac"]),
        "fft": int(max_depths["fft"]),
        "out": max_depth_out,
    }


def parse():
    adjacency_list: dict[str, list[str]] = {}

    file = open("./11/input.txt", "r")
    for line in file.readlines():
        parts = line.strip().split(" ")
        device = parts[0][:-1]
        output_devices = parts[1:]
        adjacency_list[device] = output_devices

    min_depths = get_min_depths(adjacency_list)
    max_depths = get_max_depths(adjacency_list)

    return adjacency_list, min_depths, max_depths


def find_paths_recursive(
    adjacency_list: dict[str, list[str]],
    path: list[str],
    end_device: str,
    max_depth: int,
) -> int:
    if len(path) > max_depth + 1:
        return 0

    total_paths = 0
    current_device = path[-1]
    for output_device in adjacency_list[current_device]:
        if output_device in path:
            continue

        if output_device == end_device:
            total_paths += 1
            continue

        if output_device in ["out", "dac", "fft"]:
            continue

        total_paths += find_paths_recursive(
            adjacency_list,
            path + [output_device],
            end_device,
            max_depth,
        )

    return total_paths


def process(
    adjacency_list: dict[str, list[str]],
    min_depths: dict[str, int],
    max_depths: dict[str, int],
) -> int:
    if max_depths["fft"] < min_depths["dac"]:
        option1 = 0
    else:
        svr_dac = find_paths_recursive(
            adjacency_list, ["svr"], "dac", max_depths["dac"]
        )
        dac_fft = find_paths_recursive(
            adjacency_list, ["dac"], "fft", max_depths["fft"] - min_depths["dac"]
        )
        fft_out = find_paths_recursive(
            adjacency_list, ["fft"], "out", max_depths["out"] - min_depths["fft"]
        )
        option1 = svr_dac * dac_fft * fft_out

    if max_depths["dac"] < min_depths["fft"]:
        option2 = 0
    else:
        svr_fft = find_paths_recursive(
            adjacency_list, ["svr"], "fft", max_depths["fft"]
        )
        fft_dac = find_paths_recursive(
            adjacency_list, ["fft"], "dac", max_depths["dac"] - min_depths["fft"]
        )
        dac_out = find_paths_recursive(
            adjacency_list, ["dac"], "out", max_depths["out"] - min_depths["dac"]
        )
        option2 = svr_fft * fft_dac * dac_out

    return option1 + option2


adjacency_list, min_depths, max_depths = parse()
paths = process(adjacency_list, min_depths, max_depths)
print(paths)
