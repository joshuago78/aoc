from itertools import combinations


def parse(raw_input):
    boss = {}
    for line in raw_input.strip().split('\n'):
        k,v = line.split(': ')
        boss[k] = int(v)
    shop = {}
    with open('2015/day21shop.txt','r') as shopfile:
        for section in shopfile.read().strip().split('\n\n'):
            lines = section.split('\n')
            category = lines[0].split(':')[0]
            shop[category] = []
            for line in lines[1:]:
                name,cost,damage,armor = line.split()
                shop[category].append({
                    'name': name,
                    'cost': int(cost),
                    'damage': int(damage),
                    'armor': int(armor)
                })
    return boss, shop


def build_combos(shop, reverse=False):
    combos = []
    for w in shop['Weapons']:
        for a in shop['Armor']:
            for r1,r2 in combinations(shop['Rings'],2):
                combos.append({
                    'equipment': [v['name'] for v in [w,a,r1,r2]],
                    'cost': sum([v['cost'] for v in [w,a,r1,r2]]),
                    'damage': sum([v['damage'] for v in [w,a,r1,r2]]),
                    'defense': sum([v['armor'] for v in [w,a,r1,r2]])
                })
    return sorted(combos, key=lambda x: x['cost'], reverse=reverse)


def defeats_boss(boss, player):
    bosshp = boss['Hit Points']
    bossdmg = boss['Damage']
    bossdef = boss['Armor']
    playerhp = 100
    playerdmg = player['damage']
    playerdef = player['defense']
    while True:
        damage = playerdmg - bossdef
        if damage <= 0:
            damage = 1
        bosshp -= damage
        if bosshp <= 0:
            return True
        damage = bossdmg - playerdef
        if damage <= 0:
            damage = 1
        playerhp -= damage
        if playerhp <= 0:
            return False



def part1(raw_input):
    boss, shop = parse(raw_input)
    from pprint import pprint
    combos = build_combos(shop)
    for combo in combos:
        if defeats_boss(boss, combo):
            return combo['cost']
    

def part2(raw_input):
    boss, shop = parse(raw_input)
    from pprint import pprint
    combos = build_combos(shop, reverse=True)
    for combo in combos:
        if not defeats_boss(boss, combo):
            return combo['cost']