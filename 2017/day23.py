from math import sqrt, ceil, floor


def parse(raw_input):
    return [line.split() for line in raw_input.strip().split('\n')]


def part1(raw_input):
    program = parse(raw_input)
    regs  = {c:0 for c in 'abcdefgh'}
    counter = 0
    mulcount = 0
    while counter>=0 and counter<len(program):
        offset = 1
        cmd, x, y = program[counter]
        y = int(y) if len(y)>1 or y.isdigit() else regs[y]
        match cmd:
            case 'set':
                regs[x] = y
            case 'sub':
                regs[x] -= y
            case 'mul':
                regs[x] *= y
                mulcount += 1
            case 'jnz':
                x = int(x) if len(x)>1 or x.isdigit() else regs[x]
                if x!= 0:
                    offset = y
        counter += offset
    return mulcount


def notprime(num):
    if num < 2:
        return True
    for div in range(2, floor(sqrt(num))):
        if num % div == 0:
            return True
    return False


def part2(raw_input):
    h = 0
    c = 108100 + 17001
    for num in range(108100, c, 17):
        if notprime(num):
            h += 1
    return h

