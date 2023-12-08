from collections import defaultdict
from pprint import pprint
import re
import sys


def parse_raw_input(lines):
    chunks = []
    input_map = []
    for line in lines:
        if (matches := re.match(r"(\d+) (\d+) (\d+)", line)):
            dest, source, range_length = map(int, matches.groups())
            input_map.append((dest, source, range_length))
        else:
            if input_map:
                chunks.append(input_map)
                input_map = []

    # Need to get the last lines processed
    if input_map:
        chunks.append(input_map)

    return chunks


def part1(seeds, input_maps, states):
    for seed in seeds:
        state = seed
        for input_map in input_maps:
            new_state = state
            for partition in input_map:
                dest, source, range_length = partition
                if source <= state < source + range_length:
                    offset = dest - source
                    new_state = state + offset
                    break
            state = new_state
        states.append(state)

    return min(states)
    # print(f"{min(states)}")


# input_file = sys.argv[1]

# with open(input_file) as infile:
#     seeds = infile.readline().strip().split(": ")[1].split(" ")
#     input_maps = parse_raw_input(infile.readlines())

# part1(map(int, seeds), input_maps, [])

def partition(input, size):
    for i in range(0, len(input), size):
        yield input[i: i + size]



# states = []
# for start, size in partition(list(int(s) for s in seeds), 2):
#     print(start)
#     seed_range = range(start, start + size)

#     part1(seed_range, input_maps, states)
#     # part1((start, start + size), input_maps, states)
#     print(f"{states} : {min(states)}")

# print(f"{min(states)}")

# for start, size in partition(list(int(s) for s in seeds), 2):
#     print(start, size)

import json
# print(json.dumps(input_maps))
with open(sys.argv[1]) as infile:
    input_maps = json.load(infile)
start, length = map(int, sys.argv[2].split(" "))
# length = sys.argv[3]

# print(f"Would run with maps {len(input_maps)} {start} {length}")
seed_range = range(start, start + length)
print(part1(seed_range, input_maps, []))

#print(input_maps)




# for seed in map(int, seeds):
#     state = seed
#     for input_map in input_maps:
#         new_state = state
#         for partition in input_map:
#             dest, source, range_length = partition
#             if source <= state < source + range_length:
#                 offset = dest - source
#                 new_state = state + offset
#                 break
#         state = new_state
#     states.append(state)

# print(f"{min(states)}")
