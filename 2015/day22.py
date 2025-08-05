from copy import deepcopy


class IllegalMove(Exception):
    """Move not allowed"""


def magic_missile(game):
    game['mana'] -= 53
    if game['mana'] < 0:
        raise IllegalMove('Not enough mana')
    game['mana_spent'] += 53
    game['bosshp'] -= 4


def drain(game):
    game['mana'] -= 73
    if game['mana'] < 0:
        raise IllegalMove('Not enough mana')
    game['mana_spent'] += 73
    game['bosshp'] -= 2
    game['playerhp'] += 2


def shield(game):
    if game['shield_counter'] > 1:
        raise IllegalMove('Already shielded')
    game['mana'] -= 113
    if game['mana'] < 0:
        raise IllegalMove('Not enough mana')
    game['mana_spent'] += 113
    game['shield_counter'] += 6
    game['defense'] = 7


def poison(game):
    if game['poison_counter'] > 0:
        raise IllegalMove('Already poisoned')
    game['mana'] -= 173
    if game['mana'] < 0:
        raise IllegalMove('Not enough mana')
    game['mana_spent'] += 173
    game['poison_counter'] = 6


def recharge(game):
    if game['recharge_counter'] > 0:
        raise IllegalMove('Already recharged')
    game['mana'] -= 229
    if game['mana'] < 0:
        raise IllegalMove('Not enough mana')
    game['mana_spent'] += 229
    game['recharge_counter'] = 5


SPELLS = {
    'Magic Missile': magic_missile,
    'Drain': drain,
    'Shield': shield,
    'Poison': poison,
    'Recharge': recharge
}


def take_turn(game, boss=False, hardmode=False):
    if hardmode and not boss:
        game['playerhp'] -= 1
        if game['playerhp'] == 0:
            return

    # apply poison
    if game['poison_counter'] > 0:
        game['poison_counter'] -= 1
        game['bosshp'] -= 3
    if game['bosshp'] <= 0:
        return

    # apply recharge
    if game['recharge_counter'] > 0:
        game['recharge_counter'] -= 1
        game['mana'] += 101

    # boss attacks player
    if boss:
        damage = max(game['bossdmg'] - game['defense'], 1)
        game['playerhp'] -= damage
        if game['playerhp'] <= 0:
            return

    # or player casts spell
    else:
        spellname = game['sequence'][-1]
        spellfunc = SPELLS[spellname]
        spellfunc(game)

    # decrement shield
    if game['shield_counter'] > 0:
        game['shield_counter'] -= 1
    if game['shield_counter'] == 0:
        game['defense'] = 0



def parse(raw_input):
    lines = raw_input.strip().split('\n')
    hp = int(lines[0].split(': ')[1])
    dmg = int(lines[1].split(': ')[1])
    return hp,dmg


def next_turns(games, best, hardmode=False):
    if len(games) == 0:
        return best
    new_games = []
    for game in games:
        for spellname,spellfunc in SPELLS.items():
            new_game = deepcopy(game)
            new_game['sequence'].append(spellname)
            try:
                take_turn(new_game, hardmode=hardmode)
                if best and new_game['mana_spent'] > best['mana_spent']:
                    continue
                if new_game['bosshp'] <= 0:
                    if best is None or new_game['mana_spent'] < best['mana_spent']:
                        best = new_game
                    continue
            except IllegalMove:
                continue
            take_turn(new_game, boss=True)
            if new_game['playerhp'] <= 0:
                continue
            new_games.append(new_game)
    return next_turns(new_games, best, hardmode=hardmode)


def part1(raw_input, hardmode=False):
    bosshp,bossdmg = parse(raw_input)
    games = [{
        'sequence':[],
        'bosshp': bosshp,
        'bossdmg': bossdmg,
        'playerhp': 50,
        'mana': 500,
        'mana_spent': 0,
        'shield_counter': 0,
        'poison_counter': 0,
        'recharge_counter': 0,
        'defense': 0
    },]
    best = next_turns(games, None, hardmode=hardmode)
    print(best)
    return best['mana_spent']


def part2(raw_input):
    return part1(raw_input, hardmode=True)


        