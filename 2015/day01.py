

def parse(raw_data):
    return raw_data.strip()


def part1(raw_data):
    data = parse(raw_data)
    return data.count('(') - data.count(')')


def part2(raw_data):
    data = parse(raw_data)
    floor = 0
    for pos,char in enumerate(data, start=1):
        floor += 1 if char=='(' else -1
        if floor == -1:
            return pos
