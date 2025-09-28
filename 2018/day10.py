import re


class Point(object):

    def __init__(self, args):
        self.x = int(args['px'])
        self.y = int(args['py'])
        self.vx = int(args['vx'])
        self.vy = int(args['vy'])

    def __str__(self):
        return '#'

    def in_frame(self):
        return self.x>=0 and self.y>=0

    def move(self, factor=1):
        self.x += self.vx * factor
        self.y += self.vy * factor


def parse(text):
    pattern = r'position=<(?P<px>[ \-\d]+),(?P<py>[ \-\d]+)> velocity=<(?P<vx>[ \-\d]+),(?P<vy>[ \-\d]+)>'
    points = []
    for line in text.strip().split('\n'):
        m = re.match(pattern, line)
        points.append(Point(m.groupdict()))
    return points


def build_grid(points, maxx, maxy):
    grid = [['.' for _ in range(maxx+1)] for _ in range(maxy+1)]
    for p in points:
        grid[p.y][p.x] = p
    return grid


def print_grid(grid):
    for row in grid:
        print(''.join([str(p) for p in row]))
    print()


def part1(text):
    points = parse(text)
    printable = False
    seconds = 10000
    for p in points:
        p.move(seconds)
    while True:
        seconds += 1
        printable = True
        maxx = 0
        maxy = 0
        for p in points:
            p.move()
            if printable:
                if p.in_frame():
                    if p.x > maxx:
                        maxx = p.x
                    if p.y > maxy:
                        maxy = p.y
                else:
                    printable = False
        if printable:
            grid = build_grid(points, maxx, maxy)
            print_grid(grid)
            print(f'time={seconds} seconds')
            input()
