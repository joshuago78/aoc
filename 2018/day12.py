import re


def parse(text):
    lines = text.strip().split('\n')
    pots = lines[0].split(': ')[1]
    P = r'(?P<in>[\.#]{5}) => (?P<out>[\.#])'
    patterns = []
    for line in lines[2:]:
        m = re.match(P, line)
        patterns.append(m.groupdict())
    return pots, patterns


def part1(text, gens=20):
    pots, patterns = parse(text)
    idx0 = 0
    prev = 0
    for gen in range(1,gens+1):
        if '#' in pots[:3]:
            pots = '...' + pots
            idx0 += 3
        if '#' in pots[-5:]:
            pots += '.....'
        new_pots = ''
        for idx in range(len(pots)-5):
            for pattern in patterns:
                if pots[idx:idx+5] == pattern['in']:
                    new_pots += pattern['out']
                    break
            else:
                new_pots += '.'
        idx0 -= 2
        pots = new_pots
        total = 0
        for idx,pot in enumerate(pots):
            if pot == '#':
                total += (idx-idx0)
        if gen%100==0:
            print(gen,total,len(pots), total-prev)
            prev = total
    return total


def part2(text):
    part1(text, gens=1000)
    return ((50000000000-100)//100) * 5700 + 8154
    

