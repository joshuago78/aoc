

def parse(raw_input):
    return raw_input.strip().split('\n')


def part1(raw_input):
    lines = parse(raw_input)
    grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    row,col = 1,1
    buttons = ''
    for line in lines:
        for c in line:
            match c:
                case 'U':
                    if row > 0:
                        row -= 1
                case 'D':
                    if row < len(grid) - 1:
                        row += 1
                case 'L':
                    if col > 0:
                        col -= 1
                case 'R':
                    if col < len(grid) - 1:
                        col += 1
        buttons += str(grid[row][col])
    return buttons


def part2(raw_input):
    lines = parse(raw_input)
    grid = [
        [None,None,'1',None,None],
        [None,'2','3','4',None],
        ['5','6','7','8','9'],
        [None,'A','B','C',None],
        [None,None,'D',None,None]]
    row,col = 2,0
    buttons = ''
    for line in lines:
        for c in line:
            match c:
                case 'U':
                    if row > 0 and grid[row-1][col] is not None:
                        row -= 1
                case 'D':
                    if row < len(grid) - 1 and grid[row+1][col] is not None:
                        row += 1
                case 'L':
                    if col > 0  and grid[row][col-1] is not None:
                        col -= 1
                case 'R':
                    if col < len(grid) - 1 and grid[row][col+1] is not None:
                        col += 1
        buttons += str(grid[row][col])
    return buttons

