

def parse(raw_data):
    return [[int(i) for i in line] for line in raw_data.strip().split('\n')]    


def part1(raw_data, part2=False):
    banks = parse(raw_data)
    total = 0
    for bank in banks:
        d1 = max(bank[:-1])
        idx = bank.index(d1)
        d2 = max(bank[idx+1:])
        total += int(f'{d1}{d2}')
    return total


def part2(raw_data):
    banks = parse(raw_data)
    total = 0
    for bank in banks:
        while len(bank) > 12:
            for i in range(len(bank)):
                if i==len(bank)-1 or bank[i] < bank[i+1]:
                    bank.pop(i)
                    break
        total += int(''.join([str(i) for i in bank]))
    return total
 