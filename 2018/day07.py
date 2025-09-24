import re


def parse(text):
    pattern = r'Step (?P<p>\w+) must be finished before step (?P<c>\w+) can begin.'
    steps = {}
    for line in text.strip().split('\n'):
        d = re.match(pattern, line).groupdict()
        if d['p'] not in steps.keys():
            steps[d['p']] = {'id':d['p'], 'parents':[], 'children':[], 'time':ord(d['p'])-4}
        steps[d['p']]['children'].append(d['c'])
        if d['c'] not in steps.keys():
            steps[d['c']] = {'id':d['c'], 'parents':[], 'children':[], 'time':ord(d['c'])-4}
        steps[d['c']]['parents'].append(d['p'])
    roots = []
    for k,v in steps.items():
        if v['parents'] == []:
            roots.append(k)
    return sorted(roots), steps


def part1(text):
    available, steps = parse(text)
    sequence = [available.pop(0),]
    while steps:
        step = steps.pop(sequence[-1])
        for child in step['children']:
            if set(steps[child]['parents']).issubset(sequence):
                available.append(child)
        if available:
            available.sort()
            sequence.append(available.pop(0))
    return ''.join(sequence)


def part2(text):
    available, steps = parse(text)
    workers = [None for _ in range(5)]
    time = 0
    sequence = []
    while True:
        available.sort()
        queue = []
        for w in range(len(workers)):
            if workers[w] is None and len(available)>0:
                workers[w] = steps.pop(available.pop(0))
            if workers[w] is not None:
                workers[w]['time'] -= 1
                if workers[w]['time'] == 0:
                    sequence.append(workers[w]['id'])
                    for child in workers[w]['children']:
                        if set(steps[child]['parents']).issubset(sequence):
                            queue.append(child)
                    workers[w] = None
        available.extend(queue)
        time += 1
        if len(available)==0 and workers==[None for _ in range(5)]:
            return time
