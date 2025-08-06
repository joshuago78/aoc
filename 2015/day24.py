from itertools import combinations
from math import prod


def parse(raw_input):
    return [int(line) for line in raw_input.strip().split()]


def part1(raw_input, bin_count=3):
    gifts = parse(raw_input)
    bin_size = sum(gifts) // bin_count
    for qty in range(1,len(gifts)+1):
        combos = [c for c in combinations(gifts, qty) if sum(c)==bin_size]
        if len(combos) > 0:
            return min([prod(c) for c in combos])


def part2(raw_input):
    return part1(raw_input, bin_count=4)
