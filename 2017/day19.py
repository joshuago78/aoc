

DIRS = {
    'down': (0,1),
    'up': (0,-1),
    'left': (-1,0),
    'right': (1,0)
}


def parse(raw_input):
    grid = raw_input.split('\n')
    x = grid[0].index('|')
    visited = [(x,0,'|')]
    return grid, visited


def move(grid, visited, direction):
    lastx,lasty,_ = visited[-1]
    x,y = lastx+DIRS[direction][0], lasty+DIRS[direction][1]
    symbol = grid[y][x]
    if symbol == ' ':
        return None
    visited.append((x,y,symbol))
    if symbol=='+':
        dirs = ('left','right') if direction in ('up','down') else ('up','down')
        for d in dirs:
            nextx, nexty = x+DIRS[d][0], y+DIRS[d][1]
            if nextx>=0 and nextx<len(grid[0]) and nexty>=0 and nexty<len(grid):
                if grid[nexty][nextx] != ' ':
                    direction = d
                    break
    return direction


def part1(raw_input, part2=False):
    grid, visited = parse(raw_input)
    direction = 'down'
    while direction is not None:
        direction = move(grid, visited, direction)
    if part2:
        return len(visited)
    return ''.join([c[2] for c in visited if c[2].isalpha()])


def part2(raw_input):
    return part1(raw_input, part2=True)
    