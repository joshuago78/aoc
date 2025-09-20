

def parse(raw_input):
    grid = [list(line) for line in raw_input.strip().split('\n')]
    y = len(grid) // 2
    x = len(grid[0]) // 2
    return grid, (x,y, 'N')


def part1(raw_input, iterations=10000):
    grid, (x,y,d) = parse(raw_input)
    dirs = ['N','E','S','W']
    steps = [(0,-1),(1,0),(0,1),(-1,0)]
    infect_count = 0
    for i in range(iterations):
        # turn right if infected, otherwise turn left
        offset = 1 if grid[y][x] == '#' else -1
        idx = (dirs.index(d)+offset) % 4
        d = dirs[idx]
        step = steps[idx]

        # flip infected status
        if grid[y][x]=='.':
            grid[y][x] = '#'
            infect_count += 1
        else:
            grid[y][x] = '.' 
        
        # expand grid if necessary
        if x==0:
            for row in grid:
                row.insert(0, '.')
            x=1
        elif x==len(grid[0])-1:
            for row in grid:
                row.append('.')
        if y ==0:
            grid.insert(0, ['.']*len(grid[0]))
            y = 1
        elif y==len(grid)-1:
            grid.append(['.']*len(grid[0]))

        # move forward
        x, y = x+step[0], y+step[1]

    return infect_count


def part2(raw_input, iterations=10000000):
    grid, (x,y,d) = parse(raw_input)
    dirs = ['N','E','S','W']
    steps = [(0,-1),(1,0),(0,1),(-1,0)]
    infect_count = 0
    for i in range(iterations):
        
        # turn and flip
        match grid[y][x]:
            case '.':
                offset = -1
                grid[y][x] = 'w'
            case 'w':
                offset = 0
                grid[y][x] = '#'
                infect_count += 1
            case '#':
                offset = 1
                grid[y][x] = 'f'
            case 'f':
                offset = 2
                grid[y][x] = '.'
        idx = (dirs.index(d)+offset) % 4
        d = dirs[idx]
        step = steps[idx]
        
        # expand grid if necessary
        if x==0:
            for row in grid:
                row.insert(0, '.')
            x=1
        elif x==len(grid[0])-1:
            for row in grid:
                row.append('.')
        if y ==0:
            grid.insert(0, ['.']*len(grid[0]))
            y = 1
        elif y==len(grid)-1:
            grid.append(['.']*len(grid[0]))

        # move forward
        x, y = x+step[0], y+step[1]

    return infect_count


