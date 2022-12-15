def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_line(line):
    return (int(section) for elf in line.split(',') for section in elf.split('-'))

def main(lines):
    count = 0

    for line in lines:
        elf_a_first, elf_a_last, elf_b_first, elf_b_last = parse_line(line)
        elf_a = set(range(elf_a_first, elf_a_last + 1))
        elf_b = set(range(elf_b_first, elf_b_last + 1))

        if elf_b.issubset(elf_a) or elf_a.issubset(elf_b):
            count += 1
    
    return count


if __name__ == '__main__':
    for filename in ["example.txt", "input.txt"]:
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
