


def part1(target=277678):
    target = int(target)
    size = 1
    side = 1
    while size < target:
        side += 2
        size = side**2
    d1 = side//2
    rem = (size % target) % side
    d2 = d1 - min(rem, side-rem)
    return d1 + d2


def sum_neighbors(pos, vals):
    total = 0
    ndirs = [(0,1),(-1,0),(0,-1),(1,0)]
    ndirs += [(-1,1),(-1,-1),(1,1),(1,-1)]
    for n in ndirs:
        nx,ny = (pos[0]+n[0], pos[1]+n[1])
        total += vals.get(nx, {}).get(ny, 0)
    return total


def part2(target=277678):
    target = int(target)
    idx = 1
    val = 1
    px,py = (0,0)
    vals = {0:{0:1}}
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    i = 1
    while True:
        for j in range(2):
            d = dirs.pop(0)
            dirs.append(d)
            for k in range(i):
                idx += 1
                px,py = d[0]+px, d[1]+py
                val = sum_neighbors((px,py), vals)
                if px in vals.keys():
                    vals[px][py] = val
                else:
                    vals[px] = {py:val}
                #print(f'num {idx} at ({px},{py}) has value: {val}')
                if val > target:
                    return val
        i += 1

