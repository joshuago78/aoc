

def parse(data, part2=False):
    grid = [list(line) for line in data.strip().split('\n')]
    if part2:
        grid = [[0 if c=='.' else c for c in row] for row in grid]
        grid[0][grid[0].index('S')] = 1
    return grid


def descend(grid, row, col):
    if grid[row+1][col] == '^':
        grid[row+1][col-1] = '|'
        grid[row+1][col+1] = '|'
        return 1
    grid[row+1][col] = '|'
    return 0


def part1(data):
    grid = parse(data)
    splits = 0
    for row in range(len(grid)-1):
        for col in range(len(grid[row])):
            if grid[row][col] in ('|','S'):
                splits += descend(grid, row, col)
    return splits


def quantum_descend(grid, row, col):
    if grid[row+1][col] == '^':
        grid[row+1][col-1] += grid[row][col]
        grid[row+1][col+1] += grid[row][col]
    else:
        grid[row+1][col] += grid[row][col]


def part2(data):
    grid = parse(data, part2=True)
    for row in range(len(grid)-1):
        for col in range(len(grid[row])):
            if grid[row][col] != '^' and grid[row][col]>0:
                quantum_descend(grid, row, col)
    return sum(grid[-1])
