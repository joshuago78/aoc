

def parse(raw_input):
    locs = {}
    grid = raw_input.strip().split('\n')
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isdigit():
                locs[char] = (x,y)
    return grid, locs


def find_next_steps(grid, loc):
    steps = []
    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
        x,y = loc[0]+d[0], loc[1]+d[1]
        if x>=0 and x<len(grid[0]) and y>=0 and y<len(grid):
            if grid[y][x] != '#':
                steps.append((x,y))
    return steps


def find_best_path(grid, xy1, xy2):
    visited = []
    paths = [[xy1,],]
    while paths:
        path = paths.pop(0)
        next_steps = find_next_steps(grid, path[-1])
        for next_step in next_steps:
            if next_step not in visited:
                visited.append(next_step)
                new_path = path.copy()
                new_path.append(next_step)
                if next_step == xy2:
                    return new_path
                paths.append(new_path)


def find_all_routes(grid, locs):
    all_routes = {}
    for loc1,xy1 in locs.items():
        routes = {}
        for loc2,xy2 in locs.items():
            if loc1!=loc2:
                route = find_best_path(grid,xy1,xy2)
                routes[loc2] = route
        all_routes[loc1] = routes
    return all_routes


def find_complete_route(all_routes, best_only=True):
    best = None
    completed = []
    routes = [(['0',],0),]
    while routes:
        route,steps = routes.pop(0)
        last = route[-1]
        for loc,path in all_routes[last].items():
            if loc not in route:
                new_route = route.copy()
                new_route.append(loc)
                new_steps = steps + len(path) - 1
                if len(new_route) == len(all_routes.keys()):
                    if best_only:
                        if best is None or new_steps < best[1]:
                            best = (new_route,new_steps)
                    else:
                        completed.append((new_route,new_steps))
                else:
                    routes.append((new_route,new_steps))
    if best_only:
        return best
    return completed


def part1(raw_input):
    grid, locs = parse(raw_input)
    routes = find_all_routes(grid, locs)
    best = find_complete_route(routes)
    return best[1]


def part2(raw_input):
    grid, locs = parse(raw_input)
    routes = find_all_routes(grid, locs)
    completed = find_complete_route(routes, best_only=False)
    best = None
    for route,steps in completed:
        if best is not None and steps>best[1]:
            continue
        path = find_best_path(grid, locs[route[-1]], locs['0'])
        steps += len(path) - 1
        route.append('0')
        if best is None or steps < best[1]:
            best = route,steps
    return best[1]
    