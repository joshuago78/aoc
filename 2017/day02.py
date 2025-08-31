from itertools import combinations as combos


def parse(raw_input):
    rows = raw_input.strip().split('\n')
    return [[int(num) for num in row.split()] for row in rows]


def part1(raw_input):
    rows = parse(raw_input)
    return sum([max(row)-min(row) for row in rows])


def part2(raw_input):
    rows = parse(raw_input)
    total = 0
    for row in rows:
        for combo in combos(row, 2):
            quotient, remainder = divmod(max(combo),min(combo))
            if remainder == 0:
                total += quotient
                break
    return total
