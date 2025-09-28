

def power(x, y, gsn):
    rackid = x + 10
    power = ((rackid * y) + gsn) * rackid
    return int(str(power)[-3]) - 5


def part1(text, minsize=3, maxsize=3):
    gsn = int(text)
    side = 300
    grid = [[power(x,y,gsn) for x in range(1,side+1)] for y in range(1,side+1)]
    best = None
    same = 0
    for sz in range(minsize,maxsize+1):
        change = False
        for y in range(side - sz):
            for x in range(side - sz):
                block = sum([sum(grid[row][x:x+sz]) for row in range(y,y+sz)])
                if best is None or block>best['power']:
                    best = {'x':x+1, 'y':y+1, 'power':block, 'size':sz}
                    change = True
        same = 0 if change else same+1
        if same>5:
            break
    return best['x'],best['y'],best['size']


def part2(text):
    return part1(text, 1, 300)
