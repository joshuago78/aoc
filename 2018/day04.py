import re

PATTERN = r'\[1518-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] (?P<action>.*)'

def parse(text):
    log = []
    for line in text.strip().split('\n'):
        match = re.match(PATTERN, line)
        log.append(match.groupdict())
    return sorted(log, key=lambda x: x['month']+x['day']+x['hour']+x['minute'])


def part1(text, part2=False):
    log = parse(text)
    guards = {}
    guard, start, stop = None, None, None
    for entry in log:
        tokens = entry['action'].split()
        match tokens[0]:
            case 'Guard':
                if tokens[1] not in guards.keys():
                    guards[tokens[1]] = {'total':0, 'mins':[0 for _ in range(60)]}
                guard = guards[tokens[1]]
            case 'falls':
                start = int(entry['minute'])
            case 'wakes':
                stop = int(entry['minute'])
                for m in range(start, stop):
                    guard['mins'][m] += 1
                    guard['total'] += 1
    bestid, best = None, None
    if not part2:    
        for gid,vals in guards.items():
            if best is None or vals['total'] > best['total']:
                best, bestid = vals, gid
        return int(bestid[1:]) * best['mins'].index(max(best['mins']))
    for gid,vals in guards.items():
        maxmin = max(vals['mins'])
        if best is None or maxmin>best['maxmin']:
            best, bestid = vals, gid
            best['maxmin'] = maxmin
    return int(bestid[1:]) * best['mins'].index(best['maxmin'])


def part2(text):
    return part1(text, part2=True)

