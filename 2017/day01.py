

def part1(raw_input):
    sequence = raw_input.strip() + raw_input[0]
    total = 0
    for i,char in enumerate(sequence[:-1]):
        if char == sequence[i+1]:
            total += int(char)
    return total


def part2(sequence):
    half = len(sequence) // 2
    total = 0
    for i,char in enumerate(sequence):
        j = (i+half) % (half*2)
        if char == sequence[j]:
            total += int(char)
    return total
