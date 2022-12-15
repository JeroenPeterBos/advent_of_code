import glob

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def main(lines):
    line = lines[0]

    for offset in range(len(line) - 3):
        characters = line[offset:offset + 4]
        if len(set(characters)) == 4:
            return offset + 4


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
