from itertools import combinations
from copy import deepcopy


VISITED_STATES = []


class State(object):

    def __init__(self, parent, elevator, floors):
        self.parent = parent
        self.elevator_on = elevator
        self.floors = floors
        self.steps = 0 if parent is None else parent.steps+1
        self.signature = self.sig()

    def __eq__(self, other):
        return self.signature == other.signature

    def __repr__(self):
        return f'<State: {self.signature}>'

    def sig(self):
        signature = [f'E{self.elevator_on+1}',]
        for num,floor in enumerate(self.floors):
            g,m = 0,0
            for part in floor:
                if part[-1]=='G':
                    g+=1
                else:
                    m+=1
            signature.append(f'{num+1}:G{g}M{m}')
        return '|'.join(signature)

    def history(self):
        node = self
        hist = [node]
        while node.parent is not None:
            node = node.parent
            hist.insert(0, node)
        return hist

    def is_finished(self):
        return sum(len(f) for f in self.floors[:-1]) == 0

    def is_valid(self):
        for floor in self.floors:
            has_gen = False
            free_chip = False
            for obj in floor:
                elem,type = obj[:-1], obj[-1]
                if type == 'M':
                    if elem+'G' not in floor:
                        free_chip = True
                else:
                    has_gen = True
            if free_chip and has_gen:
                return False
        return True

    def is_repeated(self):
        for state in VISITED_STATES:
            if self == state:
                return True
        return False

    def is_similar_to(self, other):
        for num,floor in enumerate(self.floors):
            gens = [o for o in floor if o[-1]=='G']
            chips = [o for o in floor if o[-1]=='M']
            pairs = [p for p in gens if p[:-1]+'M' in chips]
            ofloor = other.floors[num]
            ogens = [o for o in ofloor if o[-1]=='G']
            ochips = [o for o in ofloor if o[-1]=='M']
            opairs = [p for p in ogens if p[:-1]+'M' in ochips]
            if len(gens) != len(ogens) or len(chips) != len(ochips) or len(pairs) != len(opairs):
                return False
        return True

    def print(self):
        num = 3
        while num >= 0:
            line = f'F{num+1}: '
            line += 'E ' if self.elevator_on==num else '  '
            line += ', '.join(self.floors[num])
            num -= 1
            print(line)

    def get_combos(self):
        floor = self.floors[self.elevator_on]
        combos = list(combinations(floor,2))
        combos = [[o1,o2] for [o1,o2] in combos if o1[-1]==o2[-1] or o1[:-1]==o2[:-1]]
        singles = list(combinations(floor,1))
        return combos, singles

    def move(self, direction, parts):
        offset = 1 if direction == 'up' else -1
        for part in parts:
            index = self.floors[self.elevator_on].index(part)
            self.floors[self.elevator_on].pop(index)
            self.floors[self.elevator_on+offset].append(part)
        self.elevator_on += offset
        self.signature = self.sig()

    def possible_moves(self):
        pairs, singles = self.get_combos()
        upmoves, downmoves = [], []
        if self.elevator_on < 3:
            for combos in [pairs,singles]:
                if len(upmoves) == 0: #only try 1pc upmoves if no 2pc upmoves available
                    for combo in combos:
                        new_state = State(self, self.elevator_on, deepcopy(self.floors))
                        new_state.move('up', combo)
                        if new_state.is_valid() and not new_state.is_repeated():
                                upmoves.append(new_state)
        if self.elevator_on > 0:
            if sum([len(flr) for flr in self.floors[:self.elevator_on]]) > 0:
                for combos in [singles, pairs]:
                    if len(downmoves) == 0: #only try 2pc downmoves if no 1pc downmoves available
                        for combo in combos:
                            new_state = State(self, self.elevator_on, deepcopy(self.floors))
                            new_state.move('down', combo)
                            if new_state.is_valid() and not new_state.is_repeated():
                                downmoves.append(new_state)
        return upmoves+downmoves


def part1(raw_input):
    # skip raw input this time and just use hardcoded model of the floors
    # Test
    '''floors = [
        ['HM','LM'],
        ['HG',],
        ['LG',],
        []
    ]'''
    # Part 1
    '''floors = [
        ['PoG','ThG','ThM','PrG','RuG','RuM','CoG','CoM'],
        ['PoM','PrM'],
        [],
        []]'''
    # Part 2
    floors = [
        ['PoG','ThG','ThM','PrG','RuG','RuM','CoG','CoM','ElG','ElM','DiG','DiM'],
        ['PoM','PrM'],
        [],
        []
    ]
    solution = None
    initial_state = State(None,0,floors)
    moves = [initial_state,]
    VISITED_STATES.append(initial_state)
    while moves and not solution:
        state = moves.pop(0)
        futures = state.possible_moves()
        for next_state in futures:
            VISITED_STATES.append(next_state)
            if next_state.is_finished():
                solution = next_state
                break
            moves.append(next_state)
    if solution:
        for step,state in enumerate(solution.history()):
            print(f'\nStep {step}')
            state.print()
        return best.steps
    print('no valid paths found')
