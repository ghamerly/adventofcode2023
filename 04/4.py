#!/usr/bin/env python3

# https://adventofcode.com/2023/day/4 - "Scratchcards"
# Author: Greg Hamerly

import sys

def part1(data):
    ans = 0
    for card, hand in data:
        assert len(set(card)) == len(card)
        assert len(set(hand)) == len(hand)
        have = set(hand) & set(card)
        if have:
            ans += 2 ** (len(have) - 1)

    return ans

def part2(data):
    copies = [1] * len(data)
    for i, (card, hand) in enumerate(data):
        have = set(hand) & set(card)
        if have:
            for j in range(i+1, i+len(have)+1):
                copies[j] += copies[i]

    return sum(copies)

def mogrify(line):
    a, b = line.split(' | ')
    f = lambda x: list(map(int, x))
    return (f(a.split()[2:]), f(b.split()))

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
