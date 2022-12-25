import glob
import re
import math
from pprint import pprint

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    pass


def main(lines):
    parse_lines(lines)


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
