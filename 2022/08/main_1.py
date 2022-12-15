import glob
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    return np.array([list(map(int, line)) for line in lines])

def main(lines):
    grid = parse_lines(lines)
    number_of_edge_trees = (grid.shape[0] + grid.shape[1]) * 2 - 4

    number_of_visible_inner_trees = 0
    for x in range(1, grid.shape[0] - 1):
        for y in range(1, grid.shape[1] - 1):
            tree = grid[x, y]
            tree_lines = [
                grid[:x, y],
                grid[x+1:, y],
                grid[x, :y],
                grid[x, y+1:]
            ]

            if (np.array(list(map(np.max, tree_lines))) < tree).any():
                number_of_visible_inner_trees += 1
    
    return number_of_edge_trees + number_of_visible_inner_trees


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
