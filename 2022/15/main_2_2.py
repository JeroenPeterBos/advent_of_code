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


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def generate_candidates(sensor, m_dist):
    candidates = set()
    for i in range(m_dist + 2):
        x_offset, y_offset = m_dist - i + 1, i
        for x, y in ((x_offset, y_offset), (x_offset, -y_offset), (-x_offset, -y_offset), (-x_offset, y_offset)):
            candidate = (sensor[0] + x, sensor[1] + y)
            if min(candidate) > 0 and max(candidate) < 4_000_000:
                candidates.add(candidate)
    return candidates


def main(lines, target):
    sensors = parse_lines(lines)

    print("== Generating candidates ==")
    # Generate positions just outside sensors
    candidates = dict()
    for sensor, beacon in sensors:
        print(f"Generating candidates for sensor {sensor} with beacon {beacon}")
        for candidate in generate_candidates(sensor, manhattan(sensor, beacon)):
            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1
    
    print("== Finding best candidate ==")
    # Find the best candidate
    for candidate in sorted(candidates, key=lambda x: candidates[x], reverse=True):
        print(f"Considering candidate {candidate} with {candidates[candidate]} sensors in range")
        for sensor, beacon in sensors:
            if manhattan(sensor, beacon) >= manhattan(sensor, candidate):
                break
        else:
            return candidate[0] * 4_000_000 + candidate[1]
    
    raise Exception("No candidate found")


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            target = 20 if "example" in filename else 4_000_000
            result = main(read_lines(filename), target)
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15} with target {target}: {result}")
