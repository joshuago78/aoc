

def next_diag(row,col):
    if row == 1:
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1
    return row, col


def part1(raw_input):
    target = (2981, 3075)
    row,col = 1,1
    value = 20151125
    while (row,col) != target:
        row,col = next_diag(row,col)
        value *= 252533
        value %= 33554393
    return value
