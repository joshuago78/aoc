

def parse(raw_input):
    commands = raw_input.strip().split(', ')
    return [(c[0],int(c[1:])) for c in commands]


def new_direction(current, turn):
    dirs = ['north','east','south','west']
    offset = 1 if turn == 'R' else -1
    index = (dirs.index(current) + offset) % 4
    return dirs[index]


def part1(raw_input):
    commands = parse(raw_input)
    position = [0,0]
    direction = 'north'
    while commands:
        turn,dist = commands.pop(0)
        direction = new_direction(direction, turn)
        match direction:
            case 'north':
                position[1] += dist
            case 'east':
                position[0] += dist
            case 'south':
                position[1] -= dist
            case 'west':
                position[0] -= dist
    return abs(position[0]) + abs(position[1])


def part2(raw_input):
    commands = parse(raw_input)
    positions = [[0,0],]
    direction = 'north'
    while commands:
        turn,dist = commands.pop(0)
        direction = new_direction(direction, turn)
        for i in range(dist):
            current = positions[-1]
            new_position = current.copy()
            match direction:
                case 'north':
                    new_position[1] += 1
                case 'east':
                    new_position[0] += 1
                case 'south':
                    new_position[1] -= 1
                case 'west':
                    new_position[0] -= 1
            if new_position in positions:
                return abs(new_position[0]) + abs(new_position[1])
            positions.append(new_position)

