

FACTOR_A = 16807
FACTOR_B = 48271


class Generator(object):

    divisor = 2147483647

    def __init__(self, name, start, factor, picky=False):
        self.name = name
        self.start = start
        self.factor = factor
        self.current = start
        self.picky = picky

    def next(self):
        self.current = (self.current * self.factor) % self.divisor
        if self.picky and self.current % self.picky != 0:
            return self.next()
        return self.current

    def next_low_bin(self):
        return f'{self.next():016b}'[-16:]



def parse(raw_input):
    startA, startB = [line.split()[-1] for line in raw_input.strip().split('\n')]
    return int(startA), int(startB)


def part1(raw_input):
    startA, startB = parse(raw_input)
    genA = Generator('A', startA, FACTOR_A)
    genB = Generator('B', startB, FACTOR_B)
    matches = 0
    for i in range(40000000):
        if genA.next_low_bin() == genB.next_low_bin():
            matches += 1
    return matches


def part2(raw_input):
    startA, startB = parse(raw_input)
    genA = Generator('A', startA, FACTOR_A, picky=4)
    genB = Generator('B', startB, FACTOR_B, picky=8)
    matches = 0
    for i in range(5000000):
        if genA.next_low_bin() == genB.next_low_bin():
            matches += 1
    return matches

