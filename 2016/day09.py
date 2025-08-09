import re


def parse(raw_input):
    return raw_input.strip().split('\n')


def decompress(cypher):
    pattern = r'\((\d+)x(\d+)\)'
    plain = ''
    match = re.search(pattern, cypher)
    while match:
        start,stop = match.span()
        cap = int(match.group(1))
        rpt = int(match.group(2))
        chars = cypher[stop:stop+cap]
        plain += cypher[:start]
        plain += chars*rpt
        cypher = cypher[stop+cap:]
        match = re.search(pattern, cypher)
    plain += cypher
    return plain


def decomplen(cypher):
    pattern = r'\((\d+)x(\d+)\)'
    match = re.search(pattern, cypher)
    if match:
        start,stop = match.span()
        cap = int(match.group(1))
        rpt = int(match.group(2))
        return start + rpt * decomplen(cypher[stop:stop+cap]) + decomplen(cypher[stop+cap:])
    return len(cypher)


def part1(raw_input):
    lines = parse(raw_input)
    total = 0
    for line in lines:
        total += len(decompress(line))
    return total


def part2(raw_input):
    lines = parse(raw_input)
    total = 0
    for line in lines:
        total += decomplen(line)
    return total
