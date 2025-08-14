

def parse(raw_input):
    cmds = [l.split() for l in raw_input.strip().split('\n')]
    for cmd in cmds:
        for i in [1,2]:
            if i < len(cmd) and cmd[i].lstrip('-').isdigit():
                cmd[i] = int(cmd[i])
    return cmds


def part1(raw_input, c=0):
    commands = parse(raw_input)
    registers = {'a':0,'b':0,'c':c,'d':0}
    counter = 0
    while counter < len(commands):
        cmd = commands[counter]
        match cmd[0]:
            case 'cpy':
                registers[cmd[2]] = registers.get(cmd[1],cmd[1])
            case 'inc':
                registers[cmd[1]] += 1
            case 'dec':
                registers[cmd[1]] -= 1
            case 'jnz':
                value = registers.get(cmd[1],cmd[1])
                if value != 0:
                    counter += cmd[2]-1
        counter += 1
    return registers['a']


def part2(raw_input):
    return part1(raw_input, c=1)
    

