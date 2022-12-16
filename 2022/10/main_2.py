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
    
    result = "\n"
    for line_offset in range(0, len(cycle_trace), 40):
        for crt_pos in range(40):
            cycle_index = line_offset + crt_pos
            sprite_pos = cycle_trace[cycle_index]

            if abs(sprite_pos - crt_pos) <= 1:
                result += "#"
            else:
                result += "."
        
        result += "\n"
    
    return result


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
