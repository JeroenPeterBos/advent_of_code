import glob
import re
import math
import numpy as np
from pprint import pprint

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    sensors = []
    for line in lines:
        sensor = []
        for part in line.split(":"):
            x, y = part.split(", y=")
            x = x.split("x=")[1]
            sensor.append((int(x), int(y)))
        sensors.append(sensor)
    return sensors


def default_mask(target):
    return np.ones(shape=(target + 1, target + 1), dtype=np.int8)


def diamond_mask(manhattan):
    n = manhattan * 2 + 1
    a = np.arange(n)
    b = np.minimum(a,a[::-1])
    return ((b[:,None]+b)<(n-1)//2).astype(np.int8)


def print_mask(mask):
    for row in mask:
        print("".join("#" if x == 1 else "." for x in row))


def main(lines, target):
    print("== Generating default mask ==")
    sensors = parse_lines(lines)
    mask = default_mask(target)

    for i, (sensor, beacon) in enumerate(sensors):
        print(f"== Processing sensor {i} / {len(sensors)} ==")

        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        diamond = diamond_mask(manhattan)

        x_min = sensor[0] - manhattan
        if x_min < 0:
            diamond = diamond[-x_min:, :]
            x_min = 0
        
        x_max = sensor[0] + manhattan + 1
        if x_max > mask.shape[0]:
            diamond = diamond[:-(x_max - mask.shape[0]), :]
            x_max = mask.shape[0]

        y_min = sensor[1] - manhattan
        if y_min < 0:
            diamond = diamond[:, -y_min:]
            y_min = 0
        
        y_max = sensor[1] + manhattan + 1
        if y_max > mask.shape[1]:
            diamond = diamond[:, :-(y_max - mask.shape[1])]
            y_max = mask.shape[1]

        mask_match = mask[x_min: x_max, y_min: y_max]
        overlayed = mask_match & diamond
        mask[x_min: x_max, y_min:y_max] = overlayed

    print("== Searching for the beacon position ==")
    pos_x, pos_y = np.where(mask == 1)

    print(f"== Found {len(pos_x)} possible positions ==")

    return pos_x[0] * 4_000_000 + pos_y[0]


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            target = 20 if "example" in filename else 4_000_000
            result = main(read_lines(filename), target)
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15} with target {target}: {result}")
