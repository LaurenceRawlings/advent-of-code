with open('b.input', 'r') as f:
    tmp = list(map(int, f.readlines()))
    data = list(map(sum, list(zip(tmp[:], tmp[1:], tmp[2:]))))

last = data.pop(0)
increased = 0

for depth in data:
    if last < depth:
        increased += 1
    last = depth

print(increased)
