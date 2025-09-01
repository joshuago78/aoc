

def parse(raw_input):
    return [int(i) for i in raw_input.strip().split('\n')]


def part1(raw_input):
    jumps = parse(raw_input)
    i, count = 0, 0
    while i>=0 and i<len(jumps):
        jumps[i] += 1
        i += jumps[i] - 1
        count += 1
    return count


def part2(raw_input):
    jumps = parse(raw_input)
    i, count = 0, 0
    while i>=0 and i<len(jumps):
        val = jumps[i]
        jumps[i] += -1 if val >= 3 else 1
        i += val
        count += 1
    return count