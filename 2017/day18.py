
class Queue(object):

    def __init__(self):
        self.queues = {0:[], 1:[]}

    def push(self, pid, value):
        self.queues[pid].append(value)

    def pop(self, pid):
        return self.queues[pid].pop(0)


class Program(object):

    def __init__(self, pid, cmds, regs, queue):
        self.pid = pid
        self.cmds = cmds
        self.regs = regs.copy()
        self.regs['p'] = pid
        self.queue = queue
        self.prog_cntr = 0
        self.send_cnt = 0

    def next(self):
        if self.prog_cntr>=0 and self.prog_cntr<len(self.cmds):
            cmd, args = self.cmds[self.prog_cntr]
            x = args[0]
            y = None if len(args)==1 else args[1]
            if y:
                y = int(y) if (y.isdigit() or len(y)>1) else self.regs[y]
            jump = 1
            match cmd:
                case 'snd':
                    qid = 1 if self.pid==0 else 0
                    val = int(x) if x.isdigit() or len(x)>1 else self.regs[x]
                    self.queue.push(qid, val)
                    self.send_cnt += 1
                case 'set':
                    self.regs[x] = y
                case 'add':
                    self.regs[x] += y
                case 'mul':
                    self.regs[x] *= y
                case 'mod':
                    self.regs[x] %= y
                case 'rcv':
                    try:
                        self.regs[x] = self.queue.pop(self.pid)
                    except IndexError:
                        return False
                case 'jgz':
                    val = int(x) if x.isdigit() or len(x)>1 else self.regs[x]
                    if val > 0:
                        jump = y
            self.prog_cntr += jump
            return True
        else:
            return False


def parse(raw_input):
    program = []
    registers = {}
    for line in raw_input.strip().split('\n'):
        args = line.split()
        cmd = args.pop(0)
        for arg in args:
            if len(arg)==1 and not arg.isdigit() and arg not in registers.keys():
                registers[arg] = 0
        program.append((cmd,args))
    return program, registers


def part1(raw_input):
    program, registers = parse(raw_input)
    sound = None
    counter = 0
    while counter>=0 and counter<len(program):
        cmd, args = program[counter]
        x = args[0]
        y = None if len(args)==1 else args[1]
        if y:
            y = int(y) if y.isdigit() or len(y)>1 else registers[y]
        jump = 1
        match cmd:
            case 'snd':
                sound = int(x) if x.isdigit() or len(x)>1 else registers[x]
            case 'set':
                registers[x] = y
            case 'add':
                registers[x] += y
            case 'mul':
                registers[x] *= y
            case 'mod':
                registers[x] %= y
            case 'rcv':
                if registers[x] != 0:
                    return sound
            case 'jgz':
                if registers[x] > 0:
                    jump = y
        counter += jump


def part2(raw_input):
    cmds, regs = parse(raw_input)
    queue = Queue()
    p0 = Program(0,cmds,regs,queue)
    p0_operable = True
    p1 = Program(1,cmds,regs,queue)
    p1_operable = True
    while p0_operable or p1_operable:
        p0_operable = p0.next()
        p1_operable = p1.next()
    return p1.send_cnt

