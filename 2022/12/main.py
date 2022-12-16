import glob
import re
import math
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def char_to_int(char):
    return ord(char) - ord('a')


def index_of(grid, char):
    x, y = np.where(grid == char_to_int(char))
    return x[0], y[0]


def parse_lines(lines):
    grid = np.array([
        [
            char_to_int(char) for char in line
        ] for line in lines
    ])

    start = index_of(grid, "S")
    end = index_of(grid, "E")

    grid[start] = char_to_int("a")
    grid[end] = char_to_int("z")

    return grid, start, end


def main(lines):
    grid, start, end = parse_lines(lines)

    distance = {start: 0}
    open_set = {start}

    while open_set:
        current = min(open_set, key=lambda pos: distance[pos])
        open_set.remove(current)

        if current == end:
            return distance[current]

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            if new_pos[0] < 0 or new_pos[0] >= grid.shape[0] or new_pos[1] < 0 or new_pos[1] >= grid.shape[1]:
                # Does not exist
                continue

            if grid[current] + 1 < grid[new_pos]:
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
