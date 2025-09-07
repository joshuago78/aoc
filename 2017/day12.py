

def parse(raw_input):
    programs = {}
    for line in raw_input.strip().split('\n'):
        pid, nids = line.split(' <-> ')
        programs[pid] = nids.split(', ')
    return programs


def traverse(programs, visited, node):
    if node not in visited:
        visited.append(node)
        for neighbor in programs[node]:
            visited = traverse(programs, visited, neighbor)
    return visited


def part1(raw_input):
    programs = parse(raw_input)
    network = traverse(programs, [], '0')
    return len(network)


def part2(raw_input):
    programs = parse(raw_input)
    groups = []
    while programs:
        start = list(programs.keys())[0]
        network = traverse(programs, [], start)
        groups.append(network)
        programs = {k:v for k,v in programs.items() if k not in network}
    return len(groups)

