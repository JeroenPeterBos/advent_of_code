import glob
import math

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

direction_map = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

def parse_line(line):
    direction, distance = line.split(" ")
    return direction_map[direction], int(distance)


def add_pos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def main(lines):
    head = (0, 0)
    tail = (0, 0)

    tail_positions = {tail}

    for line in lines:
        direction, distance = parse_line(line)
        for _ in range(distance):
            head = add_pos(head, direction)

            x_dist = head[0] - tail[0]
            y_dist = head[1] - tail[1]

            if math.sqrt(x_dist ** 2 + y_dist ** 2) > math.sqrt(2):
                tail = add_pos(tail, (min(max(x_dist, -1), 1), min(max(y_dist, -1), 1)))

            tail_positions.add(tail)
    
    return len(tail_positions)


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
