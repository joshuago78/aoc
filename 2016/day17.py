from hashlib import md5


START = (0,0)
DEST = (3,3)
DIRS = [(0,-1,'U'),(0,1,'D'),(-1,0,'L'),(1,0,'R')]
OPEN_CHARS = 'bcdef'


def get_possible_moves(passcode, pos, path):
    hash = md5(f'{passcode}{path}'.encode()).hexdigest()
    moves = []
    for i in range(4):
        if hash[i] in OPEN_CHARS:
            d = DIRS[i]
            x,y = d[0]+pos[0], d[1]+pos[1]
            if x>=0 and x<=DEST[0] and y>=0 and y<=DEST[1]:
                moves.append(((x,y),path+d[2]))
    return moves


def part1(passcode, objective='shortest'):
    moves = [(START,'')]
    solution = None
    while moves:
        pos,path = moves.pop(0)
        new_moves = get_possible_moves(passcode,pos,path)
        for new_pos,new_path in new_moves:
            if new_pos == DEST:
                if objective=='shortest':
                    return new_path
                solution = (new_pos,new_path)
            else:
                moves.append((new_pos,new_path))
    if objective == 'longest':
        return len(solution[1])
    print(f'Failed to find path')


def part2(passcode):
    return part1(passcode, objective='longest')

