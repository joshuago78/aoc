

def part1(raw_input, part2=False):

    #3 axes: X:nw/se , Y:n/s , Z:ne/sw
    x,y,z = 0,0,0
    distance = 0
    farthest = 0

    for step in raw_input.strip().split(','):
        match step:
            case 'nw':
                if x==0 and (y<0 or z>0):
                    y += 1
                    z -= 1
                else:
                    x += 1
            case 'se':
                if x==0 and (y>0 or z<0):
                    y -= 1
                    z += 1
                else:
                    x -= 1
            case 'n':
                if y==0 and (z<0 or x<0):
                    x += 1
                    z += 1
                else:
                    y += 1
            case 's':
                if y==0 and (x>0 or z>0):
                    x -= 1
                    z -= 1
                else:
                    y -= 1
            case 'ne':
                if z==0 and (x>0 or y<0):
                    x -= 1
                    y += 1
                else:
                    z += 1
            case 'sw':
                if z==0 and (x<0 or y>0):
                    x += 1
                    y -= 1
                else:
                    z -= 1
        distance = abs(x) + abs(y) + abs(z)
        if distance > farthest:
            farthest = distance
            
    return farthest if part2 else distance


def part2(raw_input):
    return part1(raw_input, part2=True)

