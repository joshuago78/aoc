import re


def parse(raw_input):
    discs = []
    pattern = r'Disc #(?P<dnum>\d+) has (?P<size>\d+) positions; at time=0, it is at position (?P<start>\d+).'
    for line in raw_input.strip().split('\n'):
        m = re.match(pattern,line)
        disc = {k:int(v) for k,v in m.groupdict().items()}
        discs.append(disc)
    return discs


def aligned(t,disc):
    return (t+disc['start']) % disc['size'] == 0


def part1(raw_input, extra_disc=None):
    discs = parse(raw_input)
    if extra_disc:
        discs.append(extra_disc)
    t = 0
    while True:
        for disc in discs:
            if not aligned(t+disc['dnum'],disc):
                t += 1
                break
        else:
            return t


def part2(raw_input):
    extra_disc = {'dnum':7, 'size':11, 'start':0}
    return part1(raw_input, extra_disc)
