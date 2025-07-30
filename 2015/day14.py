DURATION = 2503
#DURATION = 1000


def parse(raw_input):
    reindeer = {}
    for line in raw_input.strip().split('\n'):
        tokens = line.split()
        reindeer[tokens[0]] = {
            'speed': int(tokens[3]),
            'timefly': int(tokens[6]),
            'timerest': int(tokens[-2]),
            'status': 'flying',
            'countdown': int(tokens[6]),
            'distance': 0,
            'score': 0
        }
    return reindeer


def update(deer):
    if deer['status'] == 'flying':
        deer['distance'] += deer['speed']
    deer['countdown'] -= 1
    if deer['countdown'] == 0:
        if deer['status'] == 'flying':
            deer['status'] = 'resting'
            deer['countdown'] = deer['timerest']
        else:
            deer['status'] = 'flying'
            deer['countdown'] = deer['timefly']


def part1(raw_input):
    reindeer = parse(raw_input)
    for s in range(DURATION):
        for deer in reindeer.values():
            update(deer)
    return max([d['distance'] for d in reindeer.values()])


def score(reindeer):
    farthest = 0
    leads = []
    for deer, nums in reindeer.items():
        if nums['distance'] > farthest:
            leads = [deer,]
            farthest = nums['distance']
        elif nums['distance'] == farthest:
            leads.append(deer)
    for lead in leads:
        reindeer[lead]['score'] += 1


def part2(raw_input):
    reindeer = parse(raw_input)
    for s in range(DURATION):
        for deer in reindeer.values():
            update(deer)
        score(reindeer)
    return max([d['score'] for d in reindeer.values()])
