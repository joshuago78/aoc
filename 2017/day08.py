import re


def parse(raw_input):
    pattern = r'(?P<reg>\w+) (?P<cmd>dec|inc) (?P<amt>-?\d+) if (?P<reg2>\w+) (?P<cond>[<>=!]+) (?P<amt2>-?\d+)'
    instructions = []
    registers = {}
    for line in raw_input.strip().split('\n'):
        m = re.match(pattern, line)
        instructions.append(m.groupdict())
        registers[m.group('reg')] = 0
        registers[m.group('reg2')] = 0
    return registers, instructions


def execute(registers, instructions):
    highest = 0
    for inst in instructions:
        val = registers[inst['reg2']]
        if eval(f'{val} {inst['cond']} {inst['amt2']}') is True:
            if inst['cmd']=='inc':
                registers[inst['reg']] += int(inst['amt'])
            else:
                registers[inst['reg']] -= int(inst['amt'])
            highest = max(registers[inst['reg']], highest)
    return highest


def part1(raw_input):
    registers, instructions = parse(raw_input)
    execute(registers, instructions)
    return max(registers.values())


def part2(raw_input):
    registers, instructions = parse(raw_input)
    return execute(registers, instructions)
