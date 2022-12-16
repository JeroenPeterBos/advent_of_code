import glob

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def noop(state, args, cycle_trace):
    cycle_trace.append(state)
    return state


def addx(state, args, cycle_trace):
    cycle_trace.append(state)
    cycle_trace.append(state)
    return state + int(args[0])


func_map = {
    "noop": noop,
    "addx": addx,
}

def parse_line(line):
    func, *args = line.split(" ")
    return func_map[func], args


def main(lines):
    cycle_trace = []
    state = 1
    for line in lines:
        func, args = parse_line(line)
        state = func(state, args, cycle_trace)
    
    result = 0
    for cycle in range(19, len(cycle_trace), 40):
        result += cycle_trace[cycle] * (cycle + 1)
    
    return result


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
