from copy import deepcopy

SIZE = 100


def parse(raw_input):
    ingredients = {}
    for line in raw_input.strip().split('\n'):
        tokens = line.strip(',').split()
        ingredients[tokens[0][:-1]] = {
            'capacity': int(tokens[2][:-1]),
            'durability': int(tokens[4][:-1]),
            'flavor': int(tokens[6][:-1]),
            'texture': int(tokens[8][:-1]),
            'calories': int(tokens[10])
        }
    return ingredients


def get_combos(combos, count):
    if count == 0:
        return combos
    new_combos = []
    for combo in combos:
        total = sum(combo)
        for i in range(1, SIZE+1-total):
            new_combo = combo.copy()
            new_combo.append(i)
            new_combos.append(new_combo)
    return get_combos(new_combos, count-1)


def get_score(ingredients, names, combo, get_calories=False):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i in range(len(names)):
        amt = combo[i]
        name = names[i]
        capacity += amt * ingredients[name]['capacity']
        durability += amt * ingredients[name]['durability']
        flavor += amt * ingredients[name]['flavor']
        texture += amt * ingredients[name]['texture']
        calories += amt * ingredients[name]['calories']
    capacity = max(0,capacity)
    durability = max(0,durability)
    flavor = max(0,flavor)
    texture = max(0,texture)
    score = capacity * durability * flavor * texture
    if get_calories:
        return score, calories
    return score


def part1(raw_input):
    ingredients = parse(raw_input)
    combos = []
    for i in range(1, SIZE+1):
        combos.append([i,])
    combos = get_combos(combos, len(ingredients)-1)
    combos = [combo for combo in combos if sum(combo) == SIZE]
    
    best = (0,None)
    names = list(ingredients.keys())
    for combo in combos:
        score = get_score(ingredients, names, combo)
        if score > best[0]:
            best = score, combo
    return best[0]


def part2(raw_input):
    ingredients = parse(raw_input)
    combos = []
    for i in range(1, SIZE+1):
        combos.append([i,])
    combos = get_combos(combos, len(ingredients)-1)
    combos = [combo for combo in combos if sum(combo) == SIZE]
    combos = [combo for combo in combos if sum(combo) == SIZE]
    
    best = (0,None)
    names = list(ingredients.keys())
    for combo in combos:
        score, calories = get_score(ingredients, names, combo, get_calories=True)
        if calories == 500:
            if score > best[0]:
                best = score, combo
    return best[0]
