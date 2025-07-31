

MATCH = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def parse(raw_input):
    aunts = []
    for line in raw_input.strip().split('\n'):
        aunt = {}
        line = line[line.index(':')+2:]
        atts = line.split(', ')
        for att in atts:
            key,val = att.split(': ')
            aunt[key] = int(val)
        aunts.append(aunt)
    return aunts


def get_score(aunt, part2=False):
    score = 0
    for key,val in aunt.items():
        if part2 and key in ['trees', 'cats', 'pomeranians', 'goldfish']:
            if key in ['trees', 'cats']:
                score += 1 if val > MATCH.get(key) else 0
            elif key in ['pomeranians', 'goldfish']:
                score += 1 if val < MATCH.get(key) else 0
        else:
            score += 1 if MATCH.get(key) == val else 0
    return score


def part1(raw_input):
    aunts = parse(raw_input)
    best_match = None
    best_score = 0
    for num, aunt in enumerate(aunts, start=1):
        score = get_score(aunt)
        if score > best_score:
            best_score = score
            best_match = num
    return best_match


def part2(raw_input):
    aunts = parse(raw_input)
    best_match = None
    best_score = 0
    for num, aunt in enumerate(aunts, start=1):
        score = get_score(aunt, part2=True)
        if score > best_score:
            best_score = score
            best_match = num
    return best_match
