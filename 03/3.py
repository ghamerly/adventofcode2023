#!/usr/bin/env python3

# https://adventofcode.com/2023/day/3 - "Gear Ratios"
# Author: Greg Hamerly

import re
import sys

def part1(data):
    symbols = set()
    for r, row in enumerate(data):
        symbols.update([(r, c) for c, col in enumerate(row) if col not in '0123456789.'])

    ans = 0
    p = re.compile('[0-9]+')
    for r, row in enumerate(data):
        for m in p.finditer(row):
            keep = False
            low, hi = m.span()
            for rr in range(r-1, r+2):
                for cc in range(low-1, hi+1):
                    if (rr, cc) in symbols:
                        keep = True
            if keep:
                ans += int(m.group())

    return ans

def part2(data):
    potential_gears = {}
    for r, row in enumerate(data):
        potential_gears.update({(r, c): [] for c, col in enumerate(row) if col == '*'})

    p = re.compile('[0-9]+')
    for r, row in enumerate(data):
        for m in p.finditer(row):
            keep = False
            low, hi = m.span()
            for rr in range(r-1, r+2):
                for cc in range(low-1, hi+1):
                    if (rr, cc) in potential_gears:
                        potential_gears[(rr, cc)].append(int(m.group()))
                        keep = True

    ans = 0
    for _, vals in potential_gears.items():
        if len(vals) == 2:
            ans += vals[0] * vals[1]
    return ans

def mogrify(line):
    return line

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
