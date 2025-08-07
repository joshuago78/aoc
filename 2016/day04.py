


def parse(raw_input):
    rooms = []
    lines = raw_input.strip().split('\n')
    for line in lines:
        parts = line.split('-')
        secid,checksum = parts[-1].strip(']').split('[')
        rooms.append({
            'name': ' '.join(parts[:-1]),
            'secid': int(secid),
            'checksum': checksum})
    return rooms


def get_checksum(name):
    chars = {}
    for c in name:
        if c.isalpha():
            if c in chars.keys():
                chars[c] += 1
            else:
                chars[c] = 1
    chars = sorted(chars.items(), key=lambda x: (-x[1],x[0]))
    return ''.join([c[0] for c in chars][:5])


def part1(raw_input):
    rooms = parse(raw_input)
    total = 0
    for room in rooms:
        if room['checksum'] == get_checksum(room['name']):
            total += room['secid']
    return total


def decrypt(name, num):
    d = ''
    for c in name:
        if c.isalpha():
            c = chr((((ord(c)-97)+num)%26)+97)
        d += c
    return d


def part2(raw_input):
    rooms = parse(raw_input)
    real = [r for r in rooms if r['checksum'] == get_checksum(r['name'])]
    for room in real:
        d = decrypt(room['name'], room['secid'])
        if d == 'northpole object storage':
            return room['secid']
    

