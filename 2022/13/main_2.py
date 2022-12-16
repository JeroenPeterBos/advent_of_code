import glob
import re
import math
import json
from functools import cmp_to_key
from pprint import pprint


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    packets = []

    line_iter = iter(lines)
    try:
        while True:
            part_a = next(line_iter)
            part_b = next(line_iter)

            packets.append(json.loads(part_a))
            packets.append(json.loads(part_b))

            _ = next(line_iter)
    except StopIteration:
        pass

    return packets

def compare_ints(l, r):
    if l < r:
        return -1
    elif l == r:
        return 0
    else:
        return 1


def ordered_lists(list_l, list_r):
    for i in range(min(len(list_l), len(list_r))):
        l = list_l[i]
        r = list_r[i]

        if isinstance(l, int) and isinstance(r, int):
            i_result = compare_ints(l, r)
        elif isinstance(l, int):
            i_result = ordered_lists([l], r)
        elif isinstance(r, int):
            i_result = ordered_lists(l, [r])
        else:
            i_result = ordered_lists(l, r)
        
        if i_result == 0:
            continue
        else:
            return i_result
    
    if len(list_l) < len(list_r):
        return -1
    elif len(list_l) > len(list_r):
        return 1
    else:
        return 0


def main(lines):
    packets = parse_lines(lines)

    divider_a = [[2]]
    divider_b = [[6]]

    packets.append(divider_a)
    packets.append(divider_b)

    sorted_packets = sorted(packets, key=cmp_to_key(ordered_lists))

    return (sorted_packets.index(divider_a) + 1) * (sorted_packets.index(divider_b) + 1)


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
