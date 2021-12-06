with open('a.input', 'r') as f:
    data = f.readlines()

horizontal = 0
depth = 0

for command in data:
    command = command.split()
    x = int(command[1])
    if (command[0] == 'forward'):
        horizontal += x
    elif (command[0] == 'down'):
        depth += x
    else:
        depth -= x

print(horizontal * depth)
