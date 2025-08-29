from itertools import combinations
from math import sqrt


DIRS = {
    'up': (0,-1),
    'down': (0,1),
    'left': (-1,0),
    'right': (1,0)
}

class Grid(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None]*width for i in range(height)]
        self.blank = None
        self.swap_count = 0

    def __str__(self):
        output = ''
        for row in self.grid:
            out += ''.join([node.symbol() for node in row]) + '\n'
        return output

    def print_path(self, path):
        for row in self.grid:
            line = ''
            for node in row:
                line += ' * ' if node in path[1:-1]else node.symbol()
            print(line)

    def add_node(self, node):
        self.grid[node.y][node.x] = node
        if node.used == 0:
            self.blank = node

    def mark_access_node(self, x, y):
        self.grid[y][x].accessible = True
        self.accessible = self.grid[y][x]

    def mark_desired_data_node(self, x, y):
        self.grid[y][x].desired = True
        self.desired = self.grid[y][x]

    def swap(self, nodeA, nodeB):
        xdiff = abs(nodeA.x - nodeB.x)
        ydiff = abs(nodeA.y - nodeB.y)
        if xdiff>1 or ydiff>1:
            raise Exception('Swapped nodes must be adjacent')
        if nodeA.used == 0 and nodeA.size>nodeB.used:
            nodeA.used = nodeB.used
            nodeA.available = nodeA.size - nodeA.used
            nodeA.use = nodeA.used // nodeA.size
            nodeB.use = 0
            nodeB.used = 0
            nodeB.available = nodeB.size
            self.swap_count += 1
            self.blank = nodeB
            if nodeB.desired == True:
                nodeB.desired = False
                nodeA.desired = True
                self.desired = nodeA
        elif nodeB.used == 0 and nodeB.size>nodeA.used:
            return self.swap(nodeB,nodeA)
        else:
            raise Exception('Incompatible sizes')

    def get_neighbors(self, node, dirs=None):
        x,y = node.x,node.y
        neighbors = []
        if dirs is None:
            dirs = DIRS.values()
        for d in dirs:
            nx,ny = x+d[0], y+d[1]
            if ny>=0 and ny<len(self.grid) and nx>=0 and nx<len(self.grid[0]):
                neighbors.append(self.grid[ny][nx])
        return neighbors

    def get_dirs_biased(self, start, finish):
        # return only 3 of the 4 directions (no going back)
        diffx = finish.x - start.x
        diffy = finish.y - start.y
        if abs(diffx) > abs(diffy):
            if diffx < 0:
                dirs = [DIRS['left'],DIRS['up'],DIRS['down']]
            else:
                dirs = [DIRS['right'],DIRS['up'],DIRS['down']]
        else:
            if diffy < 0:
                dirs = [DIRS['up'],DIRS['right'],DIRS['left']]
            else:
                dirs = [DIRS['down'],DIRS['left'],DIRS['right']]
        return dirs


    def find_greedy_path(self, start, finish, blank=False):
        visited = []
        paths = [[start,],]
        dirs = self.get_dirs_biased(start, finish)
        while paths:
            path = paths.pop(0)
            last = path[-1]
            futures = self.get_neighbors(last, dirs)
            for node in futures:
                if node not in visited:
                    if blank and (node.used>last.size or node.desired==True):
                        continue
                    new_path = path.copy()
                    new_path.append(node)
                    if node == finish:
                        return new_path
                    paths.append(new_path)
                    visited.append(node)


    def find_path_of_desired(self):
        return self.find_greedy_path(self.desired,self.accessible)        

    def find_path_of_blank(self, next_step):
        return self.find_greedy_path(self.blank,next_step,blank=True)


class Node(object):

    def __init__(self, dfline):
        name,size,used,avail,use = dfline.split()
        self.name = name.split('/')[-1]
        self.x, self.y = [int(i[1:]) for i in name.split('-')[1:]]
        self.size = int(size[:-1])
        self.used = int(used[:-1])
        self.avail = int(avail[:-1])
        self.use = int(use[:-1])
        self.desired = False
        self.accessible = False

    def __repr__(self):
        return f'<Node {self.x},{self.y}>'

    def __str__(self):
        return f'<Node {self.x},{self.y} size:{self.size} used:{self.used}>'

    def symbol(self):
        symbol = None
        if self.desired == True:
            symbol = 'G'
        elif self.used <= 10:
            symbol = '_'
        elif self.used < 100:
            symbol = '.'
        else:
            symbol = '#'
        if self.accessible == True:
            return f'({symbol})'
        return f' {symbol} '

    def distance_from(self, node):
        return sqrt((node.x-self.x)**2 + (node.y-self.y)**2)


def parse(raw_input):
    lines = raw_input.strip().split('\n')[2:]
    width,height = [int(n[1:])+1 for n in lines[-1].split()[0].split('-')[1:]]
    grid = Grid(width,height)
    for line in lines:
        grid.add_node(Node(line))
    grid.mark_access_node(0,0)
    grid.mark_desired_data_node(width-1,0)
    return grid


def part1(raw_input):
    grid = parse(raw_input)
    viable_pairs = []
    coords = [(x,y) for x in range(grid.width) for y in range(grid.height)]
    combos = combinations(coords,2)
    for (ax,ay),(bx,by) in combos:
        nodeA, nodeB = grid.grid[ay][ax], grid.grid[by][bx]
        if nodeA.used > 0 and nodeA.used <= nodeB.avail:
            viable_pairs.append((nodeA,nodeB))
        if nodeB.used > 0 and nodeB.used <= nodeA.avail:
            viable_pairs.append((nodeB,nodeA))
    return len(viable_pairs)


def part2(raw_input):
    grid = parse(raw_input)
    dpath = grid.find_path_of_desired()
    for step in dpath[1:]:
        bpath = grid.find_path_of_blank(step)
        for node in bpath[1:]:
            grid.swap(grid.blank,node)
        grid.swap(grid.blank,grid.desired)
    return grid.swap_count


