

def parse(raw_input):
    lines, molecule = raw_input.strip().split('\n\n')
    subs = {}
    for line in lines.split('\n'):
        single, compound = line.split(' => ')
        if single in subs.keys():
            subs[single].append(compound)
        else:
            subs[single] = [compound,]
    return subs, molecule


def parse2(raw_input):
    lines, molecule = raw_input.strip().split('\n\n')
    subs = {}
    for line in lines.split('\n'):
        val, key = line.split(' => ')
        subs[key] = val
    return subs, molecule


def part1(raw_input):
    subs, molecule = parse(raw_input)
    combos = set()
    for key,vals in subs.items():
        idx = molecule.find(key)
        while idx >= 0:
            for val in vals:
                combos.add(molecule[:idx]+val+molecule[idx+len(key):])
            idx = molecule.find(key,idx+1)
    return len(combos)


def part2(raw_input):
    subs, molecule = parse2(raw_input)
    longest = sorted(subs.keys(), key=len, reverse=True) 
    steps = 0
    while molecule != 'e':
        steps += 1
        for key in longest:
            if key in molecule:
                molecule = molecule.replace(key, subs[key], 1)
                break
    return steps
