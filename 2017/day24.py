

def parse(raw_input):
    return [tuple(line.split('/')) for line in raw_input.strip().split('\n')]


def explore(bridges, bridge, parts):
    for idx in range(len(parts)):
        part = parts.pop(idx)
        if bridge[-1][-1] in part:
            if part[0] != bridge[-1][-1]:
                part = (part[1],part[0])
            new_bridge = bridge.copy()
            new_bridge.append(part)
            bridges.append(new_bridge)
            explore(bridges, new_bridge, parts)
        parts.insert(idx, part)


def part1(raw_input, longest=False):
    parts = parse(raw_input)
    bridges = []
    bridge = [('0','0'),]
    explore(bridges, bridge, parts)
    best = {'length':0, 'strength':0, 'path':None}
    for bridge in bridges:
        strength = sum([sum([int(p) for p in part]) for part in bridge])
        if longest is True:
            length = len(bridge)
            if length>best['length'] or (length==best['length'] and strength>best['strength']):
                best = {'length':length, 'strength':strength, 'path':bridge}
        elif strength>best['strength']:
            best = {'length':length, 'strength':strength, 'path':bridge}
    return best['strength']


def part2(raw_input):
    return part1(raw_input, longest=True)

