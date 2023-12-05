from collections import defaultdict
from pprint import pprint
import re
import sys


def parse_raw_input(lines):
    chunks = []
    input_map = {}
    for line in lines:
        if (matches := re.match(r"(\d+) (\d+) (\d+)", line)):
            dest, source, range_length = map(int, matches.groups())
            input_map = input_map | dict(zip(range(source, source + range_length),
                                             range(dest, dest + range_length)))
        else:
            if input_map:
                chunks.append(input_map)
                input_map = {}

    # Need to get the last lines processed
    if input_map:
        chunks.append(input_map)

    return chunks

input_file = sys.argv[1]

with open(input_file) as infile:
    seeds = infile.readline().strip().split(": ")[1].split(" ")
    input_maps = parse_raw_input(infile.readlines())


states = []
for seed in map(int, seeds):
    state = seed
    for input_map in input_maps:
        new_state = input_map.get(state, state)
        state = new_state
    states.append(state)

print(f"{min(states)}")
