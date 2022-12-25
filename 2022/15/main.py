import glob
import re
import math
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


def main(lines, target):
    sensors = parse_lines(lines)
    line = target
    xs = set()
    beacons = set()

    for i in range(len(sensors)):
        sensor = sensors[i][0]
        beacon = sensors[i][1]
        beacons.add(beacon)

        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distance_to_line = abs(line - sensor[1])
        remaining_range = manhattan - distance_to_line
        if remaining_range >= 0:
            reacheable_xs = set(range(sensor[0] - remaining_range, sensor[0] + remaining_range + 1))
            xs = xs | reacheable_xs
    
    beacons_in_line = sum(1 if beacon[1] == line else 0 for beacon in beacons)
    return len(xs) - beacons_in_line


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            target = 10 if "example" in filename else 2_000_000
            result = main(read_lines(filename), target)
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15} with target {target}: {result}")
