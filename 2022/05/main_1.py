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
            for 
            if stack > len(stacks) - 1:

                stacks.append([])
    
    # The break drops the column number line, this next line drops the empty line
    next(iter_lines)


    moves = []

def main(lines):
    stacks, moves = parse_lines(lines)


if __name__ == '__main__':
    for filename in ["example.txt", "input.txt"]:
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
