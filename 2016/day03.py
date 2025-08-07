

def parse(raw_input):
    lines = raw_input.strip().split('\n')
    return [[int(n) for n in line.split()] for line in lines]


def part1(raw_input):
    triangles = 0
    for a,b,c in parse(raw_input):
        if a+b>c and b+c>a and a+c>b:
            triangles += 1
    return triangles

def part2(raw_input):
    lines = parse(raw_input)
    triangles = 0
    for r in range(0,len(lines)-2,3):
        for c in range(3):
            a = lines[r][c]
            b = lines[r+1][c]
            c = lines[r+2][c]
            if a+b>c and b+c>a and a+c>b:
                triangles += 1
    return triangles
