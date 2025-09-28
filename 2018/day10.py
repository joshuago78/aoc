import re


class Point(object):

    def __init__(self, args):
        self.x = int(args['px'])
        self.y = int(args['py'])
        self.vx = int(args['vx'])
        self.vy = int(args['vy'])

    def move(self, factor=1):
        self.x += self.vx * factor
        self.y += self.vy * factor

    def in_frame(self):
        return self.x>=0 and self.y>=0

    def check_edges(self, maxx, maxy, minx, miny):
        if self.x > maxx:
            maxx = self.x
        elif minx is None or self.x < minx:
            minx = self.x
        if self.y > maxy:
            maxy = self.y
        elif miny is None or self.y < miny:
            miny = self.y
        return maxx,maxy,minx,miny


def parse(text):
    pattern = r'position=<(?P<px>[ \-\d]+),(?P<py>[ \-\d]+)> velocity=<(?P<vx>[ \-\d]+),(?P<vy>[ \-\d]+)>'
    points = []
    for line in text.strip().split('\n'):
        m = re.match(pattern, line)
        points.append(Point(m.groupdict()))
    return points


def build_grid(points, minx, maxx, miny, maxy):
    grid = [['.' for _ in range(maxx+1)] for _ in range(maxy+1)]
    for p in points:
        grid[p.y][p.x] = '#'
    return [row[minx:] for row in grid[miny:]]


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()


def part1(text):
    points = parse(text)
    seconds = 10000
    for p in points:
        p.move(factor=seconds)
    area = None
    printable = False
    while True:
        seconds += 1
        printable = True
        maxx,maxy,minx,miny = 0,0,None,None
        for p in points:
            p.move()
            if printable:
                if p.in_frame():
                    maxx,maxy,minx,miny = p.check_edges(maxx,maxy,minx,miny)
                else:
                    printable = False
        if printable:
            new_area = (maxx-minx)*(maxy-miny)
            if area is None:
                area = new_area
            elif new_area < area:
                area = new_area
                grid = build_grid(points, minx, maxx, miny, maxy)
            else:
                print_grid(grid)
                return seconds
