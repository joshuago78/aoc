HEIGHT = 6
WIDTH = 50


def parse(raw_input):
    instructions = []
    for line in raw_input.strip().split('\n'):
        tokens = line.split()
        if tokens[0] == 'rect':
            width,height = tokens[1].split('x')
            instructions.append(('rect',int(width),int(height)))
        else:
            dim = tokens[1]
            rowcol = int(tokens[2].split('=')[1])
            offset = int(tokens[-1])
            instructions.append((f'shift{dim}',rowcol,offset))
    return instructions


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def rect(grid, width, height):
    for row in range(height):
        for col in range(width):
            grid[row][col] = '#'


def shiftrow(grid, row, offset):
    row = grid[row]
    for i in range(offset):
        row.insert(0,row.pop())


def shiftcolumn(grid, col, offset):
    for i in range(offset):
        last = grid[-1][col][:]
        for row in range(HEIGHT-1,0,-1):
            grid[row][col] = grid[row-1][col]
        grid[0][col] = last


COMMANDS = {
    'rect': rect,
    'shiftrow': shiftrow,
    'shiftcolumn': shiftcolumn
}


def part1(raw_input, print=False):
    instructions = parse(raw_input)
    grid = [['.' for i in range(50)] for j in range(6)]
    for cmd,param1,param2 in instructions:
        function = COMMANDS[cmd]
        function(grid, param1, param2)
    if print:
        print_grid(grid)
    return sum([row.count('#') for row in grid])


def part2(raw_input):
    part1(raw_input, print=True)
    
