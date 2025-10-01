

class Cart(object):

    shifts = {'>':(1,0), '<':(-1,0), '^':(0,-1), 'v':(0,1)}

    corners = {
        '/': {'^':'>', '<':'v', '>':'^', 'v':'<'},
        '\\': {'^':'<', '>':'v', '<':'^','v':'>'}}

    turns = {
        'l': {'^':'<', '<':'v', 'v':'>', '>':'^'},
        'r': {'^':'>', '>':'v', 'v':'<', '<':'^'}}

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.dir = char
        self.crashed = False
        self.options = ['l','s','r']

    def __str__(self):
        return self.dir

    def turn(self):
        o = self.options.pop(0)
        self.options.append(o)
        if o != 's':
            self.dir = Cart.turns[o][self.dir]
                
    def move(self, grid):
        grid.rows[self.y][self.x].cart = None
        shiftx, shifty = Cart.shifts[self.dir]
        self.x += shiftx
        self.y += shifty
        point = grid.rows[self.y][self.x]
        if point.cart is None:
            point.cart = self
            if point.char in Cart.corners.keys():
                self.dir = Cart.corners[point.char][self.dir]
            elif point.char == '+':
                self.turn()
        else:
            point.cart.crashed = True
            self.crashed = True
            point.cart = None
            return (self.x, self.y)


class Point(object):

    def __init__(self, char, cart=None):
        self.char = char
        self.cart = cart

    def __str__(self):
        return self.char if self.cart is None else str(self.cart)


class Grid(object):

    def __init__(self, rows, remove=False):
        self.rows = rows
        self.remove = remove

    def tick(self):
        carts = []
        for row in self.rows:
            carts.extend([p.cart for p in row if p.cart])
        for cart in carts:
            if not cart.crashed:
                crash_site = cart.move(self)
                if crash_site and not self.remove:
                    return crash_site
        if self.remove:
            carts = [c for c in carts if c.crashed==False]
            if len(carts) < 2:
                cart = carts[0]
                return cart.x, cart.y

    def print(self, crash_site=None):
        if self.remove is False and crash_site:
            x,y = crash_site
            for r,row in enumerate(self.rows):
                line = ''
                for c,pt in enumerate(row):
                    line += str(pt) if (x,y) != (c,r) else 'X'
                print(line)
        else:
            for row in self.rows:
                print(''.join([str(p) for p in row]))


def parse(text):
    rows = []
    for y, line in enumerate(text.strip('\n').split('\n')):
        row = []
        for x, char in enumerate(line):
            cart = None
            if char not in '\\/+-| ':
                cart = Cart(x,y,char)
                char = '-' if char in '<>' else '|'
            row.append(Point(char,cart))
        rows.append(row)
    grid = Grid(rows)
    return grid


def part1(text, remove=False):
    grid = parse(text)
    grid.remove = remove
    #grid.print()
    crash_site = None
    while crash_site is None:
        crash_site = grid.tick()
        #grid.print(crash_site)
    return crash_site


def part2(text):
    return part1(text, remove=True)
