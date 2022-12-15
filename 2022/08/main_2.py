import glob
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    return np.array([list(map(int, line)) for line in lines])


def view_distance(grid, pos, direction):
    tree_height = grid[pos]
    views = 0
    while True:
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos[0] < 0 or pos[0] >= grid.shape[0] or pos[1] < 0 or pos[1] >= grid.shape[1]:
            return views

        views += 1
        if grid[pos] >= tree_height:
            return views


def main(lines):
    grid = parse_lines(lines)

    max_score = 0
    for x in range(1, grid.shape[0] - 1):
        for y in range(1, grid.shape[1] - 1):
            pos = (x, y)
            tree_views = [
                view_distance(grid, pos, direction)
                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            ]
            max_score = max(max_score, np.product(tree_views))

    return max_score


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
