


def parse(raw_input):
    return raw_input.strip().split('\n')


def part1(raw_input):
    raw_length = 0
    esc_length = 0
    for line in parse(raw_input):
        esc_length += len(line)
        raw_length += len(bytes(line[1:-1], 'utf-8').decode('unicode_escape'))
    return esc_length - raw_length


def part2(raw_input):
    new_length = 0
    esc_length = 0
    for line in parse(raw_input):
        esc_length += len(line)
        new_length += len(line) + 4
        new_length += line.count('\\')
        new_length += line[1:-1].count('"')
    return new_length - esc_length
