

def parse(raw_data):
    return [(line[0],int(line[1:])) for line in raw_data.strip().split()]


def part1(raw_data, part2=False):
    data = parse(raw_data)
    dial = 50
    crossed_zero = 0
    landed_zero = 0
    for dir,dist in data:
        if dist>=100:
            quotient,remainder = divmod(dist,100)
            crossed_zero += quotient
            dist = remainder
        if dir=='L':
            dist *= -1
        num = dial+dist
        if num>=100 or (num<=0 and dial!=0):
            crossed_zero +=1
        dial = num % 100
        if dial == 0:
            landed_zero += 1
    return crossed_zero if part2 else landed_zero


def part2(raw_data):
    return part1(raw_data, part2=True)
    