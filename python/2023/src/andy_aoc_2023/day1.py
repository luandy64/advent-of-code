from functools import reduce
from operator import add
import re
import sys


NUMBERS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

BOTH = {**WORDS, **NUMBERS}


def get_numbers(line, parse_words=False):
    if parse_words:
        return re.findall(rf"(?=({'|'.join(BOTH)}))", line)
    return re.findall("|".join(NUMBERS.keys()), line)


def line_to_number(line, parse_words=False):
    string_nums = get_numbers(line, parse_words)

    if parse_words:
        lookup = BOTH
    else:
        lookup = NUMBERS

    first = lookup[string_nums[0]]
    last = lookup[string_nums[-1]]
    number = first + last
    return int(number)


def part1(lines):
    nums = map(line_to_number,
               lines)

    answer = reduce(add,
                    nums)
    print(answer)


def part2(lines):
    nums = map(lambda x: line_to_number(x, parse_words=True),
               lines)

    answer = reduce(add,
                    nums)

    print(answer)


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file) as infile:
        input_lines = [
            line.strip()
            for line in infile.readlines()
        ]

    part1(input_lines)
    part2(input_lines)
