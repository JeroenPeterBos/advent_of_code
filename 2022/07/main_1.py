import glob

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parse_lines(lines):
    commands = []
    line_iter = iter(lines)

    command = next(line_iter)[2:]
    outputs = []
    for line in line_iter:
        if line.startswith("$ "):
            commands.append((command, outputs))
            command = line[2:]
            outputs = []
        else:
            outputs.append(line)
    
    return commands


def process_commands(commands):
    files = {}
    directories = set()
    pwd = "/"
    for command, outputs in commands:
        if command.startswith("cd"):
            target = command[3:]
            if target == '/':
                pwd = "/"
            elif target == '..':
                if pwd == "/":
                    raise Exception("Cannot go up from root")
                pwd = "/".join(pwd.split('/')[:-1])
            else:
                pwd = f"{pwd}/{target}"
        elif command.startswith("ls"):
            for output in outputs:
                if output.startswith("dir"):
                    directories.add(f"{pwd}/{output[4:]}")
                else:
                    size, filename = output.split(' ')
                    files[f"{pwd}/{filename}"] = int(size)
    
    return files, directories


def main(lines):
    commands = parse_lines(lines)
    files, directories = process_commands(commands)
    
    total = 0
    for directory in directories:
        dir_size = sum(size for file, size in files.items() if file.startswith(directory))
        if dir_size <= 100_000:
            total += dir_size
    return total


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
