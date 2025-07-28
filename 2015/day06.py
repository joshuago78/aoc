


def parse(raw_input):
    instructions = []
    for line in raw_input.strip().split('\n'):
        tokens = line.split()
        cmd = tokens.pop(0)
        if cmd == 'turn':
            cmd = tokens.pop(0)
        r1,c1 = tokens[0].split(',')
        r2,c2 = tokens[2].split(',')
        instructions.append((cmd,(int(r1),int(c1)),(int(r2),int(c2))))
    return instructions


def part1(raw_input):
    grid = [[0 for c in range(1000)] for r in range(1000)]
    instructions = parse(raw_input)
    for cmd, [r1,c1], [r2,c2] in instructions:
        for row in range(r1,r2+1):
            for col in range(c1,c2+1):
                if cmd == 'on':
                    grid[row][col] = 1
                elif cmd == 'off':
                    grid[row][col] = 0
                else:
                    grid[row][col] = grid[row][col] ^ 1
    return sum([sum(row) for row in grid])


def part2(raw_input):
    grid = [[0 for c in range(1000)] for r in range(1000)]
    instructions = parse(raw_input)
    for cmd, [r1,c1], [r2,c2] in instructions:
        for row in range(r1,r2+1):
            for col in range(c1,c2+1):
                if cmd == 'on':
                    grid[row][col] += 1
                elif cmd == 'off':
                    if grid[row][col] > 0:
                        grid[row][col] -= 1
                else:
                    grid[row][col] += 2
    return sum([sum(row) for row in grid])
