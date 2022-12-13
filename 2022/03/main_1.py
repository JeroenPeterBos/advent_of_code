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
    for bag in lines:
        items_per_bag = len(bag) // 2
        common = set(bag[:items_per_bag]) & set(bag[items_per_bag:])
        result += sum(to_priority(c) for c in common)

    return result


if __name__ == '__main__':
    result = main(read_lines('input.txt'))
    print(result)