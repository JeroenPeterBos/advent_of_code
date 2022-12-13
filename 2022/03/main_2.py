def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def to_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def main(lines):
    result = 0
    for group_start in range(0, len(lines), 3):
        bags = lines[group_start:group_start + 3]
        common  = set(bags[0]) & set(bags[1]) & set(bags[2])
        result += sum(to_priority(c) for c in common)

    return result


if __name__ == '__main__':
    result = main(read_lines('input.txt'))
    print(result)