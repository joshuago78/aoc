from hashlib import md5


def has_threepeat(key):
    ptr = 0
    while ptr < len(key) - 2:
        for offset in range(1,3):
            if key[ptr] != key[ptr+offset]:
                break
        else:
            return True, key[ptr]
        ptr += offset
    return False, None


def has_fivepeat(key, char):
    ptr = 0
    while ptr < len(key) - 4:
        if key[ptr] == char:
            for offset in range(1,5):
                if key[ptr] != key[ptr+offset]:
                    break
            else:
                return True
            ptr += offset
        else:
            ptr += 1
    return False


def get_hash(string,stretch):
    key = md5(string.encode()).hexdigest()
    if stretch:
        for i in range(2016):
            key = md5(key.encode()).hexdigest()
    return key


def check_1000_hashes(has3pt,source_index,salt,stretch):
    new_index = source_index if len(has3pt)==0 else list(has3pt.keys())[-1]+1
    if new_index < source_index + 1000:
        while True:
            key = get_hash(f'{salt}{new_index}', stretch)
            yes,char = has_threepeat(key)
            if yes:
                has3pt[new_index] = (key,char)
                if new_index > source_index + 1000:
                    break
            new_index += 1


def part1(salt, stretch=False):
    keys = {}
    index = -1
    has3pt = {}
    while len(keys) < 64:
        index += 1
        check_1000_hashes(has3pt,index,salt,stretch)
        if index in has3pt.keys():
            char = has3pt[index][1]
            for idx,vals in has3pt.items():
                if idx > index and idx <= index+1000 and has_fivepeat(vals[0],char):
                    keys[index] = {
                        'key':has3pt[index][0],
                        'has5idx': idx,
                        'has5hash': has3pt[idx]}
    from pprint import pprint
    pprint(keys)
    return list(keys.keys())[-1]


def part2(salt):
    return part1(salt,stretch=True)
