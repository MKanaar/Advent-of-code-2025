def parse():
    output = []
    file = open("./01/input.txt", "r")
    for line in file.readlines():
        direction = line[0]
        value = int(line[1:].strip())
        if direction == "R":
            output.append(value)
        else:
            output.append(-value)
    return output


def process(current_value: int, change: int) -> tuple[int, int]:
    zero_clicks = 0
    zero_clicks += abs(change) // 100

    if change < 0:
        if abs(change) % 100 >= current_value and current_value != 0:
            zero_clicks += 1
    else:
        if change % 100 + current_value >= 100:
            zero_clicks += 1

    return ((current_value + change) % 100, zero_clicks)


counter = 0
current_value = 50
for change in parse():
    current_value, zero_clicks = process(current_value, change)
    counter += zero_clicks

print(counter)
