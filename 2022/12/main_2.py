import glob
import re
import math
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def char_to_int(char):
    return ord(char) - ord('a')


def index_of(grid, char, only_one=True):
    x, y = np.where(grid == char_to_int(char))

    if only_one:
        return x[0], y[0]
    else:
        return list(zip(x, y))


def parse_lines(lines):
    grid = np.array([
        [
            char_to_int(char) for char in line
        ] for line in lines
    ])

    start = index_of(grid, "E")
    grid[start] = char_to_int("z")

    end = index_of(grid, "S")
    grid[end] = char_to_int("a")

    ends = index_of(grid, "a", only_one=False)

    return grid, start, ends


def main(lines):
    grid, start, ends = parse_lines(lines)

    distance = {start: 0}
    open_set = {start}

    while open_set:
        current = min(open_set, key=lambda pos: distance[pos])
        open_set.remove(current)

        if current in ends:
            return distance[current]

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            if new_pos[0] < 0 or new_pos[0] >= grid.shape[0] or new_pos[1] < 0 or new_pos[1] >= grid.shape[1]:
                # Does not exist
                continue

            if grid[new_pos] + 1 < grid[current]:
                # Too high, can't go here
                continue

            new_distance = distance[current] + 1
            if new_pos not in distance or new_distance < distance[new_pos]:
                distance[new_pos] = new_distance
                open_set.add(new_pos)


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
