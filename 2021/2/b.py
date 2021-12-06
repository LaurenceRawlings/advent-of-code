with open('b.input', 'r') as f:
    data = f.readlines()

horizontal = 0
depth = 0
aim = 0

for command in data:
    command = command.split()
    x = int(command[1])
    if (command[0] == 'forward'):
        horizontal += x
        depth += x * aim
    elif (command[0] == 'down'):
        aim += x
    else:
        aim -= x

print(horizontal * depth)
