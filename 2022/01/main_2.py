lines = []
with open('input.txt') as f:
    lines = f.readlines()

elves = []
elf = 0
for line in lines:
    line = line.strip()
    if line == '':
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)

elves.append(elf)

top_three = sorted(elves, reverse=True)[:3]

print(sum(top_three))

