

def parse(data):
    ranges, ingredients = data.strip().split('\n\n')
    ranges = sorted([[int(n) for n in line.split('-')] for line in ranges.split('\n')])
    ingredients = [int(i) for i in ingredients.split('\n')]
    return ranges, ingredients


def part1(data):
    ranges, ingredients = parse(data)
    total = 0
    for i in ingredients:
        for start,stop in ranges:
            if i>= start and i<= stop:
                total += 1
                break
    return total


def part2(data):
    ranges,_ = parse(data)
    new_ranges = []
    start1,stop1 = ranges[0]
    for start2,stop2 in ranges[1:]:
        if stop1 >= start2:
            if stop1 < stop2:
                stop1 = stop2
        else:
            new_ranges.append([start1,stop1])
            start1,stop1 = start2,stop2
    new_ranges.append([start1,stop1])
    total = 0
    for start,stop in new_ranges:
        total += (stop - start) + 1
    return total

    