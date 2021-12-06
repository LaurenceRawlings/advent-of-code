with open('1.input', 'r') as f:
    data = list(map(int, f.readlines()))

last = data.pop(0)
increased = 0

for depth in data:
    if last < depth:
        increased += 1
    last = depth

print(increased)