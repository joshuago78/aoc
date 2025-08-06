

def parse(raw_input):
    instructions = []
    for line in raw_input.strip().split('\n'):
        parts = line.split()
        instruction = {
            'cmd':parts[0],
            'params': {
                'reg': parts[1].strip(',') if parts[0] != 'jmp' else None,
                'off': int(parts[-1]) if parts[0].startswith('j') else None
            }
        }
        instructions.append(instruction)
    return instructions


def half(counter, registers, params):
    registers[params['reg']] //= 2
    return counter + 1


def triple(counter, registers, params):
    registers[params['reg']] *= 3
    return counter + 1


def increment(counter, registers, params):
    registers[params['reg']] += 1
    return counter + 1


def jump(counter, registers, params):
    return counter + params['off']


def jump_if_even(counter, registers, params):
    if registers[params['reg']] % 2 == 0:
        return counter + params['off']
    return counter + 1


def jump_if_one(counter, registers, params):
    if registers[params['reg']] == 1:
        return counter + params['off']
    return counter + 1


INSTRUCTION_SET = {
    'hlf': half,
    'tpl': triple,
    'inc': increment,
    'jmp': jump,
    'jie': jump_if_even,
    'jio': jump_if_one
}


def part1(raw_input, part2=False):
    program = parse(raw_input)
    registers = {'a':0, 'b':0} if not part2 else {'a':1, 'b':0}
    counter = 0
    while counter >= 0 and counter < len(program):
        instruction = program[counter]
        function = INSTRUCTION_SET[instruction['cmd']]
        counter = function(counter, registers, instruction['params'])
    return registers['b']


def part2(raw_input):
    return part1(raw_input, part2=True)
