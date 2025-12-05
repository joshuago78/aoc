


def parse(data):
    return data.strip().split('\n')


def count_neighbors(grid, x, y):
    count = 0
    for n in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
        nx, ny = x+n[0], y+n[1]
        if nx>=0 and nx<len(grid[0]) and ny>=0 and ny<len(grid):
            if grid[ny][nx] == '@':
                count += 1
    return count


def part1(data):
    grid = parse(data)
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                if count_neighbors(grid, x, y) < 4:
                    total += 1
    return total


def part2(data):
    grid = parse(data)
    grand_total = 0
    total = None
    while total is None or total>0:
        total = 0
        new_grid = []
        for y in range(len(grid)):
            new_line = ''
            for x in range(len(grid[0])):
                if grid[y][x] == '@':
                    if count_neighbors(grid, x, y) < 4:
                        total += 1
                        new_line += '.'
                        continue
                new_line += grid[y][x]
            new_grid.append(new_line)
        grand_total += total
        grid = new_grid
    return grand_total
