

def parse(raw_input):
    return [int(x) for x in raw_input.strip().split()]


def distribute(seq):
    val = max(seq)
    idx = seq.index(val)
    seq[idx] = 0
    while val > 0:
        idx = (idx+1) % len(seq)
        seq[idx] += 1
        val -= 1
    return seq


def part1(raw_input, cycle=False):
    sequences = []
    sequences.append(parse(raw_input))
    count = 0
    while True:
        count += 1
        newseq = distribute(sequences[-1].copy())
        if newseq in sequences:
            if cycle:
                idx = sequences.index(newseq)
                return len(sequences) - idx
            return count
        sequences.append(newseq)


def part2(raw_input):
    return part1(raw_input, cycle=True)
    