lines = []
with open('input.txt') as f:
    lines = f.readlines()

elves = []
elf = []
for line in lines:
    line = line.strip()
    if line == '':
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

print(max(sum(elf) for elf in elves))