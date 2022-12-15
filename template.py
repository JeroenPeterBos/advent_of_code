def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_line(line):
    pass


def main(lines):
    for line in lines:
        parse_line(line)


if __name__ == '__main__':
    for filename in ["example.txt", "input.txt"]:
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
