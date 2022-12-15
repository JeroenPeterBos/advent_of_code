import re

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    iter_lines = iter(lines)
    stacks = []
    for line in iter_lines:
        if '[' not in line:
            break

        for offset in range(0, len(line), 4):
            stack = offset // 4

            # Ensure the stack exists
            if stack > len(stacks) - 1:
                stacks.append([])

            # Add the element to the stack
            if line[offset] == '[':
                stacks[stack].insert(0, line[offset + 1])
    
    # The break drops the column number line, this next line drops the empty line
    next(iter_lines)

    moves = []
    for line in iter_lines:
        _, *move_parts = re.split('move | from | to ', line)
        moves.append(tuple(map(int, move_parts)))

    return stacks, moves


def main(lines):
    stacks, moves = parse_lines(lines)

    for move_count, from_stack, to_stack in moves:
        moving = stacks[from_stack - 1][-move_count:]
        stacks[from_stack - 1] = stacks[from_stack - 1][:-move_count]
        stacks[to_stack - 1] += moving
    
    return "".join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    for filename in ["example.txt", "input.txt"]:
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
