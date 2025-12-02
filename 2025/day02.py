

def parse(raw_data):
    return [[int(n) for n in line.split('-')] for line in raw_data.strip().split(',')]


def invalid(num, part2=False):
    if part2:
        return invalid2(num)
    num = str(num)
    if len(num) % 2 != 0:
        return False
    mid = len(num)//2
    p1, p2 = num[:mid], num[mid:]
    return p1==p2


def invalid2(num):
    num = str(num)
    for d in range(2, len(num)+1):
        if len(num) % d == 0:
            l = len(num)//d
            for i in range(1,d):
                if num[:l] != num[l*(i):l*(i+1)]:
                    break
            else:
                return True
    return False


def part1(raw_data, part2=False):
    data = parse(raw_data)
    total = 0
    for start,stop in data:
        for num in range(start,stop+1):
            if invalid(num, part2):
                total += num
    return total


def part2(raw_data):
    return part1(raw_data, part2=True)
    