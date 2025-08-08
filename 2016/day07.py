

def parse(raw_input):
    lines = raw_input.strip().split('\n')
    ips = []
    for line in lines:
        regular = []
        hypernet = []
        open_idx = line.find('[')
        ctr = 0
        while open_idx > 0 and ctr < 3:
            regular.append(line[:open_idx])
            close_idx = line.find(']')
            hypernet.append(line[open_idx+1:close_idx])
            line = line[close_idx+1:]
            open_idx = line.find('[')
            ctr += 1
        if line:
            regular.append(line)
        ips.append((regular,hypernet))
    return ips


def abba(seq):
    for c in range(1,len(seq)-2):
        if seq[c-1] != seq[c] and seq[c] == seq[c+1] and seq[c-1] == seq[c+2]:
            return True


def find_abas(seq):
    abas = []
    for c in range(len(seq)-2):
        if seq[c] != seq[c+1] and seq[c] == seq[c+2]:
            abas.append(seq[c:c+3])
    return abas


def part2(raw_input):
    ips = parse(raw_input)
    ssl = 0
    for reg,hyp in ips:
        abas = []
        for seq in reg:
            abas.extend(find_abas(seq))
        babs = []
        for seq in hyp:
            babs.extend(find_abas(seq))
        for bab in babs:
            aba = bab[1]+bab[0]+bab[1]
            if aba in abas:
                ssl += 1
                break
    return ssl

    return tls
