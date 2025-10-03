
def print_scores(scores, e1, e2):
    line = ''
    chars = {e1:'()', e2:'[]'}
    for i,score in enumerate(scores):
        c = chars.get(i, '  ')
        line += f'{c[0]}{score}{c[1]}'
    print(line)


def combine_recipes(scores, e1, e2):
    combo = scores[e1] + scores[e2]
    digits = divmod(combo,10) if combo >= 10 else [combo,]
    scores.extend(digits)
    e1 = (e1 + scores[e1] + 1) % len(scores)
    e2 = (e2 + scores[e2] + 1) % len(scores)
    return e1,e2


def part1(text):
    minrecipes = int(text)
    e1,e2 = 0,1
    scores = [3,7]
    while len(scores) < (minrecipes+10):
        e1,e2 = combine_recipes(scores,e1,e2)
        print_scores(scores,e1,e2)
    return ''.join([str(n) for n in scores[minrecipes:]])


def part2(text):
    tail = [int(c) for c in text]
    e1,e2 = 0,1
    scores = [3,7]
    while scores[-len(tail):] != tail and scores[-len(tail)-1:-1] != tail:
        e1,e2 = combine_recipes(scores,e1,e2)
    total = len(scores) - len(tail)
    total -= 1 if scores[-len(tail)-1:-1] == tail else 0
    return total

