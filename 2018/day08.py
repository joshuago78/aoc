

def traverse(data):
    children = data.pop(0)
    entries = data.pop(0)
    metadata = 0
    for c in range(children):
        metadata += traverse(data)
    for m in range(entries):
        metadata += data.pop(0)
    return metadata


def part1(text):
    data = [int(n) for n in text.strip().split()]
    metadata = 0
    while data:
        metadata += traverse(data)
    return metadata


def traverse2(data):
    child_count = data.pop(0)
    entry_count = data.pop(0)
    child_values = []
    value = 0
    for _ in range(child_count):
        child_values.append(traverse2(data))
    for _ in range(entry_count):
        num = data.pop(0)
        if child_count==0:
            value += num
        elif num>0 and num<=child_count:
            value += child_values[num-1]
    return value


def part2(text):
    data = [int(n) for n in text.strip().split()]
    return traverse2(data)
