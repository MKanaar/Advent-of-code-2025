from itertools import combinations_with_replacement


class Machine:
    indicator_lights: list[bool]
    buttons: list[list[int]]

    def __init__(self, indicator_lights: list[bool], buttons: list[list[int]]) -> None:
        self.indicator_lights = indicator_lights
        self.buttons = buttons


def parse() -> list[Machine]:
    machines: list[Machine] = []

    with open("./10/input.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            lights = [light == "#" for light in parts[0][1:-1]]
            buttons: list[list[int]] = []
            for button_str in parts[1:-1]:
                button = [int(x) for x in button_str[1:-1].split(",")]
                buttons.append(button)
            machine = Machine(lights, buttons)
            machines.append(machine)

    return machines


def button_press(configured_lights: list[bool], button: list[int]) -> list[bool]:
    for light_index in button:
        configured_lights[light_index] = not configured_lights[light_index]

    return configured_lights


def configure_lights_for_machine(machine: Machine) -> int:
    number_of_presses = 0

    while True:
        for combination in combinations_with_replacement(
            machine.buttons, number_of_presses
        ):
            configured_lights = [False] * len(machine.indicator_lights)
            for button in combination:
                configured_lights = button_press(configured_lights, button)
            if configured_lights == machine.indicator_lights:
                return number_of_presses
        number_of_presses += 1


def total_button_presses(machines: list[Machine]) -> int:
    total_presses = 0

    for machine in machines:
        total_presses += configure_lights_for_machine(machine)

    return total_presses


machines = parse()
total_presses = total_button_presses(machines)
print(total_presses)
