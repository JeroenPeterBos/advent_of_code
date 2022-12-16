import glob
import re
import math
import json
from pprint import pprint


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    packet_pairs = []

    line_iter = iter(lines)
    try:
        while True:
            part_a = next(line_iter)
            part_b = next(line_iter)
            packet_pairs.append((json.loads(part_a), json.loads(part_b)))

            _ = next(line_iter)
    except StopIteration:
        pass

    return packet_pairs

def ordered_ints(l, r):
    if l < r:
        return True
    elif l == r:
        return "equal"
    else:
        return False


def ordered_lists(list_l, list_r):
    for i in range(min(len(list_l), len(list_r))):
        l = list_l[i]
        r = list_r[i]

        if isinstance(l, int) and isinstance(r, int):
            i_result = ordered_ints(l, r)
        elif isinstance(l, int):
            i_result = ordered_lists([l], r)
        elif isinstance(r, int):
            i_result = ordered_lists(l, [r])
        else:
            i_result = ordered_lists(l, r)
        
        if i_result == "equal":
            continue
        else:
            return i_result
    
    if len(list_l) < len(list_r):
        return True
    elif len(list_l) > len(list_r):
        return False
    else:
        return "equal"


def main(lines):
    pairs = parse_lines(lines)

    result = 0
    for i, (a, b) in enumerate(pairs):
        ordered = ordered_lists(a, b)

        if ordered is True:
            result += i + 1

    return result


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
