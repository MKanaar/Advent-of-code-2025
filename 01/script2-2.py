def parse():
    output = []
    file = open("./1/input.txt", "r")
    for line in file.readlines():
        direction = line[0]
        value = int(line[1:].strip())
        if direction == 'R':
            output.append(value)
        else:
            output.append(-value)
    return output

def process(current_value: int, change: int) -> tuple[int,int]:
    zero_clicks = 0
    one_click = 1 if change > 0 else -1
    for _ in range(abs(change)):
        if (current_value + one_click) % 100 == 0:
            zero_clicks += 1
        current_value = (current_value +  one_click) % 100

    return (current_value, zero_clicks)

counter = 0
current_value = 50
for change in parse():
    current_value, zero_clicks = process(current_value, change)
    counter += zero_clicks

print(counter)
