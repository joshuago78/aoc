

def randomly_pad(a):
    b = list(a[-1::-1])
    for i in range(len(b)):
        b[i] = '0' if b[i]=='1' else '1'
    b = ''.join(b)
    return a+'0'+b


def get_checksum(a):
    checksum = ''
    for i in range(1,len(a),2):
        checksum += '1' if a[i-1] == a[i] else '0'
    if len(checksum) % 2 != 0:
        return checksum
    return get_checksum(checksum)


def part1(raw_input, disc_size=272):
    a = randomly_pad(raw_input)
    while len(a) < disc_size:
        a = randomly_pad(a)
    a = a[:disc_size]
    return get_checksum(a)


def part2(raw_input):
    return part1(raw_input, disc_size=35651584)

