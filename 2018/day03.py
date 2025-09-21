import re

PATTERN = r'#(?P<id>\d+) @ (?P<lft>\d+),(?P<top>\d+): (?P<wi>\d+)x(?P<ht>\d+)'


def parse(text):
    claims = []
    for line in text.strip().split('\n'):
        m = re.match(PATTERN, line)
        claims.append({k:int(v) for k,v in m.groupdict().items()})
    return claims


def part1(text, part2=False):
    claims = parse(text)
    grid = [['.' for _ in range(1000)] for _ in range(1000)]
    colliders = set()
    for claim in claims:
        for row in range(claim['top'], claim['top']+claim['ht']):
            for col in range(claim['lft'], claim['lft']+claim['wi']):
                if grid[row][col] == '.':
                    grid[row][col] = claim['id']
                else:
                    colliders.add(claim['id'])
                    if grid[row][col] != 'X':
                        colliders.add(grid[row][col])
                        grid[row][col] = 'X'
    if not part2:
        return sum([row.count('X') for row in grid])
    for claim in claims:
        if claim['id'] not in colliders:
            return claim['id']


def part2(text):
    return part1(text, part2=True)

