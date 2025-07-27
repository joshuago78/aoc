import re


PATTERN = r'(?P<length>\d+)x(?P<width>\d+)x(?P<height>\d+)'


def parse(raw_data):
    lines = raw_data.strip().split('\n')
    gifts = []
    for line in lines:
        match = re.match(PATTERN, line)
        gifts.append({k:int(v) for k,v in match.groupdict().items()})
    return gifts


def part1(raw_data):
    gifts = parse(raw_data)
    total = 0
    for gift in gifts:
        areas = [
            gift['length'] * gift['width'],
            gift['width'] * gift['height'],
            gift['length'] * gift['height']
        ]
        total += 2 * sum(areas) + min(areas)
    return total



def part2(raw_data):
    gifts = parse(raw_data)
    total = 0
    for gift in gifts:
        volume = gift['length'] * gift['width'] * gift['height']
        perimeter = 2 * sum(sorted(gift.values())[:2])
        total += volume + perimeter
    return total
