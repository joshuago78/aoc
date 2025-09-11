

def part1(step_size, cycles=2017):
    buffer = [0]
    pos = 0
    for val in range(1,cycles+1):
        pos = 1 + (pos+int(step_size)) % val
        buffer.insert(pos, val)
    pos = 0 if pos==val else pos+1
    return buffer[pos]


def part2(step_size, cycles=50000000):
    idx0 = 0
    neighbor = None
    pos = 0
    for val in range(1,cycles+1):
        pos = 1 + (pos+int(step_size)) % val
        if pos == idx0+1:
            neighbor = val
        elif pos <= idx0:
            idx0 += 1
    return neighbor
