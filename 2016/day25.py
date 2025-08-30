

def parse(raw_input):
    cmds = [l.split() for l in raw_input.strip().split('\n')]
    for cmd in cmds:
        for i in [1,2]:
            if i < len(cmd) and cmd[i].lstrip('-').isdigit():
                cmd[i] = int(cmd[i])
    return cmds


def try_multiplication(commands, registers):
    seq = ['inc','dec','jnz','dec','jnz']
    if [c[0] for c in commands] != seq:
        return False
    if commands[1][1] != commands[2][1] or commands[3][1] != commands[4][1]:
        return False
    op1, op2 = registers[commands[1][1]], registers[commands[3][1]]
    registers[commands[0][1]] += op1*op2
    return True


def run(commands, starta):
    registers = {'a':starta,'b':0,'c':0,'d':0}
    counter = 0
    signal = []
    while counter < len(commands) and len(signal) < 100:
        cmd = commands[counter]
        res = try_multiplication(commands[counter:counter+5],registers)
        if res is True:
            counter += 5
            continue
        match cmd[0]:
            case 'cpy':
                registers[cmd[2]] = registers.get(cmd[1],cmd[1])
            case 'inc':
                registers[cmd[1]] += 1
            case 'dec':
                registers[cmd[1]] -= 1
            case 'jnz':
                value1 = registers.get(cmd[1],cmd[1])
                if value1 != 0:
                    value2 = registers.get(cmd[2],cmd[2])
                    counter += value2-1
            case 'out':
                value = registers.get(cmd[1],cmd[1])
                if value not in [0,1]:
                    return False
                if len(signal) > 0 and value==signal[-1]:
                    return False
                signal.append(value)
            case 'tgl':
                step = registers[cmd[1]]
                if counter+step < len(commands):
                    oldcmd = commands[counter+step]
                    match oldcmd[0]:
                        case 'cpy':
                            newcmd = 'jnz'
                        case 'inc':
                            newcmd = 'dec'
                        case 'dec':
                            newcmd = 'inc'
                        case 'jnz':
                            newcmd = 'cpy'
                        case 'tgl':
                            newcmd = 'inc'
                    commands[counter+step] = [newcmd,] + oldcmd[1:]
        counter += 1
    return True


def part1(raw_input, a=7):
    commands = parse(raw_input)
    astart = 0
    result = run(commands, astart)
    while result is False:
        astart += 1
        result = run(commands, astart)
    return astart
    
