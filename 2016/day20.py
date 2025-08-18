
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
    return TOTAL_IPS - blocked_count

