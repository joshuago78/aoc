

def part1(stream, count_garbage=False):
    score = 0
    garbage_score = 0
    group_lvl = 0
    garbage = False
    ignore = False
    for c in stream:
        if ignore is True:
            ignore = False
        elif c == '!':
            ignore = True
        elif garbage is True:
            if c == '>':
                garbage = False
            else:
                garbage_score += 1
        elif c == '<':
            garbage = True
        elif c == '{':
            group_lvl += 1
        elif c == '}':
            score += group_lvl
            group_lvl -= 1                
    return garbage_score if count_garbage else score


def part2(stream):
    return part1(stream, count_garbage=True)

