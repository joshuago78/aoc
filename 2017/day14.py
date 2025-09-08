from functools import reduce


SIZE = 256


def sparse_hash(nums, lengths, start=0, skip_size=0):
    for length in lengths:
        stop = (start+length) % SIZE
        if length > 0:
            if stop > start:
                nums = nums[:start] + list(reversed(nums[start:stop])) + nums[stop:]
            else:
                subset = list(reversed(nums[start:] + nums[:stop]))
                subsplit = SIZE - start
                nums = subset[subsplit:] + nums[stop:start] + subset[:subsplit]
        start = (stop + skip_size) % SIZE
        skip_size += 1
    return nums, start, skip_size


def knot_hash(input):
    lengths = [ord(c) for c in input.strip()] + [17, 31, 73, 47, 23]
    nums = list(range(SIZE))
    start, skip_size = 0, 0
    for _ in range(64):
        nums, start, skip_size = sparse_hash(nums, lengths, start, skip_size)
    dense_hash = ''
    for i in range(16):
        chunk = nums[i*16:i*16+16]
        dense_hash += f'{reduce(lambda x,y: x^y, chunk):0{2}x}'
    return dense_hash


def part1(raw_input):
    total = 0
    for i in range(128):
        input = f'{raw_input.strip()}-{i}'
        hash = knot_hash(input)
        bits = str(bin(int(hash,16))[2:])
        total += bits.count('1')
    return total


def mark_neighbors(grid, r, c, num):
    for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
        r2, c2 = x+r, y+c
        if r2>=0 and r2<len(grid) and c2>=0 and c2<len(grid[r]):
            if grid[r2][c2] == '#':
                grid[r2][c2] = str(num)
                mark_neighbors(grid, r2, c2, num)


def part2(raw_input):
    grid = []
    for i in range(128):
        input = f'{raw_input.strip()}-{i}'
        hash = knot_hash(input)
        row = f'{int(hash,16):0128b}'
        row = list(row.replace('1','#').replace('0','.'))
        grid.append(row)
    num = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '#':
                continue
            num += 1
            grid[r][c] = str(num)
            mark_neighbors(grid,r,c,num)
    return num


