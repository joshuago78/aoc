import re


def parse(raw_input):
    particles = []
    for num, line in enumerate(raw_input.strip().split('\n')):
        pattern = r'p=<(?P<p>[0-9\-\,]+)>, v=<(?P<v>[0-9\-\,]+)>, a=<(?P<a>[0-9\-\,]+)>'
        m = re.match(pattern, line)
        particle = {
            'id': num,
            'pos': [int(i) for i in m.group('p').split(',')],
            'vel': [int(i) for i in m.group('v').split(',')],
            'acc': [int(i) for i in m.group('a').split(',')],
            'dist1': sum([abs(int(i)) for i in m.group('p').split(',')]),
            'dist2': None,
            'acc2': 0
        }
        particles.append(particle)
    return particles


def part1(raw_input):
    particles = parse(raw_input)
    for tick in range(1,1000):
        for part in particles:
            for coord in range(3):
                part['vel'][coord] += part['acc'][coord]
                part['pos'][coord] += part['vel'][coord]
            part['dist2'] = sum([abs(int(j)) for j in part['pos']])
            part['acc2'] = (part['dist2'] - part['dist1']) / tick**2
    return sorted(particles, key=lambda x: x['acc2'])[0]['id']


def part2(raw_input):
    particles = parse(raw_input)
    for tick in range(1,1000):
        # update velocities and positions
        for part in particles:
            for coord in range(3):
                part['vel'][coord] += part['acc'][coord]
                part['pos'][coord] += part['vel'][coord]
        # check for collisions
        colliders = []
        for i in range(len(particles)):
            collision = False
            p1 = particles[i]
            for j in range(i+1,len(particles)):
                p2 = particles[j]
                if p1['pos'] == p2['pos']:
                    colliders.append(p1['id'])
                    colliders.append(p2['id'])
                    collision = True
                    break
        # remove colliders from set
        for id in colliders:
            for idx, part in enumerate(particles):
                if id == part['id']:
                    particles.pop(idx)
                    break
    return len(particles)
        