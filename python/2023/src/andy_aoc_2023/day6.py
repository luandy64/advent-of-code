from collections import defaultdict
from functools import reduce
import math
from pprint import pprint
import re
import sys


def parse_raw_input(lines):
    return [
        re.split(
            r"\s+",
            re.split(r":\s+", line)[1].strip()
        )
        for line in lines
    ]

def distance_traveled(pressed, total_time):
    return pressed * (total_time - pressed)

def part1(lines):

    data = []
    for line in lines:
        data.append([int(num) for num in line])

    races = list(
        map(lambda *args: list(args),
            *data)
    )

    outputs = defaultdict(lambda : 0)
    for i, (total_time, record) in enumerate(races):
        for pressed in range(total_time + 1):
            d = distance_traveled(pressed, total_time)
            if d > record:
                outputs[i] += 1

    pprint(dict(outputs))
    print(reduce(lambda x,y: x*y, outputs.values(), 1))


def distance_between_roots(b, c):
    """Because we pass in non-zero `c`, this isn't a root, just the intersection"""
    # y = -x**2 + bx + 0
    # a = -1 , b = b, c = -c

    # x = -b +- sqrt(b**2 - 4ac) / 2a
    root = math.sqrt( b**2 - (4 * c) )
    x1 = (-b + root) / (-2)
    x2 = (-b - root) / (-2)
    print(f"  root {root}, x1 {x1}, x2 {x2}")
    return int(x2) - int(x1)

def part2(input):
    total_time, record = [int("".join(line)) for line in input]

    # x = -b +- sqrt(b**2 - 4ac) / 2a
    root = math.sqrt( total_time**2 - (4 * record) )
    x1 = (-total_time + root) // (-2)
    x2 = (-total_time - root) // (-2)
    print(f"  root {root}, x1 {x1}, x2 {x2}")
    print(int(x2) - int(x1))


with open(sys.argv[1]) as infile:
    input = parse_raw_input(infile.readlines())

part1(input)
part2(input)

print("--- EXPERIMENTAL ---")

data = []
for line in input:
    data.append([int(num) for num in line])

races = list(
    map(lambda *args: list(args),
        *data)
)

outputs = {}
for i, (total_time, record) in enumerate(races):
    print(f"time {total_time}, record {record}")
    outputs[i] = distance_between_roots(total_time, record)

pprint(outputs)

print(reduce(lambda x,y: x*y, outputs.values(), 1))
