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

def process(current_value: int, change: int) -> int:
    return (current_value + change) % 100

counter = 0
current_value = 50
for change in parse():
    current_value = process(current_value, change)
    if current_value == 0:
        counter += 1

print(counter)
