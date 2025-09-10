


def spin(progs, length):
    return progs[-length:] + progs[:-length]


def exchange(progs, p1, p2):
    temp = progs[p1]
    progs[p1] = progs[p2]
    progs[p2] = temp
    return progs


def partner(progs, n1, n2):
    p1 = progs.index(n1)
    p2 = progs.index(n2)
    return exchange(progs, p1, p2)


def parse(raw_input):
    cmds = []
    for line in raw_input.strip().split(','):
        cmd,args = line[0], line[1:]
        match cmd:
            case 's':
                args = [int(args),]
                cmd = spin
            case 'x':
                args = [int(pos) for pos in args.split('/')]
                cmd = exchange
            case 'p':
                args = [name for name in args.split('/')]
                cmd = partner
        cmds.append((cmd,args))
    return cmds


def part1(raw_input):
    cmds = parse(raw_input)
    progs = [chr(97+i) for i in range(16)]
    for function, args in cmds:
        progs = function(progs, *args)
    return ''.join(progs)


def part2(raw_input):
    cmds = parse(raw_input)
    progs = list('abcdefghijklmnop')
    iterations = []
    while not iterations or iterations[-1]!='abcdefghijklmnop':
        for function, args in cmds:
            progs = function(progs, *args)
        iterations.append(''.join(progs))
    index = (1000000000 % len(iterations)) - 1
    return iterations[index]
