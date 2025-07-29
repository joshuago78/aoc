

def parse(raw_input):
    new_string = ''
    char = raw_input[0]
    count = 1
    for i in range(1, len(raw_input)):
        if raw_input[i] == char:
            count += 1
        else:
            new_string += f'{count}{char}'
            char = raw_input[i]
            count = 1
    new_string += f'{count}{char}'
    return new_string

def part1(raw_input):
    for i in range(40):
        raw_input = parse(raw_input)
    return len(raw_input)


def part2(raw_input):
    for i in range(50):
        raw_input = parse(raw_input)
    return len(raw_input)
