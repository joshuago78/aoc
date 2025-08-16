

TRAP_PATTERNS = [
    '^^.',
    '.^^',
    '^..',
    '..^'
]

def parse(raw_input):
    return '.' + raw_input.strip() + '.'


def next_row(prev):
    new = '.'
    for i in range(len(prev)-2):
        new += '^' if prev[i:i+3] in TRAP_PATTERNS else '.'
    new += '.'
    return new


def part1(raw_input, size=40):
    rows = []
    rows.append(parse(raw_input))
    for i in range(size-1):
        rows.append(next_row(rows[i]))
    return sum([row[1:-1].count('.') for row in rows])

def part2(raw_input):
    return part1(raw_input, size=400000)
    