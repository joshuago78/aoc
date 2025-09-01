

def parse(raw_input):
    return [int(i) for i in raw_input.strip().split('\n')]


def part1(raw_input):
    jumps = parse(raw_input)
    i = 0
    count = 0
    while i>=0 and i<len(jumps):
        jumps[i] += 1
        i += jumps[i] - 1
        count += 1
    return count


def part2(raw_input):
    jumps = parse(raw_input)
    i = 0
    count = 0
    while i>=0 and i<len(jumps):
        val = jumps[i]
        if val >= 3:
            jumps[i] -= 1
        else:
            jumps[i] += 1
        i += val
        count += 1
    return count