SIZE = 100
STEPS = 100


def parse(raw_input):
    grid = [[None]*SIZE for i in range(SIZE)]
    for r, row in enumerate(raw_input.strip().split('\n')):
        for c, val in enumerate(list(row)):
            grid[r][c] = 1 if val == '#' else 0
    return grid


def count_on_neighbors(grid, row, col):
    count = 0
    for r in range(-1,2):
        for c in range(-1,2):
            if r == 0 and c == 0:
                continue
            nrow = row+r
            ncol = col+c
            if nrow >= 0 and nrow < len(grid):
                if ncol >= 0 and ncol < len(grid[0]):
                    count += grid[nrow][ncol]
    return count


def update(grid, broken_corners=False):
    new_grid = [[None]*SIZE for i in range(SIZE)]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if broken_corners:
                if (r,c) in [(0,0),(0,SIZE-1),(SIZE-1,0),(SIZE-1,SIZE-1)]:
                    new_grid[r][c] = 1
                    continue
            on_neighbors = count_on_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if on_neighbors in (2,3) else 0
            else:
                new_grid[r][c] = 1 if on_neighbors == 3 else 0
    return new_grid

'''
def print_grid(grid):
    for row in grid:
        print(''.join(['#' if n==1 else '.' for n in row]))
    print()
'''

def part1(raw_input):
    grid = parse(raw_input)
    for i in range(STEPS):
        grid = update(grid)
    return sum([sum(row) for row in grid])


def part2(raw_input):
    grid = parse(raw_input)
    for i in range(STEPS):
        grid = update(grid, broken_corners=True)
    return sum([sum(row) for row in grid])
