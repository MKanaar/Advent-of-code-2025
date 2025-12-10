from pulp import LpProblem, LpMinimize, LpInteger, LpVariable
from pulp import LpStatus, value, PULP_CBC_CMD


class Machine:
    joltage_levels: list[int]
    buttons: list[list[int]]
    joltage_to_buttons: dict[int, list[int]]

    def __init__(self, joltage_levels: list[int], buttons: list[list[int]]):
        self.joltage_levels = joltage_levels
        self.buttons = buttons
        self.joltage_to_buttons = self._build_joltage_to_buttons_map()

    def _build_joltage_to_buttons_map(self) -> dict[int, list[int]]:
        joltage_map = {i: [] for i in range(len(self.joltage_levels))}
        for button_idx, button in enumerate(self.buttons):
            for joltage_idx in button:
                joltage_map[joltage_idx].append(button_idx)
        return joltage_map


def parse():
    output: list[Machine] = []
    file = open("./10/input.txt", "r")
    for line in file.readlines():
        parts = line.strip().split(" ")
        buttons: list[list[int]] = []
        for button_str in parts[1:-1]:
            button = [int(x) for x in button_str[1:-1].split(",")]
            buttons.append(button)
        joltage_levels = [int(x) for x in parts[-1][1:-1].split(",")]
        machine = Machine(joltage_levels, buttons)
        output.append(machine)

    return output


def configure_joltage_for_machine(machine: Machine) -> int:
    problem = LpProblem("Minimum_button_presses", LpMinimize)

    button_presses = []
    for i in range(len(machine.buttons)):
        button_press = LpVariable(f"button_{i}", 0, None, LpInteger)
        button_presses.append(button_press)

    problem += sum(button_presses), "Total_button_presses"

    for joltage_index, target_level in enumerate(machine.joltage_levels):
        constraint_expression = sum(
            button_presses[button_index]
            for button_index in machine.joltage_to_buttons[joltage_index]
        )
        problem += (
            constraint_expression == target_level,
            f"Joltage_{joltage_index}_target_level",
        )

    problem.solve(PULP_CBC_CMD(msg=False))

    if LpStatus[problem.status] == "Optimal":
        return int(value(problem.objective))  # type: ignore
    else:
        print(f"No solution found: {LpStatus[problem.status]}")
        return -1


def total_button_presses(machines: list[Machine]) -> int:
    total_presses = 0
    for machine in machines:
        total_presses += configure_joltage_for_machine(machine)
    return total_presses


machines = parse()
total_presses = total_button_presses(machines)
print(total_presses)
