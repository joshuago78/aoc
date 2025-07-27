

MOVES = {
    '^': ( 0, 1),
    'v': ( 0,-1),
    '>': ( 1, 0),
    '<': (-1, 0)
}


def parse(raw_data):
    return [MOVES[char] for char in raw_data.strip()]


def traverse(houses, moves):
    x,y = 0,0
    for move in moves:
        x,y = tuple(map(sum, zip((x,y), move)))
        if x in houses.keys():
            if y not in houses[x]:
                houses[x].append(y)
        else:
            houses[x] = [y,]
    return houses


def part1(raw_data):
    moves = parse(raw_data)
    houses = {0:[0,]}
    houses = traverse(houses, moves)
    return sum([len(h) for h in houses.values()])


def part2(raw_data):
    moves = parse(raw_data)
    santa = [m for i,m in enumerate(moves) if i%2==0]
    robot = [m for i,m in enumerate(moves) if i%2!=0]
    houses = {0:[0,]}
    houses = traverse(houses, santa)
    houses = traverse(houses, robot)
    return sum([len(h) for h in houses.values()])
