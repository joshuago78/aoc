import itertools


AMOUNT = 150 #liters of eggnog


def parse(raw_input):
    return [int(l) for l in raw_input.strip().split('\n')]


def min_combo_size(jars):
    min_combo_size = 1
    while min_combo_size < len(jars):
        combo = jars[:min_combo_size]
        if sum(combo) >= AMOUNT:
            return min_combo_size
        min_combo_size += 1


def part1(raw_input):
    jars = sorted(parse(raw_input), reverse=True)
    start = min_combo_size(jars)
    good_combos = []
    for size in range(start, len(jars)):
        combos = itertools.combinations(jars, size)
        for combo in combos:
            if sum(combo) == AMOUNT:
                good_combos.append(combo)
    return len(good_combos)


def part2(raw_input):
    jars = sorted(parse(raw_input), reverse=True)
    start = min_combo_size(jars)
    good_combos = []
    for size in range(start, len(jars)):
        if len(good_combos) > 0:
            break
        combos = itertools.combinations(jars, size)
        for combo in combos:
            if sum(combo) == AMOUNT:
                good_combos.append(combo)
    return len(good_combos)
