
TOTAL_IPS = 2**32
#TOTAL_IPS = 10


def parse(raw_input):
    return sorted([(int(a),int(b)) for a,b in [line.split('-') for line in raw_input.strip().split('\n')]])


def part1(raw_input):
    ranges = parse(raw_input)
    for ip in range(TOTAL_IPS):
        for start,end in ranges:
            if ip < start:
                return ip
            if ip <= end:
                break


def merge_ranges(ranges):
    merged = []
    merger = False
    idx = 0
    while idx < len(ranges):
        if idx < len(ranges)-1 and ranges[idx][1] >= ranges[idx+1][0]-1:
            idx2 = idx+1 if ranges[idx+1][1] > ranges[idx][1] else idx
            new_range = (ranges[idx][0], ranges[idx2][1])
            merged.append(new_range)
            merger = True
            idx += 2
        else:
            merged.append(ranges[idx])
            idx += 1
    if not merger:
        return merged
    return merge_ranges(merged)


def part2(raw_input):
    ranges = parse(raw_input)
    ranges = merge_ranges(ranges)
    blocked_count = sum([1+end-start for start,end in ranges])
    print(blocked_count)
    return TOTAL_IPS - blocked_count

'''
def part2(raw_input):
    ranges=[]
    maximum=2**32
    used = 0
    count = 0
    for rang in ranges:
        if rang[0] > used + 1:
            count += rang[0] - used - 1
        used = max(rang[1], used)
    count += maximum - used
    return count

def part2(raw_input):
    ranges = parse(raw_input)
    ranges = merge_ranges(ranges)
    print(ranges)
    allowed = 0
    index = 0
    for start,end in ranges:
        diff = start - index
        if diff > 0:
            allowed += diff
        index = end+1
    if index < TOTAL_IPS:
        allowed += TOTAL_IPS - index
    return allowed


def part2(raw_input):
    from pprint import pprint
    ranges = parse(raw_input)
    pprint(ranges[:10])
    pprint(ranges[-10:])
    ranges = merge_ranges(ranges)
    pprint(ranges[:10])
    pprint(ranges[-10:])
    total_blocked = 0
    for start,end in ranges:
        total_blocked += (end-start) + 1
    return TOTAL_IPS - total_blocked
'''
