

def part1(text):
    has2total = 0
    has3total = 0
    for boxid in text.strip().split('\n'):
        has2, has3 = False, False
        for char in set(boxid):
            count = boxid.count(char)
            if count==2:
                has2 = True
            elif count==3:
                has3 = True
        if has2:
            has2total += 1
        if has3:
            has3total += 1
    return has2total * has3total


def part2(text):
    boxids = text.strip().split('\n')
    for i, bid in enumerate(boxids):
        for bid2 in boxids[i+1:]:
            mismatches = 0
            common = []
            for j in range(len(bid)):
                if bid[j] != bid2[j]:
                    mismatches += 1
                    if mismatches>1:
                        break
                else:
                    common.append(bid[j])
            if mismatches==1:
                return ''.join(common)

