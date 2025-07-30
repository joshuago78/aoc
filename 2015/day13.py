from copy import deepcopy


def parse(raw_input):
    guests = {}
    for line in raw_input.strip().split('\n'):
        tokens = line.strip('.').split()
        a = tokens[0]
        b = tokens[-1]
        units = int(tokens[3])
        if tokens[2] == 'lose':
            units *= -1
        if a not in guests.keys():
            guests[a] = {}
        guests[a][b] = units
    return guests


def get_combos(combos, combo, names):
    if len(names) == 0:
        combos.append(deepcopy(combo))
    else:
        for i in range(len(names)):
            name = names.pop(0)
            combo.append(name)
            get_combos(combos, combo, names)
            combo.pop()
            names.append(name)
    return combos


def score(guests, combo):
    total = 0
    for pos,name in enumerate(combo):
        if pos == 0:
            left = combo[-1]
        else:
            left = combo[pos-1]
        if pos == len(combo)-1:
            right = combo[0]
        else:
            right = combo[pos+1]
        total += guests[name][left]
        total += guests[name][right]
    return total


def part1(raw_input):
    guests = parse(raw_input)
    names = list(guests.keys())
    combos = []
    combo = [names.pop(0),]
    combos = get_combos(combos, combo, names)
    return max([score(guests, c) for c in combos])


def part2(raw_input):
    guests = parse(raw_input)
    for name in guests.keys():
        guests[name]['me'] = 0
    guests['me'] = {name:0 for name in guests.keys()}
    names = list(guests.keys())
    combos = []
    combo = [names.pop(0),]
    combos = get_combos(combos, combo, names)
    return max([score(guests, c) for c in combos])
