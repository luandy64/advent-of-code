from functools import reduce
from operator import mul as multiply
from pprint import pprint
import sys


def parse_raw_input(lines):
    input_lines = [
        line.strip().split("; ")
        for line in lines
    ]

    line_map = {}

    for line in input_lines:
        game_id, first_game  = line[0].split(": ")
        int_id = int(game_id.split(" ")[-1])
        line_map[int_id] = [first_game] + line[1:]

    return line_map


def input_to_game_lists(input_lines):
    games = {
        id:  [
            {pieces[1]: pieces[0]}
            for game in line
            for color in game.split(", ")
            if (pieces := color.split(" "))
        ]
        for id, line in input_lines.items()

    }

    summed_games = {}
    for id, line in games.items():
        state = {"red": [], "blue": [], "green": []}
        for game in line:
            key = list(game.keys())[0]
            value = game[key]
            state[key].append(int(value))
        summed_games[id] = state

    return summed_games


def part1(input_lines):
    summed_games = input_to_game_lists(input_lines)
    filtered_games = {}

    for id, game in summed_games.items():
        if (
                all(x <= 12 for x in game["red"])
                and all(x <= 13 for x in game["green"])
                and all(x <= 14 for x in game["blue"])
        ):
            filtered_games[id] = game

    print(sum(id for id in filtered_games))


def part2(input_lines):
    summed_games = input_to_game_lists(input_lines)

    maxed_games = {
        id : {
            k : max(v)
            for k, v in game.items()
        }
        for id, game in summed_games.items()
    }

    powers = {
        id: reduce(multiply, game.values())
        for id, game in maxed_games.items()
    }

    pprint(sum(powers.values()))


input_file = sys.argv[1]

with open(input_file) as infile:
    input_lines = parse_raw_input(infile.readlines())

part1(input_lines)
part2(input_lines)
