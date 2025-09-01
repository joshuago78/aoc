

def parse(raw_input, sort=False):
    lines = [line.split() for line in raw_input.strip().split('\n')]
    if sort:
        for i in range(len(lines)):
            lines[i] = [''.join(sorted(list(word))) for word in lines[i]]
    return lines


def part1(raw_input, sort=False):
    lines = parse(raw_input, sort=sort)
    count = 0
    for line in lines:
        valid = True
        while line:
            word = line.pop(0)
            if word in line:
                valid = False
                break
        if valid:
            count += 1
    return count


def part2(raw_input):
    return part1(raw_input, sort=True)
