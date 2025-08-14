
WIDTH = 32
HEIGHT = 40
START = (1,1)
END = (31,39)
#END = (7,4)

def open_or_closed(x,y, fav):
    num = x*x + 3*x + 2*x*y + y + y*y
    num += fav
    ones = bin(num).count('1')
    if ones % 2 == 0:
        return '.'
    return '#'


def generate_map(width,height,fav):
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(open_or_closed(x,y,fav))
        grid.append(row)
    return grid


def possible_steps(path, fav):
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    last = path[-1]
    steps = []
    for d in directions:
        x,y = last[0]+d[0], last[1]+d[1]
        if x>= 0 and y>=0:
            if open_or_closed(x,y,fav) != '#' and (x,y) not in path:
                steps.append((x,y))
    return steps


def traverse(start, end,fav):
    paths = [[start,],]
    finished = False
    while not finished and len(paths)>0:
        path = paths.pop(0)
        steps = possible_steps(path,fav)
        for step in steps:
            new_path = path.copy()
            new_path.append(step)
            if step == end:
                return new_path
            paths.append(new_path)


def print_grid(grid, path=[]):
    for y,row in enumerate(grid):
        line = ''
        for x,char in enumerate(row):
            line += 'O' if (x,y) in path else char
        print(line)


def traverse_all(start,limit,fav):
    positions = set([start,])
    paths = [[start,],]
    while paths:
        path = paths.pop(0)
        steps = possible_steps(path,fav)
        for step in steps:
            new_path = path.copy()
            new_path.append(step)
            if len(new_path) <= 51:
                positions.add(step)
                paths.append(new_path)
    return list(positions)


def part1(raw_input):
    fav = int(raw_input.strip())
    path = traverse(START,END,fav)
    height = max([y for (x,y) in path]) + 1
    width = max([x for (x,y) in path]) + 1
    grid = generate_map(width,height,fav)
    print_grid(grid, path)
    return len(path)-1


def part2(raw_input):
    fav = int(raw_input.strip())
    positions = traverse_all(START,50,fav)
    height = max([y for (x,y) in positions]) + 1
    width = max([x for (x,y) in positions]) + 1
    grid = generate_map(width,height,fav)
    print_grid(grid, positions)
    return len(positions)
