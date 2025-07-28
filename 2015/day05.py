
BAD_STRINGS = ['ab', 'cd', 'pq', 'xy']
VOWELS = 'aeiou'


def parse(raw_input):
    return raw_input.strip().split()


def is_nice(line):
    vowel_count = 0
    has_repeat = False
    for i in range(len(line)):
        if line[i] in VOWELS:
            vowel_count += 1
        if i>0:
            if line[i]==line[i-1]:
                has_repeat = True
            if str(line[i-1:i+1]) in BAD_STRINGS:
                return False
    return has_repeat and vowel_count >= 3


def part1(raw_input):
    lines = parse(raw_input)
    nice_count = 0
    for line in lines:
        if is_nice(line):
            nice_count += 1
    return nice_count


def is_nice2(line):
    has_pair_repeat = False
    has_gapped_repeat = False
    pairs = {}
    for i in range(len(line)):
        if i>1 and line[i]==line[i-2]:
            has_gapped_repeat = True
        if i>0:
            new_pair = str(line[i-1:i+1])
            if new_pair in pairs.keys():
                for (j,k) in pairs[new_pair]:
                    if k != i-1:
                        has_pair_repeat = True
                        break
                pairs[new_pair].append((i-1,i))
            else:
                pairs[new_pair] = [(i-1,i),]
    return has_pair_repeat and has_gapped_repeat


def part2(raw_input):
    lines = parse(raw_input)
    nice_count = 0
    for line in lines:
        if is_nice2(line):
            nice_count += 1
    return nice_count
