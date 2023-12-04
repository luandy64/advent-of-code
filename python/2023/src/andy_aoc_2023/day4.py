from collections import defaultdict
from pprint import pprint
import re
import sys


def parse_raw_input(lines):
    output ={}
    for line in lines:
        card_num, numbers = line.strip().split(": ")
        card_id = card_num.split(" ")[-1]
        winning_nums, our_nums = numbers.split(" | ")
        output[card_id] = {
            "win": re.split(r"\s+", winning_nums),
            "our": re.split(r"\s+", our_nums),
        }
    return output

def part_1(input_lines):
    total = 0
    for id, cards in input_lines.items():
        win = set(cards["win"])
        our = set(cards["our"])

        matches = win.intersection(our)
        count = val if (val := len(matches)) > 0 else 0
        points = (2 ** (count - 1) // 1)
        total += points
        print(f"Card {id} has {count} {matches} matches, {points} points,  total {total}")


def part_2(input_lines):
    instances = defaultdict(lambda : 0)
    for id, cards in input_lines.items():
        instances[id] += 1
        for _ in range(instances[id]):
            win = set(cards["win"])
            our = set(cards["our"])

            matches = win.intersection(our)
            count = val if (val := len(matches)) > 0 else 0

            for x in range(count):
                copy_num = int(id) + 1 + x
                instances[str(copy_num)] += 1

    print(f"Total {sum( x for x in instances.values() )}")


input_file = sys.argv[1]

with open(input_file) as infile:
    input_lines = parse_raw_input(infile.readlines())

part_1(input_lines)
part_2(input_lines)
