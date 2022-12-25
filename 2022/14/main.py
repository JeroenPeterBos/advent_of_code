import glob
import re
import math
from pprint import pprint
import numpy as np

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    paths = [
        [
            tuple(map(int, pos.split(",")))
            for pos in line.split(" -> ")
        ]
        for line in lines
    ]

    max_x = max(x for path in paths for x, _ in path)
    min_x = min(x for path in paths for x, _ in path)
    max_y = max(y for path in paths for _, y in path)

    grid = np.zeros((max_x - min_x + 1, max_y + 1))
    source = (500 - min_x, 0)

    for path in paths:
        for start, end in zip(path, path[1:]):
            if start[0] == end[0]:
                mi, ma = sorted((start[1], end[1]))
                for y in range(mi, ma + 1):
                    grid[start[0] - min_x, y] = 1
            elif start[1] == end[1]:
                mi, ma = sorted((start[0], end[0]))
                for x in range(mi, ma + 1):
                    grid[x - min_x, start[1]] = 1
            else:
                raise Exception("Invalid path")

    return source, grid


def main(lines):
    source, grid = parse_lines(lines)

    sand_count = 0
    while True:
        sand = source
        while True:
            for x_direction in (0, -1, 1):
                pos = (sand[0] + x_direction, sand[1] + 1)

                if pos[0] < 0 or pos[0] >= grid.shape[0] or pos[1] >= grid.shape[1]:
                    return sand_count
                
                if grid[pos] == 0:
                    sand = pos
                    break
            else:
                grid[sand] = 8
                break
        sand_count += 1


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
