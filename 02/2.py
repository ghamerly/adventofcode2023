#!/usr/bin/env python3

# https://adventofcode.com/2023/day/2 - "Cube Conundrum"
# Author: Greg Hamerly

import sys

def part1(data):
    # The Elf would first like to know which games would have been possible if
    # the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    def valid_game(sets):
        return sets['red'] <= 12 and sets['green'] <= 13 and sets['blue'] <= 14

    sum_valid_game_ids = 0
    for game_id, sets in data:
        if all(valid_game(s) for s in sets):
            sum_valid_game_ids += game_id

    return sum_valid_game_ids

def part2(data):
    sum_powers = 0
    for game_id, sets in data:
        min_vals = {'red': 0, 'green': 0, 'blue': 0}
        for s in sets:
            for color in s:
                min_vals[color] = max(min_vals[color], s[color])

        p = min_vals['red'] * min_vals['green'] * min_vals['blue']
        sum_powers += p
    return sum_powers


def mogrify(line):
    game_number, sets = line.split(': ')
    game_id = int(game_number.split()[1])
    parsed_sets = []
    for s in sets.split('; '):
        parsed_sets.append({'red': 0, 'blue': 0, 'green': 0})
        for cube in s.split(','):
            num, color = cube.split()
            assert color in parsed_sets[-1], f"'{color}'"
            parsed_sets[-1][color] = int(num)

    return game_id, parsed_sets

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))

    print('part 1:', part1(data))
    print('part 2:', part2(data))

if __name__ == '__main__':
    main()
