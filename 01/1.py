#!/usr/bin/env python3

# https://adventofcode.com/2023/day/1 - "Trebuchet?!"
# Author: Greg Hamerly

import re
import sys

def part1(data):
    s = 0
    for line in data:
        line = [c for c in line if '0' <= c <= '9']
        s += int(line[0] + line[-1])
    return s

def part2(data):
    s = 0
    m = {name: str(i + 1) for i, name in enumerate('one two three four five six seven eight nine'.split())}
    m.update({d: str(i) for i, d in enumerate('0123456789')})

    first_pattern = re.compile('|'.join(m))
    last_pattern = re.compile('.*(' + '|'.join(m) + ')')

    for line in data:
        first = first_pattern.search(line).group(0)
        last = last_pattern.match(line).group(1)
        s += int(m[first] + m[last])

    return s

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
