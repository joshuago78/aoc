import re

BEGIN_PATTERN = r'Begin in state (?P<state>\w).'

STEP_PATTERN = r'Perform a diagnostic checksum after (?P<steps>\d+) steps.'

STATE_PATTERN = r'''In state (?P<state>\w):
  If the current value is 0:
    - Write the value (?P<write0>\d).
    - Move one slot to the (?P<move0>\w+).
    - Continue with state (?P<next0>\w).
  If the current value is 1:
    - Write the value (?P<write1>\d).
    - Move one slot to the (?P<move1>\w+).
    - Continue with state (?P<next1>\w).'''


def parse(text):
    state = re.match(BEGIN_PATTERN, text).group('state')
    steps = int(re.search(STEP_PATTERN, text).group('steps'))
    states = {}
    m = re.search(STATE_PATTERN, text)
    while m:
        states[m.group('state')] = {
            'write0': m.group('write0'),
            'move0': m.group('move0'),
            'next0': m.group('next0'),
            'write1': m.group('write1'),
            'move1': m.group('move1'),
            'next1': m.group('next1')}
        text = text[m.span()[1]:]
        m = re.search(STATE_PATTERN, text)
    return state, steps, states


def part1(raw_input):
    state, steps, states = parse(raw_input)
    dirs = {'left':-1, 'right':1}
    tape = ['0']*7
    pos = 3
    for i in range(steps):
        current = tape[pos]
        tape[pos] = states[state]['write'+current]
        pos += dirs[states[state]['move'+current]]
        state = states[state]['next'+current]
        if pos==1:
            tape.insert(0,'0')
            pos += 1
        elif pos==len(tape)-2:
            tape.append('0')
    return tape.count('1')
    
    