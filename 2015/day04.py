import hashlib


def part1(key):
    i = 0
    while True:
        i += 1
        hash = hashlib.md5(f'{key}{i}'.encode()).hexdigest()
        if hash[:5] == '00000':
            return i


def part2(key):
    i = 0
    while True:
        i += 1
        hash = hashlib.md5(f'{key}{i}'.encode()).hexdigest()
        if hash[:6] == '000000':
            return i
