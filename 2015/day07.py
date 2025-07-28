


def parse(raw_input):
    wires = {}
    for line in raw_input.strip().split('\n'):
        tokens = [int(t) if t.isdigit() else t for t in line.split()]
        wire = tokens[-1]
        if len(tokens) == 3:
            cmd = 'ASSIGN'
            inputs = tokens[0]
        elif len(tokens) == 4:
            cmd = 'NOT'
            inputs = tokens[1]
        else:
            cmd = tokens[1]
            if 'SHIFT' in cmd:
                tokens[2] = int(tokens[2])
            inputs = [tokens[0], tokens[2]]
        wires[wire] = {'cmd':cmd, 'inputs':inputs}
    return wires


def assign(wires, key):
    value = wires[key]['inputs']
    if type(value) != int:
        value = execute(wires, value)
    wires[key] = value
    return value


def donot(wires, key):
    value = wires[key]['inputs']
    if type(value) != int:
        value = execute(wires, value)
    wires[key] = ~value & 0xffff
    return wires[key]


def shift(wires, key):
    source, dist = wires[key]['inputs']
    value = wires[source]
    if type(value) != int:
        value = execute(wires, source)
    if wires[key]['cmd'] == 'LSHIFT':
        wires[key] = value << dist
    else:
        wires[key] = value >> dist
    return wires[key]


def andor(wires, key):
    a = wires[key]['inputs'][0]
    b = wires[key]['inputs'][1]
    if type(a) != int:
        a = execute(wires, a)
    if type(b) != int:
        b = execute(wires, b)
    if wires[key]['cmd'] == 'AND':
        wires[key] = a & b
    else:
        wires[key] = a | b
    return wires[key]


def execute(wires, key):
    if type(wires[key]) == int:
        return wires[key]
    cmd = wires[key]['cmd']
    if cmd == 'ASSIGN':
        return assign(wires, key)
    if cmd == 'NOT':
        return donot(wires, key)
    if cmd in ['AND', 'OR']:
        return andor(wires, key)
    if 'SHIFT' in cmd:
        return shift(wires, key)
    print('unknown cmd')


def part1(raw_input):
    wires = parse(raw_input)
    for key in wires.keys():
        execute(wires, key)
    return wires['a']


def part2(raw_input):
    wires = parse(raw_input)
    wires['b'] = 3176
    for key in wires.keys():
        execute(wires, key)
    return wires['a']
