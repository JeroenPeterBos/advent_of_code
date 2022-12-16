import glob
import re
import math
from pprint import pprint

def read_lines(filename):
    with open(filename) as f:
        return f.read()


def parse_lines(lines):
    monkeys = []
    for monkey_text in lines.split("\n\n"):
        monkeys.append(re.match(r"^Monkey (?P<id>\d+):\s*Starting items: (?P<item>\d+(, \d+)*)\s*Operation: new = (?P<func>[^\n]+)\s*Test: divisible by (?P<test_val>\d+)\s*If true: throw to monkey (?P<test_true>\d+)\s*If false: throw to monkey (?P<test_false>\d+)", monkey_text).groupdict())

    return [
        {
            'id': int(m['id']),
            'items': [int(i) for i in m['item'].split(", ")],
            'func': m['func'],
            'test_val': int(m['test_val']),
            'test_true': int(m['test_true']),
            'test_false': int(m['test_false']),
            'inspected_items': 0,
        }
        for m in monkeys
    ]

def main(lines):
    monkeys = parse_lines(lines)

    lcm = math.lcm(*[monkey["test_val"] for monkey in monkeys])

    for round in range(10000):
        for monkey in monkeys:
            monkey['inspected_items'] += len(monkey['items'])
            for old in monkey['items']:
                worry_level = eval(monkey['func'])
                worry_level = worry_level % lcm
                if worry_level % monkey['test_val'] == 0:
                    monkeys[monkey["test_true"]]['items'].append(worry_level)
                else:
                    monkeys[monkey["test_false"]]['items'].append(worry_level)
            monkey['items'] = []
        
        if round + 1 in (1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000):
        # if round % 1000 == 0:
            print(f"== After round {round + 1} ==")
            for monkey in monkeys:
                print(f"M{monkey['id']}: {monkey['inspected_items']:<20}")
                # pprint(monkey["items"])
            print("")
    
    a, b, *_ = sorted(monkeys, key=lambda m: m['inspected_items'], reverse=True)

    return a['inspected_items'] * b['inspected_items']


if __name__ == '__main__':
    for filename in sorted(glob.glob("*.txt")):
        try:
            result = main(read_lines(filename))
        except FileNotFoundError as e:
            result = "File does not exist"
        print(f"{filename:<15}: {result}")
