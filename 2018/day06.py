

def parse(text, midpoint=False):
    height, width = 0, 0
    points = []
    for num, line in enumerate(text.strip().split('\n')):
        x,y = [int(c) for c in line.split(',')]
        if x>=width:
            width = x+1
        if y>=height:
            height = y+1
        points.append({'id': num, 'x':x, 'y':y})
    if midpoint:
        return points, (width//2, height//2)
    grid = [[(None,None) for _ in range(width)] for _ in range(height)]
    return points, grid


def part1(text):
    points, grid = parse(text)
    for y,row in enumerate(grid):
        for x,cel in enumerate(row):
            pid,pdist = cel
            for point in points:
                dist = abs(point['x']-x) + abs(point['y']-y)
                if pid is None or dist<pdist:
                    pid,pdist = point['id'], dist
                elif dist==pdist and pid!=point['id']:
                    pid,dist = ('X',0)
            grid[y][x] = (pid,pdist)
    edge_points = set([p[0] for p in grid[0] + grid[-1]])
    for row in grid[1:-1]:
        edge_points.update([row[0][0],row[-1][0]])
    best = None
    for point in points:  
        if point['id'] not in edge_points:
            point['area'] = sum([[c[0] for c in r].count(point['id']) for r in grid])
            if best is None or point['area'] > best['area']:
                best = point
    return best['area']


def part2(text):
    points, midpoint = parse(text, midpoint=True)
    (x1,y1), (x2,y2) = midpoint, midpoint
    area = 1
    changes_made = True
    while changes_made:
        changes_made = False
        x1,y1 = x1-1, y1-1
        x2,y2 = x2+1, y2+1
        perim = [(x,y1) for x in range(x1,x2+1)] + [(x,y2) for x in range(x1,x2+1)]
        perim += [(x1,y) for y in range(y1+1,y2)] + [(x2,y) for y in range(y1+1,y2)]
        for x,y in perim:
            total_dist = 0
            for point in points:
                total_dist += abs(point['x']-x) + abs(point['y']-y)
            if total_dist < 10000:
                area += 1
                changes_made = True
    return area


