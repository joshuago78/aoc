

def parse(raw_input):
    return raw_input.strip().split('\n')


def part1(raw_input, reverse=True):
    lines = parse(raw_input)
    counts = [{} for i in range(len(lines[0]))]
    for line in lines:
        for i,c in enumerate(line):
            if c in counts[i].keys():
                counts[i][c] += 1
            else:
                counts[i][c] = 1
    counts = [sorted(d.items(), key=lambda x: x[1], reverse=reverse) for d in counts]
    password = [c[0][0] for c in counts]
    return ''.join(password)


def part2(raw_input):
    return part1(raw_input, reverse=False)
