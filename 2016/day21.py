import re


def swappos(password, args):
    p1,p2 = int(args['pos1']),int(args['pos2'])
    temp = password[p1]
    password[p1] = password[p2]
    password[p2] = temp
    return password


def swapltr(password, args):
    for idx,char in enumerate(password):
        if char == args['ltr1']:
            password[idx] = args['ltr2']
        elif char == args['ltr2']:
            password[idx] = args['ltr1']
    return password


def rotate(password, args):
    steps = int(args['steps']) % len(password)
    if args['dir'] == 'right':
        steps *= -1
    if args['reverse']:
        steps *= -1
    return password[steps:] + password[:steps]


def rotateltr(password, args):
    if args['reverse']:
        mapping = [None]*len(password)
        for idx in range(len(password)):
            steps = idx+2 if idx >= 4 else idx+1
            new_idx = (steps+idx) % len(password)
            mapping[new_idx] = steps % len(password)
        steps = mapping[password.index(args['ltr'])]
    else:
        steps = password.index(args['ltr'])
        steps += 2 if steps >= 4 else 1
        steps %= len(password)
        steps *= -1
    return password[steps:] + password[:steps]


def reverse(password, args):
    p1,p2 = int(args['pos1']),int(args['pos2'])
    return password[:p1] + password[p1:p2+1][-1::-1] + password[p2+1:]


def move(password, args):
    p1,p2 = int(args['pos1']),int(args['pos2'])
    if args['reverse']:
        temp = p1
        p1 = p2
        p2 = temp
    ltr = password.pop(p1)
    password.insert(p2,ltr)
    return password


OPERATIONS = {
    (r'swap position (?P<pos1>\d+) with position (?P<pos2>\d+)', swappos),
    (r'swap letter (?P<ltr1>\w) with letter (?P<ltr2>\w)', swapltr),
    (r'rotate (?P<dir>left|right) (?P<steps>\d+) step', rotate),
    (r'rotate based on position of letter (?P<ltr>\w)', rotateltr),
    (r'reverse positions (?P<pos1>\d+) through (?P<pos2>\d+)', reverse),
    (r'move position (?P<pos1>\d+) to position (?P<pos2>\d+)', move)
}


def parse(raw_input, reverse=False):
    cmds = []
    for line in raw_input.strip().split('\n'):
        for pattern, function in OPERATIONS:
            match = re.match(pattern, line)
            if match:
                args = match.groupdict()
                args['reverse'] = reverse
                cmds.append((function, args))
    return cmds[-1::-1] if reverse else cmds


def part1(raw_input, password='abcdefgh', reverse=False):
    password = list(password)
    cmds = parse(raw_input, reverse=reverse)
    for function, args in cmds:
        password = function(password,args)
    return ''.join(password)


def part2(raw_input):
    return part1(raw_input, password='fbgdceah', reverse=True)
