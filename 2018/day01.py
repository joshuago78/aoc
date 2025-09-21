

def part1(text):
    return sum([int(n) for n in text.strip().split('\n')])


def part2(text):
    history = set([0,])
    total = 0
    while True:
        for num in text.strip().split('\n'):
            total += int(num)
            if total in history:
                return total
            history.add(total)
