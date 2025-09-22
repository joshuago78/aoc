

def polar_opps(c1, c2):
    return abs(ord(c1) - ord(c2)) == 32


def part1(text):
    poly = list(text.strip())
    modified = True
    while modified:
        modified = False
        i = 0
        while i < len(poly)-1:
            if polar_opps(poly[i], poly[i+1]):
                poly.pop(i)
                poly.pop(i)
                modified = True
            i += 1
    return len(poly)


def part2(text):
    chars = [c for c in set(text.strip()) if c.isupper()]
    best = len(text)
    for char in chars:
        text2 = ''.join([c for c in text.strip() if c.upper()!= char])
        length = part1(text2)
        if length<best:
            best = length
    return best

