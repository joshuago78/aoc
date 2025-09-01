import re


def parse(raw_input):
    progs = {}
    PATTERN = r'(?P<name>\w+) \((?P<weight>\d+)\)( -> (?P<kids>.+))*'
    for line in raw_input.strip().split('\n'):
        m = re.match(PATTERN, line)
        progs[m.group('name')] = {
            'weight': int(m.group('weight')),
            'children': m.group('kids').split(', ') if m.group('kids') else []}
    return progs


def find_root(progs):
    for parent_name in progs.keys():
        for vals in progs.values():
            if parent_name in vals['children']:
                break
        else:
            return parent_name


def get_totals(progs, p):
    progs[p]['total'] = sum([get_totals(progs,c) for c in progs[p]['children']])
    progs[p]['total'] += progs[p]['weight']
    return progs[p]['total']


def find_error(progs, node):
    # first find the problem child (or no problem)
    error = None
    for child in progs[node]['children']:
        diff_count = 0
        for c2 in progs[node]['children']:
            if progs[child]['total'] != progs[c2]['total']:
                diff_count += 1
                if diff_count > 1:
                    error = child
                    break
        if error is not None:
            break
    if error is None:
        return None

    # next, determine if the problem is with that child's children
    downstream_error = find_error(progs, error)
    if downstream_error:
        return downstream_error
        
    # if not, find the weight that would match siblings' totals
    sibling = [s for s in progs[node]['children'] if s!=error][0]
    ideal_wt = progs[sibling]['total']
    return ideal_wt - (progs[error]['total']-progs[error]['weight'])


def part1(raw_input):
    progs = parse(raw_input)
    return find_root(progs)


def part2(raw_input):
    progs = parse(raw_input)
    root = find_root(progs)
    get_totals(progs, root)
    return find_error(progs, root)

